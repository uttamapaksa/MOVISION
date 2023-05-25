<template>
<div>
  <div class="content">
    <br><br>
    <div class="row">
        <div class="col-4 reco-img" v-for="movie in recommend_movies" :key="movie.pk">
          <div>{{ movie.title}}</div><br>
          <img @click="godetailmovie(movie.pk)" :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" alt="">
          <br><br><br>
        </div>
    </div>
  </div>

</div>
</template>

<script>
export default {
  name: 'RecommendView',
  mounted() {
    const user_id = this.$route.params.user_id
    this.$store.dispatch('getRecommendMovies', user_id)
  },
  computed: {
    recommend_movies() {
      return this.$store.getters.recommend_moives
    }
  },
  methods: {
    godetailmovie(movie_id) {
      this.$router.push({ name: 'MovieDetailView', params: { movie_id: movie_id }})
    }
  }
}
</script>

<style scoped>
.row {
  margin: 0 50px;
}

.reco-img {
  font-size: 1.5vw;
}

img {
  width: 70%;
}
</style>