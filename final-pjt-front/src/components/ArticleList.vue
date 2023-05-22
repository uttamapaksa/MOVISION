<template>
  <div class="article-list" @click="goreviewdetail">
    <div class="article-pic">
    {{article.picture}}

    </div>
    <div class="article-title">
    작성자 : {{ article.user}}
    
    제목 :{{article.title}}

    영화 제목 : ㅁㅁㅁㅁ
    (내용) : ~~~~~~
    작성일 : num

    </div>

    <div class="article-rate">
    별점 : 

    </div>
    
  </div>
</template>

<script>

export default {
  name : 'ArticleList',
  props: {
    article: Object,
  },
  methods: {
    goreviewdetail() {
      this.$router.push({name: 'ReviewDetialView', params:{review_id:this.article.id}})
    }
  }
}
</script>

<style>
.article-list {
  display: flex;
  border: solid 1px green;
  width: 100%;
  margin: 0 auto;
  height: 50px;
}

.article-pic {
  border: solid 1px red;
  width: 30%;
}
.article-title {
  border: solid 1px red;
  width: 60%;
}

.article-rate {
  border: solid 1px purple;
  width: 10%;
}
</style>