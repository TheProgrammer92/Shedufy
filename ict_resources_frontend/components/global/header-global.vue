<template>
    

<v-app-bar
      :clipped-left="clipped"
      fixed
      app   
    >
     <v-btn
        icon
        @click.stop="drawer_left = !drawer_left"
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
        @click.stop="clipped = !clipped"
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



    <nuxt-link :to="'/resources/schedule/params'">
      <v-btn icon > <v-icon>settings</v-icon> </v-btn>     
    </nuxt-link>
    
      <v-btn icon @click.prevent ="set_show_notification" > <v-icon>notifications</v-icon> </v-btn>     
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
import notifications from '~/components/utils/notifications'
export default {
    
    data() {

        return {

             clipped: true,
        drawer: false,
        fixed: false,
        drawer_left:true,
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
            'is_show_notification'
        ])

    },
 

  methods: {
      ...mapActions('resources/notifications',['set_show_notification'])
  }
}
</script>