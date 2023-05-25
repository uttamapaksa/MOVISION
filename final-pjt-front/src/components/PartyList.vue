<template>
  <div class="partyitem" @click="gopartydetail">

    사이트 : {{ party.check_site }}<br>
    작성자 : {{ party.username}}<br>
    제목 : {{party.title}}<br>
    작성일 : {{ party.created_at.slice(0, 10)}}<br>
    인원 : {{ partymembersnum }} / {{ party.members_limit}}<br>
  </div>
</template>

<script>

export default {
  name : 'PartyItem',
  props: {
    party: Object,
  },
  methods: {
    gopartydetail() {
      this.$router.push({name: 'PartyDetialView', params:{party_id: this.party.id}})
    }
  },
  computed: {
    partymembersnum() {
      return this.party.members.length + 1
    }
  }
}
</script>

<style>
.partyitem {
  border: solid 2px black;
}
</style>