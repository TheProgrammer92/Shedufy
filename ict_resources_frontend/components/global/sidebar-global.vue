


<template>
     <!-- right navigation -->
     
    <v-navigation-drawer
   
      :right="right_sidebar_global"
      :mini-variant="false"
     :v-model="get_drawer_sidebar"
     :value="drawer_sidebar_global"

     :clipped="clipped_sidebar_global"

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
         
              
            
                <v-list-item-action >
                  <v-icon >{{ item.icon }}</v-icon>
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



    </v-navigation-drawer>

</template>



<script>

import {mapActions, mapGetters} from 'vuex'
export default {
    data() {

        return {

            
        fixed: false,
        selected_actors:"",
         miniVariant: false,
        rightDrawer: false,
        title: 'MyResource4D',


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
          title: 'Notifications',
          to: '/notifications',
          type_is_show:"guest"
          
        },
        
        {
          icon: 'mdi-chart-bubble',
          title: 'Reservation',
          to: '/resources/reservation/index-teacher',
          type_is_show:"guest"
          
        } 
      ],
        }
    },

    computed : {


        ...mapGetters('utils/utils-global-view',
         ['clipped_sidebar_global','drawer_left' , 'drawer_sidebar_global' ,'right_sidebar_global']),

    

           get_drawer_sidebar: {

             get(){
                return this.drawer_sidebar_global

             },

             set(newvalue) {
               this.set_drawer_sidebar_global()

             }
           }
         


    },

    methods: {
          ...mapActions('utils/utils-global-view', [
            'set_drawer_sidebar_global'
          ]),

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

 

    }
    
   
}
</script>