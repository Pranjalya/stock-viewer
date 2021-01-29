<template>
  <section id="do" class="section">
    <div class="container">
      <div class="columns">
        <div class="column is-10 is-offset-1 has-text-centered">
          <h1 class="title is-2">Stock Table</h1>
          <separator></separator>
          <h2 class="subtitle is-5">
            Check out the daily stock values in the Stock Market, updated every
            day at 1800 hours IST. Search for the stocks of the companies, and
            additionally you can download the result in a CSV format too.
          </h2>
        </div>
      </div>
      <div class="columns">
        <article class="column do-col panel is-primary is-12 is-fullwidth">
          <p class="panel-heading has-text-centered">Stock Viewer</p>
          <div class="panel-block">
            <b-button type="is-info" outlined>Export as CSV</b-button>
          </div>
          <div class="panel-block">
            <p class="control has-icons-left">
              <input
                class="input is-primary"
                type="text"
                placeholder="Search"
              />
              <span class="icon is-left">
                <i class="fas fa-search" aria-hidden="true"></i>
              </span>
            </p>
          </div>
          <div class="panel-block is-fullwidth">
            <b-table
              class="is-fullwidth"
              :data="getrows"
              :loading="loading"
              :total="total"
              @page-change="onPageChange"
              backend-paginated
              :hoverable="true"
              :paginated="true"
              :per-page="perPage"
              :current-page.sync="page"
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
                searchable
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
  name: "do",
  data() {
    return {
      data: [],
      loading: false,
      isScrollMode: false,
      // columns: [
      //   {
      //     label: "Stock Code",
      //     field: "SC_CODE",
      //     centered: true,
      //     class: "tag is-success",
      //   },
      //   {
      //     label: "Stock Name",
      //     field: "SC_NAME",
      //     centered: true,
      //     align: "center",
      //     searchable: true,
      //   },
      //   {
      //     label: "Open",
      //     field: "OPEN",
      //     centered: true,
      //   },
      //   {
      //     label: "Close",
      //     field: "CLOSE",
      //     centered: true,
      //   },
      //   {
      //     label: "High",
      //     field: "HIGH",
      //     centered: true,
      //   },
      //   {
      //     label: "Low",
      //     field: "LOW",
      //     centered: true,
      //     // format: (value) => "£" + value,
      //   },
      // ],
      isPaginated: true,
      defaultSortDirection: "asc",
      sortIcon: "arrow-up",
      sortIconSize: "is-small",
      page: 1,
      total: 0,
      perPage: 10,
    };
  },
  methods: {
    onPageChange(page) {
      this.page = page;
      this.loadAllData();
    },
    loadAllData() {
      this.loading = true;
      var el = this;
      axios
        .get("http://127.0.0.1:8000/api/stocks/")
        .then((res) => {
          console.log(res.data);
          el.total = res.data.count;
          el.data = res.data.items;
          el.loading = false;
        })
        .catch((err) => {
          console.log(err);
        });
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
    checkScrollMode() {
      return this.isScrollMode;
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../assets/styles/variables.scss";
// @import "~buefy/src/scss/buefy";

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
  min-height: 50rem;
  width: 100%;
}
</style>
