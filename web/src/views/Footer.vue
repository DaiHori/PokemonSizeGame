<template>
  <v-footer dark padless>
    <v-card color="white" class="flex" flat tile>
      <v-card-title class="black">
        <v-layout justify-center>
          <v-btn v-for="item in items" :key="item.icon" icon @click="moveLink">
            <v-icon class="position" size="68px">{{ item.icon }}</v-icon>
          </v-btn>
        </v-layout>
      </v-card-title>

      <v-card-text class="py-2 black--text text-center">
        ©{{ new Date().getFullYear() }} — <strong>DaiHori</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  methods: {
    moveLink: () => {
      window.open("https://github.com/DaiHori/PokemonSizeGame", "_blank");
    },
  },
  data: () => ({
    items: [
      {
        icon: "mdi-github",
      },
    ],
  }),
};
</script>

<style lang="scss">
.position {
  float: right;
}
</style>
