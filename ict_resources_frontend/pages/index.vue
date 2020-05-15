<template>
  <v-layout
    column
    justify-center
    align-center
  >



  <h1>Bienvenu  <router-link :to="'/inspire'"> Inspire </router-link>   {{user.username}}   😂😂😂😜</h1>



       <nuxt/>


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
