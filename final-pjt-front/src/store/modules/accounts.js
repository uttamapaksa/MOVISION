import router from '@/router'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  state: {
    token: null,
		currentuser: null,
    userdata: null,
  },
  getters: {    
    isLogin: (state) => state.token ? true : false,
    authHeader: (state) => ({Authorization: `Token ${state.token}`}),
    currentuser: (state) => state.currentuser,
    userdata: (state) => state.userdata,
  },
  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentuser = user,
    SET_USERDATA: (state, userdata) => state.userdata = userdata,
  },
  actions: {
    signUp(context, data) {
      console.log('signup.axios')
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data,
      })
      .then(res => {
        console.log('signup.then')
        console.log(res)
        context.commit('SET_TOKEN', res.data.key)
        context.dispatch('getCurrentUser')
        // context.dispatch('userdatasignUp')
        // router.push({name: 'MainView'})
        
        
      })
      .catch(err => {
        console.log(err)
      }) 
    },
    userdatasignUp(context, id) {
      console.log('userdata.axios')
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/profile/${id}/`,
        data: {
          nickname: id, user: id,
        },
        headers: this.getters.authHeader,
      })
      .then(res => {
        console.log(res)
        console.log('userdata.then')
        context.commit('SET_USERDATA', res.data)
        router.push({name: 'MainView'})
      })
      .catch(err => {
        console.log(err)
        console.log('userdata.catch')
      })
    },
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
        // commit('SET_USERINFO', null)
        // router.push({name: 'LogInView'})
      })
      .catch(err => {
        console.log(err)
        console.log('logout.catch')
      })
    },
    getCurrentUser({ dispatch, commit, getters }) {
      console.log('currentuser.axios')
      axios({
        url: `${API_URL}/accounts/user/`,
        method: 'get',
        headers: getters.authHeader,
      })
      .then((res) => {
        console.log(res)
        console.log('currentuser.then')
        commit("SET_CURRENT_USER", res.data.pk)
        dispatch("userdatasignUp", res.data.pk)
      })
      .catch((err) => {
        console.log(err)
        console.log('currentuser.catch')
    })
		},
  },
}
