<template>
  <div id="mainview">
    <nav style="display: none;"></nav>
    
    <header>
      <section @click='check' class="content-section" data-scroll>
        <figure class="figure">
          <video class="mainvideo" muted autoplay @ended="replay">
            <source src="@/movieplay/movie.mp4" type="video/mp4">
          </video>
        </figure>
      </section>
      <div class="maintext" data-aos="fade-up" data-aos-duration="1000">
        <div class="maintext-text">
          <div class="logocol" data-aos="fade" data-aos-duration="1000" data-aos-delay="200">
            <img style="height: 70%" src="../assets/logo.png" alt="logo.png">
          </div>
          <div class="numcol" data-count="48251" data-aos="fade-up" data-aos-duration="1000">
            <div style="height: 80%;">
              <div data-aos="fade" data-aos-duration="1000" data-aos-delay="500">
                <span class="count-num" data-count="48251">0</span> 개의 영화<br>
              </div>
              <div data-aos="fade" data-aos-duration="1000" data-aos-delay="1000">
                <span class="count-num" data-count="125439" >0</span> 개의 리뷰<br>
              </div>
              <div data-aos="fade" data-aos-duration="1000" data-aos-delay="1500">
                회원수 : <span class="count-num" data-count="304">0</span> 명
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
    
    
    <main >

      <br><br><br>
      <br><br><br>
    <div class="slide_wrapper">
      <ul class="slides">
        <li>slide 01</li>
        <li>slide 02</li>
        <li>slide 03</li>
        <li>slide 04</li>
        <li>slide 05</li>
      </ul>
    </div>
    <p class="controls">
      <span class="prev">prev</span>
      <span class="next">next</span>
      <span class="material-symbols-outlined">arrow_forward_ios</span>
    </p>
    
    <div class="slide_wrapper2">
      <ul class="slides2">
        <li>slide 11</li>
        <li>slide 12</li>
        <li>slide 13</li>
        <li>slide 14</li>
        <li>slide 15</li>
      </ul>
    </div>

    <div class="slide_wrapper3">
      <ul class="slides3">
        <li>slide 21</li>
        <li>slide 22</li>
        <li>slide 23</li>
        <li>slide 24</li>
        <li>slide 25</li>
      </ul>
    </div>




      <div class="mainbox"  data-aos="fade-up" data-aos-duration="1000">
        <h3>최신 영화</h3>
        <br>
        <h3>개봉 예정 영화</h3>
        <br>
      </div>
      
      <div class="searchbox" data-aos="fade-up" data-aos-duration="1000">
        <div class="searchinput"></div>
        <router-link :to="{name: 'search'}">
          <div class="searchsubmit">
          </div>
        </router-link>
      </div>


      <div class="mainbox search" data-aos="fade-up" data-aos-duration="1000">
        <div class="custom-1wp6uk4">
          <h3 class="custom-1histt2">
            <span>세상의 모든 영화 종류별 검색<br></span>
          </h3><br>
          <div class="custom-1yltisf">
          </div>
        </div>
        <img class="mainimg" src="@/assets/mainsearch.jpg" alt="mainsearch">
      </div>
      
      <div class="mainbox popular" data-aos="fade-up"
     data-aos-duration="1000">
        <div class="custom-1wp6uk4">
          <h3 class="custom-1histt2">
            <span>현재 가장 HOT한 영화 인기 순위<br></span>
          </h3>
          <div class="custom-1yltisf">
            <router-link :to="{name: 'popular'}" class="custom-1cqzdpo">인기순위 보기</router-link>
          </div>
        </div>
        <img class="mainimg" src="@/assets/mainpopular.jpg" alt="mainpopular">
      </div>
      
      <div class="mainbox recommend" data-aos="fade-up"
     data-aos-duration="1000">
        <div class="custom-1wp6uk4">
          <h3 class="custom-1histt2">
            <span>내 맘대로 고르는 맞춤 영화 추천<br></span>
          </h3>
          <div class="custom-1yltisf">
            <router-link :to="{name: 'recommend'}" class="custom-1cqzdpo">영화 추천받기</router-link>
          </div>
        </div>
        <img class="mainimg" src="@/assets/mainrecommend.jpg" alt="mainrecommend">
      </div>
      
      <div class="mainbox user-recommend" data-aos="fade-up"
     data-aos-duration="1000">
        <div class="custom-1wp6uk4">
          <h3 class="custom-1histt2">
            <span>user님 이런 영화 어떠세요?<br></span>
          </h3>
          <div class="custom-1yltisf">
            <a href="#" class="custom-1cqzdpo">#</a>
          </div>
        </div>
      </div>
  
      <div class="mainbox" data-aos="fade-up"
     data-aos-duration="1000">
        <h3>유저 기반 추천리스트 모음</h3>
      </div>
  
    </main>

    <footer>
      <h3>footer</h3>
      <br>
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
      maintextvis: 0
    }
  },
  mounted() {
    if (!this.$store.state.movies.length) {
      this.$store.dispatch('fetchMovies');
      console.log(this.$store.state.movies)
    } else {
      console.log(this.$store.state.movies)
    }

    this.numcount()
    window.addEventListener('scroll', this.handleScroll)

    var slides = this.$el.querySelector('.slides');               //슬라이드 구현
    var slide = this.$el.querySelectorAll('.slides li');
    var currentIdx = 0;
    var slideCount = slide.length;
    var slideWidth = 550;
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
      var initialTranslateValue = -(slideWidth+slideMargin)*slideCount+100;   //시작위치 결정
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

  slides2.addEventListener('mouseenter',function(){    // 마우스 갖다 대면 이벤트 정지
    slowSlide2();
  });
  slides2.addEventListener('mouseleave',function(){
    autoSlide2();
  }) //
  function slowSlide2() {
    slides2.style.animation = 'slide-animation2 52s linear infinite'
  }
  function autoSlide2() {
    slides2.style.animation = 'slide-animation2 27s linear infinite'
  }
  slides3.addEventListener('mouseenter',function(){    // 마우스 갖다 대면 이벤트 정지
    slowSlide3();
  });
  slides3.addEventListener('mouseleave',function(){
    autoSlide3();
  }) //
  function slowSlide3() {
    slides3.style.animation = 'slide-animation3 50s linear infinite'
  }
  function autoSlide3() {
    slides3.style.animation = 'slide-animation3 25s linear infinite'
  }



  }, 

  methods: {
    replay(event) {
      event.target.currentTime = 0;
      event.target.play();
    },
    
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

  check() {

  }
    // handleScroll() {
    //   const service = document.querySelector('.maintext');
    //   const threshold = window.pageYOffset;
    //   const serviceTop = service.offsetTop-710;
    //   console.log(service)
    //   console.log(threshold)
    //   console.log(serviceTop)
      

    //   if (serviceTop < threshold) {
    //     this.isServiced = 1
    //     console.log(this.isServiced, 'aaaaaaaaaaa')
    //   } else {
    //     this.isServiced = 0
    //     console.log(this.isServiced, 'aaaaaaaaaaa')
    //   }
    // }
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

header {
  background: rgb(46, 46, 53);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.maintext {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 75vw;
  height: 40vh;
  background: rebeccapurple;
  overflow: hidden;
  margin: 2vw;
  color: white;
  opacity: 0;
}

.maintext-text {
  display: flex;
  width: 75vw;
  height: 25vh;
  background: rgb(75, 69, 69);
  overflow: hidden;
  color: white;
}

.logocol {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 50%;
}

.numcol {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 50%;
  font-size: 3vh;
}

.count-num {
  text-align: center;
  font-weight: 700;
  height: 5vh;
}

.mainvideo {
  width: 100%;
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

.mainimg {
  top: 0;
  left: 0;
  position: absolute;
  width: 100vw;
  opacity: 0.4;
}

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

.custom-1cqzdpo {
    display: inline-block;
    background-color: #ffb10a;
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
  width: 95%;
  margin: 0 auto;
  height: 420px;
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
  width: 550px;
  height: 390px;
  background: #ccc;
  float: left;
  border-radius: 15px;
}
.slides li:not(:last-child){
  margin-right: 18px;
}
/* 슬라이드 css 2 */
.slide_wrapper2 {   
  position: relative;
  width: 95%;
  margin: 0 auto;
  height: 180px;
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
  width: 260px;
  height: 160px;
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
  width: 95%;
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
  width: 260px;
  height: 160px;
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