<template>
  <v-layout
    column
    justify-center
    align-center
  >

  <h1>Bienvenue  {{user.username}}   😂😂😂😜</h1>

  <update_date_component> </update_date_component>




  </v-layout>
</template>

<script>



import update_date_component from '~/components/resources/update_date_component.vue'

export default {

  middleware: 'isauth',

  components: {
update_date_component
  },


  mounted(){

    console.log(this.$auth)
  }
}
</script>
