<template>
  <div id="app">
    <nav>
      <div>
        <img class="navtableimg" :src="`${SERVER_URL}/media/movisions.png`" alt="">
      </div>
      <div class="fronts">
        <router-link to="/">Mainpage   &nbsp; &nbsp;&nbsp;</router-link>
        
        <router-link :to="{ name: 'SearchView' }"><span>Search </span>   &nbsp; &nbsp;&nbsp;</router-link> 
        <router-link :to="{ name: 'RecommendView' , params: {user_id: currentuser}}">Recommend  &nbsp; &nbsp; &nbsp;</router-link> 
        <router-link :to="{ name: 'CommunityView' }">Community  </router-link> 
      </div>
      <div>

       <!-- 로그인 버튼-->
      <a class="fronts" v-if="!isLogin" data-bs-toggle="modal" data-bs-target="#staticBackdrop" href="">Login</a>
      <!-- 로그인 -->
      <div class="modal  signup_modal" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h1 class="modal-title fs-5" id="staticBackdropLabel">로그인</h1>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
              <div class="modal-body">
                <label for="username">아이디 : &nbsp;</label>
                <input type="text" id="username" v-model="username"><br><br>
                
                <label for="password">비밀번호 : &nbsp;</label>
                <input type="password" id="password" v-model="password"><br>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">취소</button>
                <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="login">로그인</button>
              </div>
            <div class="modal-footer ">
              <p class="mx-auto" data-bs-dismiss="modal">
                아이디가 없다면 ? <router-link :to="{ name: 'SignUpView' }">회원가입</router-link>
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- 로그아웃 버튼 -->
      <a class="fronts" v-if="isLogin" data-bs-toggle="modal" data-bs-target="#staticBackdrop2" @click.prevent="logout">Logout</a>
      <span v-if="isLogin"> | </span>
      <!-- 로그아웃 -->
      <div class="modal signup_modal fade modal-sm" id="staticBackdrop2" tabindex="-1" aria-labelledby="staticBackdropLabel2" data-bs-dismiss="modal" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h1 class="modal-title fs-5" id="staticBackdropLabel2"></h1>
              <!-- <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button> -->
            </div>
            <div class="modal-body">
              <br><p>안전하게 로그아웃 되었습니다.</p><br>
            </div>
          </div>
        </div>
      </div>

      <a @click.prevent="apptoProfile">{{currentusername}}</a><span v-if="isLogin">님의 프로필</span>
      </div>
    </nav>
    <router-view/>
  </div>
</template>


<script>
export default {
  name: 'App',
  data() {
    return {
      username: null,
      password: null,
      SERVER_URL: 'http://localhost:8000',
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    },
    currentuser() {
      return this.$store.getters.currentuser
    },
    currentusername() {
      return this.$store.getters.currentusername
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password,
      }

      this.password = null
      this.$store.dispatch('logIn', payload)
    },
    logout() {
      this.$store.dispatch('logOut')
    },
    apptoProfile() {
      this.$store.dispatch('getProfile', this.currentuser)
      this.$router.push({name: 'ProfileView', params: {profile_id: this.currentuser}})
    }
  },
}
</script>


<style>
#app {
  font-family: 'Noto Sans KR', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  display: flex;
  padding: 30px;
  height: 45px;
  align-items: center;
  justify-content: space-between;
  font-family: 'Poppins', sans-serif;
  background-color: rgb(221, 226, 231);
  font-size: 19px;
  /* color: aliceblue; */
}
.navtableimg {
  width: 150px;
}
.fronts {
  text-shadow: 1px 1px gray;
}

nav a {
  font-weight: bold;
  color: #636566;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #4675bb;
}

.signup_modal {
  color:#2c3e50;
} 

.modalhidden {
  display: none;
}
</style>
