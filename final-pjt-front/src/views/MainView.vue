<template>
  <div id="mainview">
    <nav style="display: none;"></nav>
    
    <header>
      <!-- 영상 -->
      <section  class="content-section" data-scroll>
        <video  @wheel="handleWheelScroll" class="mainvideo" :style="{ opacity: videoOpacity, transform: 'scale(' + scale + ')' }" muted autoplay @ended="replay">
          <source src="@/movieplay/movie.mp4" type="video/mp4">
        </video>
      </section>
      
      <!-- 이미지 -->
      <div v-if="upimg" class="tvtable" data-aos="fade-up" data-aos-duration="1500">
        <img class="tvtableimg" :src="`${SERVER_URL}/media/table.png`" alt="">
      </div>
      
      <!-- 텍스트 -->
      <div class="maintext row" data-aos="fade-up" data-aos-duration="1000">
        <div class="maintext-text col-6">

          <div class="logocol" data-aos="fade" data-aos-duration="1000" data-aos-delay="200">
            <img class="navtableimg2" :src="`${SERVER_URL}/media/movisions.png`" alt="">
          </div>
        </div>
        <div class="img_text col-6">
          <div class="fads" data-aos="fade" data-aos-duration="2000" data-aos-delay="1000">
            <span class="count-num" data-count="7251">0</span> 개의 영화<br>
          </div>
          <div class="fads" data-aos="fade" data-aos-duration="2300" data-aos-delay="1300">
            <span class="count-num" data-count="130">0</span> 개의 OTT 공유그룹
          </div>
          <div class="fads" data-aos="fade" data-aos-duration="1000" data-aos-delay="1800">
            <span class="count-num" data-count="125" >0</span> 개의 리뷰<br>
          </div>
          <div class="fads" data-aos="fade" data-aos-duration="1000" data-aos-delay="2000">
            회원수 : <span class="count-num" data-count="42">0</span> 명
          </div>
        </div>
      </div>
      <!-- 텍스트 검색 -->
      <div class="maintext2">
        <div class='text-search'>
          <div>
            <p class='text3' data-count="48251" data-aos="fade-up" data-aos-duration="2200">
              영화 이름이 기억나지 않을때, 
            </p><br>
            <p class='text3' data-count="48251" data-aos="fade-up" data-aos-duration="2500">
              볼 영화가 없을때,
            </p><br>
          </div>
          <div>
            <p class='text3' data-count="48251" data-aos="fade-up" data-aos-duration="2800">
              좋아하는 장르와 영화를 기반으로 영화를 추천받고 싶다면,
              </p>
          </div><br>
          <div class="input_box" data-aos="fade-up" data-aos-duration="2800">
            <div class="container-4">
              <input type="search" id="search" placeholder="Search..." />
              <button @click="gosearchmovie" class="icon"><i class="fa fa-search">검색</i></button>
            </div>
          </div>
        </div>
      </div>
    </header>
    <!-- 검색버튼 -->
    <!-- <div class="button">
      <div class="compass"></div>
      <div class="msg">Over here !</div>
    </div> -->

    <main ><br><br><br><br><br><br>
      <!-- 영화 포스터 슬라이드-->
      <h3 class="office">월간 박스 오피스</h3><br>
      <div class="slide_wrapper">
        <!-- 왼쪽버튼 -->
        <div class="prev" @click='prev' style="position: absolute; top: 50%; left: 5%; transform: translate(-50%, -50%); z-index: 1;">
          <!-- <button>prev</button> -->
          <svg style="position: absolut; top: 50%; left: 5%; transform: translate(-50%, -50%); z-index: 1;  fill: white;" xmlns="http://www.w3.org/2000/svg" width="60" height="60" fill="currentColor" class="prev bi bi-chevron-compact-left" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M9.224 1.553a.5.5 0 0 1 .223.67L6.56 8l2.888 5.776a.5.5 0 1 1-.894.448l-3-6a.5.5 0 0 1 0-.448l3-6a.5.5 0 0 1 .67-.223z"/>
          </svg>
        </div>
        <!-- 오른쪽버튼 -->
        <div class="next" @click='next' style="position: absolute; top: 50%; left: 95%; transform: translate(-50%, -50%); z-index: 1;">
          <svg style="position: absolute; top: 50%; left: 95%; transform: translate(-50%, -50%); z-index: 1;  fill: white;" xmlns="http://www.w3.org/2000/svg" width="60" height="60" fill="currentColor" class="next bi bi-chevron-compact-right" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M6.776 1.553a.5.5 0 0 1 .671.223l3 6a.5.5 0 0 1 0 .448l-3 6a.5.5 0 1 1-.894-.448L9.44 8 6.553 2.224a.5.5 0 0 1 .223-.671z"/>
          </svg>
        </div>
        <!-- 슬라이드 -->
        <ul class="slides">
          <li class="snip1" v-for="(populor_movie,idx) in top10_movies" :key="idx">
              <div style="position: relative;">
                <button @click="gomovie(populor_movie.id)" style="position: absolute; top: 60%; left: 50%; transform: translate(-50%, -50%); ">영화 정보보기</button>
                <p style="position:absolute; top: 40%; left: 50%; transform: translate(-50%, -50%); font-size: 3vh;">{{populor_movie.title}}</p>
                <img :src="`https://image.tmdb.org/t/p/original${populor_movie.backdrop_path}`" class="card-img-top" alt="..." style="border-radius: 15px; object-fit: cover; width: 100%; height: 100%;">
              </div>
          </li>
        </ul>
      </div>
      <br>
      <!-- <p style="color: white; font-family: 'Helvetica Neue', Arial, sans-serif; margin-top: 15px;">최신 영화</p> -->
      <div class="slide_wrapper2">
        <ul class="slides2">
          <li class="snip1" v-for="(recent30_movie,idx) in recent30_movies" :key="idx">
            <div style="position: relative;">
              <button @click="gomovie(recent30_movie.id)" style="position: absolute; top: 65%; left: 50%; transform: translate(-50%, -50%); ">영화 정보보기</button>
              <p style="position:absolute; top: 35%; left: 50%; transform: translate(-50%, -50%); font-size: 1.5vh;">{{recent30_movie.title}}</p>
              <img :src="`https://image.tmdb.org/t/p/original${recent30_movie.backdrop_path}`" class="card-img-top" alt="..." style="border-radius: 10px; object-fit: cover; width: 100%; height: 100%;">
            </div>
          </li>
        </ul>
      </div>

      <!-- <p style="color: white; font-family: 'Helvetica Neue', Arial, sans-serif;">개봉 예정 영화</p> -->
      <div class="slide_wrapper3">
        <ul class="slides3">
          <li class="snip1" v-for="(new10_movie,idx) in new10_movies" :key="idx">
            <div style="position: relative;">
              <button @click="gomovie(new10_movie.id)" style="position: absolute; top: 65%; left: 50%; transform: translate(-50%, -50%); ">영화 정보보기</button>
              <p style="position:absolute; top: 35%; left: 50%; transform: translate(-50%, -50%); font-size: 1.5vh;">{{new10_movie.title}}</p>
              <!-- {{new10_movie.backdrop_path}} -->
              <img :src="`https://image.tmdb.org/t/p/original${new10_movie.backdrop_path}`" class="card-img-top" alt="..." style="border-radius: 10px; object-fit: cover; width: 100%; height: 100%;">
            </div>
          </li>
        </ul>
      </div>



