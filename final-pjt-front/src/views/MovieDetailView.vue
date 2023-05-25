<template>
  <div id="moviedetailview">
    <div class="poster-line">
      <div class="poster-header" style="position:fixed; z-index: -100; ">
        <img :src="`https://image.tmdb.org/t/p/original${movie.backdrop_path}`"  style="opacity: 0.3; width: 110vw" alt="...">
      </div>
      <div class="poster-img" style="z-index: 20;">
        <img :src="`https://image.tmdb.org/t/p/w400${movie.poster_path}`" class="card-img-detail" alt="..." style="z-index: 20;"> 
      </div>
      <div class="poster-detail">
        <div class="detail-info container">
        <div class="row">
          <div class="detailss detailss-title my-auto ">
            {{ movie.title }}({{ movie.release_date.slice(0,4) }})
          </div>
        </div>
        <div class="row movie-detail-info">
          <div class="col-5 movie-detail-text">


            <div class="row">
              <div class="detailss col-8">
                <span v-for="genre in movie.genres" :key="genre.id">
                  {{ genre.name }}
                </span>
              </div>
              <!-- <div class="detailssss col-4">인기 {{ movie.popularity }}</div> -->
              <div class="detailss col-4">{{ movie.release_date }}</div>
              <!-- <div class="detailss col-2">
                <a :href="`https://www.youtube.com/watch?v=${movie.youtube_key}`">예고편 보기</a> 
              </div> -->
            </div>
            <div class="row ">
              <br>
              <div class="detailss col-4">평점 {{ movie.vote_average }}</div>
              <div class="detailssss col-4" @click="likemovie">
                <br>
                <svg v-if="isLike" style="width: 45%;" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M47.6 300.4L228.3 469.1c7.5 7 17.4 10.9 27.7 10.9s20.2-3.9 27.7-10.9L464.4 300.4c30.4-28.3 47.6-68 47.6-109.5v-5.8c0-69.9-50.5-129.5-119.4-141C347 36.5 300.6 51.4 268 84L256 96 244 84c-32.6-32.6-79-47.5-124.6-39.9C50.5 55.6 0 115.2 0 185.1v5.8c0 41.5 17.2 81.2 47.6 109.5z"/></svg>
                <svg v-if="!isLike" style="width: 45%;" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M225.8 468.2l-2.5-2.3L48.1 303.2C17.4 274.7 0 234.7 0 192.8v-3.3c0-70.4 50-130.8 119.2-144C158.6 37.9 198.9 47 231 69.6c9 6.4 17.4 13.8 25 22.3c4.2-4.8 8.7-9.2 13.5-13.3c3.7-3.2 7.5-6.2 11.5-9c0 0 0 0 0 0C313.1 47 353.4 37.9 392.8 45.4C462 58.6 512 119.1 512 189.5v3.3c0 41.9-17.4 81.9-48.1 110.4L288.7 465.9l-2.5 2.3c-8.2 7.6-19 11.9-30.2 11.9s-22-4.2-30.2-11.9zM239.1 145c-.4-.3-.7-.7-1-1.1l-17.8-20c0 0-.1-.1-.1-.1c0 0 0 0 0 0c-23.1-25.9-58-37.7-92-31.2C81.6 101.5 48 142.1 48 189.5v3.3c0 28.5 11.9 55.8 32.8 75.2L256 430.7 431.2 268c20.9-19.4 32.8-46.7 32.8-75.2v-3.3c0-47.3-33.6-88-80.1-96.9c-34-6.5-69 5.4-92 31.2c0 0 0 0-.1 .1s0 0-.1 .1l-17.8 20c-.3 .4-.7 .7-1 1.1c-4.5 4.5-10.6 7-16.9 7s-12.4-2.5-16.9-7z"/></svg>
                <br>좋아요 : {{ movie.like_users.length }}
              </div>
              <div class="detailssss col-4" @click="seenmovie">
                <br>
                <svg v-if="isSeen" style="width: 45%;" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M316.9 18C311.6 7 300.4 0 288.1 0s-23.4 7-28.8 18L195 150.3 51.4 171.5c-12 1.8-22 10.2-25.7 21.7s-.7 24.2 7.9 32.7L137.8 329 113.2 474.7c-2 12 3 24.2 12.9 31.3s23 8 33.8 2.3l128.3-68.5 128.3 68.5c10.8 5.7 23.9 4.9 33.8-2.3s14.9-19.3 12.9-31.3L438.5 329 542.7 225.9c8.6-8.5 11.7-21.2 7.9-32.7s-13.7-19.9-25.7-21.7L381.2 150.3 316.9 18z"/></svg>
                <svg v-if="!isSeen" style="width: 45%;" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M287.9 0c9.2 0 17.6 5.2 21.6 13.5l68.6 141.3 153.2 22.6c9 1.3 16.5 7.6 19.3 16.3s.5 18.1-5.9 24.5L433.6 328.4l26.2 155.6c1.5 9-2.2 18.1-9.6 23.5s-17.3 6-25.3 1.7l-137-73.2L151 509.1c-8.1 4.3-17.9 3.7-25.3-1.7s-11.2-14.5-9.7-23.5l26.2-155.6L31.1 218.2c-6.5-6.4-8.7-15.9-5.9-24.5s10.3-14.9 19.3-16.3l153.2-22.6L266.3 13.5C270.4 5.2 278.7 0 287.9 0zm0 79L235.4 187.2c-3.5 7.1-10.2 12.1-18.1 13.3L99 217.9 184.9 303c5.5 5.5 8.1 13.3 6.8 21L171.4 443.7l105.2-56.2c7.1-3.8 15.6-3.8 22.6 0l105.2 56.2L384.2 324.1c-1.3-7.7 1.2-15.5 6.8-21l85.9-85.1L358.6 200.5c-7.8-1.2-14.6-6.1-18.1-13.3L287.9 79z"/></svg>
                <br>봤어요 : {{ movie.seen_users.length}}
              </div>
            </div>


          </div>
          <div class="col-7 movie-detail-video">
            <div class="ratio ratio-16x9 movie-detail-video-item">
              <iframe :src="videoUrl" frameborder="0"></iframe>
            </div>
          </div>
        </div>
      </div>
      
      <div class="detail-overview">
        <div class="detailss">개요 {{ movie.overview }}</div>
      </div>
    </div>
  </div>

  <div class="director-actor">
    <div v-for="actor in movie.actors" :key="actor.id" class="actors-item">
      {{ actor.name }}<br>
      <img :src="`https://image.tmdb.org/t/p/original${actor.poster_path}`" class="actor-image" alt="...">
    </div>
  </div><br>
  
  <div class="one-comment">
    
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
  </div><br>
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
    },
    isLike() {
      return this.movie.like_users.some(user => user.pk = this.currentuser)
    },
    isSeen() {
      return this.movie.seen_users.some(user => user.pk = this.currentuser)
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

#moviedetailview {
  color: black;
}
/* 포스터+설명 박스 */
.poster-line {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  /* border: solid 3px blueviolet; */
  width: 90%;
  height: 68vh;
}

