<template>
  <v-app dark id="inspire" >


    <v-navigation-drawer
      v-model="drawer"
      app
      left
       :mini-variant="false"

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
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content v-if="item.isLogout">
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>

          <v-list-item-content v-if="!item.isLogout">
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
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




      <template v-slot:append>
        <div class="pa-2" @click.prevent="logout">
          <v-btn block>Se Deconnecter</v-btn>
        </div>
      </template>

    </v-navigation-drawer>

    <v-app-bar
     

      fixed
      app 
    >
      <v-spacer></v-spacer>

      <v-toolbar-title color="black">IXcvxcvoxcvxc</v-toolbar-title>

      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    </v-app-bar>
   <v-main>
      <v-container fluid>
        <nuxt />
      </v-container>
    </v-main>

    <v-footer
      color="white"
      app
    >
      <v-spacer></v-spacer>

      <span class="black--text">&copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
import {mapActions,mapGetters} from 'vuex'

  export default {
    name: 'LayoutsDemosBaselineFlipped',
    props: {
      source: String,
    },
    data: () => ({
      drawer: null,

       items: [
        {
          icon: 'mdi-apps',
          title: 'Welcome',
          to: '/'
        },
     
      
      {
                icon: 'mdi-chart-bubble',
                title: 'Profil',
                to: '/users/profil'
              },
     
      {
         icon: 'mdi-chart-bubble',
            title: 'Emploie de temps',
            to: '/resources/schedule/'
              },

        
        
        {
          icon: 'mdi-chart-bubble',
          title: 'Reservation',
          to: '/reservation/index-teacher'
        } ,
        
        {
          icon: 'mdi-chart-bubble',
          title: 'Reservation',
          to: '/reservation/'
        }
      ],
    }),

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
   'salle_selected','filiere_selected', 'type_schedule_selected','department_selected']),
  }
,
    methods: {
 ...mapActions('resources/reserver', ['getAllReservationSchedule',]),
     ...mapActions('resources/classes', ['getClasses','getAllCategoryClasse']),
     ...mapActions('resources/equipment',['getEquipments']),
     ...mapActions('resources/course',['getAllCourse','getCourse']),
    ...mapActions('users/profil', ['getAllUser']),
    ...mapActions('resources/events', ['getTypeEvent','getEvents']),
     ...mapActions('resources/utils', ['getDepartmentFilierLevelId','getAllDepartment',
     'set_salle','set_filiere','set_type_schedule',
     'set_level','set_cours']),

      async  logout() {

          let data_refresh = {

            refresh_token:  this.$auth.$storage.getLocalStorage("refresh_token")
          }


              let res= await  this.$auth.logout({data: data_refresh})

          this.$router.push({name: 'auth-login'})



        },
  },

 
  }
</script>