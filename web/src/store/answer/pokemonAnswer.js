import POKEMON from "@/common/pokemon";

export const state = {
  pokemons: POKEMON.POKEMONS,
};
export const getters = {
  pokemonAry(state) {
    return state.pokemons.length;
  },
};
export const mutations = {
  random1(state, { pokemons }) {
    {
      pokemons;
    }
    const ary = Math.floor(Math.random() * this.pokemons.length);
    return ary;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
