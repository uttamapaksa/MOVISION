<template>
<div id="profileview">
  
  <h2>프로필</h2>
  <div class="profile-0">
    <div class="profile-1">
      <div class="profile-photo">
        <img src="#" alt="">프로필 사진
      </div>
      <div class="profile-status">프로필 정보
        <p>닉네임(ID) | 팔로우버튼(토글)</p>
        <p>팔로잉 | 팔로우</p>
        <p>가입일</p>
        <button>회원정보수정(버튼)</button>
        <div>
          <p>경험치바</p>
          <p>레벨</p>
        </div>
      </div>
    </div>

    <div class="profile-2">
      <div class="article-num nums">article
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
  height: 25vh;
  border: solid 1px black;
}
.profile-2 {
  margin: 0 auto;
  width: 90%;
  height: 10vh;
  border: solid 1px black;
}
.profile-3 {
  margin: 0 auto;
  width: 90%;
  height: 45vh;
  border: solid 1px black;
}

</style>