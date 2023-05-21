<template>
<div class="card" @click="godetailmovie" >
  <img :src="`https://image.tmdb.org/t/p/w400${movie.poster_path}`" class="card-img-top" alt="...">
  <div class="card-body">
    <div class="card-text">
      제목 : {{ movie.title}}<hr>
      장르 : {{ genres }}<br>
      id값 : {{ movie.id}}<hr>
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
      console.log(this.movie.id)
      this.$router.push({ name: 'MovieDetailView', params: { movie_id: this.movie.id }})
    }
  }
}
</script>

<style>
</style>