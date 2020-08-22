<template>


  <div>

    <dialog-message :dialog_message_teacher="dialog_message_teacher"></dialog-message>
    <v-row
      justify="center"
    >
      

      <v-dialog
        v-model="dialog"
        fullscreen
        hide-overlay
        transition="dialog-bottom-transition"
        scrollable
      >
        <v-card tile>
          <v-toolbar
            flat
            dark
            color="primary"
          >
            <v-btn
              icon
              dark
              @click="dialog = false"
            >
              <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-toolbar-title>Settings</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items>
              <v-btn
                dark
                text
                @click="dialog = false"
              >
                Save
              </v-btn>
            </v-toolbar-items>
            <v-menu
              bottom
              right
              offset-y
            >
              <template v-slot:activator="{ on }">
                <v-btn
                  dark
                  icon
                  v-on="on"
                >
                  <v-icon>mdi-dots-vertical</v-icon>
                </v-btn>
              </template>
              <v-list>
                <v-list-item
                  v-for="(item, i) in items"
                  :key="i"
                  @click="() => {}"
                >
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </v-toolbar>
          <v-card-text>

          <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
    
    <v-select v-if="user.is_admin"
        v-model="eventInput.id_type"

        :items="tab_type_events"
        filled
        chips
        color="blue-grey lighten-2"
        label="Type Event"
        item-text="value"
        item-value="type"   

      
      
      >
        </v-select>

      <v-select v-if="user.is_teacher"
        v-model="eventInput.id_type"

        :items="get_type_for_teacher"
        filled
        chips
        color="blue-grey lighten-2"
        label="Type d'evenement"
        item-text="value"
        item-value="type"   
      > 
        </v-select> 

      <v-select 
      v-if="user.is_teacher"
        v-model="eventInput.type_reservation"

        :items="tab_type_events"
        filled
        chips
        color="blue-grey lighten-2"
        label="Type reservation"
        item-text="value"
        item-value="type"   
      >
    <!-- Template for render selected data -->
   
    <!-- Template for render data when the select is expanded -->
 
  </v-select>


    <v-select
        v-model="eventInput.id_course"
        :items="tab_course"
        filled
        chips
        color="blue-grey lighten-2"
        label="Cours"
        item-text="name"
        item-value="id"

        
      >
    <!-- Template for render selected data -->
   
    <!-- Template for render data when the select is expanded -->
 
  </v-select>


   <v-text-field
      v-model="eventInput.start"
   
      label="start"
      required
      type="datetime-local"
    ></v-text-field>

  <v-text-field
      v-model="eventInput.end"
   
      label="End"
      required
      type="datetime-local"
    ></v-text-field>



     <v-select
           item-text="code_classe"
              item-value="id"
              :items="tab_classe"
              filled
              label="Classe"
              v-model="eventInput.id_classe"
             
            >
    </v-select>
         

    <v-select
      item-text="level_code"
              item-value="id"
              :items="tab_level"
              filled
              label="Niveau"
              v-model="eventInput.id_level"
             
            >
    </v-select>
         
  <v-overflow-btn
  v-if="user.is_admin"
      class="my-2"
      :items="tab_teacher"
      label="Professeur"
      editable
      item-value="id"
      item-text="email"
      v-model="eventInput.id_teacher"
    ></v-overflow-btn>


   <div v-if="verify_if_reservation(eventInput.type_reservation)">
   
     <v-btn
      color="primary"
      class="mr-4"
     @click.prevent="addEvent"
    >
      Valider
    </v-btn> 
    
    <v-btn
      color="error"
      class="mr-4"
     @click.prevent="deleteEvent"
    >
      Faire attendre
    </v-btn>

    <v-btn
      color="warning"
    
  @click.prevent="updateEvent"
    >

     Annuler
    </v-btn>
   </div>


  <div  v-if="(user.is_admin || user.is_teacher)  && !(verify_if_reservation(eventInput.type_reservation))">
   
     <v-btn
      color="primary"
      class="mr-4"
     @click.prevent="addEvent"
    >
      Add
    </v-btn> 
    
    <v-btn
      color="error"
      class="mr-4"
     @click.prevent="deleteEvent"
    >Supprimer
    </v-btn>

    <v-btn
      color="warning"
    
  @click.prevent="updateEvent"
    >

     Update
    </v-btn>
   </div> 
  
  </v-form>
           
         
            <v-divider></v-divider>
            <v-list
              three-line
              subheader
            >
              <v-subheader>General</v-subheader>

              <v-list-item>
                <v-list-item-action>
                  <v-checkbox v-model="notifications"></v-checkbox>
                </v-list-item-action>
                <v-list-item-content>
                  <v-list-item-title>Notifications</v-list-item-title>
                  <v-list-item-subtitle>Notify me about updates to apps or games that I downloaded</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              
              <v-list-item>
                <v-list-item-action>
                  <v-checkbox v-model="sound"></v-checkbox>
                </v-list-item-action>
                <v-list-item-content>
                  <v-list-item-title>Sound</v-list-item-title>
                  <v-list-item-subtitle>Auto-update apps at any time. Data charges may apply</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-action>
                  <v-checkbox v-model="widgets"></v-checkbox>
                </v-list-item-action>
                <v-list-item-content>
                  <v-list-item-title>Auto-add widgets</v-list-item-title>
                  <v-list-item-subtitle>Automatically add home screen widgets</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card-text>

          <div style="flex: 1 1 auto;"></div>
        </v-card>
      </v-dialog>

     
    </v-row>
  </div>
