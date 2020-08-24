<template>
 <v-content>
 <br><br>
    <v-row class="flex-column"  align="center" justify="center" >



     
     <h2>Information personnelle</h2>
     <p>Informaition de base utilisés pour votre profil</p>

  <v-card align="center">
   
    <v-tabs vertical>
      <v-tab>
        <v-icon left>mdi-account</v-icon>
        User name
      </v-tab>
      <v-tab>
        <v-icon left>mdi-lock</v-icon>
        Email
      </v-tab>
      <v-tab>
        <v-icon left>mdi-access-point</v-icon>
        Password
      </v-tab>
   

      <v-tab-item>
         <username></username>
      </v-tab-item>


      <v-tab-item>
       <update-email></update-email>
      </v-tab-item>
      <v-tab-item>
        <v-card flat>
          <v-card-text>
            <p>
              Fusce a quam. Phasellus nec sem in justo pellentesque facilisis. Nam eget dui. Proin viverra, ligula sit amet ultrices semper, ligula arcu tristique sapien, a accumsan nisi mauris ac eros. In dui magna, posuere eget, vestibulum et, tempor auctor, justo.
            </p>

            <p class="mb-0">
              Cras sagittis. Phasellus nec sem in justo pellentesque facilisis. Proin sapien ipsum, porta a, auctor quis, euismod ut, mi. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nam at tortor in tellus interdum sagittis.
            </p>
          </v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs>
  </v-card>

  

    
    </v-row>

    
    </v-content>
</template>


<script>

import username from '~/components/users/update/username.vue';
import updateEmail from '~/components/users/update/updateEmail.vue';

export default {

    layout:'profil',

    middleware: 'isauth',

   components: {
       username,
       updateEmail
   }
    
}
</script>