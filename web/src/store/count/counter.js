export const state = {
  counter: 1,
};

export const mutations = {
  increment(state) {
    state.counter++;
  },
};
export const actions = {
  increment({ commit }) {
    commit("increment");
  },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
};
