<template>
    

<v-app-bar
      :clipped-left="clipped"
      fixed
      app   
    >
     <v-btn
        icon
        @click.stop="set_drawer_left"
      >
        <v-icon>mdi-menu</v-icon>
      </v-btn>

      <v-btn
        icon
        @click.stop="miniVariant = !miniVariant"
      >
        <v-icon>mdi-{{ `chevron-${miniVariant ? 'right' : 'left'}` }}</v-icon>
      </v-btn>

      <v-btn
        icon
        @click.stop="set_clipped"
      >
        <v-icon>mdi-application</v-icon>
      </v-btn>
      <v-btn
        icon
        @click.stop="fixed = !fixed"
      >
        <v-icon>mdi-minus</v-icon>
      </v-btn>
      <v-toolbar-title v-text="title" />
      <v-spacer />

      <v-avatar color="indigo" size="25">
        <v-icon dark>schedule</v-icon>
      </v-avatar>




    <nuxt-link :to="'/resources/schedule/params'">
      <v-btn icon > <v-icon>settings</v-icon> </v-btn>     
    </nuxt-link>
    
      <v-btn icon @click.prevent ="set_show_notification" > <v-icon>notifications</v-icon> </v-btn>  

      <notifications></notifications>

      
        <v-btn
        icon
        @click.stop="drawer = !drawer"
      >
        <v-icon>mdi-menu</v-icon>
      </v-btn>

    <!-- <notifications></notifications> -->

    </v-app-bar>

</template>


<script>

import {mapActions, mapGetters} from 'vuex'
import notifications from '~/components/utils/notifications-component-header'
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
    components: {notifications},

    computed: {

        ...mapGetters('resources/notifications', [
            'is_show_notification' , 'tab_notification'
        ]),
        ...mapGetters('utils/utils-global-view', ['clipped','drawer_left']),


    },
 

  methods: {
      ...mapActions('resources/notifications',['set_show_notification' , 'get_notification_user_id']),
               ...mapActions('utils/utils-global-view', ['set_clipped','set_drawer_left']),

  },

  mounted() {

  }
}
</script>