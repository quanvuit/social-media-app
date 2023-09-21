import { createRouter, createWebHistory } from "vue-router";
import HomeLayout from "../layouts/HomeLayout.vue";
// import ProductLayout from "../layouts/ProductLayout.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      redirect: "/",
      component: HomeLayout,
      children: [
        {
          path: "/",
          component: () => import("../views/HomeView.vue"),
        },
        {
          path: "/Follows",
          component: () => import("../views/FollowsView.vue"),
        },
        {
          path: "/Profile",
          component: () => import("../views/ProfileView.vue"),
        },
        {
          path: "/Search-Friends",
          component: () => import("../views/SfView.vue"),
        },
        {
          path: "/Profile-Friends/:user",
          component: () => import("../views/PfView.vue"),
        },
      ]
    },
  ],
  scrollBehavior() {
    window.scrollTo(0, 0);
  },
});

export default router;
