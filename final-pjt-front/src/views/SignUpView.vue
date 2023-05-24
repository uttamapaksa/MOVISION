<template>
  <div>
    <h1>Sign Up Page</h1><br>
    <form @submit.prevent="signup">
      <label for="username1">아이디 : &nbsp;</label>
      <input type="text" id="username1" v-model="username"><br><br>

      <label for="password1">비밀번호 : &nbsp;</label>
      <input type="password" id="password1" v-model="password1"><br><br>

      <label for="password2">비밀번호 확인 : &nbsp;</label>
      <input type="password" id="password2" v-model="password2"><br><br>
      
      <label for="nickname">별명 : &nbsp;</label>
      <input type="text" id="nickname" v-model="nickname"><br><br>

      <div class="dropdown">
        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">{{genre}}</button>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
          <li  v-for="(genre, idx) in genres" :key="idx"><a class="dropdown-item" href="#" @click=choice(idx)>{{ genre }}</a></li>
        </ul>
      </div>
      <br><input type="submit" value="회원가입">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      nickname: null,
      genre: '선호장르',
      idx: 0,
    }
  },
  methods: {
    signup() {
      // console.log('signup')
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const nickname = this.nickname
      const like_genre = this.idx

      const payload = {
        username, password1, password2, nickname, like_genre,
      }
      this.$store.dispatch('signUp', payload)
      
      // const nickname = this.nickname
      // this.$store.dispatch('userdatasignUp', nickname)
      // }
    },
    choice(idx) {
      this.idx = idx
      this.genre = this.genres[idx]
    },
  },
  computed: {
    genres() {
      return this.$store.getters.totalgenres
    }
  }
}
</script>
