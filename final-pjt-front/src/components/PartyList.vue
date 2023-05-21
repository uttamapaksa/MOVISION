<template>
  <div class="partyitem">
      db: 사이트 이미지<br>
      제목 : {{party.title}} <br>
      <!-- 작성자 : ~~~
      기간 : num -->
      내용 : {{party.content}}
      <!-- 인원수 : ( / ) -->
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