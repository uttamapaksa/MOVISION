<template>
<div class="card snip1" @click="godetailmovie" >
  <img :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" class="card-img-search" alt="...">
  <div class="card-body">
    <div class="card-text">
      제목 : {{ movie.title}}<hr>
      평점 : {{ movie.vote_average}}<hr>
      인기 : {{ movie.popularity}}<hr>
      개봉일 : {{ movie.release_date}}<hr>
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
      return Object.values(this.movie.genres).map(id => this.totalgenres[id])
    },
  },
  methods: {
    godetailmovie() {
      this.$router.push({ name: 'MovieDetailView', params: { movie_id: this.movie.id }})
    }
  }
}
</script>

<style>
</style>