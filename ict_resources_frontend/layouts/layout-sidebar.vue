<template>
  <v-app >



  <!-- left navigation -->
     

 
    <header-global></header-global>

<sidebar-global></sidebar-global>
    <!-- main -->
    <v-main>
      <v-container fluid>
        <nuxt />
      </v-container>
    </v-main>
   
    <v-footer
      :fixed="fixed"
      app
    >
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>

import {mapActions,mapGetters} from 'vuex'

import headerGlobal from '~/components/global/header-global'
import sidebarGlobal from '~/components/global/sidebar-global'

import Vue from 'vue'


export default {


  auth: true,

  components: {headerGlobal,sidebarGlobal},

  data () {
    
    return {
      drawer: false,
      fixed: false,
      drawer_left:true,
      selected_actors:"",

       
      items_left: [
        {
          id: 1,
          name: 'Paramettre generaux',
          
        }],
     
      
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'MyResource4D'
    }
  },

   head () {
    return {
      title:"TheProgrammer Default page",
      meta: [
        // hid est utilisé comme identifiant unique. N'utilisez pas `vmid` car ça ne fonctionnera pas
        { hid: 'description', name: 'description', content: 'Ma description personnalisée' }
      ]
    }
  },

  



    async fetch() {

      console.log(this.$route.params.id)

    //verification s'il est admin pour le selectionner

    let params ={}
    


       this.getClasses()
      this.getAllUser()
       this.getAllCourse()

     this.getAllCategoryClasse()
       this.getCourse()

      this.getTypeEvent()


    this.get_notification_id(this.$route.params.id)


      
  },


  fetchOnServer: false,

  computed: {

    ...mapGetters('resources/events', ['tab_type_events']),
  ...mapGetters('resources/utils', ['tab_filiere' ,'tab_department' ,
   'tab_level', 'tab_course','cours_selected','level_selected', 
   'salle_selected','filiere_selected',
    'type_schedule_selected','department_selected' , 'by_type_selected' , ]),


  },
  methods: {
    ...mapActions('resources/reserver', ['getAllReservationSchedule',]),
     ...mapActions('resources/classes', ['getClasses','getAllCategoryClasse']),
     ...mapActions('resources/equipment',['getEquipments']),
     ...mapActions('resources/course',['getAllCourse','getCourse']),
    ...mapActions('users/profil', ['getAllUser']),
    ...mapActions('resources/events', ['getTypeEvent','getEvents']),
     ...mapActions('resources/utils', ['getDepartmentFilierLevelId','getAllDepartment',
     'set_salle','set_filiere','set_type_schedule',
     'set_level','set_cours' , 'set_by_type']),
      ...mapActions('resources/notifications',['get_notification_user_id','get_notification_id']),
      ...mapActions('utils/utils-global-view',['set_drawer_sidebar_global','set_direct_value_drawer_sidebar_global']),

 


    
  },

  mounted() {
  }


}
</script>
