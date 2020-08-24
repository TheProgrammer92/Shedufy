<template>
  <v-app >
    <v-navigation-drawer
      v-model="drawer"
      :right="right"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
      app
      
    >
     <v-treeview
            
         open-all
    :activatable="true"
      :hoverable="true"
      :shaped="true"
      :rounded="true"
      dense

    :items="items"
  ></v-treeview>

    </v-navigation-drawer>


    <v-app-bar
      :clipped-left="clipped"
      fixed
      app 
      
    >
    <nuxt-link :to="'/resources/schedule'">
    
    
        <v-btn
          icon
        >
          <v-icon>mdi-{{ `chevron-${miniVariant ? 'right' : 'left'}` }}</v-icon>
        </v-btn>
     
       </nuxt-link>

    </v-app-bar>
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

import {mapActions} from 'vuex'
export default {

  auth: true,
  data () {
    return {
      clipped: false,
      drawer: true,
      fixed: true,
     
     
      items: [
        {
          id: 1,
          name: 'Paramettre generaux',
          children: [
            { id: 2, name: 'Département' },
            { id: 3, name: 'Filiere' },
            { id: 4, name: 'Niveau' },
            { id: 5, name: 'Sales' },
          ],
        },
        {
          id: 3,
          name: 'Changer Année',
         
        },
        {
          id: 5,
          name: 'Importer/Exporter :',
         
        },
        {
          id: 15,
          name: 'Options :',
          children: [
            { id: 16, name: 'Langue' },
            { id: 17, name: 'Fuseaux horairees' },
            { id: 18, name: 'Horloge mondiale' },
          ],
        },
       
      ],
      miniVariant: false,
      right: false,
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



methods:{

  ...mapActions('resources/utils', ['getDepartmentFilierLevelId','set_salle',
  'set_cours','set_filiere','set_level']),

}



}
</script>
