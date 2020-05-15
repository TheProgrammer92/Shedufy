<template>
  <v-layout>

    <h1 >Bienvenue dans  myResources</h1>
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
