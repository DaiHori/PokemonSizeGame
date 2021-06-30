<template>
  <div>
    <HeaderViews />
    <ContentsViews />
  </div>
</template>

<script>
import HeaderViews from "../components/HeaderViews";
import ContentsViews from "../components/ContentsViews";

export default {
  name: "Home",

  components: {
    HeaderViews,
    ContentsViews,
  },
};
</script>
