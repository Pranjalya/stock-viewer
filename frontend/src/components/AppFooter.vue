<template>
  <footer class="footer">
    <div class="container">
      <div class="content has-text-centered">
        <p class="reveal">
          © 2021 Pranjalya Tiwari, looking for more awesome stuff to do :) ☕️.
        </p>
        <p class="reveal">
          <a class="icon"
            v-for="item in social"
            :href="item.link"
            :key="item.id"
            target="_blank"
            rel="noopener">
            <b-icon :icon="item.icon"></b-icon>
          </a>
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
  data() {
    return {
      social: [
        {
          icon: 'linkedin',
          link: 'https://www.linkedin.com/in/pranjalya-tiwari/',
        },
        {
          icon: 'twitter',
          link: 'https://twitter.com/PranjalyaQuasar',
        },
        {
          icon: 'github',
          link: 'https://github.com/Pranjalya',
        },
      ],
    };
  },
};
</script>
