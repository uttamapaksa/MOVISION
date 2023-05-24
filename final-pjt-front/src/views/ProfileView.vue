<template>
<div id="profileview">
  
  <h2>프로필</h2>
  <div class="profile-0">
    <div class="profile-1">
      <div class="profile-photo">
        <div class="profile-photo-image">
          <img id="profile-photo-image-url" :src="`${SERVER_URL}${profile.profile_pic}`" alt="profileimg"><br>
        </div>
        <!-- Button trigger modal -->
        <button v-if="isYourself" type="button" data-bs-toggle="modal" data-bs-target="#profileimageModal">
          프로필 사진 변경
        </button>
        <!-- Modal -->
        <div class="modal fade" id="profileimageModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="#profileimageModal2" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header">
                <h1 class="modal-title fs-5" id="profileimageModal2">프로필 사진</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                  <input type="file" @change="handleImageChange" accept="image/*">
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button @click="saveProfileImage" class="btn btn-primary">Save</button>
              </div>
            </div>
          </div>
        </div>

      </div>
      <div class="profile-status">
        <br>
        <div>아이디 : {{ profile.username }} 
          <p v-if="!isYourself">
            <button @click="follow()">
              <span v-if="isfollow">언팔로우</span>
              <span v-if="!isfollow">팔로우</span>
            </button>
          </p>
        </div>
        <div>닉네임 : {{ profile.nickname }}</div>
        <div>가입일 : {{ profile.created_at.slice(0,10)}}</div><br>
        <div>
          <!-- 팔로잉 모달 버튼 -->
          <span type="button" data-bs-toggle="modal" data-bs-target="#FollowingModal">
            {{ profile.followings.length }} 팔로잉 &nbsp;| &nbsp;
          </span>

          <!-- 팔로잉 모달 내용 -->
          <div class="modal" id="FollowingModal" tabindex="-1" aria-labelledby="#FollowingModal2" aria-hidden="true">
            <div class="modal-dialog  modal-dialog-scrollable">
              <div class="modal-content">
                <div class="modal-header">
                  <h1 class="modal-title fs-5" id="#FollowingModal2">내가 팔로우하는 사람</h1>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div @click.prevent="ProfiletoProfile(following.id)" v-for="following in profile.followings" :key="following.id" class="follow-doby modal-body" data-bs-dismiss="modal">
                    아이디 : {{  following.username }}&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;닉네임 : {{ following.nickname }}
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
              </div>
            </div>
          </div>
          <!-- 팔로워 모달 버튼 -->
          <span type="button" data-bs-toggle="modal" data-bs-target="#FollowerModal">
            {{ profile.followers.length }} 팔로워
          </span>
          <!-- 팔로워 모달 내용 -->
          <div class="modal" id="FollowerModal" tabindex="-1" aria-labelledby="#FollowerModal2" aria-hidden="true">
            <div class="modal-dialog  modal-dialog-scrollable">
              <div class="modal-content">
                <div class="modal-header">
                  <h1 class="modal-title fs-5" id="FollowerModal2">나를 팔로우하는 사람</h1>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div @click.prevent="ProfiletoProfile(follower.id)" v-for="follower in profile.followers" :key="follower.id" class="modal-body" data-bs-dismiss="modal">
                    아이디 : {{ follower.username }}&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;닉네임 : {{ follower.nickname }}
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <br>
        <button v-if="isYourself">회원정보수정(버튼)</button>
        <div>
          <br>
          <div>Lv : {{ profile.level }}</div>
          <div>영화 점수 : {{ profile.exp }}</div>
          <!-- <p>경험치 : {{ profile.exp }}</p> -->
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
const API_URL = 'http://127.0.0.1:8000'
import axios from 'axios'
export default {
  name: 'ProfileView',
  created() {
    const profile_id = this.$route.params.profile_id
    this.$store.dispatch('getProfile', profile_id)
  },
  updates() {
    const profile_id = this.$route.params.profile_id
    this.$store.dispatch('getProfile', profile_id)
  },
  data() {
    return {
      SERVER_URL: 'http://localhost:8000',
      profileshow: 1,
      profileImage: null,
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
    handleImageChange(event) {
      this.profileImage = event.target.files[0]
    },
    saveProfileImage() {
      console.log('saveimage.axios')
      if (this.profileImage) {
        const formData = new FormData();
        formData.append('profile_pic', this.profileImage)
        axios({
          method: 'post',
          url: `${API_URL}/api/v1/profile/${this.currentuser}/profile_image/`,
          data: formData,
          headers: {
            'Content-Type': 'multipart/form-data'
          },
        })
          .then(res => {
            console.log(res)
            console.log('saveimage.then')
            this.$store.dispatch('getProfile', this.currentuser)
          })
          .catch(err => {
            console.log(err)
            console.log('saveimage.catch')
          })
      } else {
        alert('사진을 업로드 해주세요')
      }
    },
    ProfiletoProfile(profile_id) {
      this.$store.dispatch('getProfile', profile_id)
      this.$router.push({name: 'ProfileView', params: {profile_id: profile_id}})
    },
  }
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

.profile-photo {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border: solid 1px black;
  height: 40vh;
}

.profile-photo-image {
  border: solid 1px black;
  width: 250px;
  height: 250px;
  /* width: fit-content; */
  overflow: hidden;
}

#profile-photo-image-url {
  width: 100%;
  height: 100%;
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