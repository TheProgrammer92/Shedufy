<template>
  <div>
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
    <v-text-field
      v-model="eventInput.name"
      :counter="10"
      label="Name"
      required
    ></v-text-field>

    <v-text-field
      v-model="eventInput.details"
   
      label="Details"
      required
    >
    
    </v-text-field>

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


  <v-text-field
      v-model="eventInput.color"
   
      label="Color"
      required
      type="color"
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
      item-text="equipment"
              item-value="id"
              :items="tab_equipment"
              filled
              label="Equipement"
              v-model="eventInput.id_equipment"
             
            >
    </v-select>
         

   
   

    <v-btn
      color="primary"
      class="mr-4"
     @click.prevent="addEvent(eventInput)"
    >
      Add
    </v-btn> 
    
    <v-btn
      color="error"
      class="mr-4"
     @click.prevent="deleteEvent"
    >
      Delete
    </v-btn>

    <v-btn
      color="warning"
    
  @click.prevent="updateEvent"
    >

     Update
    </v-btn>
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
  export default {

    props:{
        
            selectedEvent:Object,
            id_classe:Number
    },

    data () {

        
      return {

        eventInput: {
            name: "",
            details: "",
            start_date: "",
            color: "#1976D2",
            end_date: "",
            'id_classe':""
        },
        
    
       
        dialog2: false,
        dialog3: false,
        notifications: false,
        sound: true,
        widgets:true,
        items: [], 
        valid: true,

       
      
      }
    },

  
  
     computed: {
      ...mapGetters('resources/reserver', [
     'events','dialogUpdate','tab_classe', 'tab_equipment'
    ]),
    
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

           ...mapActions('resources/reserver', [
      
                'setDialog' , 'getEvents','setDialogUpdate','addEvent','getClasses','getEquipments'
                ]),



  async addEvent(eventInput) {

    
  
        if (eventInput.name && eventInput.start && eventInput.end && eventInput.details) {
            let data = (await this.$axios.post('api/resources/', eventInput)).data

            //   state.getEvents()

             this.getEvents(this.id_classe)
            
             this.setDialogUpdate()

        } else {
            alert('You must enter event name, start, and end time')
        }
  },
 
     async deleteEvent () {
      
        let data = (await this.$axios.delete('api/resources/' + this.selectedEvent.id + '/')).data
        this.getEvents(this.id_classe)

       this.setDialogUpdate()
    },


  



   async  updateEvent() {



      let data = (await this.$axios.put('api/resources/' + this.selectedEvent.id + '/', 
        this.selectedEvent
    ))
       this.getEvents(this.id_classe)

   
      this.setDialogUpdate()
     


    }


    },

   
    updated() {

       this.eventInput= this.selectedEvent


 

    },


   

  }
</script>



