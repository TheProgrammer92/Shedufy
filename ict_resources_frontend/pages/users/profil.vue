<template>

<v-container fluid style="padding:0">


 <v-app-bar
      
      color="#6A76AB"
      dark
 width="100%"
      prominent
      src="https://picsum.photos/1920/1080?random"
      fade-img-on-scroll
      scroll-target="#scrolling-techniques-3"
    >
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top right, rgba(100,115,201,.7), rgba(25,32,72,.7)"
        ></v-img>
      </template>

      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Title</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>

      <template v-slot:extension>
       <v-tabs
      v-model="tab"
      background-color="transparent"
      color="basil"
      align-with-title
    >
      <v-tab
        v-for="item in items"
        :key="item"
      >
        {{ item.name }}
      </v-tab>
    </v-tabs>


        

        
      </template>

      


      
 
      
    </v-app-bar>
    <br>
<v-content>

 <v-tabs-items v-if="tab !==null" v-model="tab">
      <v-tab-item
        v-for="(item,index) in items"
        :key="index"
      >

       <component :is="item.tag"></component>



      </v-tab-item>
  </v-tabs-items>

  


</v-content>
</v-container>
</template>


<script>

import indexProfilComponent from "~/components/users/index-profil-component"
import personnalProfilComponent from "~/components/users/update/personal-profil-component"
import securiteProfilComponent from "~/components/users/update/securite-profil-component"


export default {

    layout:'profil',

    middleware: 'isauth',
    components: {

      indexProfilComponent,
      personnalProfilComponent,
      securiteProfilComponent
    },

    data() {

        return {

           tab: null,
        items: [
          {

            tag:'indexProfilComponent',
            name:'Accueil'
          },
          {

            tag:'personnalProfilComponent',
            name:'Information Personnelle'
          },
           {
             tag :'securiteProfilComponent',
             name: 'Sécurité'
           },{
             tag :'securiteProfilComponent',
             name :'Autre'
           }
        ],
        text: 'Lorem ipsum.',
            messages: [
        {
          avatar: 'https://avatars0.githubusercontent.com/u/9064066?v=4&s=460',
          name: 'John Leider',
          title: 'Welcome to Vuetify.js!',
          excerpt: 'Thank you for joining our community...',
        },
        {
          color: 'red',
          icon: 'people',
          name: 'Social',
          new: 1,
          total: 3,
          title: 'Twitter',
        },
        {
          color: 'teal',
          icon: 'local_offer',
          name: 'Promos',
          new: 2,
          total: 4,
          title: 'Shop your way',
          exceprt: 'New deals available, Join Today',
        },
      ],
      lorem: 'Lorem ipsum dolor sit amet, at aliquam vivendum vel, everti delicatissimi cu eos. Dico iuvaret debitis mel an, et cum zril menandri. Eum in consul legimus accusam. Ea dico abhorreant duo, quo illum minimum incorrupte no, nostro voluptaria sea eu. Suas eligendi ius at, at nemore equidem est. Sed in error hendrerit, in consul constituam cum.',
   
  }

    }
    
}
</script>