<template>
     <v-row class="flex-column"  align="center" justify="center" >

 

   <v-container fluid>
    <v-row justify="center">
      <v-subheader>Reservation valid</v-subheader>
         <reservation-component :tab_reservation="tab_reservation_valid" :is_valid="true" ></reservation-component>

         <br><br>
         <v-subheader  >Rerservation échoué</v-subheader>

       <reservation-component v-if="!(tab_reservation_refus == [])" :tab_reservation = "tab_reservation_refus" :is_valid="false" ></reservation-component>

    </v-row>
  </v-container>
     
          

    
    </v-row>
</template>


<script>
import reservationComponent from "~/components/resources/reservation_component"

import  {mapActions, mapGetters} from "vuex"

export default {

    middleware: 'admin',
    layout: 'layout-home',

  data() {

        return {

            messages: [],
            tab_classe_selected: []
            }

    },
  components : {
        reservationComponent
    }, 
    computed: {

   ...mapGetters('resources/reserver', ['tab_reservation_valid',
            'tab_reservation_refus','tab_reservation_attente' ,
            'tab_reservation_annulle' ]),     
     ...mapGetters('resources/classes', ['tab_classe' ]),
        ...mapGetters('resources/equipment', [ 'tab_equipment']),
        
        ...mapGetters('users/profil', ['tab_user']),

       
    },

    

    methods: {

       ...mapActions('resources/reserver', ['getAllReservationSchedule','getAllReservationSchedule',]),
     ...mapActions('resources/classes', ['getClasses']),
     ...mapActions('resources/equipment',['getEquipments']),
     ...mapActions('resources/course',['getAllCourse']),
    ...mapActions('users/profil', ['getAllUser']),

    

    },
    mounted() {
    
                    this.getAllReservationSchedule()
}

 


}
</script>