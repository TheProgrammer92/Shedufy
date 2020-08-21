<template>
  <v-app >

  <!-- left navigation -->
     
  <v-navigation-drawer
      v-model="drawer_left"
      :right="false"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
      app
      
    >
   {{user.is_admin ? 'admin': "no-admin"}}
   <br/>
   {{user.is_teacher ? 'teacher': "no-teacher"}}
 
  <br>
<div class="ml-5">

   
      <h4>{{getDepartmentByID}}</h4>
  
  </div>

  <br>
  <div class="ml-5">

   
      <h5>{{getFiliereById}}</h5>
  
  </div>
  
   <br>
  <div class="ml-5">

   
      <h5>{{getLevelById}}</h5>
  
  </div>
  <!-- si c'est pas un prof, nou admin, on affche pas la ""RESERVATION3""" -->
 <div class="ml-5" v-if="!(user.is_teacher || user.is_admin)">
 
  <h6>Trie</h6>


    <div  v-for="type in tab_type_events"   :key="type.id" >


      <template v-if="type.value !== 'RESERVATION'">
        <p-radio  
            @change="load_by_type_schedule" :value="type.type" 
              class="p-default p-curve" name="color" color="primary-o">{{type.value}} </p-radio> 

      <br>
      </template>
    </div>
  
</div>

 <div class="ml-5" v-if="user.is_teacher || user.is_admin">
 
  <h6>Trie</h6>

    <div   v-for="type in tab_type_events"   :key="type.id">
     <p-radio  
     @change="load_by_type_schedule" :value="type.type" 
      class="p-default p-curve" name="color" color="primary-o">{{type.value}} </p-radio> 

      <br>
    </div>
  
</div>

<br>

<div class="ml-5">
  <h6>Trie par</h6>


  
     <p-radio @change="load_by_level_or_salle" value="salle" 
      class="p-default p-curve" name="level_or_salle" color="primary-o">Salle </p-radio> 
      
           <p-radio @change="load_by_level_or_salle" value="level" 
      class="p-default p-curve" name="level_or_salle" color="primary-o">Niveau </p-radio> 

      <br>
    
  
    </div>



    </v-navigation-drawer>


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

import headerGlobal from '~/components/global/header-global'
export default {


  auth: true,

  components: {headerGlobal},
  data () {
    
    return {
      clipped: true,
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

  getDepartmentByID(value) {


      let department =  this.tab_department.find(department => department.id == this.department_selected)

      if(department !==undefined) {

        
        return department.department_name
      }
      else {
        return "aucun departement "
      }
  },
  
  getLevelById() {



      let level = this.tab_level.find(lev => lev.id == this.level_selected)

    if(level == undefined) {
        return "Aucun niveau"
    }

    else {
      return level.level_code
    }
  },

  getFiliereById(value) {
      let filiere =  this.tab_filiere.find(filiere => filiere.id == this.filiere_selected)


    
      if(filiere !==undefined) {

        
        return filiere.filiere_name
      }
      else {
        return "aucune filiere "
      }
  }

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


  load_by_type_schedule(value){
      this.set_type_schedule(value)

      if(this.verify_not_empty_data) {

         let params_load_event = {
            id_type: this.type_schedule_selected,
            id_level: this.level_selected,
            by_type: this.by_type_selected,
            id_user: this.user.id,
            id_classe:this.salle_selected,
            id_department:this.department_selected

        }

        this.getEvents(params_load_event)
      }
     
  }
    ,
    

 load_by_level_or_salle(value) {



      this.set_by_type(value)

      console.log("type is set", this.by_type_selected)
      console.log("classe is set",this.classe_selected,)

      if(this.verify_not_empty_data) {

         let params_load_event = {
            id_type: this.type_schedule_selected,
            id_level: this.level_selected,
            by_type: this.by_type_selected,
            id_user: this.user.id,
            id_classe:this.salle_selected,
            id_department:this.department_selected

        }

        this.getEvents(params_load_event)
      }

    },

     /**verifions si les  level, departement, filiere, sont sélectionné*/
      verify_not_empty_data() {


        
        if (this.level_selected !== undefined && this.filiere_selected !== undefined  && this.department_selected!== undefined
         && this.type_schedule_selected !== undefined){
          return true
        }

        else {


          return false
        }


      },
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
