<template>
  <footer class="footer">
    <div class="container">
      <div class="content has-text-centered">
        <p class="reveal">
          © 2021 Pranjalya Tiwari, looking for more awesome stuff to do 😃
        </p>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'app-footer',
  mounted() {
    this.sr.reveal('.footer .reveal', 250);
  },
};
</script>
