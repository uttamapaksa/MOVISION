import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '../views/MainView'
import SearchView from '../views/SearchView'
import RecommendView from '../views/RecommendView'
import CommunityView from '../views/CommunityView'
import ProfileView from '../views/ProfileView'
import SignUpView from '../views/SignUpView'
import MovieDetailView from '../views/MovieDetailView.vue'
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
  routes,
  
})

// router.beforeRouteUpdate((to, from, next) => {
//   // 모든 URL 이동 시 실행되는 로직
//   console.log('URL이 변경되어 모든 컴포넌트를 새로 렌더링합니다.');
//   next();
// });

  // router.beforeEach(to, from, next) {
  //   // this.maintextvis =  0,
  //   console.log('이동')
  //   this.scale = 1 // 초기 축소 비율
  //   const mainVideo = document.querySelector('.mainvideo')
  //   mainVideo.style.opacity = 1;
  //   this.$refs.videoContainer.style.transform = `scale(${this.scale})`;
  //   document.body.style.overflow = '';
  //   next()
  // },


export default router
