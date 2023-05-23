<template>
<div id="profileview">
  
  <h2>프로필</h2>
  <div class="profile-0">
    <div class="profile-1">
      <div class="profile-photo">
        <img src="#" alt="">프로필 사진
      </div>
      <div class="profile-status">프로필 정보
        <p></p>
        <!-- {{ profile }} -->
        <div>아이디 : {{ profile.username }} 
          <p v-if="!isYourself">
            <button @click="follow()">
              <span v-if="isfollow">언팔로우</span>
              <span v-if="!isfollow">팔로우</span>
            </button>
          </p>
        </div>
        <p>닉네임 : {{ profile.nickname }}</p>
        <p>팔로잉 : {{ profile.followings.length }} | 팔로워 : {{ profile.followers.length }}</p>
        <p>가입일 : {{ profile.created_at.slice(0,10)}}</p>
        <button v-if="isYourself">회원정보수정(버튼)</button>
        <div>
          <p>레벨 : {{ profile.level }}</p>
          <p>경험치 : {{ profile.exp }}</p>
        </div>
      </div>
    </div>

    <div class="profile-2 row">
      <div @click="profileshow=1" class="article-num nums">
        내 글<br>
        {{ profile.reviews.length }} 개
      </div>
      <div @click="profileshow=2" class="comment-num nums">
        내 댓글<br>
        {{ profile.reviewcomments.length }} 개
      </div>
      <div @click="profileshow=3" class="likes-num nums">
        내가 좋아하는 영화<br>
        {{ profile.like_movies.length }} 개
      </div>
      <div @click="profileshow=4" class="bookmark-num nums">
        내가 본 영화<br> 
        {{ profile.seen_movies.length }} 개
      </div>
    </div>
    <div class="profile-3">
      <div v-if="profileshow == 1" style="width: 100%;"> 
        <router-link class="profile-3-item row" v-for="review in profile.reviews" :key="review.id" :to="{ name: 'ReviewDetialView', params: {review_id: review.id }}">
          <div class="col-9">
            제목 : {{ review.title }}<br>
          </div>
          <div class="col-3">
            작성시간 : {{  review.created_at.slice(2, 10) }}-{{  review.created_at.slice(11, 16)}}
          </div>
        </router-link>
      </div>
      <div v-if="profileshow == 2" style="width: 100%;"> 
        <router-link class="profile-3-item" v-for="comment in profile.reviewcomments" :key="comment.id" :to="{ name: 'ReviewDetialView', params: {review_id: comment.review }}">
          <div class="col-9">
            제목 : {{ review_articles[comment.review - 1].title }}<br>
            내 댓글 : {{ comment.content }}
          </div>
          <div class="col-3">
            작성시간 : {{  comment.created_at.slice(2, 10)}}-{{ comment.created_at.slice(11, 16) }}
          </div>
        </router-link>
      </div>
      <div v-if="profileshow == 3" style="width: 100%;"> 
        <router-link class="profile-3-item" v-for="movie in profile.like_movies" :key="movie.id" :to="{ name: 'MovieDetailView', params: {movie_id: movie.id} }">
          <div class="col-9">
            제목 : {{ movie.title }}<br>
          </div>
          <div class="col-3">
            평점 : {{  movie.vote_average }}
          </div>
        </router-link>
      </div>
      <div v-if="profileshow == 4" style="width: 100%;">
        <router-link class="profile-3-item" v-for="movie in profile.seen_movies" :key="movie.id" :to="{ name: 'MovieDetailView', params: {movie_id: movie.id} }">
          <div class="col-9">
            제목 : {{ movie.title }}<br>
          </div>
          <div class="col-3">
            평점 : {{  movie.vote_average }}
          </div>
        </router-link>
      </div>
    </div>
  </div>

</div>
</template>

<script>
export default {
  name: 'ProfileView',
  created() {
    const profile_id = this.$route.params.profile_id
    this.$store.dispatch('getProfile', profile_id)
  },
  data() {
    return {
      VUE_URL: 'http://localhost:8080',
      profileshow: 1,
    }
  },
  computed: {
    profile() {
      return this.$store.getters.profile
    },
    currentuser() {
      return this.$store.getters.currentuser
    },
    isfollow() {
      return this.profile.followers.some(person => person.id == this.currentuser)
    },
    isYourself() {
      const profile_id = this.$route.params.profile_id
      return this.currentuser == profile_id
    },
    review_articles() {
      return this.$store.state.review_articles
    },
  },
  methods: {
    follow() {
      const profile_id = this.$route.params.profile_id
      this.$store.dispatch('follow', profile_id)
    },
  },
}
</script>


<style>
.profile-0 {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  margin: 0 auto;
  width: 90%;
  height: 90vh;
  border: solid 1px black;
}
.profile-1 {
  display: flex;
  justify-content: space-evenly;
  margin: 0 auto;
  width: 90%;
  height: 40vh;
  border: solid 1px black;
}
.profile-2 {
  display: flex;
  margin: 0 auto;
  width: 90%;
  height: 15vh;
  border: solid 1px black;
  font-size: 2vh;
}

.nums {
  display: flex;
  justify-content: center;
  align-items: center;
  border: solid 1px black;
  width: 25%;
  height: 100%;
}

.profile-3 {
  display: flex;
  justify-content: center;
  margin: 0 auto;
  width: 90%;
  height: 45vh;
  border: solid 1px black;
}

.profile-3-item {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
  width: 100%;
  height: 10vh;
  border: solid 1px red;
}


</style>