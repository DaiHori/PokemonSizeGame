<template>
  <div>
    <HeaderViews />
    <Footer />
  </div>
</template>

<script>
import HeaderViews from "../components/HeaderViews";
import Footer from "../components/Footer";

export default {
  name: "Home",

  components: {
    HeaderViews,
    Footer,
  },
};
</script>
