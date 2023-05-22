<template>
  <div>
    <h1>Sign Up Page</h1><br>
    <form @submit.prevent="signup">
      <label for="username1">username : &nbsp;</label>
      <input type="text" id="username1" v-model="username"><br><br>

      <label for="password1"> password : &nbsp;</label>
      <input type="password" id="password1" v-model="password1"><br><br>

      <label for="password2"> password confirmation : &nbsp;</label>
      <input type="password" id="password2" v-model="password2">
      <!-- <label for="nickname"> nickname : &nbsp;</label>
      <input type="text" id="nickname" v-model="nickname"> -->
      
      &nbsp; <input type="submit" value="SignUp">
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
    }
  },
  methods: {
    signup() {
      // console.log('signup')
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }
      this.$store.dispatch('signUp', payload)
      
      // const nickname = this.nickname
      // this.$store.dispatch('userdatasignUp', nickname)
      // }
    }
  }
}
</script>
