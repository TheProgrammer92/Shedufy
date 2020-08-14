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

      <v-toolbar-title color="black">MyResource4D </v-toolbar-title>

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
          title: 'Reservation',
          to: '/resources/classe'
        }
      ],
    }),

    methods: {

      async  logout() {

          let data_refresh = {

            refresh_token:  this.$auth.$storage.getLocalStorage("refresh_token")
          }


              let res= await  this.$auth.logout({data: data_refresh})

          this.$router.push({name: 'auth-login'})



        }
  },
  }
</script>