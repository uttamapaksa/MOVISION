<template>
  <div>
    <h1>Detail</h1>
    <div>사이트 : {{ party.check_site }}</div>
    <div> 인원 : {{partymembersnum}} / {{party.members_limit}}</div><br>
    <div @click="detailtoProfile(party.user)">작성자 : {{ party.username }}</div>
    <div>참여자 : 
      <span @click="detailtoProfile(member.id)" v-for="(member, idx) in party.members" :key="idx">{{member.username}}</span>
    </div><br>
    <div>제목 : {{ party.title}}</div>
    <div>내용 : {{ party.content }}</div><br>

    <div>작성시간 : {{ party.created_at.slice(0, 10) }}-{{party.created_at.slice(11,19)}}</div>
    <div>수정시간 : {{ party.updated_at.slice(0, 10) }}-{{party.updated_at.slice(11,19)}}</div>
    <br>
    <button v-if="party.user!=currentuser" @click="joinparty(party.id)">참가하기</button>
    <br><br>
    <!-- 댓글 input -->
    <div>
      댓글을 남겨주세요.
      <input type="text" v-model="party_comment" @keyup.enter="party_save_comment">
      <button @click="party_save_comment">작성하기</button>
    </div>
    <!-- 댓글 리스트 -->
    <div v-for="comment in party.partycomments" :key="comment.id" >
      내용 : {{comment.content}}<br>
      댓글번호:{{comment.id}} |
      <a @click.prevent="detailtoProfile(comment.user)">작성자: {{comment.username}}</a> | 
      작성시간 : {{comment.created_at.slice(0, 10)}}
      <button v-if="comment.user == currentuser" @click="party_delete_comment(comment.id)">댓글삭제</button>
    </div>
    <br><br>
    <!-- 글 삭제,수정 -->
    <div>
      <button v-if="party.user == currentuser" @click="party_delete(party.id)">글 삭제하기</button>
      &nbsp;&nbsp;&nbsp;&nbsp; <!-- 공백문자 -->
      <!-- <button @click="review_update(review.id)">글 수정하기</button> -->
      <button v-if="party.user == currentuser">글 수정하기</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'PartyDetailView',
  data() {
    return {
      party_comment: '',
    }
  },
  created() {
    const party_id = this.$route.params.party_id
    this.$store.dispatch('getPartyDetail', party_id)
  },
  computed: {
    party() {
      return this.$store.state.party_detail
    },
    partymembersnum() {
      return this.party.members.length + 1
    },
    partymembers_id() {
      return this.party.members.map(member => member.id)
    },
    currentuser() {
      return this.$store.getters.currentuser
    }
  },
  methods: {
      joinparty(party_id) {
        if (this.partymembers_id.includes(this.currentuser)) {
          this.$store.dispatch('joinParty', party_id)
        } else if (this.party.members_limit == this.partymembersnum) {
          alert('파티가 이미 찼습니다')
        } else {
          this.$store.dispatch('joinParty', party_id)
        }
      },
      party_save_comment() {     //댓글 저장 요청
      const content = this.party_comment
      const party_id = this.$route.params.party_id
      const user = this.$store.getters.currentuser  //현재 유저id 정보
      const username = this.$store.getters.currentusername  //현재 유저id 이름
      const authHeader = this.$store.getters.authHeader   // 유저 토큰
      console.log('party_save_comment.axios')
      axios({
        method: 'POST',
        url: `${API_URL}/api/v1/articles/parties/${ party_id }/create/`,
        data: {content, party: party_id, user, username,},
        headers: authHeader,   //user정보를 data에 넣을땐 토큰 추가필수
      })
      .then((res) => {
        const party_id = this.$route.params.party_id
        console.log(res)
        console.log('party_save_comment.then')
        this.$store.dispatch('getPartyDetail', party_id)
      })
      .catch((err) => {
        console.log(err)
        console.log('party_save_comment.catch')
      })
      this.party_comment = ''
    },

    party_delete_comment(com_id) {      //댓글 삭제 요청
      const authHeader = this.$store.getters.authHeader
      console.log('partydeletecomment.axios')
      axios({
        method: 'DELETE',
        url: `${API_URL}/api/v1/articles/party_comments/${com_id}/`,
        headers: authHeader,
      })
      .then((res) => {
        const party_id = this.$route.params.party_id
        console.log(res)
        console.log('partydeletecomment.then')
        this.$store.dispatch('getPartyDetail', party_id)
      })
      .catch((err) => {
        console.log(err)
        console.log('partydeletecomment.catch')
      })
    },

    party_delete(party_id) { //글 삭제 요청
      console.log('party_delete.axios')
      axios({
        method: 'DELETE',
        url: `${API_URL}/api/v1/articles/parties/${party_id}/`,
      })
      .then((res) => {
        console.log(res)
        console.log('party_delete.then')
        this.$router.push({name: 'CommunityView'})
      })
      .catch((err) => {
        console.log(err)
        console.log('party_delete.catch')
      })
    },
    detailtoProfile(profile_id) {
      console.log(profile_id)
      this.$store.dispatch('getProfile', profile_id)
      this.$router.push({name: 'ProfileView', params: {profile_id: profile_id},})
    },
  }
}
</script>