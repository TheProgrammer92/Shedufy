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
 


    <v-sheet           id="mycalendar"
 style="height:80vh" width="100%">
    



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
          @click:date="viewDay"

        >

        <template #event="{ event, timed, eventSummary }">
            <div
              class="v-event-draggable"
              v-html="eventSummary()"
            ></div>
            <div
              v-if="timed"
              class="v-event-drag-bottom"
              @mousedown.stop="extendBottom(event)"
            ></div>
</template>
        
        
        
        </v-calendar>
        
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
    layout:'default',
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

       dragEvent: null,
      dragStart: null,
      createEvent: null,
      createStart: null,
      extendOriginal: null,
      

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
     ...mapActions('resources/events', ['getEvents' ,'set_tab_event' ]),
    ...mapActions('users/profil', ['getAllUser']),
    


  

   
 

      viewDay ({ date }) {

        console.log("date view day )= ", date)
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
        console.log("show event")
         
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


      },



      
     startDrag ({ event, timed }) {
        if (event && timed) {
          this.dragEvent = event
          this.dragTime = null
          this.extendOriginal = null
        }
      },
    rndElement (arr) {
        return arr[this.rnd(0, arr.length - 1)]
      },

      startTime (tms) {


        if(this.is_teacher  || this.is_admin) {


        const mouse = this.toTime(tms)

        if (this.dragEvent && this.dragTime === null) {
          const start = this.dragEvent.start

          this.dragTime = mouse - start
        } else {
          this.createStart = this.roundTime(mouse)


          this.createEvent = {
            name: `Event #${this.events.length}`,
            color: 'blue',
            start: this.createStart,
            end: this.createStart,
            timed: true,
          }
        this.set_tab_event(this.createEvent)

           this.selectedEvent.start = this.createStart
           this.selectedEvent.end = this.createStart

    



            }

          



        
              

        }
      },


       extendBottom (event) {
        this.createEvent = event
        this.createStart = event.start
        this.extendOriginal = event.end


      },
      mouseMove (tms) {

        const mouse = this.toTime(tms)

        if (this.dragEvent && this.dragTime !== null) {
          const start = this.dragEvent.start
          const end = this.dragEvent.end
          const duration = end - start
          const newStartTime = mouse - this.dragTime
          const newStart = this.roundTime(newStartTime)
          const newEnd = newStart + duration

          this.dragEvent.start = newStart
          this.dragEvent.end = newEnd
        } else if (this.createEvent && this.createStart !== null) {
          const mouseRounded = this.roundTime(mouse, false)
          const min = Math.min(mouseRounded, this.createStart)
          const max = Math.max(mouseRounded, this.createStart)

          this.createEvent.start = min
          this.createEvent.end = max
        }


      },
      endDrag () {
        this.dragTime = null
        this.dragEvent = null
        this.createEvent = null
        this.createStart = null
        this.extendOriginal = null

        this.setDialogUpdate()
       


      },
      cancelDrag () {

        // if (this.createEvent) {
        //   if (this.extendOriginal) {
        //     this.createEvent.end = this.extendOriginal
        //   } else {
        //     const i = this.events.indexOf(this.createEvent)
        //     if (i !== -1) {
        //       this.events.splice(i, 1)
        //     }
        //   }
        // }

        // this.createEvent = null
        // this.createStart = null
        // this.dragTime = null
        // this.dragEvent = null
      },
    roundTime (time, down = true) {
        const roundTo = 15 // minutes
        const roundDownTime = roundTo * 60 * 1000

        return down
          ? time - time % roundDownTime
          : time + (roundDownTime - (time % roundDownTime))
      },
      toTime (tms) {
        return new Date(tms.year, tms.month - 1, tms.day, tms.hour, tms.minute).getTime()
      },
    },

    
    mounted() {


      console.log("departement = ", this.department_selected)

     
        if(this.verify_not_empty_data()){
           let params_load_event = {
            id_type: this.type_schedule_selected,
            id_level: this.level_selected,
            by_type: "level",
            id_user: this.user.id,
            id_classe:this.classe_selected,
            id_department:this.department_selected

        }

            this.getEvents(params_load_event)

        }

        else {

        }

      

    },



  }
</script>


<style lang="scss">
  .v-event-draggable {
padding-left: 6px;
}

.v-event-timed {
user-select: none;
-webkit-user-select: none;
}

.v-event-drag-bottom {
position: absolute;
left: 0;
right: 0;
bottom: 4px;
height: 4px;
cursor: ns-resize;

&::after {
  display: none;
  position: absolute;
  left: 50%;
  height: 4px;
  border-top: 1px solid white;
  border-bottom: 1px solid white;
  width: 16px;
  margin-left: -8px;
  opacity: 0.8;
  content: '';
}

&:hover::after {
  display: block;
}
}
</style>