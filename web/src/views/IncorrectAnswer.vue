<template>
  <div>
    <HeaderViews />
    <v-card class="mx-auto mt-2" max-width="1280" height="500">
      <v-card-text class="text-center">
        <h1>不正解</h1>
      </v-card-text>
      <v-card-actions> </v-card-actions>
    </v-card>
    <Footer />
  </div>
</template>

<script>
import HeaderViews from "./HeaderViews";
import Footer from "./Footer";

export default {
  name: "IncorrectAnswer",

  components: {
    HeaderViews,
    Footer,
  },
};
</script>
