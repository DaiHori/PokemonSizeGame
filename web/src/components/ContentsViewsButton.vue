<template>
  <v-container>
    <v-row>
      <v-col class="text">
        <v-btn v-for="pokemon in 1" :key="pokemon.name" @click="answer1"
          ><h1>{{ pokemons[pokemon1].name }}</h1></v-btn
        >
        <v-btn v-for="pokemon in 1" :key="pokemon.name" @click="answer2"
          ><h1>{{ pokemons[pokemon2].name }}</h1></v-btn
        >
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState, mapGetters } from "vuex";

export default {
  name: "ContentsViewsButton",

  created() {
    this.pokemon1 = this.random1();
    this.pokemon2 = this.random1();
  },
  methods: {
    random1: function() {
      const ary = Math.floor(Math.random() * pokemonAry);
      return ary;
    },
    answer1: function() {
      if (
        this.pokemons[this.pokemon1].weight >
        this.pokemons[this.pokemon2].weight
      ) {
        this.$router.push({
          name: "Answer",
        });
      } else {
        this.$router.push({
          name: "IncorrectAnswer",
        });
      }
    },
    answer2: function() {
      if (
        this.pokemons[this.pokemon1].weight <
        this.pokemons[this.pokemon2].weight
      ) {
        this.$router.push({
          name: "Answer",
        });
      } else {
        this.$router.push({
          name: "IncorrectAnswer",
        });
      }
    },
  },
  computed: {
    ...mapState("pokemonAnswer", ["pokemons"]),
    ...mapGetters("answer", ["pokemonAry"]),
  },
  data: () => ({
    pokemon1: "",
    pokemon2: "",
  }),
};
</script>