<!-- 
      <div class="mainbox search" data-aos="fade-up" data-aos-duration="1000">
        <div class="custom-1wp6uk4">
          <h3 class="custom-1histt2">
            <span>세상의 모든 영화 종류별 검색<br></span>
          </h3><br>
          <div class="custom-1yltisf">
          </div>
        </div>
        <img class="mainimg" src="@/assets/mainsearch.jpg" alt="mainsearch">
      </div> -->
      
    </main>

    <footer>
      <div class="endbox" data-aos="fade-up" data-aos-duration="1000"></div>
    </footer>
  </div>
</template>

<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
<script src="https://unpkg.com/scroll-out/dist/scroll-out.min.js"></script>
<script>
AOS.init();

// import VueSimpleScrollbar from 'vue-simple-scrollbar'
// import common from '@/assets/js/common.js'
import $ from 'jquery'
// import 'simplyscroll'
// Vue.use(common)


export default {
  name: 'MainView',
  data() {
    return {
      SERVER_URL: 'http://localhost:8000',
      maintextvis: 0,
      scale: 1, // 초기 축소 비율
      scaleFactor: 0.05, // 스크롤 한 번당 축소 비율
      minScale: 0.5, // 최소 축소 비율
      maxScale: 1, // 최대 축소 비율
      videoOpacity: 1,  //영상 투명도
      // pass_scrolling :1,
      // currentIdx : 0,
      slideCount: 0, // 초기 슬라이드1의 갯수
      slideWidth1: 900,   //슬라이드1의 개당 길이
      slideMargin1: 18,   //슬라이드 1의 개당 마진
      newWidth: 1500,   // 슬라이드1의 전체 길이
      newSlideCount: 0,    // 슬라이드1 갯수
      currentIdx :0,  //현재 슬라이드1의 위치
      upimg : false,


    }
  },
  mounted() {
    console.log(this.$store.getters.movies)
    if (!this.$store.getters.movies) {
      this.$store.dispatch('fetchMovies');
    } else {
      this.$store.dispatch('fetchMovies');
    }

    //휠스크롤 영상 축소
    
    this.numcount()
    window.addEventListener('scroll', this.handleScroll)
  
    var slides = this.$el.querySelector('.slides');               //슬라이드 구현
    var slide = this.$el.querySelectorAll('.slides li');
    var currentIdx = 0;
    var slideCount = slide.length;
    var slideWidth = 900;
    var slideMargin = 18;
    var prevBtn = this.$el.querySelector('.prev');
    var nextBtn = this.$el.querySelector('.next');

    makeClone();

    function makeClone() {
      for (var i = 0; i < slideCount; i++) {
        var cloneSlide = slide[i].cloneNode(true);
        cloneSlide.classList.add('clone');
        slides.appendChild(cloneSlide);
      }
      for (var i = slideCount - 1; i >= 0; i--) {
        var cloneSlide = slide[i].cloneNode(true);
        cloneSlide.classList.add('clone');
        slides.prepend(cloneSlide);
      }
     updateWidth();
      setInitialPos(); 
      setTimeout(function(){
        slides.classList.add('animated');

      },100);
    }

    function updateWidth() {
      var currentSlides = slides.querySelectorAll('.slides li');
      var newSlideCount = currentSlides.length;
      var newWidth = (slideWidth + slideMargin) * newSlideCount - slideMargin;
      slides.style.width = newWidth+'px';
 
    }   //
    function setInitialPos(){     // 슬라이드 중앙에 배치하기위에 앞쪽의 길이 계산
      var initialTranslateValue = -(slideWidth+slideMargin)*slideCount+280;   //시작위치 결정
      slides.style.transform='translateX('+initialTranslateValue+'px)';
      console.log('translateX('+initialTranslateValue+'px)')
    }

    nextBtn.addEventListener('click',function() {
      moveSlide(currentIdx+1);

    })
    prevBtn.addEventListener('click',function() {
      moveSlide(currentIdx-1);
    })
    
    function moveSlide(num){
      slides.style.left = -num*(slideWidth+slideMargin)+'px';      //버튼 누를시 이동할 거리
      currentIdx =num;

      if(currentIdx ==slideCount || currentIdx == -slideCount){                      //일정 범위이후 재위치로 || 반대방향 추가
        setTimeout(function(){
          slides.classList.remove('animated');
          slides.style.left = '0px';                   //재위치
          currentIdx =0;
        },500);
        setTimeout(function(){
          slides.classList.add('animated');
        },600);
      }
    }
  var timer =undefined;    // 자동 이동 
  
  function autoSlide() {
    if(timer ==undefined) {
      timer =setInterval(function(){   //반복호출
        moveSlide(currentIdx +1);
      }, 3000);
    }
  }
  function autoSlide() {
    if(timer ==undefined) {
      timer =setInterval(function(){   //반복호출
        moveSlide(currentIdx +1);
      }, 3000);
    }
  }
  autoSlide();
  function stopSlide() {
    clearInterval(timer);
  }
  slides.addEventListener('mouseenter',function(){    // 마우스 갖다 대면 이벤트 정지
    stopSlide();
  });
  slides.addEventListener('mouseleave',function(){
    autoSlide();
  }) //
  // 2,3번 슬라이드
  var slides2 = this.$el.querySelector('.slides2');
  var slides3 = this.$el.querySelector('.slides3');
  var slide2 = this.$el.querySelectorAll('.slides2 li');
  var slide3 = this.$el.querySelectorAll('.slides3 li');
  var slideCount2 =slide2.length;
  var slideCount3 =slide3.length;

  makeClone2();
  makeClone3();

  function makeClone2(){
    for (var j =0; j < slideCount; j++) {
      var cloneSlide2 = slide[j].cloneNode(true);
      cloneSlide2.classList.add('clone');
      slides2.appendChild(cloneSlide2);
    }}
  function makeClone3(){
    for (var j =0; j < slideCount; j++) {
      var cloneSlide3 = slide[j].cloneNode(true);
      cloneSlide3.classList.add('clone');
      slides3.appendChild(cloneSlide3);
    }}
  updateWidth2();
  // setInitialPos2(); 
  updateWidth3();
  // setInitialPos3(); 

    function updateWidth2() {
      var currentSlides2 = slides2.querySelectorAll('.slides2 li');
      var newSlideCount2 = currentSlides2.length;
      var newWidth2 = (slideWidth + slideMargin) * newSlideCount2 - slideMargin + 'px';
      slides2.style.width = newWidth2;
    }   
    function updateWidth3() {
      var currentSlides3 = slides3.querySelectorAll('.slides3 li');
      var newSlideCount3 = currentSlides3.length;
      var newWidth3 = (slideWidth + slideMargin) * newSlideCount3 - slideMargin + 'px';
      slides3.style.width = newWidth3;
    }   //

  // slides2.addEventListener('mouseenter',function(){    // 마우스 갖다 대면 이벤트 정지
  //   slowSlide2();
  // });
  // slides2.addEventListener('mouseleave',function(){
  //   autoSlide2();
  // }) //
  // function slowSlide2() {
  //   slides2.style.animation = 'slide-animation2 60s linear infinite'
  // }
  // function autoSlide2() {
  //   slides2.style.animation = 'slide-animation2 50s linear infinite'
  // }
  // slides3.addEventListener('mouseenter',function(){    // 마우스 갖다 대면 이벤트 정지
  //   slowSlide3();
  // });
  // slides3.addEventListener('mouseleave',function(){
  //   autoSlide3();
  // }) //
  // function slowSlide3() {
  //   slides3.style.animation = 'slide-animation3 50s linear infinite'
  // }
  // function autoSlide3() {
  //   slides3.style.animation = 'slide-animation3 25s linear infinite'
  // }



  }, 
  computed: {
    top10_movies() {
      return this.$store.getters.top10_movies.reverse()
    },
    recent30_movies() {
      return this.$store.getters.recent30_movies
    },
    new10_movies() {
      console.log('확인')
  
      return this.$store.getters.new10_movies
    },
    currentuser() {
      return this.$store.getters.currentuser
    }
  },

  methods: {
    // 영상 확대 축소
    handleWheelScroll(event) {

      // const mainVideo = document.querySelector('.mainvideo');
  
        // 휠 스크롤 방향에 따라 축소 비율 조절
        if (event.deltaY > 0) {
          this.scale -= 0.05; // 비디오 크기조절
          this.videoOpacity = 0.6;   //비디오 투명도 조절
          this.scale = Math.max(this.scale, this.minScale);
        } else {
          this.scale += this.scaleFactor;
          this.scale = Math.min(this.scale, this.maxScale);
        }
        // 비디오 컨테이너에 축소 비율 적용
        // this.sacle = `scale(${this.scale})`;
        if (this.scale <0.8) {
          this.upimg = true 

        }
        if (this.scale <0.6) {

          document.body.style.overflow = '';
          
        }
      
    },

    replay(event) {
      event.target.currentTime = 0;
      event.target.play();
    },
        
    next() {
      console.log('asdf')
      this.moveSlide(this.currentIdx+1);
    },
    prev() {
      this.moveSlide(this.currentIdx-1);
    },
    //슬라이드1
    moveSlide(num) {
      console.log(this.slideMargin)
      this.slides.style.left = -num*(this.slideWidth+this.slideMargin)+'px';      //버튼 누를시 이동할 거리
      this.currentIdx =num;

      if(this.currentIdx == this.slideCount || this.currentIdx == -this.slideCount){                      //일정 범위이후 재위치로 || 반대방향 추가
        setTimeout(function(){
          slides.classList.remove('animated');
          slides.style.left = '0px';                   //재위치
          this.currentIdx =0;
        },500);
        setTimeout(function(){
          slides.classList.add('animated');
        },600);
      }
    },
    //슬라이드 1
    numcount() {
      $('.count-num').each(function() { 
      var $this = $(this),
          countTo = $this.attr('data-count');
          
      $({ countNum: $this.text()}).animate({
        countNum: countTo 
      },
      {
      duration: 3000, 
      easing:'linear',
      step: function() {
        $this.text(Math.floor(this.countNum));
      },
      complete: function() { 
        $this.text(this.countNum);
      }
      });  
    });
    },

    //영화 세부페이지 이동
    gomovie(movie_id) {
      // console.log(movie_id)
      this.$router.push({ name: 'MovieDetailView', params: { movie_id: movie.id }})
    },

    //검색기능
    gosearchmovie() {
      this.$router.push({ name: 'SearchView'})
    }
  },
}

