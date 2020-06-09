<template>
    
 
      <v-card>
        <v-card-title class="headline">{{message.title}}</v-card-title>

        <v-card-text>
           {{message.message}}
        </v-card-text>

        <v-col >
        <v-textarea
          filled
          auto-grow
          label="Message"
          rows="4"
          row-height="30"
          shaped
          v-model="message_reservation"
        ></v-textarea>
      </v-col>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="green darken-1"
            text
               @click.prevent="Close(true)"

          >
            Ok
          </v-btn>
        <v-btn
            color="green darken-1"
            text
            @click.prevent="Close(false)"
          >
            No
          </v-btn>

          
        </v-card-actions>
      </v-card>
 

</template>


<script>

import {mapGetters, mapActions} from "vuex" 
export default {

    props: {

        is_dialog_reservation:Boolean,
        message:Object,
        id_reservation: [String , Number],
    },

    data() {


        return {

         message_reservation:"",
         id_reserv:55

        }
    },


     methods: {

           ...mapActions('resources/reserver', [
        'getAllReservationSchedule',
    ]),
        Close(response) {
            // using without callback

            if(response) {
               this.updateReservation()

                this.$xmodal.close();
            }

            else {
              this.$xmodal.close();

            }
        },

        async updateReservation() {
            let id=this.id_reservation
            


            let req = {
              id:this.id_reservation, 
              message:this.message_reservation
            }


             let data = (await this.$axios.put('api/reservationSchedule/' + id + '/' , req)).data

          if(data.status = 200) {

          

            this.getAllReservationSchedule()
          

          }
    }
    },
    mounted() {

      this.id_reserv = this.id_reservation

      
    }

  
    
}
</script>