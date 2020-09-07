import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home";
import Users from "../components/Users";
import Detail from "../components/Detail";


Vue.use(Router)

export default new Router({
  routes: [
      {path:'/',component:Home},
      {path:'/home',component:Home},
      {path:'/users',component:Users},
      {path:'/detail/:id/:name/:age',component:Detail},
      {path:'/*',component:Home},
  ]
})
