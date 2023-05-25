<template>
<div>
  <div class="poster-line">
    <!-- <div class="poster-header" style="position:absolute; ">
      <img :src="`https://image.tmdb.org/t/p/original${movie.backdrop_path}`"  style="opacity: 0.5; z-index: -10; object-fit: cover; width: 100%; height: 100%;" alt="...">
    </div>
    <div class="poster-img" style="z-index: 20;">
      <img :src="`https://image.tmdb.org/t/p/w400${movie.poster_path}`" class="card-img-detail" alt="..." style="z-index: 20;"> 
    </div> -->
    <div class="poster-detail">
      <div class="detail-info container">
        <div class="row h-50">
          <div class="detailss detailss-title my-auto ">
            {{ movie.title }}({{ movie.release_date.slice(0,4) }})
          </div>
        </div>
        <div class="row h-25">
          <div class="detailss col-2">장르
            <span v-for="genre in movie.genres" :key="genre.id">
              {{ genre.name }}
            </span>
          </div>
          <div class="detailss col-2">인기 {{ movie.popularity }}</div>
          <div class="detailss col-2">개봉일{{ movie.release_date }}</div>
          <div class="detailss col-2">
            <!-- <router-link :to="`https://www.youtube.com/`" target="_blank">예고편 보기</router-link> -->
            <a :href="`https://www.youtube.com/watch?v=${movie.youtube_key}`">예고편 보기</a> 
          </div>
        </div>
        <div class="row h-25">
          <div class="detailss col-2">평점 {{ movie.vote_average }}</div>
          <div class="detailss col-2" @click="likemovie">
            좋아요 개수 : {{ movie.like_users.length }}
            ❤
          </div>
          <div class="detailss col-2" @click="seenmovie">
            봤어요 개수 : {{ movie.seen_users.length}}
            <div>
              ⭐
              </div>
          </div>
          <div class="detailss col-2">언어(보류)</div>
        </div>
        <div  class="ratio ratio-16x9">
          <iframe :src="videoUrl" frameborder="0"></iframe>
        </div>
      </div>
      
      <div class="detail-overview">
        <div class="detailss">개요 {{ movie.overview }}</div>
      </div>
    </div>
    
  </div>

  <div class="one-comment">한줄평
    
    <div v-for="comment in movie_comments" :key="comment.id">
      {{ comment.content }} | 
      {{ comment.username }} | 
      {{ comment.created_at.slice(0, 10) }}
      <button v-if="comment.user==currentuser" @click="movieCommentDelete(comment.id)">삭제 </button>
    </div>
  </div>
  <div>
    <input type="text" v-model="one_comment" @keyup.enter="save_comment">
    <button @click="save_comment">한줄평 작성</button>
  </div>
  <div class="">이 영화를 좋아하는 사람들이 본 영화</div>
  <div class="director-actor">
    <div v-for="actor in movie.actors" :key="actor.id" class="actors-item">
      {{ actor.name }}
      <img :src="`https://image.tmdb.org/t/p/original${actor.poster_path}`" class="actor-image" alt="...">
    </div>
  </div>
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
      return this.$store.getters.movie
    },
    release_year() {
      return this.movie.release_date.slice(0,4)
    },
    videoUrl () {
      return `https://www.youtube.com/embed/${this.movie.youtube_key}`
    },
    movie_comments() {
      const movie_id = this.$route.params.movie_id
      return this.$store.getters.movie_comments.filter(comment => comment.movie == movie_id)
    },
    currentuser() {
      return this.$store.getters.currentuser
    },
    movie_id() {
      return this.$route.params.movie_id
    }
  },
  methods: {
    save_comment() {
      const movie_id = this.$route.params.movie_id
      const currentuser = this.$store.getters.currentuser
      const currentusername = this.$store.getters.currentusername
      const authHeader = this.$store.getters.authHeader
      console.log(authHeader)
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/detail/${movie_id}/comment_list/`,
        data: {
          user: currentuser, username: currentusername, movie: movie_id, content: this.one_comment,
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
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/movie_comment/${comment_id}/`,
      })
       .then(res => {
         const movie_id = this.$route.params.movie_id
        console.log(res)
        this.$store.dispatch('getMovieComments', movie_id)
       })
       .catch(err => {
         console.log(err)
       })
    },
    likemovie() {
      const movie_id = this.$route.params.movie_id
      if (!this.currentuser) {
        alert('로그인 해야 좋아요를 누를 수 있습니다')
        return
      }
      this.$store.dispatch('likeMovie', movie_id)
    },
    seenmovie() {
      const movie_id = this.$route.params.movie_id
      if (!this.currentuser) {
        alert('로그인 해야 봤어요를 누를 수 있습니다')
        return
      }
      this.$store.dispatch('seenMovie', movie_id)
    },
  },
}
</script>

<style>

/* 포스터+설명 박스 */
.poster-line {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  border: solid 3px blueviolet;
  width: 90%;
  height: 68vh;
}

/* 포스터 이미지 박스 */
.poster-img {
  border: solid 3px blueviolet;
  width: 30%;
  height: 63vh;
}

/* 포스터 이미지 */
.card-img-detail {
  height: 100%;
  /* object-fit: cover; */
}

/* 영화 정보 박스 */
.poster-detail {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 65%;
  height: 63vh;
  margin: 5% 0;
}

/* 영화 세부 정보 */
.detail-info {
  border: solid 3px blueviolet;
  width: 100%;
  height: 60%;
}

/* 영화 세부 정보 하위 박스 */
.detailss {
  border: solid 2px lightcoral;
  /* height: 100%; */
}

.detailss-title {
  font-size: 5vh;
}

/* 영화 개요 */
.detail-overview {
  border: solid 3px blueviolet;
  overflow: hidden;
  width: 100%;
  height: 40%;
}


.one-comment {
  border: solid 3px blueviolet;
  width: 90%;
  height: 20vh;
}

.director-actor {
  display: flex;
  border: solid 3px blue;
  width: 90%;
  height: 35vh;
}

.actor-image {
  height: 80%;
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