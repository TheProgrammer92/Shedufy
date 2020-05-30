<template>
 <v-content>
     <h1 >Salut</h1>

     <h1 v-if="is_teacher"> je suis professeur</h1>


    
    </v-content>
</template>


<script>
export default {

    middleware: 'isauth',

    mounted() 
    {

    }
    
}
</script>