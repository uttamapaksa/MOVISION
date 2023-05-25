<template>
<div>
  <div>
    <div id="loader">
      <div class="face">

      <svg version="1.1"
        xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
        x="0px" y="0px" width="270px" height="270px" viewBox="0.032 0 270 270"
        overflow="visible" enable-background="new 0.032 0 270 270" xml:space="preserve">
      <defs>
      </defs>
      <g id="supervisior">
        <g class="head">
          <path fill="#58585A" d="M135,10c33.389,0,64.778,13.002,88.388,36.612S260,101.611,260,135s-13.003,64.779-36.612,88.388
        S168.389,260,135,260s-64.778-13.002-88.388-36.612C23.002,199.779,10,168.389,10,135s13.002-64.779,36.612-88.388
        C70.222,23.002,101.611,10,135,10 M135,0C60.442,0,0,60.441,0,135s60.442,135,135,135s135-60.441,135-135S209.558,0,135,0L135,0z"
          />
        </g>
        <g id="eyeLeft">
          <g class="eyeLeft">
            <circle class="eye" fill="none" stroke="#58585A" stroke-width="4" stroke-linecap="round" stroke-miterlimit="10" cx="66.063" cy="127.51" r="18.849"/>
            <circle class="pupil" fill="#58585A" cx="66.063" cy="127.511" r="8.949"/>
          </g>
          <path class="closedLeft" fill="none" stroke="#58585A" stroke-width="4" stroke-linecap="round" stroke-miterlimit="10" d="
      M47.238,127.972c0.247,10.194,8.57,18.387,18.824,18.387s18.579-8.193,18.826-18.387"/>
        </g>
        <g id="eyeRight">
          <g class="eyeRight">
            <circle class="eye" fill="none" stroke="#58585A" stroke-width="4" stroke-linecap="round" stroke-miterlimit="10" cx="203.936" cy="127.51" r="18.849"/>
            <circle class="pupil" fill="#58585A" cx="203.935" cy="127.511" r="8.949"/>
          </g>
          <path class="closedRight" fill="none" stroke="#58585A" stroke-width="4" stroke-linecap="round" stroke-miterlimit="10" d="
      M185.11,127.972c0.247,10.194,8.571,18.387,18.824,18.387c10.255,0,18.579-8.193,18.826-18.387"/>
        </g>
        <g class="mouth">
          <polyline class="bar" fill="none" stroke="#58585A" stroke-width="4" stroke-linecap="round" stroke-miterlimit="10" points="
      111.532,232.832 135.032,232.832 158.532,232.832 "/>
          <path class="smile" fill="none" stroke="#58585A" stroke-width="4" stroke-linecap="round" stroke-miterlimit="10" d="
      M62.485,168.615c0.951,35.593,33.016,64.198,72.511,64.198c39.503,0,71.566-28.605,72.519-64.198"/>
        </g>
      </g>
      </svg>
      </div>
      <div class="loading-bar"></div>
    </div>
    <!-- <div id="refresher">
      <p class="refresh">refresh</p>
    </div> -->
  </div>


<!-- 결과 확인 버튼 -->

<div v-if='!button_on' class="cont">
  <div class="textcont">
    <p class="textconts">내가 좋아하는 영화들의 개요를 백터로 변환 - 코싸인유사도 검증 - 내가 좋아하는 장르의 영화들에 가중치 부여 -내가 좋아하는 영화의 개요와 유사한 영화 추천 </p>

  </div>
<!-- 버튼1 -->

  <div class="cont2 fade-in" :class="{ active: showElement }">
    <div class="screws">
      <div class="screw"></div>
      <div class="screw"></div>
    </div>
    <div class="button idea" @click="recommends(1)">
      <i class="fa fa-solid fa-info fa-3x"></i>
    </div>
      <div class="screws">
      <div class="screw"></div>
      <div class="screw"></div>
    </div>
  </div>
      <p style="font-size: 20px;"> : 한 개의 영화 추천 받기</p>
      <p>   </p>
