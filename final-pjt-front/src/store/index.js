import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles: [], 
    movies: [],
    movie: null,
    token: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    // GET_ARTICLES(state,articles) {
    //   state.articles = articles
    // },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'ArticleView'}) // store/index.js $router 접근 불가 -> import를 해야함
    },

    GET_MOVIES(state,movies) {
      state.movies = movies
      console.log(movies)
    },
    GET_MOVIE_DETAIL: (state, movie) => state.movie = movie,
  },
  actions: {
    // getArticles(context) {
    //   axios({
    //     method:'get',
    //     url: `${API_URL}/api/v1/articles/`,
    //   })
    //     .then((res)=> {
    //       context.commit('GET_ARTICLES',res.data)
    //     })
    //     .catch((err) => {
    //       console.log(err)
    //     })
    // },
    fetchMovies(context) {
      console.log('push123')
      axios({
        method:'get',
        url: `${API_URL}/api/v1/`,
      })
        .then((res)=> {
          context.commit('GET_MOVIES',res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          // console.log(res)
          // context.commit('SIGN_UP', res.data.key)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    login(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        })
      .catch((err) => console.log(err))
    },
    getMovieDetail(context, id) {
      axios({
        url:`http://127.0.0.1:8000/api/v1/movies/${id}`,
        method: 'get',
      })
        .then(res => {
          console.log(res)
          context.commit('GET_MOVIE_DETAIL', res.data)
        })
        .catch(err => {
          console.log('err')
          console.log(err)
        })
    },
  },
  modules: {
  }
})
