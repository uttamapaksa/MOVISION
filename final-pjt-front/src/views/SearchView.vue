<template>
<div id="searchview">
  <!-- 검색창 -->
    <br>
    <div class="input_box2" >
      <div class="container-2">
        <input type="text" :value="titleinput" @input="titleinput = $event.target.value" @keyup_enter="submitresult" id="search" placeholder="작품명, 배우, 장르를 검색해보세요." />
        <button class="icon2"  @click="submitresult" ><i class="fa fa-search">제목이 기억나지 않는다면, 클릭!</i></button>
      </div>
    </div><br>
    
<!-- 리모콘 -->
  <div class="search-box row">
    <div class="checkbox col-3" >
      <div class=checkboxheader>
        <div class="circle"></div>
      </div>
      <div class="check check-sort">
        <ul class="dropdown-menu">
          <li v-for="(sortname, idx) in sorts" :key="idx" class="dropdown-item" @click="checksort(idx)">{{sortname}}</li>
        </ul>
        <button class="btn btn-secondary btn-first dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
          {{ sortname }}
        </button>  
      </div>

      <div class="check check-genre" >
        <br>
        <button class="genre-button " @click="checkgenre(0)" :class="{selected: select_total}" style="margin: 5px;">전체</button>
        <div style="display: inline-block; margin: 4px;" v-for="(genre, idx) in genres" :key="idx">
          <button class="genre-button" @click="checkgenre(genre)" :class="{selected: isSelected(genre)}">{{ totalgenres[genre] }}</button>
        </div>
      <div class='check-futter'>
        <br><br>
        <button class="btn btn-secondary btn-second" @click="checkgenre(0)"  type="button">취 소</button>
 
      </div>
      </div>
    </div>
<!-- 영화 포스터,데이터 --> 
    <div class="search-result-parent col-8">
      <div v-if="!this.checking" class="search-result row">
        <SearchViewItem class="searchitem col-3" v-for="(movie, idx) in movies.slice(0, 10)" :key="idx" :movie="movie" :totalgenres="totalgenres"/>
      </div>
      <div v-if="this.checking" class="search-result row">
        <SearchViewItem2 class="searchitem col-3" v-for="(movie2, idx) in this.movies2" :key="idx" :movie2="movie2" :totalgenres="totalgenres"/>
      </div>
    </div>
  </div>
</div>
</template>
<script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/js/all.min.js" integrity="sha384-0XnGf5E3F+4G8q4e4LM0o3K/KM3ppaATdXuVSzhrBx0R3cy9H6TxBViu7BwDH0Ru" crossorigin="anonymous"></script>
<script>
import SearchViewItem from '@/components/SearchViewItem'
import SearchViewItem2 from '@/components/SearchViewItem2'
// import RatebarView from '@/components/RatebarView'
import axios from 'axios'
export default {
  name: 'SearchView',
  components: {
    SearchViewItem,
    SearchViewItem2,
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
      checking: false,
      movies2: [], 
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
      this.checking = false
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
    },
    // movies2() {
    //   return this.movies2
    // }
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
      this.checking= true
      const search = this.titleinput
      console.log(`http://127.0.0.1:8000/api/v1/search/${search}/`)
      axios({
        method: 'get',
        url:`http://127.0.0.1:8000/api/v1/search/${search}/`,
  
      })
        .then(res => {
          this.movies2 = res.data
          console.log(res.data[0].pk)
        })
        .catch(err => {
          console.log('asdsad')
          console.log(err)
        })
    }
  }
}
</script>


<style>
/* * {
  background-color: #343235;
} */
/* 검색버튼 */
#searchview {
  background-color: #777279;
}
.input_box2 {
  /* margin-top: 3%; */
  display: flex;
  /* flex-direction: column; */
  justify-content: center;
  align-items: center;
  /* width: 100%; */
}
.container-2{
  overflow: hidden;
  width: 800px;
  vertical-align: middle;
  white-space: nowrap;
  border: 2px solid rgb(171, 170, 169);
}

.container-2 input#search{
  width: 800px;
  height: 65px;
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

.container-2 input#search::-webkit-input-placeholder {
  color: #65737e;
}
.container-2 input#search:-moz-placeholder { /* Firefox 18- */
  color: #65737e;  
}
.container-2 input#search::-moz-placeholder {  /* Firefox 19+ */
  color: #65737e;  
}
.container-2 input#search:-ms-input-placeholder {  
  color: #65737e;  
}

.container-2 button.icon2{
  -webkit-border-top-right-radius: 5px;
  -webkit-border-bottom-right-radius: 5px;
  -moz-border-radius-topright: 5px;
  -moz-border-radius-bottomright: 5px;
  border-top-right-radius: 5px;
  border-bottom-right-radius: 5px;
  border: none;
  background: #232833;
  height: 65px;
  width: 250px;
  border-radius: 40px 0px 0px 40px ;
  color: #4f5b66;
  opacity: 0;
  font-size: 10pt;
  -webkit-transition: all .55s ease;
  -moz-transition: all .55s ease;
  -ms-transition: all .55s ease;
  -o-transition: all .55s ease;
  transition: all .55s ease;
}
.container-2:hover button.icon2, .container-4:active button.icon2, .container-4:focus button.icon2{
    outline: none;
    opacity: 1;
    margin-left: -250px;
  }
  .container-2:hover button.icon2:hover{
    background: white;
  }

.search-box {
  display: flex;
  justify-content: center;
  /* flex-direction: column; */
  /* align-items: center; */
  width: 100vw;
  height: 100vh;
  background-color: #ddd6d6;
  overflow: hidden;
}

.checkbox {
  display: flex;
  flex-direction: column;
  border: solid 1px black;
  margin-top: 14vh;
  margin-right: 7vh;
  width: 13%;
  height: 60vh;
  border-radius: 10px;
  background-color: white;
  /* align-items: center; */
}
.checkboxheader {
  height: 50px;

}
.check-sort {
  height: 10%;
  border: solid 1px black;
}
.dropdown-item{
  font-size: 17px;
}
.btn-first {
  font-size: 17px;
}
.check-genre {
  /* margin-top: 5vh; */
  height: 90%;
  border: solid 1px black;
}

.check {
  /* margin: 3px; */
  /* text-align: center; */
  width: 100%;
}
.check-futter{
  margin-top: 4vh;
  border: solid 1px black;
}
.genre-button {
  border: solid 1px gray;
  background-color: white;
  border-radius: 50px;
  font-size: 1vw;
  font-size: 20px;
  margin: 0.1vh;
}
.circle{
  width: 12px;
  height: 12px;
  border: solid 1px black;
  border-radius: 50%;
  margin-left: 89%;
  margin-top: 4%;
}
.selected {
  background-color: orange;
}
.check-futter {
  /* margin-bottom: 80%; */
  border-bottom: none !important;
  border-right: none !important;
  border-left: none !important;
}
.btn-second{
  width: 70%;
  height: 20%;
  border-radius: 30px;
}
.search-result-parent {
  display: flex;
  margin-top: 7vh;
  margin-right: 13vh;
  justify-content: space-evenly;
  width: 57%;
  height: 70vh;
  overflow: hidden;
  border: 18px solid rgb(32, 32, 32);
  border-radius: 15px;
  background-color: rgb(89, 86, 86) ;

}

.search-result {
  display: flex;
  /* justify-content: space-evenly; */

  /* border: solid 1px darkgoldenrod; */
  /* width: 100%; */
  height: 100%;
  font-size: 0.6vw;
}
.searchitem{
  width: 20%;


}
</style>