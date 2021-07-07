<template>
  <div>
    <HeaderViews />
    <ContentsViews />
    <Footer />
  </div>
</template>

<script>
import HeaderViews from "./HeaderViews";
import ContentsViews from "./ContentsViews";
import Footer from "./Footer";

export default {
  name: "Home",

  components: {
    HeaderViews,
    ContentsViews,
    Footer,
  },
};
</script>
