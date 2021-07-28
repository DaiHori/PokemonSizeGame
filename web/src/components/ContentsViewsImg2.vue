<template>
  <v-layout class="position">
    <div class="size align-end" v-for="img in imgs" :key="img.imgs">
      <v-img :src="img.img2" />
    </div>
  </v-layout>
</template>

<script>
export default {
  name: "ContentsViewsImg2",

  data: () => ({
    imgs: [
      {
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
