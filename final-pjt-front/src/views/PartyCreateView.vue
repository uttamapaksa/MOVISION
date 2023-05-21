<template>
  <div>
    <h1>파티 게시글 작성</h1>
    <form @submit.prevent="createParty">
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
  name : 'PartyCreate',
  data() {
    return {
      title: null,
      content: null,
    }
  },

  methods: {
    createParty() {
      const title = this.title
      const content = this.content

      if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/parties/`,
        data: { title, content},
      })
      .then(() => {
        this.$router.push({name: 'CommunityView'})
      })
      .catch((err) => {
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