<template>
  <v-row class="fill-height">

 
    <v-col>
      <v-sheet height="64">
        <v-toolbar flat color="white">

           <v-btn  v-if="is_teacher || is_admin" color="primary" dark @click.stop="setDialogUpdate">
            New Event
          </v-btn>
          <v-btn outlined class="mr-4" color="grey darken-2" @click="setToday">
            Today
          </v-btn>
          <v-btn fab text small color="grey darken-2" @click="prev">
            <v-icon small>mdi-chevron-left</v-icon>
          </v-btn>
          <v-btn fab text small color="grey darken-2" @click="next">
            <v-icon small>mdi-chevron-right</v-icon>
          </v-btn>
          <v-toolbar-title>{{ title }}</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-menu bottom right>
            <template v-slot:activator="{ on }">
              <v-btn
                outlined
                color="grey darken-2"
                v-on="on"
              >
                <span>{{ typeToLabel[type] }}</span>
                <v-icon right>mdi-menu-down</v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item @click="type = 'day'">
                <v-list-item-title>Day</v-list-item-title>
              </v-list-item>
              <v-list-item @click="type = 'week'">
                <v-list-item-title>Week</v-list-item-title>
              </v-list-item>
              <v-list-item @click="type = 'month'">
                <v-list-item-title>Month</v-list-item-title>
              </v-list-item>
              <v-list-item @click="type = '4day'">
                <v-list-item-title>4 days</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-toolbar>
      </v-sheet>


          <create_date_component > </create_date_component>

            <update_date_component :selectedEvent="selectedEvent" :id_classe="id_classe"> </update_date_component>
 


    <v-sheet height="100%" width="100%">
    



        <v-calendar
          ref="calendar"
          v-model="focus"
          color="primary"
          :events="events"
          :event-color="getEventColor"
          :event-margin-bottom="3"
          :event-more-text = "'more text event'"
          :now="today"
          :type="type"
          @click:event="showEvent"
          @click:more="viewDay"
          @click:date="setDialog"
          @change="updateRange"
        ></v-calendar>
        
      </v-sheet>
    </v-col>
  </v-row>
</template>



<script>

import create_date_component from '~/components/resources/create_date_component.vue'
import {mapActions, mapGetters} from "vuex"
import update_date_component from '~/components/resources/update_date_component.vue'

  export default {


    middleware: 'isauth',
    data: () => ({
      today: new Date().toISOString().substr(0, 10),
      focus: new Date().toISOString().substr(0, 10),
      type: 'week',
      typeToLabel: {
        week: 'Week',
        month: 'Month',
        
        day: 'Day',
        '4day': '4 Days',
      },
      start: null,
      end: null,
      selectedEvent: {

          id_course: "",
            start: "",
            color: "#1976D2",
            end: "",
            id_classe:1,
            id_teacher:"",
            id_type_event:''
      },
      selectedElement: null,
 
      
  
      currentlyEditing: null,

      id_classe:null,
      id_cat:"",
      is_modal:true,
      

    }),


    components: {

        create_date_component,
        update_date_component
    },
    computed: {
      ...mapGetters('resources/reserver', [
   'dialogUpdate', 'events'
    ]),
  ...mapGetters('resources/events', [
  'events'
    ]),
     ...mapGetters('resources/utils', [
  'cours_selected','level_selected', 'salle_selected','filiere_selected', 'type_schedule_selected','department_selected'
    ]),

    selectedOpen: {
        get () {
            return this.dialogUpdate
            },
            set (value) {
            this.setDialogUpdate()
            }
        }
,

    
      title () {
        const { start, end } = this
        if (!start || !end) {
          return ''
        }

        const startMonth = this.monthFormatter(start)
        const endMonth = this.monthFormatter(end)
        const suffixMonth = startMonth === endMonth ? '' : endMonth

        const startYear = start.year
        const endYear = end.year
        const suffixYear = startYear === endYear ? '' : endYear

        const startDay = start.day + this.nth(start.day)
        const endDay = end.day + this.nth(end.day)

        switch (this.type) {
          case 'month':
            return `${startMonth} ${startYear}`
          case 'week':
          case '4day':
            return `${startMonth} ${startDay} ${startYear} - ${suffixMonth} ${endDay} ${suffixYear}`
          case 'day':
            return `${startMonth} ${startDay} ${startYear}`
        }
        return ''
      },
      monthFormatter () {
        return this.$refs.calendar.getFormatter({
          timeZone: 'UTC', month: 'long',
        })
      },
    },

   
    methods: {


       ...mapActions('resources/reserver', ['getAllReservationSchedule','setDialog','setDialogUpdate']),
     ...mapActions('resources/classes', ['getClasses','getClasseCategoryId']),
     ...mapActions('resources/equipment',['getEquipments']),
     ...mapActions('resources/course',['getAllCourse','getCourse']),
     ...mapActions('resources/events', ['getEvents']),
    ...mapActions('users/profil', ['getAllUser']),
    



  

   
 

      viewDay ({ date }) {
        this.focus = date
        this.type = 'day'
      },
      getEventColor (event) {
        return event.color
      },
      setToday () {
        this.focus = this.today
      },
      prev () {
        this.$refs.calendar.prev()
      },
      next () {
        this.$refs.calendar.next()
      },

      showEvent ({ nativeEvent, event }) {

          // s'il es professeur seulement

         
          if(this.is_teacher  || this.is_admin) {

                const open = () => {

              this.selectedEvent = event
            
              this.selectedElement = nativeEvent.target
              setTimeout(() => this.setDialogUpdate(), 10)
              }

              if (this.dialogUpdate) {
                this.setDialogUpdate() 
                setTimeout(open, 10)
              } else {
                open()
              }

              nativeEvent.stopPropagation()

            }
            else {

              alert("Vous devez etre un professeur")
            }
          
      },

      updateRange ({ start, end }) {



        this.start = start
        this.end = end
        
      },
      nth (d) {
        return d > 3 && d < 21
          ? 'th'
          : ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th'][d % 10]
      },
      rnd (a, b) {
        return Math.floor((b - a + 1) * Math.random()) + a
      },
      formatDate (a, withTime) {
        return withTime
          ? `${a.getFullYear()}-${a.getMonth() + 1}-${a.getDate()} ${a.getHours()}:${a.getMinutes()}`
          : `${a.getFullYear()}-${a.getMonth() + 1}-${a.getDate()}`
      },




      /**verifions si les  level, departement, filiere, sont sélectionné*/
      verify_not_empty_data() {

        if (this.level_selected !==undefined && this.filiere_selected !==undefined  && this.department_selected!==undefined
         && this.type_schedule_selected !==undefined){
          return true
        }

        else {


          return false
        }


      }
    },

    
    mounted() {

    this.id_classe= this.$route.params.id


      

     
        if(this.verify_not_empty_data()){
           let params_load_event = {
            id_type: this.type_schedule_selected,
            id_level: this.level_selected,
            by_type: "level",
            id_user: this.user.id,
            id_classe:this.classe_selected,
            department_selected:this.department_selected

        }

            this.getEvents(params_load_event)

        }

        else {

        }

      

    },

  }
</script>
