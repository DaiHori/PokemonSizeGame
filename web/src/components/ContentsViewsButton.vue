<template>
  <v-container>
    <v-row>
      <v-col class="text">
        <v-btn v-for="pokemon in 1" :key="pokemon.name"
          ><h1>{{ ramdom() }}</h1></v-btn
        >
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import POKEMON from "@/common/pokemon";

export default {
  name: "ContentsViewsButton",

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
