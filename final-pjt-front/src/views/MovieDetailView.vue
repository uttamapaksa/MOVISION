<template>
<div id="moviedetailview">
  <div class="poster-header">poster header</div>
  <div class="poster-line">
    <div class="poster-img">
    </div>
    
    <div class="poster-detail">
      <div class="detail-info">
        <div class="detailss">제목</div>
        <div class="detailss">상영연도</div>
        <div class="detailss">평점</div>
        <div class="detailss">장르(누르면 장르별 검색 이동)</div>
        <div class="detailss">인기</div>
        <div class="detailss">개봉일자</div>
        <div class="detailss">좋아요</div>
        <div class="detailss">언어</div>
        <div class="detailss">예고편보기</div>
      </div>

      <div class="detail-overview">
        <div class="detailss">개요</div>
      </div>
    </div>

  </div>

  <div class="one-comment">one comment</div>
  <div class="">이 영화를 좋아하는 사람들이 본 영화</div>
  <div class="director-actor">director-actor</div>
  <div class="detail-ost">OST</div>

  <div class="reviews row">
    <h1>리뷰</h1>
    <div class="review col-5 m-auto"></div>
    <div class="review col-5 m-auto"></div>
    <div class="review col-5 m-auto"></div>
    <div class="review col-5 m-auto"></div>
  </div>
</div>
</template>

<script>
export default {
  name: 'MovieDetailView',
}
</script>

<style>
.poster-header {
  width: 90%;
  height: 15vh;
  background: orange;
}

.poster-line {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  border: solid 3px blueviolet;
  width: 90%;
  height: 55vh;
}

.poster-img {
  border: solid 3px blueviolet;
  width: 25%;
  height: 45vh;
}

.poster-detail {
  display: flex;
  flex-direction: column;
  width: 65%;
  height: 45vh;
}

.detail-info {
  border: solid 3px blueviolet;
  width: 100%;
  height: 30vh;
  
}
.detail-overview {
  border: solid 3px blueviolet;
  width: 100%;
  height: 15vh;
}

.detailss {
  border: solid 2px lightcoral;
  width: 20%;
  height: 10%;
}

.one-comment {
  border: solid 3px blueviolet;
  width: 90%;
  height: 20vh;
}

.director-actor {
  border: solid 3px blue;
  width: 90%;
  height: 35vh;
}
.detail-ost {
  border: solid 3px blue;
  width: 90%;
  height: 20vh;
}

.reviews {
  display: flex;
  border: solid 3px blue;
  width: 90%;
  height: 40vh;
}

.review {
  border: solid 3px green;
  width: 40%;
  height: 15vh;
}
</style>