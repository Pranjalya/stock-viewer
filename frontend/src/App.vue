<template>
  <div id="app" v-cloak>
    <hero></hero>
    <stock-table></stock-table>
    <app-footer></app-footer>
  </div>
</template>

<script>
import Hero from "./components/Hero";
import StockTable from "./components/StockTable";
import AppFooter from "./components/AppFooter";

export default {
  name: "app",
  components: {
    Hero,
    StockTable,
    AppFooter
  },
};
</script>

<style lang="scss">
#app {
  height: 100%;
  width: 100%;
  overflow: hidden;
}
</style>
