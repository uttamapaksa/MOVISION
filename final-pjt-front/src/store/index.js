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
    review_comments: [],
    party_articles: [],
    party_comments: [],
    party: false,
  },

  mutations: {
    //게시판
    GET_REVIEWARTICLES: (state, articles)=> state.review_articles = articles,
    GET_PARTYARTICLES: (state, articles) => state.party_articles = articles,
    //게시판 종류 체크
    SET_PARTY: (state, party) => state.party = party,
    //리뷰게시판 댓글
    GET_REVIEWCOMMENT: (state,review_comments) => state.review_comments = review_comments,
  },
  actions: {
    //게시판
    getReviewArticles(context) {   //리뷰게시판 조회
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/reviews/`,
      })
        .then((res) => {
          context.commit('GET_REVIEWARTICLES', res.data)
        })
        .catch((err) => {
        console.log(err)
        console.log('리뷰게시판 내용이 없어')
      })
    },
    getPartyArticles(context) {     //파티게시판 조회
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
        console.log('파티게시판 내용이 없어')
      })
      // 게시글 아무것도 없을 시 404 에러
    },
    setparty(context, data) {
      context.commit('SET_PARTY', data)
    },

    //리뷰게시판 댓글 조회
    getreviewcomment(context) {  
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/review_comments/`,
      })
        .then((res) => {
          console.log(res, context)
          context.commit('GET_REVIEWCOMMENT', res.data)
        })
        .catch((err) => {
          console.log(err)
          console.log('리뷰 내용이 없어')
      })
    }
  },
  
  modules: {
    accounts,
    moviestore,
  },
})
