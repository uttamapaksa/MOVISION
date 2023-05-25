<template>
<div class="ArticleView">
      
      <div class="community-buttons">
        <button class="commu-btn" :class="{selected: !isParty}" @click="isParty=false">리뷰 게시판</button>
        <button class="commu-btn" :class="{selected: isParty}" @click="isParty=true" >모집 게시판</button>
      </div><br>
  
  
      <div v-if="!isParty">
        <div class="commu-box">
          <router-link :to="{ name: 'ReviewCreateView' }"><button class="commu-create-btn">리뷰 작성하기</button></router-link>
          <ArticleList v-for="(article, idx) in articles" :key="idx" :article="article"/>
        </div>
        <br>
        <div class="search-bar">
          <input type="text">
          <input type="submit" value="검색">
        </div>
        <br>
      </div>
      <div v-if="isParty">
        <div class="commu-box">
          <router-link class="commu-create-btn" :to="{ name: 'PartyCreateView' }"><button class="commu-create-btn">그룹 만들기</button></router-link><br><br>
          <div class="party-site-list">
            <button class="party-site" :class="{selected: pick1}" @click="site='전체'; picksite(1)">전체</button>
            <button class="party-site" :class="{selected: pick2}" @click="site='디즈니플러스'; picksite(2)">디즈니플러스</button>
            <button class="party-site" :class="{selected: pick3}" @click="site='넷플릭스'; picksite(3)">넷플릭스</button>
            <button class="party-site" :class="{selected: pick4}" @click="site='왓챠'; picksite(4)">왓챠</button>
            <button class="party-site" :class="{selected: pick5}" @click="site='유튜브'; picksite(5)">유튜브</button>
            <br><br>
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
      site: '전체',
      isParty: false,
      pick1: true,
      pick2: false,
      pick3: false,
      pick4: false,
      pick5: false,
    }
  },
  mounted() {
    this.$store.dispatch('getReviewArticles');
    this.$store.dispatch('getPartyArticles');
  },
  computed: {
    articles() {
      return this.$store.state.review_articles
    },
    parties() {
      if (this.site == '전체') {
        return this.$store.state.party_articles
      } else {
        return this.$store.state.party_articles.filter(party => party.check_site == this.site)
      }
    },
  },
  methods: {
    picksite(num) {
      if (num == 1) {this.pick1=true; this.pick2=false; this.pick3=false; this.pick4=false; this.pick5=false
      } else if (num == 2) {this.pick1=false; this.pick2=true, this.pick3=false, this.pick4=false, this.pick5=false
      } else if (num == 3) {this.pick1=false, this.pick2=false, this.pick3=true, this.pick4=false, this.pick5=false
      } else if (num == 4) {this.pick1=false, this.pick2=false, this.pick3=false, this.pick4=true, this.pick5=false
      } else {this.pick1=false, this.pick2=false, this.pick3=false, this.pick4=false, this.pick5=true}
    }
  }
}
</script>
  
<style scoped>

.community-buttons {
  display: flex;
  justify-content: space-evenly;
}

.commu-btn {
  border: solid 1px gray;
  background-color: white;
  border-radius: 20px;
  font-size: 3vw;
}

.commu-btn:hover {
  background-color: rgb(255, 124, 59);
}

.selected {
  background-color: orange;
}

/* .commu-content {
  margin:200px auto;
} */

.commu-create-btn {
  border: solid 1px gray;
  background-color: white;
  border-radius: 2px;
  font-size: 1.5vw;
  width: 100%;
}


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


.part-site-list {
  display: flex;

}
.party-site {
  border: solid 1px green;
  width: 20%;
  margin: 0 auto;
  height: 6vh;
  font-size: 2.3vh;
  border-radius: 5px;
  background-color: white
}

.party-content {
  width: 90%;
  margin: 0 auto;
  /* border: solid 1px brown; */
}

.selected {
  background-color: orange;
}
</style>