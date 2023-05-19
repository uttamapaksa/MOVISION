<template>
  <div class="partyitem">
      db: 영화사이트 이미지
      제목 : ㅁㅁㅁㅁ
      작성자 : ~~~
      기간 : num
      인원수 : ( / )
  </div>
</template>

<script>

export default {
  name : 'PartyItem',
  props: {
    party: Object,
  }
}
</script>

<style>
.partyitem {
  border: solid 1px blue;
}
</style>