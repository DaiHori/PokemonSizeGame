<template>
  <v-card class="mx-auto mt-2" max-width="1280" height="500">
    <v-layout class="size align-end">
      <v-img src="@/assets/ピカチュウ_なみのり.gif" />
    </v-layout>

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
    </v-card-text>
    <v-card-actions> </v-card-actions>

    <v-layout class="size position">
      <v-img src="@/assets/イーブイ.gif" />
    </v-layout>
  </v-card>
</template>

<script>
import Button from "@/components/ContentsViewsButton.vue";

export default {
  name: "ContentsViews",

  components: {
    Button,
  },
};
</script>

<style lang="scss">
.size {
  width: 10%; /* 横幅を割合で指定 */
  height: auto; /* 高さは自動指定 */
}
.position {
  float: right;
}
</style>
