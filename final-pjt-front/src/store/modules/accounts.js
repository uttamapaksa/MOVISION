import router from '@/router'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  state: {
    token: null,
		currentuser: null,
		currentusername: null,
    userdata: null,
  },
  getters: {    
    isLogin: (state) => state.token ? true : false,
    authHeader: (state) => ({Authorization: `Token ${state.token}`}),
    currentuser: (state) => state.currentuser,
    currentusername: (state) => state.currentusername,
    userdata: (state) => state.userdata,
  },
  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentuser = user,
    SET_CURRENT_USERNAME: (state, username) => state.currentusername = username,
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
        console.log(res)
        console.log('signup.then')
        context.commit('SET_TOKEN', res.data.key)
        context.dispatch('getCurrentUser', 1)
      })
      .catch(err => {
        console.log(err)
        console.log('signup.catch')
      }) 
    },
    userdatasignUp(context, id) {
      console.log('userdatasignup.axios')
      console.log(id)
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/profile/${id}/`,
        data: {
          user: id, nickname: id, username: this.getters.currentusername,
        },
        headers: this.getters.authHeader,
      })
      .then(res => {
        console.log(res)
        console.log('userdatasignup.then')
        context.dispatch('getUserData')
        router.push({name: 'ProfileView', params: {profile_id: id}})
      })
      .catch(err => {
        console.log(err)
        console.log('userdatasignup.catch')
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
        context.dispatch('getCurrentUser', 0)
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
        commit('SET_CURRENT_USER', null)
        commit('SET_CURRENT_USERNAME', null)
        commit('SET_USERDATA', null)
        // router.push({name: 'LogInView'})
      })
      .catch(err => {
        console.log(err)
        console.log('logout.catch')
      })
    },
    getCurrentUser({ dispatch, commit, getters }, isSignup) {
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
        commit("SET_CURRENT_USERNAME", res.data.username)
        if (isSignup) {
          dispatch("userdatasignUp", res.data.pk)
        } else {
          dispatch('getUserData')
        }
      })
      .catch((err) => {
        console.log(err)
        console.log('currentuser.catch')
      })
		},
    getUserData(context) {
      const user_id = this.getters.currentuser
      console.log(user_id)
      console.log('getuserdata.axios')
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/profile/${user_id}/`,
        headers: this.getters.authHeader,
      })
        .then((res) => {
          console.log(res)
          console.log('getuserdata.then')
          context.commit("SET_USERDATA", res.data[0])
        })
        .catch((err) => {
          console.log(err)
          console.log('getuserdata.catch')
        })
    },
  },
}
