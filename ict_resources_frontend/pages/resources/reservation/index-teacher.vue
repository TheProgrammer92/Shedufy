<template>
     <v-row class="flex-column"  align="center" justify="center" >

 

   <v-container fluid>
    <v-row justify="center">

  <v-subheader>Reservation valid</v-subheader>
         <reservation-component v-if="!(tab_reservation_valid == [])" 
          :tab_reservation="tab_reservation_valid" :is_valid="true" ></reservation-component>
 <br><br>

      <v-subheader  >Rerservation échoué</v-subheader>

       <reservation-component v-if="!(tab_reservation_failed == [])"
        :tab_reservation="tab_reservation_failed" :is_valid="false" ></reservation-component>

    
        
       
    </v-row>
  </v-container>
     
          

    
    </v-row>
</template>


<script>
import reservationComponent from "~/components/resources/reservation_component"

import  {mapActions, mapGetters} from "vuex"

export default {
    middleware: 'teacher',

  data() {

        return {

            messages: [],
            tab_classe_selected: [],
            page:1
            }

    },
  components : {
        reservationComponent
    }, 
    computed: {

        ...mapGetters('resources/reserver', [
            'tab_reservation_valid','tab_reservation_failed', 'tab_classe', 'tab_equipment' , 'tab_user', 'tab_course'
        ]),
        
        ...mapGetters('users/profil', [
             'tab_user'
        ]),

       
    },

    

    methods: {

       ...mapActions('resources/reserver', [
        'getAllReservationScheduleTeacher','getClasses','getEquipments','getAllCourse'
    ]),
    
    ...mapActions('users/profil', [
       'getAllUser'
    ]),

    

    },

    mounted() {
    

     
      this.getAllReservationScheduleTeacher(this.user.id)

      this.getClasses()
      this.getEquipments()
      this.getAllUser()
      this.getAllCourse()
    }
  


}
</script>