<template>
<div id="profileview">
  
  <h2>프로필</h2>
  <div class="profile-0">
    <div class="profile-1">
      <div class="profile-photo">
        <img src="#" alt="">프로필 사진
      </div>
      <div class="profile-status">프로필 정보
        <p>{{ userdata.nickname }} | 팔로우버튼(토글)</p>
        <p>팔로잉 | 팔로우</p>
        <p>가입일 : {{ userdata.created_at }}</p>
        <button>회원정보수정(버튼)</button>
        <div>
          <p>경험치 : {{ userdata.exp }}</p>
          <p>레벨 : {{ userdata.exp }}</p>
        </div>
      </div>
    </div>

    <div class="profile-2 row">
      <div v-for="article in articles" :key="article.id" class="article-num nums col-6">article
        {{article.id}}
        {{article.id}}
      </div>
      <div class="comment-num nums">comment
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
    userdata() {
      return this.$store.getters.userdata
    },
    // article() {
    //   return this.$store.state.articles.filter(article => article.user = this.currentuser)
    // },
    // currentuser() {
    //   return this.$store.getters.currentuser
    // }
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
  width: 50%;
  height: 50%;
}

</style>