<template>
  <footer class="footer">
    <div class="container">
      <div class="content has-text-centered">
        <p class="reveal">
          © 2021 Pranjalya Tiwari, looking for more awesome stuff to do 😃
        </p>
        <p class="reveal">
          <a href="https://twitter.com/PranjalyaQuasar" target="_blank"><img src="https://img.icons8.com/doodle/48/000000/old-twitter-logo.png"/></a>
          <a href="https://linkedin.com/in/pranjalya-tiwari" target="_blank"><img src="https://img.icons8.com/doodle/48/000000/linkedin-circled.png"/></a>
          <a href="https://github.com/Pranjalya" target="_blank"><img src="https://img.icons8.com/doodle/48/000000/github.png"/></a>
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
