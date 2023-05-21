import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '../views/MainView'
import SearchView from '../views/SearchView'
import RecommendView from '../views/RecommendView'
import CommunityView from '../views/CommunityView'
import ProfileView from '../views/ProfileView'
import SignUpView from '../views/SignUpView'
import MovieDetailView from '../views/MovieDetailView'
import ReviewCreateView from '@/views/ReviewCreateView'
import PartyCreateView from '@/views/PartyCreateView'
import ReviewDetialView from '@/views/ReviewDetialView'
import PartyDetialView from '@/views/PartyDetialView'
Vue.use(VueRouter)

const routes = [

  {
    path: '/',
    name: 'MainView',
    component: MainView
  },
  {
    path: '/search',
    name: 'SearchView',
    component: SearchView
  },
  {
    path: '/recommend',
    name: 'RecommendView',
    component: RecommendView
  },
  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView
  },
  {
    path: '/profile/:profile_id',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/movie/:movie_id',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path: '/review_create',
    name: 'ReviewCreateView',
    component: ReviewCreateView
  },
  {
    path: '/party_create',
    name: 'PartyCreateView',
    component: PartyCreateView
  },
  {
    path: '/party/:party_id',
    name: 'PartyDetialView',
    component: PartyDetialView
  },
  {
    path: '/review/:review_id',
    name: 'ReviewDetialView',
    component: ReviewDetialView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
