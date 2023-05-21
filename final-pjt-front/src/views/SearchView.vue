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
          {{ sort }}
        </button>  
        <ul class="dropdown-menu">
          <li v-for="(sortname, idx) in sorts" :key="idx" class="dropdown-item" @click="checksort(idx)">{{sorts[idx]}}</li>
        </ul>
      </div>
      <!-- <div class="check check-seen">
      </div> -->
      <div class="check check-date">

      </div>
      <div class="check check-genre" >
        <button class="genre-button" @click="checkgenre(0)" :class="{selected: select_total}" style="margin: 5px;">전체</button>
        <div style="display: inline-block; margin: 5px;" v-for="(genre, idx) in genres" :key="idx">
          <button class="genre-button" @click="checkgenre(genre)" :class="{selected: isSelected(genre)}">{{ totalgenres[genre] }}</button>
        </div>
      </div>
      <!-- <div class="check check-ennding">
      </div> -->
      <div class="check check-rate" >
        <!-- <RatebarView/> -->
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
      <SearchViewItem class="col-3" v-for="(movie, idx) in movies" :key="idx" :movie="movie" :totalgenres="totalgenres"/>
    </div>
  </div>

</div>
</template>

<script>
import SearchViewItem from '@/components/SearchViewItem'
// import RatebarView from '@/components/RatebarView'

export default {
  name: 'SearchView',
  components: {
    SearchViewItem,
    // RatebarView,
  },
  data() {
    return {
      sorts: ['평점 높은순', '평점 낮은순', '개봉 빠른순', '개봉 늦은순', '인기 높은순', '인기 낮은순', '제목 오름차순', '제목 내림차순',],
      sort: '평점 높은순',
      genres: [12, 18, 16, 27, 28, 35, 36, 37, 53, 80, 99, 878, 9648, 10402, 10749, 10751, 10752, 10770,],
      select_total: true,
      select_genres: [],
      directorinput: '',
      actorinput: '',
    }
  },
  computed: {
    movies() {
      if (this.select_total) {
        return this.$store.state.movies
      }
      else {
        return this.$store.state.movies.filter(movie => Object.values(movie.genres).some(genre => this.select_genres.includes(genre)))
      }
    },
    totalgenres() {
      return this.$store.getters.totalgenres
    }
  },
  methods: {
    checksort(idx) {
      this.sort = this.sorts[idx]
    },
    checkgenre(genre) {
      if (!genre) {
        this.select_total = true
        this.select_genres = []
        return
      }
      const index = this.select_genres.indexOf(genre)
      this.select_total = false
      if (index === -1) {
        this.select_genres.push(genre)
      } else {
        this.select_genres.splice(index, 1)
        if (!this.select_genres.length) {
          this.select_total = true
        }
      }
    },
    isSelected(id) {
      return this.select_genres.includes(id)
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
  height: 100%;

}

.genre-button {
  border: solid 1px gray;
  background-color: white;
  border-radius: 15px;
}

/* .genre-button:hover {
  cursor: pointer;
  background-color: orange;
}

.genre-button.selected:hover {
  cursor: pointer;
  background-color: white;
} */

.selected {
  background-color: orange;
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