import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import accounts from './modules/accounts'
import moviestore from './modules/moviestore'
Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'


export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    review_articles: [],
    party_articles: [],
    movies: [],
    movie: null,
    party: false,
    movie_comments: [],
  },

  mutations: {
    // GET_ARTICLES(state,articles) {
    //   state.articles = articles
    // },
    //영화
    GET_MOVIES: (state, movies) => state.movies = movies,
    GET_MOVIE_DETAIL: (state, movie) => state.movie = movie,
    GET_MOVIE_COMMENTS: (state, movie_comments) => state.movie_comments = movie_comments,



    //게시판
    GET_REVIEWARTICLES: (state, articles)=> state.review_articles = articles,
    GET_PARTYARTICLES: (state, articles) => state.party_articles = articles,
    //게시판 종류 체크
    SET_PARTY: (state, party) => state.party = party
  },
  actions: {
    //영화
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
        method: 'get',
        url:`http://127.0.0.1:8000/api/v1/detail/${id}`,
      })
        .then(res => {
          context.commit('GET_MOVIE_DETAIL', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    getMovieComments(context,id) {
      axios({
        method: 'get',
        url:`http://127.0.0.1:8000/api/v1/detail/${id}/comment_list`,
      })
        .then(res => {
          console.log(res,'댓글생성확인')
          context.commit('GET_MOVIE_COMMENTS', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },


    //게시판
    getReviewArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/reviews/`,
      })
        .then((res) => {
          context.commit('GET_REVIEWARTICLES', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },

    getPartyArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/parties/`,
      })
        .then((res) => {
        console.log(res, context)
          context.commit('GET_PARTYARTICLES', res.data)
        })
        .catch((err) => {
        console.log(err)
        console.log('에러2')
      })
      // 게시글 아무것도 없을 시 404 에러
    },
    setparty(context, data) {
      context.commit('SET_PARTY', data)
    }
  },
  modules: {
    accounts,
    moviestore,
  }
})
