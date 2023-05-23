import router from '@/router'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  state: {
    token: null,
		currentuser: null,
		currentusername: null,
    profile: null,
  },
  getters: {    
    isLogin: (state) => state.token ? true : false,
    authHeader: (state) => ({Authorization: `Token ${state.token}`}),
    currentuser: (state) => state.currentuser,
    currentusername: (state) => state.currentusername,
    profile: (state) => state.profile,
  },
  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentuser = user,
    SET_CURRENT_USERNAME: (state, username) => state.currentusername = username,
    SET_PROFILE: (state, profile) => state.profile = profile,
  },
  actions: {

    // 회원가입
    signUp(context, data) {
      console.log('signup.axios')
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data,
      })
      .then(res => {
        console.log(res)
        console.log('signup.then')
        context.commit('SET_TOKEN', res.data.key)
        context.dispatch('getCurrentUser')
        router.push({name: 'MainView'})
      })
      .catch(err => {
        console.log(err)
        console.log('signup.catch')
      }) 
    },

    // 로그인
    logIn(context, data) {     
      console.log('login.axios')
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data,
      })
      .then(res => {
        console.log(res)
        console.log('login.then')
        context.commit('SET_TOKEN', res.data.key)
        context.dispatch('getCurrentUser')
        // context.dispatch('getUserInfo')
      })
      .catch(err => {
        console.log(err)
        console.log('login.catch')
      })
    },

    // 로그아웃
    logOut({commit, getters}) {
      console.log('logout.axios')
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: getters.authHeader,
      })
      .then(res => {
        console.log(res)
        console.log('logout.then')
        commit('SET_TOKEN', null)
        commit('SET_CURRENT_USER', null)
        commit('SET_CURRENT_USERNAME', null)
      })
      .catch(err => {
        console.log(err)
        console.log('logout.catch')
      })
    },

    // 현재 로그인한 유저(나)
    getCurrentUser({ commit, getters }) {
      console.log('currentuser.axios')
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: getters.authHeader,
      })
      .then((res) => {
        console.log(res)
        console.log('currentuser.then')
        commit("SET_CURRENT_USER", res.data.pk)
        commit("SET_CURRENT_USERNAME", res.data.username)
      })
      .catch((err) => {
        console.log(err)
        console.log('currentuser.catch')
      })
		},

    // 현재 프로필 페이지
    getProfile(context, id) {
      console.log('getprofile.axios')
      axios({
        method:'get',
        url: `${API_URL}/api/v1/profile/${id}/`,
      })
      .then((res) => {
        console.log(res)
        console.log('getprofile.then')
        context.commit('SET_PROFILE', res.data)
      })
      .catch((err) => {
        console.log(err)
        console.log('getprofile.catch')
      })
    },
    
    // 팔로우, 언팔로우
    follow(context, id) {
      console.log('follow.axios')
      axios({
        method:'post',
        url: `${API_URL}/api/v1/profile/${id}/follow/`,
        headers: this.getters.authHeader,
      })
      .then((res) => {
        console.log(res)
        console.log('follow.then')
        context.dispatch('getProfile', id)
      })
      .catch((err) => {
        console.log(err)
        console.log('follow.catch')
      })
    }
  },
}
