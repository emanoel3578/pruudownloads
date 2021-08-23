import { createWebHistory, createRouter } from "vue-router";
import Maingames from "@/views/Maingames.vue";
import Game from "@/views/Game.vue";
import Aboutus from "@/views/Aboutus.vue";
import DMCA from '@/views/DMCA.vue'
import Search from '@/views/Search.vue'
import Page from '@/views/Page.vue'

const routes = [
  {
    path: "/home",
    name: "Home",
    component: Maingames,
  },
  {
    path: "/aboutus",
    name: "Aboutus",
    component: Aboutus,
  },
  {
    path: "/dmca",
    name: "DMCA",
    component: DMCA,
  },
  {
    path: "/game/:name",
    name: "Game",
    component: Game,
    props: true,
  },
  {
    path: "/page/:numberPage",
    name: "Page",
    component: Page,
    props: true,
  },
  {
    path: "/search/s:query",
    name: "Search",
    component: Search,
    props: true,
  },
  {
    path:"", 
    redirect:"/home"
  },
  {
    path:"/page/", 
    redirect:"/home"
  },
  {
    path:"/page/1", 
    redirect:"/home"
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;