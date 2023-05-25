<template>
  <div class="article-list" @click="goreviewdetail">
    <div class="article-title">
    제목 : {{ article.title }}
    </div>

    <div class="article-user" @click="goprofiledetail(article.user)">
      {{ article.username}}
    </div>
    <div class="article-date">
      {{article.created_at.slice(0,10)}}
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
    },
    goprofiledetail(profile_id) {
      this.$store.dispatch('getProfile', profile_id)
      this.$router.push({name: 'ProfileView', params: {profile_id: profile_id}})
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
  height: 10vh;
  font-size: 2.3vh;
}


.article-title {
  margin: auto 10px;
  /* border: solid 1px red; */
  width: 60%;
  overflow: hidden;
}

.article-user {
  margin: auto 0;
  /* border: solid 1px purple; */
  width: 20%;
  overflow: hidden;
}

.article-user:hover {
  color: rgb(255, 98, 0);
}

.article-date {
  margin: auto 0;
  /* border: solid 1px purple; */
  width: 20%;
  overflow: hidden;
}
</style>