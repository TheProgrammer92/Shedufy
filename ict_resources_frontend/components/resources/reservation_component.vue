<template>
    <v-expansion-panels popout>
        <xmodal v-model="isModal" :params="options" />

        <v-expansion-panel
          v-for="(reservation, i) in tab_reservation"
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
                <strong> {{getTeacherById(reservation.id_teacher).username}}</strong>
               
                <span
                
                  class="grey--text"
                  v-if="getTeacherById(reservation.id_teacher).matricule !== null"
                >
                  &nbsp;
                  {{getTeacherById(reservation.id_teacher).matricule}}
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
                  {{getCodeclasse(reservation.id_classe)}}
                </v-chip>
                <strong v-html="'Rien'"></strong>
              </v-col>

              <v-col
               
                class="grey--text text-truncate hidden-sm-and-down"
              >
            
               {{reservation.message}}
              </v-col>
            </v-row>
          </v-expansion-panel-header>

          <v-expansion-panel-content>
            <v-divider></v-divider>
            <v-card-text >
              <p>Course :{{getCourseName(reservation.id_course) + ' ('+ getCourseCodeCourse(reservation.id_course)+ ' )'}}</p>
              <p >Classe :{{getCodeclasse(reservation.id_classe)}}</p>

               <p>Début du cours : {{reservation.start}}</p>
               <p>Fin  du cours: {{reservation.end}}</p>
               <p v-if="getEquipmentById(reservation.id_equipment).equipment !== undefined">Equipement  :{{getEquipmentById(reservation.id_equipment).equipment}}</p>

             <div v-if="is_admin">
              <v-btn v-if="!is_valid" @click.prevent="updateReservationSchedule(reservation.id_reservation)" 
              class="pl-0" text small color="primary">Valider</v-btn>

              <v-btn v-if="is_valid" class="pl-0" text small color="error"
                 @click.prevent="updateReservationSchedule(reservation.id_reservation)">Refuser</v-btn>
            </div>

         <div v-if="is_teacher">
            <p v-if="is_valid" class="font-weight-medium blue--text " >Votre reservation a été validé .</p>
            <p v-if="!is_valid" class="font-weight-medium red--text" >Votre reservation a été rejeté</p>


         </div>
            </v-card-text>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
</template>


<script>



import {mapActions, mapGetters} from "vuex"
import dialogReservation from "~/components/alert/dialog_reservation.vue"
export default {
    props: {
        tab_reservation: Array,
        is_valid: Boolean // verifier si on va afficher le boutton valid ou refuser
    },

    data() {

        return {
            message_update:  {
                title: "Voulez vous vraiment mettre a jour ?",
                message: "Reflechissez bien avant "
            },
            is_dialog_reservation:false,


              isModal: false,
			
			// basic modal options
            options: {
              	isDisable: false // prevent user click
,
                component: require("~/components/alert/dialog_reservation.vue").default,
                backgroundColor: "#000000",
                opacity: "0.7",
                animation: "scaleLeft",
                props: {

                   is_dialog_reservation:true,
                   id_reservation :"",

                message:  {
                   title: "Voulez vous vraiment mettre a jour ?",
                   message: "Reflechissez bien avant "
                   },
           
                }
            }

    }
    },

    components: {

        dialogReservation
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
        'getAllReservationSchedule',
    ]),

     Open() {
          
        },
    
   
  


     getClasseById:function(id) {

            let classe = this.tab_classe.filter(classe => classe.id == id)[0]
            return classe == undefined ? "" : classe

        },
    getCodeclasse:function(id) {


           if (this.tab_classe !== []) {
               let classe = this.tab_classe.filter(classe => classe.id == id)[0]
                    return classe == undefined ? "" : classe.code_classe
           }
           return ""

        },

    getEquipmentById:function(id) {
          if(this.tab_equipment !== []) {
            let equipment = this.tab_equipment.filter(equipment => equipment.id == id)[0]
            return equipment == undefined ? "":equipment 
          }
          return {}
        },
        
    getTeacherById:function(id) {

          return this.tab_user.filter(user => user.id == id)[0]
        },


     getCourseCodeCourse:function(id) {

        if(id) {

             if(this.tab_course !== []) {

              return this.tab_course.filter(course => course.id == id)[0].code_course
            }

            return {}
        }


        },



        getCourseName:function(id) {

            if(this.tab_course !== []) {
            
                let name = this.tab_course.filter(course => course.id == id)[0]
               return name.name == undefined ? "" :name.name
            }

            return {}
        },


    async updateReservationSchedule(id){

     
       
             this.options.props.id_reservation = id
              console.log("avant id reservation = "  ,this.options.props)

             this.isModal= !this.isModal

     

    }},

}
</script>