<template>
  <div>
    <h1>Detail</h1>

    <p>작성자 : {{ review.user }}</p>
    <p>글 번호 : {{ review.id }}</p>
    <p>제목 : {{ review.title }}</p>
    <p>내용 : {{ review.content }}</p>
    <p>작성시간 : {{ review.created_at }}</p>
    <p>수정시간 : {{ review.updated_at }}</p>
    <!-- 댓글 input -->
    <div>
      댓글을 남겨주세요.
      <input type="text" v-model="review_comment" @keyup.enter="review_save_comment">
      <button @click="review_save_comment">작성하기</button>
    </div>
    <!-- 댓글 리스트 -->
    <div v-for="comment in comment_lst" :key=comment.id >
      댓글 작성자: {{comment.user}}
      댓글 번호:{{comment.id}} <br>
      내용 :{{comment.content}} <br>
      생성일 :{{comment.created_at}}
      <button @click="review_delete_comment(comment.id)">삭제</button>
    </div>
    <br><br>
    <!-- 글 삭제,수정 -->
    <div>
      <button @click="review_delete(review.id)">글 삭제하기</button>
      <!-- <button @click="review_update(review.id)">글 수정하기</button> -->
      <button>글 수정하기</button>
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
    comment_lst() {   
      return this.$store.state.review_comments.filter(comment=> (comment.review == this.$route.params.review_id))
    },
    review() {
      return this.$store.state.review_articles.filter(review=> (review.id ==this.$route.params.review_id))[0]
    }
  },
  methods: { 
    review_save_comment() {     //댓글 저장 요청
      const current_id = this.$route.params.review_id
      const currentuser = this.$store.getters.currentuser  //현재 유저id 정보
      const authHeader = this.$store.getters.authHeader   // 유저 토큰
      axios({
        method: 'POST',
        url: `${API_URL}/api/v1/articles/reviews/${ current_id }/create/`,
        data: {content :this.review_comment, review : this.$route.params.review_id, user: currentuser,},
        headers: authHeader,   //user정보를 data에 넣을땐 토큰 추가필수
      })
      .then((res) => {
        console.log(res)
        this.$store.dispatch('getreviewcomment')
      })
      .catch((err) => {
        console.log(err)
      })
    },

    review_delete_comment(com_id) {      //댓글 삭제 요청
      axios({
        method: 'DELETE',
        url: `${API_URL}/api/v1/articles/review_comments/${com_id}`,
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
      axios({
        method: 'DELETE',
        url: `${API_URL}/api/v1/articles/reviews/${review_id}`,
      })
      .then((res) => {
        console.log(res)
        this.$router.push({name: 'CommunityView'})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // review_update(review_id) { //글 수정 요청
    
    // },

  }
}
</script>
