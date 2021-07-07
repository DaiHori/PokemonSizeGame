<template>
  <v-card class="mx-auto mt-2" max-width="1280" height="500">
    <Img />

    <v-card-text class="text-center">
      <h1>第{{ $store.state.counter }}問</h1>
      <br />
      <h2>
        <p class="text-h4 text--primary">
          どっちが重いかな？
        </p>
      </h2>
      <Button />
      <br />
      <Button />
      <Img2 />
    </v-card-text>
    <v-card-actions> </v-card-actions>
  </v-card>
</template>

<script>
import Button from "@/components/ContentsViewsButton.vue";
import Img from "@/components/ContentsViewsImg.vue";
import Img2 from "@/components/ContentsViewsImg2.vue";

export default {
  name: "ContentsViews",

  components: {
    Button,
    Img,
    Img2,
  },
};
</script>
