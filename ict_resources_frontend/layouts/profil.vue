<template>
<v-app dark

 >
    <vue-snotify></vue-snotify>


   
    <v-card
   
      class="overflow-hidden "
    >
      <v-navigation-drawer
        v-model="drawer"
       
        router
        dark
        app
        right


    
        :color="color"
        :expand-on-hover="expandOnHover"
        :mini-variant="miniVariant"
       
        :permanent="permanent"
        
        stateless
        

      >

      
        <v-list
          dense
          nav
          class="py-0"
        >
          <v-list-item two-line :class="miniVariant && 'px-0'">
            <v-list-item-avatar>
              <img src="https://randomuser.me/api/portraits/men/81.jpg">
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title>{{user.username}}</v-list-item-title>
              <v-list-item-subtitle>{{user.last_name}}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-divider></v-divider>

          <v-list-item
            v-for="item in items"
            :key="item.title"
            link
            :to='item.to'
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
    </v-card>

<v-content style="padding:0">

        <nuxt />


    

      
    </v-content>

   

    </v-app>

</template>

<script>



  export default {

    
    data () {
      return {
        drawer: true,
        items: [
          { title: 'Home', icon: 'mdi-view-dashboard',to:'/' },
          { title: 'Information personnelle', icon: 'mdi-image' , to:'personal/'},
          { title: 'About', icon: 'mdi-help-box' },
        ],
        color: 'dark',
        colors: [
          'primary',
          'blue',
          'success',
          'red',
          'teal',
        ],
        right: true,
        permanent: true,
        miniVariant: false,
        expandOnHover: true,
        background: true,
      }
    },
    computed: {
      bg () {
        return this.background ? 'https://images.pexels.com/photos/162568/oil-pump-jack-sunset-clouds-silhouette-162568.jpeg?cs=srgb&dl=a-contre-jour-aube-bien-carburant-162568.jpg&fm=jpg' : undefined
      },
    },

    mounted() {

    

    }
  }
</script>