<template>
  <div>
    <HeaderViews />
    <ContentsViews />
    <Footer />
  </div>
</template>

<script>
import HeaderViews from "../components/HeaderViews";
import ContentsViews from "../components/ContentsViews";
import Footer from "../components/Footer";

export default {
  name: "Home",

  components: {
    HeaderViews,
    ContentsViews,
    Footer,
  },
};
</script>
