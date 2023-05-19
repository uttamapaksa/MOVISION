<template>
<div class="ArticleView">
    
    <div>
      <button @click="party=false">리뷰</button>
      <button @click="party=true" >모집</button>
    </div>


    <div v-if="!party">
      <h3>리뷰게시판</h3>
      <div class="commu-box">
      <ArticleList v-for="(article, idx) in articles" :key="idx" :article="article"/>
      </div>
      <br>
      <div class="search-bar">
        <input type="text">
        <input type="submit" value="검색">
      </div>
      <br>
    </div>
    <div v-if="party">
      <h3>모집게시판</h3>
      <div class="commu-box">
        <div class="party-list">
          <div class="party-site">
            <button @click="site=0">전체</button>
            <button @click="site=1">디즈니플러스</button>
            <button @click="site=2">넷플릭스</button>
            <button @click="site=3">왓챠</button>
            <button @click="site=4">유튜브</button>
          </div>
          <div class="party-content row">
            <PartyList class="col-5 mx-auto" v-for="(party, idx) in parties" :key="idx" :party="party"/>
          </div>
        </div>
      </div>
    </div>


</div>
</template>

<script>
import ArticleList from '@/components/ArticleList'
import PartyList from '@/components/PartyList.vue'
export default {
  name: 'CommunityView',
  components: {
    ArticleList,
    PartyList,
  },
  data() {
    return {
      party: false,
      genres: [],
      site: 0,
    }
  },
  computed: {
    articles() {
      return  [{title:'A',picture:'dasdf'},{title:'B',picture:'dasdf2'},{title:'C',picture:'dasdf3'}]
      // return this.$store.state.articles
    },
    parties() {
      return  [{title:'A', picture:'dasdf'},{title:'B',picture:'dasdf2'},{title:'C',picture:'dasdf3'}]
      // return this.$store.state.parties.filter(party => (party.id === this.site))
    }
  },
}
</script>

<style scoped>

/* .commu-content {
  margin:200px auto;
} */

.commu-box {
  margin-left: auto;
  margin-right: auto;
  width: 70vw;
  height: 90vh;
  border: solid 2px black;
}

.genre-list {
  display: flex;
}

.genre-choice {
  border: solid 1px black;
  height: 10px;
  width: 10px;
}

.party-content {
  width: 90%;
  margin: 0 auto;
  border: solid 1px brown;
}
</style>