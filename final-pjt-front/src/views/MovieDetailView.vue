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
        <div class="detailss">인기 {{ movie.popularlity }}</div>
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
    <button @click="save_comment"></button>
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
  // }
  },
  methods: {
    save_comment() {
      const current_id = this.$route.params.movie_id
      const currentuser = this.$store.getters.currentuser
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/detail/${current_id}/comment_list`,
        data: {
          content: this.one_comment,
          user: currentuser,
        },
      })
        .then(res => {
          console.log(res)
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
  /* height: 30vh; */
  
}
.detail-overview {
  border: solid 3px blueviolet;
  width: 100%;
  height: 15vh;
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