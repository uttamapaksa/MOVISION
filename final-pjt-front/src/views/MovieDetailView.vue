<template>
<div id="moviedetailview">
  <div class="poster-header">poster header</div>
  <div class="poster-line">
    <div class="poster-img">
      <img :src="`https://image.tmdb.org/t/p/w400${movie.poster_path}`" class="card-img-top" alt="...">
    </div>

    <div class="poster-detail">
      <div class="detail-info">
        <div class="detailss">영화제목 {{ movie.id }}</div>
        <div class="detailss">상영년도{{ release_year }}</div>
        <div class="detailss">평점 {{ movie.vote_average }}</div>
        <div class="detailss">장르 {{ movie.genres }}</div> (누르면 장르 검색창 이동)
        <div class="detailss">인기 {{ movie.popularity }}</div>
        <div class="detailss">개봉일{{ movie.release_date }}</div>
        <div class="detailss">좋아요 {{ movie.like_users }}</div> ()
        <div class="detailss"> 찜하기 버튼(토글)(MtoM: Movie-User)</div> ()
        <div class="detailss"> 본 영화 버튼(토글)(MtoM: Movie-User)</div> ()
        <div class="detailss">언어(보류)</div>
        <div class="detailss">예고편보기</div>
        <!-- <div  class="ratio ratio-16x9">
          <iframe :src="videoUrl" frameborder="0"></iframe>
        </div> -->
      </div>
      
      <div class="detail-overview">
        <div class="detailss">개요 {{ movie.overview }}</div>
      </div>
    </div>
    
  </div>

  <div class="one-comment">one comment
    <input type="text" v-model="one_comment" @keyup.enter="save_comment">
    <button @click="save_comment">댓글작성</button>

    <div v-for="comment in movie_comments" :key="comment.id">
      {{ comment }}
      <button @click="movieCommentDelete(comment.id)">삭제 </button>
    </div>
  </div>
  <div class="">이 영화를 좋아하는 사람들이 본 영화</div>
  <div class="director-actor">director-actor</div>
  <div class="detail-ost">OST</div>

  <div class="reviews row">
    <h1>리뷰</h1>
    <div class="review col-5 m-auto"></div>
    <div class="review col-5 m-auto"></div>
    <div class="review col-5 m-auto"></div>
    <div class="review col-5 m-auto"></div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetailView',
  mounted() {
    const current_id = this.$route.params.movie_id
    this.$store.dispatch('getMovieDetail', current_id)
    this.$store.dispatch('getMovieComments', current_id)
  },
  data() {
    return {
      one_comment: '',
    }
  },
  computed: {
    movie() {
      return this.$store.state.movie
    },
  //   movie() {
  //     const current_id = this.$route.params.movie_id
  //     return this.$store.state.movies.filter(movie => movie.id = current_id )[0]
  //   },
    release_year() {
      return this.movie.release_date.slice(0,4)
    },
    // videoUrl() {
    //   return `https://www.youtube.com/watch?v=${this.movie.youtube_key}`
    // }
    // videoUrl () {
    //   return `https://www.youtube.com/embed/${this.movie.youtube_key}`
    // }
  // },
    movie_comments() {
      const movie_id = this.$route.params.movie_id
      return this.$store.state.movie_comments.filter(comment => comment.movie == movie_id)
    }
  },
  methods: {
    save_comment() {
      const movie_id = this.$route.params.movie_id
      const currentuser = this.$store.getters.currentuser
      const authHeader = this.$store.getters.authHeader
      console.log(authHeader)
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/detail/${movie_id}/comment_list/`,
        data: {
          user: currentuser, movie: movie_id, content: this.one_comment,
        },
        headers: authHeader,
      })
        .then(res => {
          console.log(res)
          this.$store.dispatch('getMovieComments', movie_id)
        })
        .catch(err => {
          console.log(err)
        })
    },
    movieCommentDelete (comment_id) {
      console.log(comment_id)
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/movie_comment/${comment_id}`,
      })
       .then(res => {
        const movie_id = this.$route.params.movie_id
        console.log(res)
        this.$store.dispatch('getMovieComments', movie_id)
       })
       .catch(err => {
         console.log(err)
       })
    }
  }
}
</script>

<style>
.poster-header {
  width: 90%;
  height: 15vh;
  background: orange;
}

.poster-line {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  border: solid 3px blueviolet;
  width: 90%;
  height: 55vh;
}

.poster-img {
  border: solid 3px blueviolet;
  width: 25%;
  height: 45vh;
}

.poster-detail {
  display: flex;
  flex-direction: column;
  width: 65%;
  height: 45vh;
}

.detail-info {
  border: solid 3px blueviolet;
  width: 100%;
  height: 60%;
  
}
.detail-overview {
  border: solid 3px blueviolet;
  overflow: hidden;
  width: 100%;
  height: 40%;
}

.detailss {
  border: solid 2px lightcoral;
  /* width: 20%; */
  height: 10%;
}

.one-comment {
  border: solid 3px blueviolet;
  width: 90%;
  height: 20vh;
}

.director-actor {
  border: solid 3px blue;
  width: 90%;
  height: 35vh;
}
.detail-ost {
  border: solid 3px blue;
  width: 90%;
  height: 20vh;
}

.reviews {
  display: flex;
  border: solid 3px blue;
  width: 90%;
  height: 40vh;
}

.review {
  border: solid 3px green;
  width: 40%;
  height: 15vh;
}
</style>