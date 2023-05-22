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

        {{ userdata }}
        <p>아이디 : {{ userdata.username }} | <button v-if="userdata.user!==currentuser">팔로우</button></p>
        <!-- <p>닉네임 : {{ userdata.nickname }}</p> -->
        <p>팔로잉 | 팔로우</p>
        <p>가입일 : {{ userdata.created_at}}</p>
        <button v-if="userdata.user===currentuser">회원정보수정(버튼)</button>
        <div>
          <p>레벨 : {{ userdata.level }}</p>
          <p>경험치 : {{ userdata.exp }}</p>
        </div>
      </div>
    </div>

    <div class="profile-2 row">
      <div class="article-num nums col-6">
        내 글 : {{articles.length}} 개
      </div>
      <div class="comment-num nums">
        내 댓글 : {{ comments.length }} 개
      </div>
      <div class="likes-num nums">likes
      </div>
      <div class="bookmark-num nums">bookmark
      </div>
    </div>
    
    <div class="profile-3">
      <div class=""></div>
      <div></div>
    </div>
  </div>

</div>
</template>

<script>
export default {
  name: 'ProfileView',
  computed: {
    // article() {
      //   return this.$store.state.articles.filter(article => article.user = this.currentuser)
      // },
      // currentuser() {
        //   return this.$store.getters.currentuser
        // }
    articles() {
      return this.$store.state.review_articles.filter(article => article.user)
    },
    comments() {
      const review_comments = this.$store.state.review_comments.filter(comment => comment.user)
      const party_comments = this.$store.state.party_comments.filter(comment => comment.user)
      return [...review_comments, ...party_comments]
    },
    currentuser() {
      return this.$store.getters.currentuser
    },
    userdata() {
      return this.$store.getters.userdata
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
  margin: 0 auto;
  width: 90%;
  height: 20vh;
  border: solid 1px black;
}
.profile-3 {
  margin: 0 auto;
  width: 90%;
  height: 45vh;
  border: solid 1px black;
}

.nums {
  border: solid 1px black;
  width: 25%;
  height: 100%;
}

</style>