import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  state: {
    totalgenres: {12:'모험', 14:'판타지', 16:'애니메이션', 18:'드라마', 27:'공포', 28:'액션', 35: '코미디', 36: '역사',37: '서부', 53: '스릴러', 80: '범죄',99: '다큐멘터리',878: 'SF',9648: '미스터리',10402: '음악',10749: '로맨스',10751: '가족', 10752: '전쟁',10770: 'TV영화',},
    movies: [],
    movie: null,
    movie_comments: [],
    movie_likes: [],
    movie_seens: [],
    top10_movies: [],
    recent30_movies: [],
    new10_movies: [],
    recommend_moives: [],
  },
  
  getters: {
    totalgenres: (state) => state.totalgenres,
    movie: (state) => state.movie,
    movies: (state) => state.movies,
    movie_comments: (state) => state.movie_comments,
    movie_likes: (state) => state.movie_likes,
    movie_seens: (state) => state.movie_seens,
    top10_movies: (state) => state.top10_movies,
    recent30_movies: (state) => state.recent30_movies,
    new10_movies: (state) => state.new10_movies,
    recommend_moives: (state) => state.recommend_moives,
  },

  mutations: {
    GET_MOVIES: (state, movies) => state.movies = movies,
    GET_TOP10_MOVIES(state, movies) {
      const top10_movies = movies.sort(function (a,b) {
        return b.vote_average - a.vote_average
      }).slice(0,10)
      return state.top10_movies = top10_movies
    },
    GET_RECENT30_MOVIES(state, movies) {
      const recent30_movies = movies.sort(function (a,b) {
        return new Date(b.release_date) - new Date(a.release_date)
      }).slice(10,40)
      return state.recent30_movies = recent30_movies
    },
    GET_NEW10_MOVIES(state, movies) {
      const new10_movies = movies.sort(function (a,b) {
        return new Date(b.release_date) - new Date(a.release_date)
        // return 0.5 - Math.random()
      }).slice(0,10)
      return state.new10_movies = new10_movies
    },
    GET_MOVIE_DETAIL: (state, movie) => state.movie = movie,
    GET_MOVIE_COMMENTS: (state, movie_comments) => state.movie_comments = movie_comments,
    GET_MOVIE_LIKES: (state, movie_likes) => state.movie_likes = movie_likes,
    GET_RECOMMEND_MOVIES: (state, recommend_moives) => state.recommend_moives = recommend_moives,
  },

  actions: {
    //영화
    fetchMovies(context) {
      axios({
        method:'get',
        url: `${API_URL}/api/v1/`,
      })
        .then((res)=> {
          console.log('fetchMovies.then')
          context.commit('GET_MOVIES', res.data)
          context.commit('GET_TOP10_MOVIES', res.data)
          context.commit('GET_RECENT30_MOVIES', res.data)
          context.commit('GET_NEW10_MOVIES', res.data)
        })
        .catch((err) => {
          console.log(err)
          console.log('fetchMovies.catch')
        })
    },
    getMovieDetail(context, id) {
      axios({
        method: 'get',
        url:`http://127.0.0.1:8000/api/v1/detail/${id}/`,
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
        url:`http://127.0.0.1:8000/api/v1/detail/${id}/comment_list/`,
      })
        .then(res => {
          console.log(res,'댓글생성확인')
          context.commit('GET_MOVIE_COMMENTS', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    likeMovie(context, movie_id) {
      console.log('likemovie.axios')
      axios({ 
        method: 'post',
        url: `${API_URL}/api/v1/detail/${movie_id}/like/`,
        data: {
          user: this.getters.currentuser,
        },
        headers: this.getters.authHeader,
      })
        .then(res => {
          console.log(res)
          console.log('likemovie.then')
          context.dispatch('getMovieDetail', movie_id)
        })
        .catch(err => {
          console.log(err)
          console.log('likemovie.catch')
        })
    },
    seenMovie(context, movie_id) {
      console.log('seenmovie.axios')
      axios({ 
        method: 'post',
        url: `${API_URL}/api/v1/detail/${movie_id}/seen/`,
        data: {
          user: this.getters.currentuser,
        },
        headers: this.getters.authHeader,
      })
        .then(res => {
          console.log(res)
          console.log('seenmovie.then')
          context.dispatch('getMovieDetail', movie_id)
        })
        .catch(err => {
          console.log(err)
          console.log('seenmovie.catch')
        })
    },
    getRecommendMovies(context, user_id) {
      console.log('recommendmovie.axios')
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/${user_id}/recommendation/`,
      })
      .then(res => {
        console.log(res)
        console.log('recommendmovie.then')
        context.commit('GET_RECOMMEND_MOVIES', res.data)
      })
      .catch(err => {
        console.log(err)
        console.log('recommendmovie.catch')
      })
    }
  }
}