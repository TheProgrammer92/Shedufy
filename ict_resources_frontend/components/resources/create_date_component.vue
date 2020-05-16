<template >
     

 <v-dialog v-model="dialog" max-width="500">
        <v-card>
          <v-container>
            <v-form @submit.prevent="addNewEvent">
              <v-text-field v-model="eventInput.name" type="text" label="event name (required)"></v-text-field>
              <v-text-field v-model="eventInput.details" type="text" label="detail"></v-text-field>
              <v-text-field v-model="eventInput.start" type="datetime-local" label="start (required)"></v-text-field>
              <v-text-field v-model="eventInput.end" type="datetime-local" label="end (required)"></v-text-field>
              <v-text-field v-model="eventInput.color" type="color" label="color (click to open color menu)"></v-text-field>
              <v-btn type="submit" color="primary" class="mr-4" @click.stop="setDialog">
                create event
              </v-btn>
              <v-btn color="red" class="mr-4" @click.stop="setDialog">
               close
              </v-btn>
            </v-form>
          </v-container>
        </v-card>
      </v-dialog>
    
</template>

<script>


import {mapGetters, mapActions} from 'vuex'


export default {
  name: 'create_date_component',

  
  data() {

    return {

        eventInput: {

          name: '',
          color: '#1976D2',
          details :"",
          start: "",
          end: ""
        }
    }
  },



   computed: {

    ...mapGetters('resources/reserver', [
     'dialog'
    ]),
    
    
  },
  methods: {
    ...mapActions('resources/reserver', [
      
      'setDialogDate', 'addEvent','setDialog'


    ]),

    addNewEvent:function() {

      this.addEvent(this.eventInput)
    }
  
}

}
</script>

