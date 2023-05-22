<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>

</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'ReviewCreate',
  data() {
    return {
      title: null,
      content: null,
    }
  },

  methods: {
    createArticle() {   //리뷰 게시글 생성
      const title = this.title
      const content = this.content
      const currentuser = this.$store.getters.currentuser  //현재 유저id 정보
      const authHeader = this.$store.getters.authHeader   // 유저 토큰
      if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/reviews/`,
        data: { title, content, user: currentuser},
        headers: authHeader,   //user정보를 data에 넣을땐 토큰 추가필수
      })
      .then(() => {
        console.log('asdf')
        this.$router.push({name: 'CommunityView'})
      })
      .catch((err) => {
        console.log('게시판 생성 애러')
        console.log(err)
      })
    }
  }

}
</script>

<style>
.partyitem {
  border: solid 1px blue;
}
</style>