</script>

<style>
/* @import url("http://www.songdobeer.com/songdo_html/lib/simplyscroll/simplyscroll.css"); */


#mainview {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #343235;
}

/* 영상 헤더 */
header {
  /* background: rgb(46, 46, 53); */
  display: flex;
  flex-direction: column;
  /* align-items: center; */
  
}
.mainvideo {
  align-items: center;
  width: 2000px;
  /* 비디오 확대축소 애니메이션 */
  transition: transform 0.5s ease;   
  opacity: 1;
  border: 30px solid black;
  /* margin: 200px; */
  /* filter: blur(2px); 약간의 흐릿한 효과를 주는 필터 */
}

/* 텍스트바 */
.tvtable {
  margin: 0px auto;
  width: 1500px;
  height: 400px;
  /* background-color: black; */
}
.tvtableimg {
  margin-top: -100px;
  width: 1300px;
  height: 200px;
  /* background-color: black; */
}

.maintext { 
  /* display: flex; */
  /* flex-direction: column; */
  /* justify-content: center; */
  /* align-items: center; */
  width: 2000px;
  height: 600px;
  /* background: rebeccapurple; */
  overflow: hidden;
  margin-top:20vh;
  /* color: white; */
  opacity: 0;
  font-size: 30px;
  background-color: #3f3d40;
}
.maintext {
  width: 2000px;
}
.text-search {
  font-size: 40px;
  background-color: #3f3d40;
}
.img_text {
  margin: auto;
}
.fads {
  color: #cdb5b5;
  text-decoration: underline;
  
}
.count-num {
  color: #979720;
  font-size: 50px;
}
.logocol {
  display: flex;
  align-items: center;
  margin-top: 200px;
  margin-left: 150px;
}
/* 검색 버튼 */
/* .button {
    position: fixed;
    left:80%; top:50%;
    width:100px; height:100px;
    margin:-70px 0 0 -70px;
    cursor: pointer;
}
.compass {
    position: absolute;
    width:100%; height:100%;
    background: #444;
    border-radius: 0 50% 50% 50%;
    border: 10px solid white;
    box-shadow: 0 0 8px rgba(0,0,0,.2);
    border-right-color: coral;
    border-bottom-color: coral;
    transition: border-radius .2s;
    box-sizing: border-box;
}
.button:hover .compass {
    border-radius: 50%;
}
.msg {
    position: absolute;
    width:100%; height:100%;
    line-height: 140px;
    text-align: center;
    color: #fff;
    font-family: 'Roboto', sans-serif;
    font-size: 20px;
    font-weight: 300;
} */