</template>
<script>

    import {mapActions, mapGetters} from 'vuex'

    import dialogMessage from "~/components/alert/dialog_message.vue"
  export default {

    props:{
        
            selectedEvent:Object,
            id_classe:Number
    },

    data () {

        
      return {

        eventInput: {
            
            id_course: "",
            start: "",
            color: "#1976D2",
            end: "",
            id_classe:1,
            id_teacher:"",
            id_type:'',
            id_level:'',
            id_etat:1,
            id_user:'',
            type_reservation:'',
            id_department:''
        },
        
    
       
        dialog2: false,
        dialog3: false,
        notifications: false,
        sound: true,
        widgets:true,
        items: [], 
        valid: true,
        dialog_message_teacher:false,
       
      
      }
    },

    components: {
      dialogMessage
    },

  
  
     computed: {
      ...mapGetters('resources/reserver', ['dialogUpdate' ]),
      ...mapGetters('resources/classes', ['tab_classe']),
      ...mapGetters('resources/equipment', [ 'tab_equipment', ]),
    
    ...mapGetters('resources/course', ['tab_course_category']),
    ...mapGetters('resources/events', ['events','tab_type_events']),
    ...mapGetters('resources/utils', ['events','tab_course', 'tab_level','tab_teacher', 'department_selected']),

    get_type_for_teacher() {

        let f = this.tab_type_events.find(type_event => type_event.type === this.RESERVATION)
        return f
    },



    
    dialog: {
        get () {
            return this.dialogUpdate
            },
            set (value) {
            this.setDialogUpdate()
            }
        }

     },

    methods: {

           ...mapActions('resources/reserver', ['setDialog' ,'setDialogUpdate',]),

           ...mapActions('resources/events', ['getEvents']),
           ...mapActions('resources/equipment', ['getEquipments']),
           ...mapActions('resources/classes', ['getClasses']),


    getClasseById() {

        let id = this.$route.params.id

       let classe= this.tab_classe.filter(classe => classe.id == id)
       
       return classe
        
    },

    //verifions si l'emploie qu'il a cliqué est une reservation
    verify_if_reservation(id_reservation){
    
  
       

        if (id_reservation == this.RESERVATION) {
console.log("éééé true = ")

            return true
        }
        else {
console.log("éééé false = ")

          return false
        }



   



    },

  async addEvent() {

        let eventInput = this.eventInput
        eventInput.id_user = this.user.id
        eventInput.id_department = this.department_selected


        console.log(eventInput)
    

        if (true) {

            

        //verifions si c'est un prof ou un admin, pour voir si c'est une reservation ou pas et change  l'etat

            if(this.user.is_admin) {


                eventInput.id_etat = 1 //etat valide
            }
            else if(this.user.is_teacher) {
                eventInput.id_teacher = this.user.id
                eventInput.id_etat =  this.ETAT_ATTENTE //etat en atttente de validation par secretaire

            }

            let data = (await this.$axios.post('api/resources/', eventInput)).data

            //   state.getEvents()

           //  this.getEvents(this.id_classe)
            
             this.setDialogUpdate()


        } else {
            alert('You must enter event name, start, and end time')
        }
  },
 
     async deleteEvent () {
      
        let data = (await this.$axios.delete('api/resources/' + this.selectedEvent.id + '/')).data
        this.getEvents()

       this.setDialogUpdate()
    },


  



   async  updateEvent() {



      let data = (await this.$axios.put('api/resources/' + this.selectedEvent.id + '/', 
        this.selectedEvent
    ))
       this.getEvents()

   
      this.setDialogUpdate()
     


    }


    },

   
    updated() {

       this.eventInput= this.selectedEvent

       console.log("selected event = ", this.selectedEvent)


 

    },

    


   

  }
</script>



