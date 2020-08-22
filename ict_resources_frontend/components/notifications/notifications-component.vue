<template>
    <v-expansion-panels popout>

        <v-expansion-panel
          v-for="(notification, i) in tab_notification"
          :key="i"
          hide-actions
        >
          <v-expansion-panel-header>
            <v-row
              align="center"
              class="spacer"
              no-gutters
            >
              <v-col
                cols="4"
                sm="2"
                md="1"
              >
                <v-avatar
                  size="36px"
                >
                  <img
                   
                    alt="Avatar"
                    src="https://avatars0.githubusercontent.com/u/9064066?v=4&s=460"
                  >
                  <!-- <v-icon
                    v-else
                    :color="message.color"
                    v-text="message.icon"
                  ></v-icon> -->
                </v-avatar>
              </v-col>

              <v-col
                class="hidden-xs-only"
                sm="5"
                md="3"
              >
                <strong> {{getInfoUserId(notification.id_emetter, 'email', tab_user)}}</strong>
               
                <span
                
                  class="grey--text"
            
                >
                  {{getInfoUserId(notification.id_emetter, 'username', tab_user)}}
                </span>
              </v-col>

              <v-col
                class="text-no-wrap"
                cols="5"
                sm="3"
              >
                <v-chip
                 
                  color="lighten-4"
                  class="ml-0 mr-2 black--text"
                  label
                  small
            
                >
fgh                </v-chip>
                <strong v-html="'Rien'"></strong>
              </v-col>

              <v-col
               
                class="grey--text text-truncate hidden-sm-and-down"
              >
            
salut              </v-col>
            </v-row>
          </v-expansion-panel-header>

          <v-expansion-panel-content>
            <v-divider></v-divider>
            <v-card-text >
           
              <p>message : {{notification.message}}</p>
             <div v-if="is_admin">
              <v-btn 
              class="pl-0" text small color="primary">vue</v-btn>

              <v-btn class="pl-0" text small color="error"
              >Non vue</v-btn>
            </div>

     
            </v-card-text>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
</template>


<script>



import {mapActions, mapGetters} from "vuex"
import dialogReservation from "~/components/alert/dialog_reservation.vue"
import {getInfoUserId} from '~/plugins/facades/facades.js'
export default {
    props: {
        tab_notification: Array,
    },



    data() {

        return {

           
    }
    },

  

  computed: {
    ...mapGetters('users/profil', ['tab_user']),


     

       
    },


     methods: {

      
   
  },

  mounted() {

      console.log(this)
  }

}
</script>