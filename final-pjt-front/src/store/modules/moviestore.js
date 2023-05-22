import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  state: {
    totalgenres: { 12: '모험',
      14: '판타지',
      16: '애니메이션',
      18: '드라마', 
      27: '공포', 
      28: '액션', 
      35: '코미디', 
      36: '역사',
      37: '서부', 
      53: '스릴러', 
      80: '범죄',
      99: '다큐멘터리',
      878: 'SF',
      9648: '미스터리',
      10402: '음악',
      10749: '로맨스',
      10751: '가족', 
      10752: '전쟁',
      10770: 'TV영화',
    },
    movies: [],
    movie_comments: [],
    movie: null,
  },
  getters: {
    totalgenres: (state) => state.totalgenres,
  },
  mutaions: {
    GET_MOVIES: (state, movies) => state.movies = movies,
    GET_MOVIE_DETAIL: (state, movie) => state.movie = movie,
    GET_MOVIE_COMMENTS: (state, movie_comments) => state.movie_comments = movie_comments,
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
  }
}