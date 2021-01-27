<template>
  <section class="section-hero section-shaped my-0">
    <div class="shape shape-style-1 shape-primary">
      <span class="span-150"></span>
      <span class="span-50"></span>
      <span class="span-50"></span>
      <span class="span-75"></span>
      <span class="span-100"></span>
      <span class="span-75"></span>
      <span class="span-50"></span>
      <span class="span-100"></span>
      <span class="span-50"></span>
      <span class="span-100"></span>
    </div>
    <section class="section section-lg">
      <div class="container">
        <div
          class="row justify-content-center"
          @mouseover="showIconsAnimation = true"
        >
          <div class="col-lg-8 text-center">
            <h2 class="display-2 text-white">Stock Viewer</h2>
            <p class="lead text-white">
              Check out the daily stock values in the Stock Market, updated
              every day at 1800 hours IST. Search for the stocks of the
              companies, and additionally you can download the result in a CSV
              format too.
            </p>
          </div>
        </div>
      </div>
    </section>
    <div class="container container-lg">
      <div class="row align-items-center">
        <div class="col-md-12 mb-5 mb-md-0">
          <div class="card shadow border-0">
            <div class="col-xs-12 col-md-4 form-inline">
              <div class="form-group">
                <label for="filter" class="sr-only">Filter</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="filter"
                  placeholder="Filter"
                  @keydown="$event.stopImmediatePropagation()"
                />
              </div>
            </div>
          </div>
          <br />
          <div class="card card-lift--hover shadow border-0">
            <bootstrap-4-datatable
              :columns="data.columns"
              :data="data.rows"
              :per-page="5"
              name="stocks"
            ></bootstrap-4-datatable>
            <bootstrap-4-datatable-pager
              v-model="data.page"
              table="stocks"
            ></bootstrap-4-datatable-pager>
            <!-- </div> -->
            <!-- <img v-lazy="'img/theme/landing.jpg'" class="card-img" /> -->
            <!-- Table with panel -->

            <!-- Table with panel -->
          </div>
        </div>
      </div>

      <br />
    </div>
  </section>
</template>
<script>
import "vuejs-datatable/dist/themes/bootstrap-4.esm";
import { debounce } from "lodash";

export default {
  data() {
    return {
      year: new Date().getFullYear(),
      filter: "",
      data: {
        page: 1,
        columns: [
          {
            label: "Name",
            field: "name",
            sort: true,
            align: "center",
          },
          {
            label: "Position",
            field: "position",
            sort: true,
          },
          {
            label: "Office",
            field: "office",
            sort: true,
          },
          {
            label: "Age",
            field: "age",
            sort: true,
          },
          {
            label: "Start date",
            field: "date",
            sort: true,
          },
          {
            label: "Salary",
            field: "salary",
            sort: false,
            format: (value) => "£" + value,
          },
        ],
        rows: [
          {
            name: "Tiger Nixon",
            position: "System Architect",
            office: "Edinburgh",
            age: "61",
            date: "2011/04/25",
            salary: "320",
          },
          {
            name: "Rhona Davidson",
            position: "Integration Specialist",
            office: "Tokyo",
            age: "55",
            date: "2010/10/14",
            salary: "327",
          },
          {
            name: "Colleen Hurst",
            position: "Javascript Developer",
            office: "San Francisco",
            age: "39",
            date: "2009/09/15",
            salary: "205",
          },
          {
            name: "Sonya Frost",
            position: "Software Engineer",
            office: "Edinburgh",
            age: "23",
            date: "2008/12/13",
            salary: "103",
          },
          {
            name: "Jena Gaines",
            position: "Office Manager",
            office: "London",
            age: "30",
            date: "2008/12/19",
            salary: "90",
          },
          {
            name: "Quinn Flynn",
            position: "Support Lead",
            office: "Edinburgh",
            age: "22",
            date: "2013/03/03",
            salary: "342",
          },
          {
            name: "Charde Marshall",
            position: "Regional Director",
            office: "San Francisco",
            age: "36",
            date: "2008/10/16",
            salary: "470",
          },
          {
            name: "Haley Kennedy",
            position: "Senior Marketing Designer",
            office: "London",
            age: "43",
            date: "2012/12/18",
            salary: "313",
          },
          {
            name: "Tatyana Fitzpatrick",
            position: "Regional Director",
            office: "London",
            age: "19",
            date: "2010/03/17",
            salary: "385",
          },
          {
            name: "Michael Silva",
            position: "Marketing Designer",
            office: "London",
            age: "66",
            date: "2012/11/27",
            salary: "198",
          },
          {
            name: "Paul Byrd",
            position: "Chief Financial Officer (CFO)",
            office: "New York",
            age: "64",
            date: "2010/06/09",
            salary: "725",
          },
          {
            name: "Howard Hatfield",
            position: "Office Manager",
            office: "San Francisco",
            age: "51",
            date: "2008/12/16",
            salary: "164",
          },
        ],
      },
    };
  },
  components: {},
  mounted() {
    this.$datatables.debounced.processRows = debounce(
      this.$datatables.debounced.processRows,
      1000
    );
  },
};
</script>
<style>
</style>