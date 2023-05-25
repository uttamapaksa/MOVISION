<template>
<div :key="movie.id" class="card snip1" @click="godetailmovie" >
  <img :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" class="card-img-search" alt="...">
  <div class="card-body">
    <div class="card-text">
      {{ movie.title}} ({{ movie.release_date.slice(0,4)}})<hr>
      평점 : {{ movie.vote_average}}<hr>
      {{ genres }}<br>
      <!-- test2 : {{ test2 }} -->
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'SearchViewItem',
  props: {
    movie: Object,
    totalgenres: Object,
  },
  computed: {
    genres() {
      return this.movie.genres.map(genre => this.totalgenres[genre.id])
    },
  },
  methods: {
    godetailmovie() {
      this.$router.push({ name: 'MovieDetailView', params: { movie_id: this.movie.id }})
    }
  }
}
</script>

<style scoped>
.card-img-search {
  
}
</style>