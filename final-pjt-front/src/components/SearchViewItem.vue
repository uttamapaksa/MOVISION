<template>
<div class="card">
  <img :src="`https://image.tmdb.org/t/p/w400${movie.poster_path}`" class="card-img-top" alt="...">
  <div class="card-body">
    <p class="card-text">
    {{movie.title}}
    </p>
  </div>
</div>

</template>

<script>
export default {
  name: 'SearchViewItem',
  props: {
    movie: Object,
  },
}
</script>

<style>
</style>