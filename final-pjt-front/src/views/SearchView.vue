<template>
<div id="searchview">
    <div class="input_box" >
      <div class="container-4">
        <input type="text" :value="titleinput" @input="titleinput = $event.target.value" id="search" placeholder="작품명, 배우, 장르를 검색해보세요." />
        <button class="icon"  @keyup_enter="submitresult" ><i class="fa fa-search">검색</i></button>
      </div>
    </div><br>
    

  <div class="search-box">
    <div class="checkbox">
      <div class="check check-sort">
        <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
          {{ sortname }}
        </button>  
        <ul class="dropdown-menu">
          <li v-for="(sortname, idx) in sorts" :key="idx" class="dropdown-item" @click="checksort(idx)">{{sortname}}</li>
        </ul>
      </div>

      <div class="check check-genre" >
        <button class="genre-button" @click="checkgenre(0)" :class="{selected: select_total}" style="margin: 5px;">전체</button>
        <div style="display: inline-block; margin: 5px;" v-for="(genre, idx) in genres" :key="idx">
          <button class="genre-button" @click="checkgenre(genre)" :class="{selected: isSelected(genre)}">{{ totalgenres[genre] }}</button>
        </div>
      </div>

    </div>
<!-- 영화 포스터,데이터 --> 
    <div class="search-result-parent">
      <div class="search-result row">
        <SearchViewItem class="searchitem col-3" v-for="(movie, idx) in movies" :key="idx" :movie="movie" :totalgenres="totalgenres"/>
      </div>
    </div>
  </div>
</div>
</template>
<script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/js/all.min.js" integrity="sha384-0XnGf5E3F+4G8q4e4LM0o3K/KM3ppaATdXuVSzhrBx0R3cy9H6TxBViu7BwDH0Ru" crossorigin="anonymous"></script>
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
      titleinput: '',
      sorts: ['평점 높은순', '평점 낮은순', '개봉 빠른순', '개봉 늦은순', '인기 높은순', '인기 낮은순', '제목 오름차순', '제목 내림차순',],
      sort: 0,
      genres: [12, 18, 16, 27, 28, 35, 36, 37, 53, 80, 99, 878, 9648, 10402, 10749, 10751, 10752, 10770,],
      select_total: true,
      select_genres: [],
      directorinput: '',
      actorinput: '',
    }
  },
  computed: {
    sortname() {
      return this.sorts[this.sort]
    },
    totalgenres() {
      return this.$store.getters.totalgenres
    },
    movies() {
      // 장르별 검색
      let movies_by_genres = []
      if (this.select_total) {
        movies_by_genres = this.$store.getters.movies;
      } else {
        movies_by_genres = this.$store.getters.movies.filter(movie => movie.genres.some(genre => this.select_genres.includes(genre['id'])));
      }

      // 제목별 검색
      let movies_by_search = []
      if (!this.titleinput) {
        movies_by_search = movies_by_genres
      } else {
        movies_by_search = movies_by_genres.filter(movie => movie.title.includes(this.titleinput))      
      }

      // 검색 결과 정렬
      if (this.sort === 0) {
        return movies_by_search.sort(function (a, b) {
          return b.vote_average - a.vote_average
        })
      } else if (this.sort === 1) {
        return movies_by_search.sort(function (a, b) {
          return a.vote_average - b.vote_average
        })
      } else if (this.sort === 2) {
        return movies_by_search.sort(function (a, b) {
          return new Date(b.release_date) - new Date(a.release_date);
        })
      } else if (this.sort === 3) {
        return movies_by_search.sort(function (a, b) {
          return new Date(a.release_date) - new Date(b.release_date);
        })
      } else if (this.sort === 4) {
        return movies_by_search.sort(function (a, b) {
          return b.popularity - a.popularity
        })
      } else if (this.sort === 5) {
        return movies_by_search.sort(function (a, b) {
          return a.popularity - b.popularity
        })
      } else if (this.sort === 6) {
        return movies_by_search.sort(function (a, b) {
          return b.title.localeCompare(a.title);
        })
      } else if (this.sort === 7) {
        return movies_by_search.sort(function (a, b) {
          return a.title.localeCompare(b.title);
        })
      } else {
        return movies_by_search.sort(function (a, b) {
          return b.vote_average - a.vote_average
        })
      }
    }
  },
  methods: {
    refreshComponent() {
      this.searchview;
    },
    checksort(idx) {
      this.sort = idx
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
    },
    submitresult() {
      console.log(this.titleinput)
    }
  }
}
</script>


<style>
/* 검색버튼 */
.input_box {
  margin-top: 120px;
  display: flex;
  /* flex-direction: column; */
  justify-content: space-around;
  align-items: center;
  width: 100%;
}
.container-4{
  overflow: hidden;
  width: 700px;
  vertical-align: middle;
  white-space: nowrap;
}

.container-4 input#search{
  width: 700px;
  height: 50px;
  background: #2b303b;
  border: none;
  font-size: 10pt;
  float: left;
  color: #fff;
  padding-left: 15px;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  border-radius: 5px;
}

.container-4 input#search::-webkit-input-placeholder {
  color: #65737e;
}
.container-4 input#search:-moz-placeholder { /* Firefox 18- */
  color: #65737e;  
}
.container-4 input#search::-moz-placeholder {  /* Firefox 19+ */
  color: #65737e;  
}
.container-4 input#search:-ms-input-placeholder {  
  color: #65737e;  
}

.container-4 button.icon{
  -webkit-border-top-right-radius: 5px;
  -webkit-border-bottom-right-radius: 5px;
  -moz-border-radius-topright: 5px;
  -moz-border-radius-bottomright: 5px;
  border-top-right-radius: 5px;
  border-bottom-right-radius: 5px;
  border: none;
  background: #232833;
  height: 50px;
  width: 50px;
  color: #4f5b66;
  opacity: 0;
  font-size: 10pt;
  -webkit-transition: all .55s ease;
  -moz-transition: all .55s ease;
  -ms-transition: all .55s ease;
  -o-transition: all .55s ease;
  transition: all .55s ease;
}
.container-4:hover button.icon, .container-4:active button.icon, .container-4:focus button.icon{
    outline: none;
    opacity: 1;
    margin-left: -50px;
  }
  .container-4:hover button.icon:hover{
    background: white;
  }

.search-box {
  display: flex;
  justify-content: space-evenly;
  /* flex-direction: column; */
  /* align-items: center; */
  width: 100%;
}

.checkbox {
  display: flex;
  flex-direction: column;
  border: solid 1px black;
  width: 18%;
  height: 70vh;
}

.check-sort {
  height: 10%;
  border: solid 1px black;
}
.check-genre {
  margin-top: 5vh;
  height: 90%;
  border: solid 1px black;
}

.check {
  width: 100%;

}

.genre-button {
  border: solid 1px gray;
  background-color: white;
  border-radius: 50px;
  font-size: 1.5vw;
}

.selected {
  background-color: orange;
}


.search-result-parent {
  display: flex;
  justify-content: space-evenly;
  width: 50%;
}

.search-result {
  display: flex;
  justify-content: space-evenly;
  margin-top: 3vh;
  border: solid 1px black;
  width: 100%;
  height: 30vh;
  font-size: 0.6vw;
}
</style>