<!-- 버튼2 -->
  <div class="cont2 " >
    <div class="screws">
      <div class="screw"></div>
      <div class="screw"></div>
    </div>
    <div class="button codepen" @click="recommends(2)">
      <i class="fa fa-brands fa-codepen fa-3x"></i>
    </div>
    <div class="screws">
      <div class="screw"></div>
      <div class="screw"></div>
    </div>
  </div>
      <p style="font-size: 20px;"> : 영화 리스트로 추천 받기</p>
  <div class="link-main">
    <div class="link-cont link2">
      <div class="cont ">
        <div class="link">FOLLOW ME ON CODEPEN</div>
        <div class="link-button button">
          <a href="https://codepen.io/Juxtopposed" target="_blank">GO!</a>
        </div>
      </div>
    </div>
    <div class="link-cont link3">
      <div class="cont ">
        <div class="link">LINK TO INSPIRATION</div>
        <div class="link-button button">
          <a href="https://pierrelouis.design/" target="_blank">GO!</a>
        </div>
      </div>
    </div>
  </div>
  <div class="backdrop">
  </div>
</div>  






  <!-- 결과 내용 -->
  <div class="content" v-if="button_on">
    <br><br>
    <div class="row" v-if="button_pick2">
        <div class="col-4 reco-img" v-for="movie in recommend_movies" :key="movie.pk">
          <div>{{ movie.title}}</div><br>
          <img @click="godetailmovie(movie.pk)" :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" alt="">
          <br><br><br>
        </div>
    </div>
    <div v-if="button_pick1">
      <div v-for="movie in random_recommend_movie" :key="movie.pk">
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
  data() {
    return {
      button_on: false,
      button_pick2: false,
      button_pick1: false,
      get_movies : [],
      showElement:false
    }
  },
  mounted() {
    const user_id = this.$route.params.user_id
    this.$store.dispatch('getRecommendMovies', user_id)
    this.showElement = true;
  },
  computed: {
    recommend_movies() {
      return this.$store.getters.recommend_moives
    },
    // button_on() {
    //   return this.button_on
    // }
    random_recommend_movie() {
      // this.movies = this.$store.getters.recommend_movies;
      // console.log(this.movies)
      // const randomIndex = Math.floor(Math.random() * 7);

      return this.$store.getters.recommend_movies
    },
    
      
    
  },
  methods: {
    godetailmovie(movie_id) {
      this.$router.push({ name: 'MovieDetailView', params: { movie_id: movie_id }})
    },
    recommends(idx) {
      this.button_on = true
      if (idx ==1) {
        this.button_pick1 = true
      }
      if (idx ==2) {
        this.button_pick2 = true
      }
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
.fade-in {
  opacity: 0;
  transition: opacity 10s;
}
.fade-in.active {
  opacity: 1;
}
/* 로딩 애니메이션 */
@import url(https://fonts.googleapis.com/css?family=Open+Sans+Condensed:300);
*, *:before, *:after {
  margin:0;
  padding:0;
  -webkit-box-sizing:border-box;
  -moz-box-sizing:border-box;
  box-sizing:border-box;
}
body {
  background:#58585A;
  /* -webkit-transform:translateZ(0); */
  display: flex;
  justify-content: center;
  align-items: center;
    flex-direction: row;
  gap: 2em;
  
  height: 100vh;
  width: 100vw;
  overflow: hidden;
  
  background-color: #1C1C25;
  font-family: 'Montserrat';
}
html, body {
  width:100%;
  height:100%;
}
/*
----------------------------------------------
Wrapper 
----------------------------------------------
*/
#loader {
  /* margin-top: 10vh; */
  position:absolute;
  top:0;
  right:0;
  bottom:0;
  left:0;
  width:100%;
  height:100%;
  display:flex;
  flex-direction:column;
  justify-content:center;
  align-items:center;
  background:#E9E8E3;
  z-index:99;
  /* 로딩 시작속도 */
  -webkit-animation:offscreen .5s 5s forwards; 
  animation:offscreen .5s 5s forwards;
}
#refresher {
  position:absolute;
  top:0;
  right:0;
  bottom:0;
  left:0;
  width:100%;
  height:100%;
  display:flex;
  flex-direction:column;
  justify-content:center;
  align-items:center;
  z-index:1;
  opacity:0;
  -webkit-animation:show .15s 5s forwards;
  animation:show .15s 5s forwards;
}
.refresh {
  color:#E9E8E3;
  font-family:'Open Sans Condensed', sans-serif;
  font-size:2rem;
  text-transform:uppercase;
  letter-spacing:.1rem;
}
.face {
  width:270px;
  height:270px;
}
/*
----------------------------------------------
SVG 
----------------------------------------------
*/
.head {
  transform-origin: 135px 135px;
  transform:scale(0);
  -webkit-animation:popup .6s 0.3s cubic-bezier(0.95, 0.05, 0.795, 0.035) forwards;
  animation:popup .6s 0.3s cubic-bezier(0.95, 0.05, 0.795, 0.035) forwards;
}
#eyeLeft, #eyeRight {
  transform:scale(0);
}
#eyeLeft {
  transform-origin:66px 127px;
  -webkit-animation:popup .5s 0.4s cubic-bezier(0.95, 0.05, 0.795, 0.035) forwards;
  animation:popup .5s 0.4s cubic-bezier(0.95, 0.05, 0.795, 0.035) forwards;
}
#eyeRight {
  transform-origin:203px 127px;
  -webkit-animation:popup .5s 0.4s cubic-bezier(0.95, 0.05, 0.795, 0.035) forwards;
  animation:popup .5s 0.4s cubic-bezier(0.95, 0.05, 0.795, 0.035) forwards;
}
.eyeLeft {
  transform-origin:66px 127px;
  -webkit-animation:downup 4s 0.5s cubic-bezier(.44,0,.01,.99) forwards;
  animation:downup 4s 0.5s cubic-bezier(.44,0,.01,.99) forwards;
}
.eyeRight {
  transform-origin:203px 127px;
  -webkit-animation:downup 4s 0.5s cubic-bezier(.44,0,.01,.99) forwards;
  animation:downup 4s 0.5s cubic-bezier(.44,0,.01,.99) forwards;
}
.eyeLeft > .pupil {
  transform-origin:66px 127px;
  -webkit-animation:follow 4s 0.5s forwards;
  animation:follow 4s 0.5s forwards;
}
.eyeRight > .pupil {
  transform-origin:203px 127px;
  -webkit-animation:follow 4s 0.5s forwards;
  animation:follow 4s 0.5s forwards;
}
.closedLeft {
  transform-origin:66px 127px;
  -webkit-animation:blink 4s 0.5s cubic-bezier(.44,0,.01,.99) forwards;
  animation:blink 4s 0.5s cubic-bezier(.44,0,.01,.99) forwards;
} 
.closedRight {
  transform-origin:203px 127px;
  -webkit-animation:blink 4s 0.5s cubic-bezier(.44,0,.01,.99) forwards;
  animation:blink 4s 0.5s cubic-bezier(.44,0,.01,.99) forwards;
}
.mouth {
  transform-origin:135px 233px;
  -webkit-animation:mouth 4s 0.5s cubic-bezier(.44,0,.01,.99) forwards;
  animation:mouth 4s 0.5s cubic-bezier(.44,0,.01,.99) forwards;
}
.bar {
  transform-origin:135px 233px;
  transform:scale(0);
  -webkit-animation:patient 4s 0.3s ease-in forwards;
  animation:patient 4s 0.3s ease-in forwards;
}
.smile {
  transform-origin:135px 233px;
  transform:scale(0);
  -webkit-animation:happy 4.3s 0.3s ease-in forwards;
  animation:happy 4.3s 0.3s ease-in forwards;
}
/*
----------------------------------------------
LOADING BAR 
----------------------------------------------
*/
.loading-bar {
  position:relative;
  margin-top:4rem;
  width:250px;
  background:#C1C0BC; 
}
.loading-bar:before {
  content:'';
  position:absolute;
  top:0;
  left:0;
  width:0;
  background:#58585A;
  -webkit-animation:load 4s 0.3s forwards;
  animation:load 4s 0.3s forwards;
}
.loading-bar, .loading-bar:before {
  height:4px;
  border-radius:5px;
}
/*
----------------------------------------------
ANIMATIONS
----------------------------------------------
*/
@keyframes popup {
  0% {transform:scale(0);}
  80% {transform:scale(1);}
  90% {transform:scale(0.75);}
  100% {transform:scale(1);}
}
@keyframes downup {
  0% {transform: translateY(0);}
  15% {transform: translateY(40px);}
  50% {opacity:1;}
  50.7% {opacity:0;}
  51.4% {opacity:1;}
  98% {transform: translateY(40px);}
  100% {transform: translateY(0);}
}
@keyframes mouth {
  0% {transform: translateY(-20px);}
  15% {transform: translateY(0px);}
  100% {transform: translateY(0px);}
}
@keyframes blink {
  0% {transform: translateY(0);}
  15% {transform: translateY(40px);}
  50% {opacity:1;}
  98% {transform: translateY(40px);}
  100% {transform: translateY(0);}
}
@keyframes follow {
  0% {transform: translate(0, 0);}
  15% {transform: translate(-4px, 8px);}
  95.5% {transform: translate(-2px, 10px);}
  98% {transform: translate(8px, 10px);}
  100% {transform: translate(0, 0);}
}
@keyframes patient {
  0% {transform:scale(0);}
  3% {transform:scale(0);}
  3.5% {transform:scale(1);}
  4% {transform:scale(0.75);}
  4.5% {transform:scale(1);}
  99% {transform:scale(1);}
  100% {transform:scale(0);}
}
@keyframes happy {
  0% {transform:scale(0);}
  98% {transform:scale(0);}
  100% {transform:scale(1);}
}
@keyframes load {
  0% {width:0;}
  97% {width:50px;}
  100% {width:250px;}
}
@keyframes offscreen {
  0% {transform:translateY(0);}
  100% {transform:translateY(-200%);}
}
@keyframes show {
  0% {opacity:0;}
  100% {opacity:1;}
}


