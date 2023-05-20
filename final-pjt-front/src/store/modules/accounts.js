import router from '@/router'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  state: {
    token: null,
		currentuser: null,
    // userInfo: null,
  },
  getters: {    
    isLogin: (state) => state.token ? true : false,
    authHeader: (state) => ({Authorization: `Token ${state.token}`}),
    currentuser: (state) => state.currentuser,
  },
  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentuser = user,
    // SET_USERINFO: (state, userInfo) => state.userInfo = userInfo,
  },
  actions: {
    signUp(context, data) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data,
      })
        .then(res => {
          console.log(res)
          context.commit('SET_TOKEN', res.data.key)
          context.dispatch('getCurrentUser')
          router.push({name: 'MainView'})
        })
        .catch(err => console.log(err))
    },
    logIn(context, data) {     
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data,
      })
        .then(res => {
          console.log(res)
          context.commit('SET_TOKEN', res.data.key)
          context.dispatch('getCurrentUser')
          // context.dispatch('getUserInfo')
        })
        .catch(err => console.log(err))      
    },
    // getUserInfo({getters, commit}) {
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/accounts/user/`,
    //     headers: getters.authHeader
    //   })
    //     .then(res => {
    //       console.log(res)
    //       commit('SET_USERINFO', res.data)
    //     })
    //     .catch(err => console.log(err))
    // },
    logOut({commit, getters}) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res)
          commit('SET_TOKEN', null)
          // commit('SET_USERINFO', null)
          // router.push({name: 'LogInView'})
        })
        .catch(err => console.log(err))
    },
    getCurrentUser({ commit, getters }) {
      console.log(111)
      axios({
        url: `${API_URL}/accounts/user/`,
        method: 'get',
        headers: getters.authHeader,
      })
        .then((res) => {
          console.log(res)
          commit("SET_CURRENT_USER", res.data.pk)
        })
        .catch((err) => {
          console.log(err)
        })
		},
  },
}
