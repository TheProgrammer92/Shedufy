<template>
  <v-app >



  <!-- left navigation -->
     
      <sidebar-schedule></sidebar-schedule>

  <!-- right navigation -->
    <v-navigation-drawer
      v-model="drawer"
      :right="right"
      :mini-variant="miniVariant"
      fixed
      app
      
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
    
          @click.prevent="item.isLogout ? logout: null"
       
        >
         
              
            <template  v-if="get_bool_is_show(item.type_is_show)">
            
                <v-list-item-action >
                  <v-icon >{{ item.icon }}</v-icon>
                </v-list-item-action>
                <v-list-item-content v-if="item.isLogout">
                  <v-list-item-title v-text="item.title" />
                </v-list-item-content>

                <v-list-item-content v-if="!item.isLogout">
                  <v-list-item-title v-text="item.title" />
                </v-list-item-content>
  


            </template>
                  </v-list-item>

      </v-list>

      <v-list>
        <v-list-item

          router
          exact

          @click.prevent="logout"
        >
          <v-list-item-action>
            <v-icon>mdi-chart-bubble</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="'Se deconnecter'" />
          </v-list-item-content>


        </v-list-item>
      </v-list>



    </v-navigation-drawer>

    <header-global></header-global>

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

import facade from '~/plugins/mixins/facade.js'
import sidebarSchedule from '~/components/global/sidebar-schedule'
import headerGlobal from '~/components/global/header-global'


import Vue from 'vue'

Vue.mixin(facade)
export default {


  auth: true,

  components: {headerGlobal,sidebarSchedule},

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
     
       items: [
        {
          icon: 'mdi-apps',
          title: 'Welcome',
          to: '/',
                    is_show:true

        },
     
      
      {
                icon: 'mdi-chart-bubble',
                title: 'Profil',
                to: '/users/profil',
                  type_is_show:"guest"

              },

        
        
     
        {
          icon: 'mdi-chart-bubble',
          title: 'Emploie de temps',
          to: '/resources/schedule',
         type_is_show:"admin"

        } ,
        
        
        {
          icon: 'mdi-chart-bubble',
          title: 'Reservation',
          to: '/resources/reservation/index-teacher',
          type_is_show:"guest"
          
        } ,{
          icon: 'mdi-chart-bubble',
          title: 'Mes Disponibilité',
          to: '/resources/schedule/teacher',
         type_is_show:"teacher"
        }
      ],
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


    get_bool_is_show:function(type) {


          switch (type) {
            case "admin":
              return this.user.is_admin
              break;
            case "teacher":
              return this.user.is_teacher
              break;
            case "guest":
              return true
            default:
              break;
          }

    }
  },


}
</script>