/* 포스터 이미지 박스 */
.poster-img {
  /* border: solid 3px blueviolet; */
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
  /* border: solid 3px blueviolet; */
  width: 100%;
  height: 60%;
}

.movie-detail-info {
  display: flex;
  width: 100%;
  height: 50%;
  margin: 0;
  /* border: solid 1px green; */
}

.movie-detail-text {
  margin: auto 0;
  /* border: solid 1px blue; */
}

.movie-detail-video-item {
  height: 100%;
}

/* 영화 세부 정보 하위 박스 */
.detailss {
  margin: auto 0;
  /* border: solid 2px lightcoral; */
  font-weight: bold;
  color: black;
  font-size: 2vh;
}

.detailssss {
  margin: auto 0;
  /* border: solid 2px lightcoral; */
  height: 10vh;
  font-size: 1.8vh;
  font-weight: bold;
}

.detailss-title {
  font-size: 5vh;
  text-align: start;
}

/* 영화 개요 */
.detail-overview {
  display: flex;
  flex-direction: column;
  justify-content: center;
  /* border: solid 3px blueviolet; */
  overflow: hidden;
  font-size: 2.2vh;
  width: 100%;
  height: 40%;
}


.one-comment {
  border: solid 1px black;
  width: 90%;
  height: 20vh;
}

.director-actor {
  display: flex;
  justify-content: space-evenly;
  border: solid 1px black;
  width: 90%;
  height: 35vh;
}

.actor-image {
  height: 80%;
}

</style>