<template>
  <section id="stocktable" class="section">
    <div class="container">
      <div class="columns">
        <div class="column is-10 is-offset-1 has-text-centered">
          <h1 class="title is-2">Stock Table</h1>
          <separator></separator>
          <h2 class="subtitle is-5">
            Check out the daily stock values in the Stock Market, updated every
            day at 1800 hours IST. Search for the stocks either by prefix, or
            search for the keywords in the stock name, and additionally you can
            download the result in a CSV format too.
          </h2>
        </div>
      </div>
      <div class="columns">
        <article class="column do-col panel is-primary is-12 is-fullwidth">
          <p class="panel-heading has-text-centered">Stock Viewer</p>
          <div class="panel-block">
            <b-button type="is-info" outlined @click.prevent.stop="exportAsCsv"
              >Export as CSV</b-button
            >
          </div>
          <div class="panel-block">
            <b-field grouped>
              <b-input
                placeholder="Search the Stock Name by prefix..."
                type="search"
                icon="magnify"
                label="Prefix"
                lazy
                v-model="prefix"
                @keyup.native.enter="loadByPrefix"
              >
              </b-input>
              <p class="control">
                <b-button
                  label="Search"
                  type="is-info"
                  @click.prevent.stop="loadByPrefix"
                />
              </p>
              <b-input
                placeholder="Search the Stock Name by text..."
                type="search"
                icon="magnify"
                class="is-right"
                label="Full Text"
                expanded
                lazy
                v-model="fulltext"
                @keyup.native.enter="loadByFulltext"
              >
              </b-input>
              <p class="control">
                <b-button
                  label="Search"
                  type="is-info"
                  @click.prevent.stop="loadByFulltext"
                />
              </p>
              <p class="control">
                <b-button
                  label="Clear Search"
                  type="is-danger"
                  @click.prevent.stop="clearSearch"
                />
              </p>
              <p class="control">
                <b-select placeholder="Rows per page" v-model="perPage">
                  <option v-for="index in 10" :key="index">
                    {{ (parseInt(index) + 1) * 5 }}
                  </option>
                </b-select>
              </p>
            </b-field>
          </div>
          <div class="panel-block is-fullwidth">
            <b-table
              class="is-fullwidth my-table"
              :data="getrows"
              :loading="loading"
              :total="total"
              @page-change="onPageChange"
              paginated
              backend-pagination
              :hoverable="true"
              :per-page="perPage"
              pagination-position="bottom"
              :default-sort-direction="defaultSortDirection"
              :sort-icon="sortIcon"
              :sort-icon-size="sortIconSize"
              aria-next-label="Next page"
              aria-previous-label="Previous page"
              aria-page-label="Page"
              aria-current-label="Current page"
            >
              <b-table-column field="SC_CODE" label="Stock Code" v-slot="props">
                {{ props.row.SC_CODE }}
              </b-table-column>

              <b-table-column
                field="SC_NAME"
                label="Stock Name"
                sortable
                v-slot="props"
              >
                <span class="tag is-primary is-medium is-light">
                  {{ props.row.SC_NAME }}
                </span>
              </b-table-column>

              <b-table-column
                field="OPEN"
                label="Opening Price"
                centered
                numeric
                v-slot="props"
              >
                <span
                  :class="
                    props.row.OPEN - props.row.CLOSE == 0
                      ? 'tag is-warning is-light'
                      : props.row.OPEN - props.row.CLOSE > 0
                      ? 'tag is-success is-light'
                      : 'tag is-danger is-light'
                  "
                >
                  {{ props.row.OPEN }}
                </span>
              </b-table-column>

              <b-table-column
                field="CLOSE"
                label="Closing Price"
                centered
                numeric
                v-slot="props"
              >
                <span
                  :class="
                    props.row.OPEN - props.row.CLOSE == 0
                      ? 'tag is-warning is-light'
                      : props.row.OPEN - props.row.CLOSE < 0
                      ? 'tag is-success is-light'
                      : 'tag is-danger is-light'
                  "
                >
                  {{ props.row.CLOSE }}
                </span>
              </b-table-column>

              <b-table-column
                field="HIGH"
                label="Highest Price"
                centered
                numeric
                v-slot="props"
              >
                <span
                  :class="
                    props.row.HIGH - props.row.LOW == 0
                      ? 'tag is-warning is-light'
                      : props.row.HIGH - props.row.LOW > 0
                      ? 'tag is-success is-light'
                      : 'tag is-danger is-light'
                  "
                >
                  {{ props.row.HIGH }}
                </span>
              </b-table-column>

              <b-table-column
                field="LOW"
                label="Lowest Price"
                centered
                numeric
                v-slot="props"
              >
                <span
                  :class="
                    props.row.HIGH - props.row.LOW == 0
                      ? 'tag is-warning is-light'
                      : props.row.LOW - props.row.HIGH > 0
                      ? 'tag is-success is-light'
                      : 'tag is-danger is-light'
                  "
                >
                  {{ props.row.LOW }}
                </span>
              </b-table-column>
            </b-table>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";

