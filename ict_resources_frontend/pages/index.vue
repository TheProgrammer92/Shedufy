<template>
  <v-layout
    column
    justify-center
    align-center
  >

  <h1>Bienvenue  {{user.username}}   😂😂😂😜</h1>






  </v-layout>
</template>

<script>


export default {

  middleware: 'isauth',


  mounted(){

    console.log(this.$auth)
  }
}
</script>
