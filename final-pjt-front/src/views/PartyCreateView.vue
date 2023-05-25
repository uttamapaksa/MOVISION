<template>
  <div >
    <h1>파티 게시글 작성</h1><br>

      <!-- <div class="btn-group dropend">
        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton2" data-bs-toggle="dropdown" aria-expanded="false">모집 사이트명</button>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
          <li  v-for="(genre, idx) in sites" :key="idx"><a class="dropdown-item" href="#" @click=choice(idx)>{{ genre }}</a></li>
        </ul>
      </div><br><br>
      <div>
        <label for="title">제목 : </label>
        <input type="text" id="title" v-model.trim="title"><br>
      </div>
      <div>
        <label for="content">내용 : </label>
        <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      </div><br>
  
      <input type="submit" id="submit"> -->


	
	<!-- /.row -->
    <div class="party_grup">
      <div class="row ">
        <div class="col-lg-12">
          <div class="panel panel-default">
            <form @submit.prevent="createParty">
            <div class="panel-body">
              <div class="btn-group dropend">
                <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownsite" data-bs-toggle="dropdown" aria-expanded="false">{{ check_site_name }}</button>
                <ul class="dropdown-menu" aria-labelledby="dropdownsite">
                  <li  v-for="(genre, idx) in sites" :key="idx"><a class="dropdown-item" href="#" @click=choice(genre)>{{ genre }}</a></li>
                </ul>
              </div><br><br>
              <div class="form-group">
                <label for="title">제목</label> <input  type="text" id="title" v-model.trim="title">
              </div>

              <div class="form-group">
                <label for="content">내용</label>
                <textarea id="content" cols="30" rows="10" v-model="content"></textarea>
              </div>

              <div class="dropdown">
                제한 인원 : 
                <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownmemberlimit" data-bs-toggle="dropdown" aria-expanded="false">
                  {{ members_limit }}
                </button>
                <ul class="dropdown-menu" aria-labelledby="dropdownmemberlimit">
                  <li v-for="(limit, idx) in members_limits" :key="idx" @click=limitchoice(limit)>
                    {{limit}}</li>
                </ul> 명
              </div>

              <div align="center">
                <span>
                <button type="submit" class="btn btn-primary">작성완료</button>
                </span>
                <span>
                <button type="reset" class="btn btn-default">다시작성</button>
                </span>
                <span>
                <input type="button" value="메인으로" class="btn btn-success" onclick="javascript:window.location='/'">
                </span>
              </div>
            </div>
            </form>
          </div>
        </div>
      </div>

    </div>

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
      sites: ['디즈니플러스','넷플릭스','왓챠','유튜브'],
      check_site: null,
      check_site_name: '사이트명',
      members_limits: [2, 3, 4, 5, 6, 7, 8, 9, 10],
      members_limit: 10,
    }
  },

  methods: {
    createParty() {
      const title = this.title
      const content = this.content
      const user = this.$store.getters.currentuser  //현재 유저id 정보
      const username = this.$store.getters.currentusername  //현재 유저id 이름
      const authHeader = this.$store.getters.authHeader   // 유저 토큰
      const check_site = this.check_site
      const members_limit = this.members_limit
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
        data: { title, content, user, username, check_site, members_limit },
        headers: authHeader,   //user정보를 data에 넣을땐 토큰 추가필수
      })
      .then(() => {
        this.$router.push({name: 'CommunityView'})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    choice(genre) {
      this.check_site = genre
      this.check_site_name = genre
      console.log(genre)
    },
    limitchoice(limit) {
      this.members_limit = limit
      console.log(limit)
    },
  }

}
</script>

<style>
.partyitem {
  border: solid 1px blue;
}
.party_grup {
  display: flex;
  justify-content: center;
  /* align-items: center; */
  /* flex-direction: column; */
  /* width: 1500px; */
  /* margin: 0 auto; */
}
</style>