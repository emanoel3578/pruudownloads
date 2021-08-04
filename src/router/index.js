import { createWebHistory, createRouter } from "vue-router";
import Maingames from "@/views/Maingames.vue";
import Game from "@/views/Game.vue";

const routes = [
  {
    path: "/home",
    name: "Home",
    component: Maingames,
  },
  {
    path: "/game/:name",
    name: "Game",
    component: Game,
    props: true,
  },
  {
    path:"", 
    redirect:"/home"
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;