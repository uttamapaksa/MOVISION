<template>
<div>
  <div>
    제목 <input type="text">
    <input type="submit">
  </div>

  
  <div class="search-box">

      
  <div class="checkbox">
    <div class="check check-sort">
      <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
        정렬
      </button>  
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" @click="checksort(0)">평점 높은순</a></li>
        <li><a class="dropdown-item" @click="checksort(1)">평점 낮은순</a></li>
        <li><a class="dropdown-item" @click="checksort(2)">개봉 빠른순</a></li>
        <li><a class="dropdown-item" @click="checksort(3)">개봉 늦은순</a></li>
        <li><a class="dropdown-item" @click="checksort(4)">인기 높은순</a></li>
        <li><a class="dropdown-item" @click="checksort(5)">인기 낮은순</a></li>
        <li><a class="dropdown-item" @click="checksort(6)">제목 오름차순</a></li>
        <li><a class="dropdown-item" @click="checksort(7)">제목 내림차순</a></li>
      </ul>
    </div>
    <!-- <div class="check check-seen">
    </div> -->
    <div class="check check-date">

    </div>
    <div class="check check-genre" >
      <div style="display: inline-block; margin: 5px;" v-for="(genre,idx) in genres" :key="idx">
        <button @click="checkgenre(idx)">{{ genre }}</button>
      </div>
    </div>
    <!-- <div class="check check-ennding">
    </div> -->
    <div class="check check-rate" >
      <div style="width: 100%">
        <RatebarView/>
      </div>
    </div>
    <div class="check check-director">
      감독 : <input type="text" v-model="directorinput" style="width: 100%">
      <button>검색</button>
    </div>
    <div class="check check-actor"> 
      배우 : <input type="text" v-model="actorinput" style="width: 100%">
      <button>검색</button>
    </div>
  </div>

  <div class="search-result row">
    <SearchViewItem class="col-3" v-for="movie in movies" :key="movie.id" :movie="movie"/>
  </div>

  </div>



</div>
</template>

<script>
import SearchViewItem from '@/components/SearchViewItem'
import RatebarView from '@/components/RatebarView'

export default {
  name: 'SearchView',
  components: {
    SearchViewItem,
    RatebarView,
  },
  data() {
    return {
      sort: 'ratehigh',
      sorts: ['ratehigh', 'raterow', 'datehigh', 'daterow', 'pophigh', 'poprow', 'titlehigh', 'titlerow',],
      genres: [12, 14, 16, 18, 27, 28, 35, 36, 37, 53, 80, 99, 878, 9648, 10402, 10749, 10751, 10752, 10770],
      select_genres: [],
      directorinput: '',
      actorinput: '',
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    }
  },
  methods: {
    checksort(idx) {
      console.log(this.sorts[idx])
      this.sort = this.sorts[idx]
    },
    checkgenre(idx) {
      const its = this.select_genres.indexOf(this.genres[idx])
      if (its === -1) {
        this.select_genres.push(this.genres[idx])
      } else {
        this.select_genres.splice(its, 1)
      }
    }
  }
}
</script>


<style>
.search-box {
  display: flex;
  /* flex-direction: column; */
  justify-content: space-around;
  align-items: center;
  width: 100%;
}

.checkbox {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  border: solid 1px black;
  width: 30%;
  height: 70vh;
}

.check {
  border: solid 1px black;
  width: 100%;

}

.search-result {

  border: solid 1px black;
  width: 60%;
  height: 70vh;
}

.searchitem {
  width: 5vw;
  height: 5vh;
}
</style>