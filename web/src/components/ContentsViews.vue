<template>
  <v-card class="mx-auto mt-2" max-width="1280" height="800">
    <v-layout class="size align-end">
      <v-img src="@/assets/ピカチュウ_なみのり.gif" />
    </v-layout>

    <v-card-text class="text-center">
      <h2>
        <p class="text-h4 text--primary">
          どっちが大きいかな？
        </p>
      </h2>
    </v-card-text>
    <v-card-actions> </v-card-actions>

    <v-layout class="size position">
      <v-img src="@/assets/イーブイ.gif" />
    </v-layout>
  </v-card>
</template>

<script>
export default {
  name: "ContentsViews",
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
