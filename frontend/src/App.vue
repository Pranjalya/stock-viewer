<template>
  <div id="app" v-cloak>
    <hero></hero>
    <about></about>
    <do></do>
    <app-footer></app-footer>
  </div>
</template>

<script>
import Hero from "./components/Hero";
import About from "./components/About";
import Do from "./components/Do";
import AppFooter from "./components/AppFooter";

export default {
  name: "app",
  components: {
    Hero,
    About,
    Do,
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
