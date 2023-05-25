<template>
  <div id="review-detail-view">
    <div class="review-detail-title">
      <h1>{{ review.title }}</h1>
    </div><br>
    <h4 class="review-detail-user" @click.prevent="detailtoProfile(review.user)"><br>작성자 : {{ review.username }}</h4>
    <div class="review-detail-content"><br>
      <p>내용 : {{ review.content }}</p>
      <p>작성시간 : {{ review.created_at.slice(0,10) }}</p>
    </div><br>

    <!-- 댓글 input -->
    <div>
      <input type="text" v-model="review_comment" @keyup.enter="review_save_comment">
      <button @click="review_save_comment">댓글 작성하기</button>
    </div>
    <!-- 댓글 리스트 -->
    <div v-for="comment in comment_lst" :key=comment.id ><br>
      내용 : {{comment.content}} | 
      <a class="review-comment-user" @click.prevent="detailtoProfile(comment.user)">작성자: {{comment.username}}</a> | 
      작성시간 : {{comment.created_at.slice(0, 10)}}
      <button v-if="comment.user == currentuser" @click="review_delete_comment(comment.id)">댓글삭제</button>
    </div>
    <br><br>
    <!-- 글 삭제,수정 -->
    <div>
      <button v-if="review.user == currentuser" @click="review_delete(review.id)">글 삭제하기</button>
      &nbsp;&nbsp;&nbsp;&nbsp; <!-- 공백문자 -->
      <!-- <button @click="review_update(review.id)">글 수정하기</button> -->
      <button v-if="review.user == currentuser">글 수정하기</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReViewDetailView',
  data() {
    return {
      article: null,
      review_comment : '',
    }
  },
  mounted() {  //get으로 데이터 요청
    this.$store.dispatch('getreviewcomment')
  },
  
  computed: {   //변수로 사용할 함수
    review() {
      return this.$store.state.review_articles.filter(review=> (review.id ==this.$route.params.review_id))[0]
    },
    comment_lst() {   
      return this.$store.state.review_comments.filter(comment=> (comment.review == this.$route.params.review_id))
    },
    currentuser() {
      return this.$store.getters.currentuser
    }
  },
  methods: { 
    review_save_comment() {     //댓글 저장 요청
      const current_id = this.$route.params.review_id
      const currentuser = this.$store.getters.currentuser  //현재 유저id 정보
      const currentusername = this.$store.getters.currentusername  //현재 유저id 이름
      const authHeader = this.$store.getters.authHeader   // 유저 토큰
      console.log('reivew_save_comment.axios')
      axios({
        method: 'POST',
        url: `${API_URL}/api/v1/articles/reviews/${ current_id }/create/`,
        data: {content :this.review_comment, review : this.$route.params.review_id, user: currentuser, username: currentusername,},
        headers: authHeader,   //user정보를 data에 넣을땐 토큰 추가필수
      })
      .then((res) => {
        console.log(res)
        console.log('reivew_save_comment.then')
        this.$store.dispatch('getreviewcomment')
      })
      .catch((err) => {
        console.log(err)
        console.log('reivew_save_comment.catch')
      })
      this.review_comment = ''
    },
    
    review_delete_comment(com_id) {      //댓글 삭제 요청
      axios({
        method: 'DELETE',
        url: `${API_URL}/api/v1/articles/review_comments/${com_id}/`,
      })
      .then((res) => {
        console.log(res)
        this.$store.dispatch('getreviewcomment')
      })
      .catch((err) => {
        console.log(err)
      })
    },

    review_delete(review_id) { //글 삭제 요청
      console.log('reivew_delete.axios')
      axios({
        method: 'DELETE',
        url: `${API_URL}/api/v1/articles/reviews/${review_id}/`,
      })
      .then((res) => {
        console.log(res)
        console.log('reivew_delete.then')
        this.$router.push({name: 'CommunityView'})
      })
      .catch((err) => {
        console.log(err)
        console.log('reivew_delete.catch')
      })
    },

    detailtoProfile(profile_id) {
      this.$store.dispatch('getProfile', profile_id)
      this.$router.push({name: 'ProfileView', params: {profile_id: profile_id}})
    }
    // review_update(review_id) { //글 수정 요청
    
    // },

  }
}
</script>

<style>
#review-detail-view {
  border: solid 1px black;
  height: 900px;
  width: 80%;
  margin: 0 auto;
}

.review-detail-user {
  border: solid 1px black;
  height: 90px;
  width: 80%;
  margin: auto;
}

.review-detail-user:hover {
  color: orange;
}

.review-detail-content {
  border: solid 1px black;
  height: 400px;
  width: 80%;
  margin: 0 auto;
}

.review-comment-user:hover {
  color: orange;
}
</style>