export default {
  name: "stock-table",
  data() {
    return {
      data: [],
      loading: false,
      isScrollMode: false,
      isPaginated: true,
      defaultSortDirection: "asc",
      sortIcon: "arrow-up",
      sortIconSize: "is-small",
      page: 1,
      total: 0,
      perPage: 10,
      prefix: "",
      fulltext: "",
      currentPagination: "all",
    };
  },
  methods: {
    onPageChange(page) {
      this.page = page;
      switch (this.currentPagination) {
        case "all":
          this.loadAllData();
          break;
        case "prefix":
          this.loadByPrefix();
          break;
        case "fulltext":
          this.loadByFulltext();
          break;
        default:
          this.loadAllData();
      }
    },
    alertCustomError() {
      this.$buefy.dialog.alert({
        title: "Not Found",
        message: "Requested table was not found 😞",
        type: "is-danger",
        hasIcon: true,
        icon: "times-circle",
        iconPack: "fa",
        ariaRole: "alertdialog",
        ariaModal: true,
      });
    },
    clearSearch() {
      this.prefix = "";
      this.fulltext = "";
      this.loadAllData();
    },
    loadAllData() {
      this.loading = true;
      this.currentPagination = "all";
      axios
        .get(
          `http://127.0.0.1:8000/api/stocks/page=${this.page}&perPage=${this.perPage}`
        )
        .then((res) => {
          this.total = res.data.count;
          this.data = res.data.items;
          this.loading = false;
        })
        .catch((err) => {
          console.log(err);
          this.loading = false;
          this.alertCustomError();
        });
    },
    loadByPrefix() {
      this.loading = true;
      this.currentPagination = "prefix";
      this.fulltext = "";
      if (this.prefix != "") {
        axios
          .get(
            `http://127.0.0.1:8000/api/stocks/prefix/name=${this.prefix}&page=${this.page}&perPage=${this.perPage}`
          )
          .then((res) => {
            console.log(res.data);
            this.total = res.data.count;
            console.log(this.total);
            this.data = res.data.items;
            this.loading = false;
          })
          .catch((err) => {
            console.log(err);
            this.loading = false;
            this.alertCustomError();
          });
      }
    },
    loadByFulltext() {
      this.loading = true;
      this.currentPagination = "fulltext";
      this.prefix = "";
      if (this.fulltext != "") {
        axios
          .get(
            `http://127.0.0.1:8000/api/stocks/search/name=${this.fulltext}&page=${this.page}&perPage=${this.perPage}`
          )
          .then((res) => {
            console.log(res.data);
            this.total = res.data.count;
            console.log(this.total);
            this.data = res.data.items;
            this.loading = false;
          })
          .catch((err) => {
            console.log(err);
            this.loading = false;
            this.alertCustomError();
          });
      }
    },
    exportAsCsv() {
      var key = "",
        text = "";
      if (this.prefix != "") {
        key = "prefix";
        text = this.prefix;
      } else if (this.fulltext != "") {
        key = "fulltext";
        text = this.fulltext;
      } else {
        key = "all";
        text = "o";
      }
      window.open(
        `http://127.0.0.1:8000/api/stocks/download/key=${key}&text=${text}`,
        "_blank"
      );
    },
  },
  mounted() {
    this.sr.reveal(".do-col", 250);
    this.loadAllData();
  },
  computed: {
    getrows() {
      return this.data;
    },
    getTotal() {
      return this.total;
    },
  },
  watch: {
    perPage(perPage) {
      this.perPage = perPage;
      this.page = 1;
      if (this.prefix != "") {
        this.loadByPrefix();
      } else if (this.fulltext != "") {
        this.loadByFulltext();
      } else {
        this.loadAllData();
      }
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../assets/styles/variables.scss";

.panel-block {
  flex-flow: column nowrap;
  border: none;

  p {
    font-size: 17px;
    line-height: 1.4;
  }

  i {
    color: $secondary;
    font-size: 5em;
  }
}

.my-table {
  min-height: 40rem;
  width: 100%;
}
</style>
