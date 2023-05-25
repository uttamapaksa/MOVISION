<template>
<div :key="movie2.pk" class="card snip1 searchcard" @click="godetailmovie" @mouseover="showCardBody2" @mouseout="hideCardBody2">
  <img :src="`https://image.tmdb.org/t/p/original${movie2.poster_path}`" class="card-img-search" alt="...">
  <div class="card-body2" :class="{ 'show': showCardBody }" style="position:absolute; top: 40%; left: 50%; transform: translate(-50%, -50%);">
    <div class="card-text">
      <p class="movie_detail">{{ movie2.title }} </p>
      <button class="movie_d_button">정보 보기</button>
      <!-- <div class="vote-front"><p class="vote-text">평점 : {{ movie2.vote_average }}</p></div> -->
      <hr>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'SearchViewItem2',
  props: {
    movie2: Object,
    totalgenres: Object,
  },
  data() {
    return {
      showCardBody: false
    };
  },
  computed: {
    // genres() {
    //   return this.movie2.genre.map(genre => this.totalgenres[genre.id])
    // },
  },
  methods: {
    godetailmovie() {
      this.$router.push({ name: 'MovieDetailView', params: { movie_id: this.movie2.pk }})
    },
    checking(){
      console.log('sadf')
    },
    defchecking(){
      console.log('aaaa')
    } ,
    showCardBody2() {
      this.showCardBody = true;
    },
    hideCardBody2() {
      this.showCardBody = false;
    }

  }
}
</script>

<style scoped>
.card-body2 {
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
  opacity: 0;
  transition: opacity 0.1s;
}

.card-body2.show {
  display: block;
  opacity: 1;
  transition: opacity 1s;
}

@keyframes buttonClickAnimation {
  0% { transform: scale(1); }
  50% { transform: scale(0.5); }
  100% { transform: scale(1); }
}
.movie_detail{
  color: aliceblue;
  font-size: 1.5vh;
  margin-top: 15vh;
  margin-bottom: 4vh;
}
.card-text{
  /* display: flex; */
  align-content: center;
}
.vote-front{
  display: flex;
  margin-top: 9vh;
  margin-left: 7vw;
  height: 1.7vh;
  width: 6vh;
  background-color: rgb(59, 59, 42);
  color: rgb(180, 189, 160);
}
.vote-text {
  margin: auto;
  
}
.movie_d_button{
  width: 6vw;
  height: 3vh;
  border-radius: 20px;

}
.searchcard {
  border-radius: 0;
  
}




</style>