<template>
    <div>
        <hero-index></hero-index>
        <extension></extension>
    </div>
</template>
<script>
import Extension from './components/Extension';
import HeroIndex from "./components/HeroIndex";

export default {
  name: "appindex",
  components: {
    Extension,
    HeroIndex
  }
};
</script>