/* 검색2 */
.input_box {
  margin-top: 20px;
  margin-bottom: 50px;
  display: flex;
  justify-content: center;
}
.icon {

  border: 20px solid green;

}
.container-4{
  overflow: hidden;
  width: 700px;
  vertical-align: middle;
  white-space: nowrap;
  /* border: 5px solid black */
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


main {
  width: 1500px;
  margin-top: 100px;
}

.mainbox {
  display: flex;
  flex-direction: column;
  justify-content: center;
  position: relative;
  width: 75vw;
  height: 25vh;
  aspect-ratio: 16/6;
  background: rgb(75, 69, 69);
  overflow: hidden;
  margin: 2vw;
  color: white;
}

/* .mainbox:hover{
  background-color: gray;
} */
/* 
.mainimg {
  top: 0;
  left: 0;
  position: absolute;
  width: 100vw;
  opacity: 0.4;
} */

.custom-1wp6uk4 {
    position: relative;
    z-index: 100;
    text-align: center;
}

.custom-1histt2 {
    color: #fff;
    font-size: 2vw;
    font-weight: 400;
    letter-spacing: -0.24305555555555555vw;
    line-height: 4.375vw;
    white-space: pre-wrap;
    margin-bottom: 1.1111111111111112vw;
}

.custom-1yltisf {
  text-align: center;
}
.endbox {
  background-color: #201c12;
  width: 100vw;
  height: 50px;
}
.text3 {
  font-size: 35px;
  color: rgb(225, 222, 222);
}
.custom-1cqzdpo {
    display: inline-block;
    background-color: #917c4e;
    color: #FFFFFF;
    /* font-size: 15px; */
    /* font-weight: 700; */
    /* letter-spacing: -0.1px; */
    /* line-height: 51px; */
    text-align: center;
    /* width: 100%; */
    /* height: 52px; */
    border-radius: 40px;
    font-size: 1vw;
    font-weight: 700;
    letter-spacing: -0.0625vw;
    line-height: 4.166666666666666vw;
    width: auto;
    min-width: 13.125vw;
    height: 4.166666666666666vw;
    padding: 0 1.5625vw;
    border-radius: 2.083333333333333vw;
    text-decoration: none;
  }
  
  .searchbox {
    display: flex;
    margin: 0 19%;
  }
  
  .searchinput {
    width: 50vw;
    height: 4.166666666666666vw;
    background-color:rgba(217.0000022649765, 217.0000022649765, 217.0000022649765, 1);
    border-top-left-radius: 2.083333333333333vw;
    border-bottom-left-radius:2.083333333333333vw;
    
  }
  
  .searchsubmit {
    width: 6.5vw;
    height: 4.166666666666666vw;
    /* background-color:rgba(217.0000022649765, 217.0000022649765, 217.0000022649765, 1); */
    background-color: #ffb10a;
    border-top-right-radius: 2.083333333333333vw;
    border-bottom-right-radius: 2.083333333333333vw;
    
  }
/* 슬라이드 css */
.slide_wrapper {   
  position: relative;
  /* width: 95%; */
  margin: 0 auto;
  height: 550px;
  overflow: hidden;
}
.slides{
  position:absolute;
  left: 0;
  top: 0;
}
.slides.animated{
  transition: 0.5s ease-out;
}
.slides li{
  width: 900px;
  height: 500px;
  background: #ccc;
  float: left;
  border-radius: 15px;
}
.slides li:not(:last-child){
  margin-right: 15px;
}

/* 마우스 오버 효과 */
.snip1 {
  overflow: hidden;
  background: #000000;
}

.snip1 * {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-transition: all 0.45s ease-in-out;
  transition: all 0.45s ease-in-out;
}

.snip1 img {
  max-width: 100%;
  position: relative;
  opacity: 1;
}
.office {
  font-size : 50px;
  margin-bottom: 30px;
  color: #a3a7aa;
  shape-outside: -moz-element();
  text-decoration: underline;
}

.snip1:hover img,
.snip1.hover img {
  opacity: 0.5;
  -webkit-transform: scale(1.05);
  transform: scale(1.05);
}


/* 슬라이드 css 2 */
.slide_wrapper2 {   
  position: relative;
  /* width: 95%; */
  margin: 0 auto;
  height: 160px;
  overflow: hidden;
}
.slides2{
  position:absolute;
  left: 0;
  top: 0;
  animation: slide-animation2 27s linear infinite;

}
@keyframes slide-animation2 {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-2200px);
  }
}
.slides2 li{
  width: 250px;
  /* height: 160px; */
  background: #ccc;
  float: left;
  border-radius: 10px;
}
.slides2 li:not(:last-child){
  margin-right: 18px;
}

/* 슬라이드 css 3 */
.slide_wrapper3 {   
  position: relative;
  /* width: 95%; */
  margin: 0 auto;
  height: 180px;
  overflow: hidden;
}
.slides3{
  position:absolute;
  left: 0;
  top: 0;
  animation: slide-animation3 25s linear infinite;
}
@keyframes slide-animation3 {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-2200px);
  }
}
.slides3 li{
  width: 250px;
  /* height: 160px; */
  background: #ccc;
  float: left;
  border-radius: 10px;
}
.slides3 li:not(:last-child){
  margin-right: 18px;
}





  footer {
    color: white;
  }
  </style>