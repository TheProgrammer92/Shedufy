<template>
     <v-row class="flex-column"  align="center" justify="center" >

 

   <v-container fluid>

   
    <v-row justify="center">
       <notification-component :tab_notification="tab_notification" ></notification-component>

         <br><br>


    </v-row>
  </v-container>
     
          

    
    </v-row>
</template>


<script>
import notificationComponent from '~/components/notifications/notifications-component'
import  {mapActions, mapGetters} from "vuex"

export default {

    layout: 'layout-no-sidebar',

  data() {

        return {

           
            }

    },
  components : {
        notificationComponent
    }, 
      computed: {

        ...mapGetters('resources/notifications', [
            'is_show_notification','tab_notification'
        ]),
       

    },

    

 methods: {
      ...mapActions('resources/notifications',['set_show_notification','get_notification_user_id']),
  getAllNotification() {
    this.get_notification_user_id(this.user.id)
   }
   
  },


 


}
</script>