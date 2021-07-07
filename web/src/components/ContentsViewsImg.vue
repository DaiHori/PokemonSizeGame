<template>
  <div>
    <v-layout>
      <div class="size align-end" v-for="img in imgs" :key="img.imgs">
        <v-img :src="img.img1" />
      </div>
    </v-layout>
  </div>
</template>

<script>
export default {
  name: "ContentsViewsImg",

  data: () => ({
    imgs: [
      {
        img1: require("@/assets/ピカチュウ_なみのり.gif"),
        img2: require("@/assets/イーブイ.gif"),
      },
    ],
  }),
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