/* 푸쉬 버튼 애니메이션 */
.button {
  height: 100px;
  width: 100px;
  border-radius: 100%;
  
  background-color: #25252F;
  filter: drop-shadow(0 10px 0 #101016);
  
  display: flex;
  justify-content: center;
  align-items: center;

  
  cursor: pointer;
  transition: all ease 0.1s;
  
  position: relative;
  top: -10px;
}

.fa {
  color: #656572;
}

.button:hover {
  transform: translate(0, 10px);
  filter: none;
  clip-path: circle(50%);
}

.button:hover > .fa {
  color: #C4C4C4;
}


.button:active {
  filter: drop-shadow(0 -10px 0 #101016);
  transform: translate(0, 20px);
  clip-path: circle(50% at 50px 40px);
  background-color: #21212A;
}

.cont {
  margin-top: 2vh;
  background-color: #25252F;
  border-radius: 15px;
  transition: all ease 0.3s;
  filter: drop-shadow(0 0 10px rgb(0,0,0,30%));
  border: solid 0.5px #25252F;
  
  display: flex;
  /* flex-direction: row; */
  justify-content: center;
  align-items: center;
  gap: 20px;
  height: 1200px;
  padding: 20px;
}
.textcont{
  position: absolute;
  margin-bottom: 500px;
}
.textconts{
  /* color: wheat; */
  font-size: 20px;
}
.cont:hover {
  background-color: #2D2D38;
  border: solid 0.5px #97979B;
}

.cont2 {
  height: 200px;
  width: 200px;
  background-color: #1C1C25;
  border-radius: 10px;
  
  display: flex;
  justify-content: space-around;
  align-items: center;
}

a {
  text-decoration: none;
  color: #656572;
  font-size: 20px;
}

.button:hover > a {
  color: #C4C4C4;
}


.screws {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  gap: 150px;
}

.screw {
  height: 10px;
  width: 10px;
  background-color: #3B3B44;
  border-radius: 100%;
}

.link {
  background-color: #1C1C25;

  border-radius: 10px;
  display: flex;
  align-items: center;
  color: #DBDBD4;
  padding: 20px;
}

.link-cont > .cont {
  height: 60px;
}

.link-button {
  border-radius: 5px;
  background-color: #44AC9E; 
  height: auto;
  width: auto;
  padding: 15px 20px;
  font-weight: bold;
  filter: drop-shadow(0 10px 0 #267267);
  clip-path: inset(0% 0% -50% 0% round 5px);

}

.link-button:hover {
  clip-path: inset(0% 0% 0% 0% round 5px);
  
}

.link-button:active {
  background-color: #3D9A8E;
  clip-path: inset(-30% 0% 20% 0% round 5px);
  filter: drop-shadow(0 -10px 0 #267267);
}

.link-button > a {
  color: #267267;
  font-size: 16px;
}

.link-button:hover > a {
   color: #267267;
}


.link-cont {
  visibility: hidden;
  display: none;
}

.link-cont.visible {
  display: flex;
  visibility: visible;
}

.link-main {
  position: absolute;
  z-index: 10;
  left: 20%;
}

.backdrop {
  position: absolute;
  width: 100%;
  height: 100%;
  background-color: rgb(29, 29, 38, 90%);
  z-index: 5;
  left: 0px;
  border-radius: 15px;
  display: none;
  visibility: hidden;
}

.backdrop.visible {
  display: block;
  visibility: visible;
  cursor: pointer;
}

.button-cont {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
  gap: 10px;
}

p {
  color: #C4C4C4;
  line-height: 0;
  font-size: 14px;
}
</style>