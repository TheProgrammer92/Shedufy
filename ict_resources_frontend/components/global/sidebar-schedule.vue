<template>
   <v-navigation-drawer
      :value="drawer_left"
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

</template>


<script>

import {mapActions, mapGetters} from 'vuex'
export default {
    data() {

        return {

            
        drawer: false,
        fixed: false,
        selected_actors:"",
         miniVariant: false,
        right: true,
        rightDrawer: false,
        title: 'MyResource4D'
        }
    },

    computed : {

    ...mapGetters('resources/events', ['tab_type_events']),
  ...mapGetters('resources/utils', ['tab_filiere' ,'tab_department' ,
   'tab_level', 'tab_course','cours_selected','level_selected', 
   'salle_selected','filiere_selected',
    'type_schedule_selected','department_selected' , 'by_type_selected' , ]),
        ...mapGetters('utils/utils-global-view', ['clipped','drawer_left']),

        
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
     'set_level','set_cours' , 'set_by_type']),
...mapActions('utils/utils-global-view', ['set_clipped','set_drawer_left']),



    
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
    
    },
}
</script>