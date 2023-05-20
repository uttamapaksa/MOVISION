import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import accounts from './modules/accounts'
Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'


export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    // articles: [], 
    movies: [],
    movie: null,
  },

  mutations: {
    // GET_ARTICLES(state,articles) {
    //   state.articles = articles
    // },

    GET_MOVIES: (state, movies) => state.movies = movies,
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
      axios({
        method:'get',
        url: `${API_URL}/api/v1/`,
      })
        .then((res)=> {
          context.commit('GET_MOVIES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
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
          console.log(err)
        })
    },
  },
  modules: {
    accounts,
  }
})
