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
      <v-row :align="align">
        <v-col class="text">
          <v-btn v-for="pokemon in 1" :key="pokemon.name"
            ><h1>{{ ramdom() }}</h1></v-btn
          >
        </v-col>
      </v-row>
      <br />

      <v-row>
        <v-col>
          <v-btn v-for="pokemon in 1" :key="pokemon.name"
            ><h1>{{ ramdom() }}</h1></v-btn
          >
        </v-col>
      </v-row>
    </v-card-text>
    <v-card-actions> </v-card-actions>

    <v-layout class="size position">
      <v-img src="@/assets/イーブイ.gif" />
    </v-layout>
  </v-card>
</template>

<script>
import POKEMON from "@/common/pokemon";

export default {
  name: "ContentsViews",

  methods: {
    ramdom: function() {
      const ary = Math.floor(Math.random() * this.pokemons.length);
      return this.pokemons[ary].name;
    },
    // answer: function() {
    //     const
    // }
  },
  data: () => ({
    pokemons: POKEMON.POKEMONS,
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
