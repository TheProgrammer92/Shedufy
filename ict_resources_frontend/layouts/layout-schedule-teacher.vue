<template>
 <v-app >     
      <v-card style="width:100%">
        <v-toolbar dark color="dark">

         <nuxt-link  :to="'/resources/schedule/'">
          <v-btn icon dark >
            <v-icon>mdi-close</v-icon>
          </v-btn>
          </nuxt-link>
          <v-toolbar-title>MyCalendar</v-toolbar-title>
          <v-spacer></v-spacer>
       
        </v-toolbar>

        <v-main>
      <v-container fluid>
        <nuxt />
      </v-container>
    </v-main>
      
      </v-card>
  </v-app>
</template>

<script>

import {mapActions, mapGetters} from 'vuex'

  export default {
    data () {
      return {
        dialog: true,
        notifications: false,
        sound: true,
        widgets: false,
      }
    },


     

  async fetch() {


   

      this.getTypeEvent()


    
           let params_load_event = {
            id_type:this.TYPE_TEACHER,

            id_user: this.user.id,
           

        }

            this.getEvents(params_load_event)


    

      
  },

  fetchOnServer:false,
  methods: {

        ...mapActions('resources/events', ['getTypeEvent','getEvents']),
         ...mapActions('resources/course',['getAllCourse','getCourse']),


  }
  }
</script>