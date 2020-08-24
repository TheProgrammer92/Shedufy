<template>
  <v-app >



  <!-- left navigation -->
     
      <sidebar-schedule></sidebar-schedule>

 
    <header-global></header-global>

    <sidebar-global ></sidebar-global>
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
      <span>
  {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>

import {mapActions,mapGetters} from 'vuex'

import facade from '~/plugins/mixins/facade.js'
import sidebarSchedule from '~/components/global/sidebar-schedule'
import headerGlobal from '~/components/global/header-global'
import sidebarGlobal from '~/components/global/sidebar-global'


import Vue from 'vue'

Vue.mixin(facade)
export default {

  auth: true,

  transition:{
  name: 'layout',
  mode: 'out-in'
},

  components: {headerGlobal,sidebarSchedule ,sidebarGlobal},
  loading: true,

  data () {
    
    return {
    
   
         fixed:true,

      items_left: [
        {
          id: 1,
          name: 'Paramettre generaux',
          
        }],
     
    
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

    

    //verification s'il est admin pour le selectionner

    let params ={}
    if(this.user.is_admin) {
       params.what_action ="admin"
       params.id_user=this.user.id

       
       this.getDepartmentFilierLevelId(params)


    }
    else {
      
          this.getAllDepartment()

    }



       this.getClasses()
      this.getAllUser()
       this.getAllCourse()

     this.getAllCategoryClasse()
       this.getCourse()

      this.getTypeEvent()


    

      
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
      ...mapActions('resources/notifications',['get_notification_user_id']),

 

   async  logout() {

      let data_refresh = {

        refresh_token:  this.$auth.$storage.getLocalStorage("refresh_token")
      }


          let res= await  this.$auth.logout({data: data_refresh})

      this.$router.push({name: 'auth-login'})



    }, 


    
  },

  mounted() {

    this.$nextTick(() => {
      this.$nuxt.$loading.start()

      setTimeout(() => this.$nuxt.$loading.finish(), 500)
    })
  }


}
</script>
