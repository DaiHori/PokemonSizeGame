import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/answer",
    name: "answer",
    component: () => import("../views/Answer.vue"),
  },
  {
    path: "/incorrectanswer",
    name: "IncorrectAnswer",
    component: () => import("../views/IncorrectAnswer.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
