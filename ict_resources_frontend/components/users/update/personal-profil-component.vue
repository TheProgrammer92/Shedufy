<template>
     <v-form>

      <div  class="d-flex justify-end">
        <v-btn text @click.prevent="enableForm"    small color="primary">{{btn_update_name}}</v-btn>
      </div>
  <v-divider></v-divider>

    <v-container>

       <input type="file"     
         ref="file" :name="uploadFieldName"  
              @change="onFileChange($event)"     >

  
      <v-row>

        <v-col cols="12" sm="6">
          <v-text-field
            v-model="user.first_name"
            label="Prenom"
            outlined
            shaped
            :disabled="disabled"
          ></v-text-field>
        </v-col>

        <v-col cols="12" sm="6">
          <v-text-field
            v-model="user.last_name"
            label="Nom"
            filled
            shaped

            :disabled="disabled"
          ></v-text-field>
        </v-col>

      </v-row> 


       <v-row>

        <v-col cols="12" sm="6">
          <v-text-field
            v-model="user.username"
            label="Username"
            outlined
            shaped
            :disabled="disabled"
          ></v-text-field>
        </v-col> 
        
        <v-col cols="12" sm="6">
          <v-text-field
            v-model="user.matricule"
            label="Matricule"
            outlined
            shaped
            :disabled="disabled"
          ></v-text-field>
        </v-col>

      </v-row>
      
      <v-row>

        <v-col cols="12" sm="6">
          <v-text-field
            v-model="user.email"
            label="Email"
            outlined
            shaped
            :disabled="disabled"
          ></v-text-field>
        </v-col>

       <v-col class="d-flex" cols="12" sm="6">
        <v-select
         
          filled
          label="Sexe"
          :disabled="disabled" 

          item-text="value"
              item-value="number"
              :items="tab_sexe"

              v-model= "user.sexe"
        ></v-select>
      </v-col>

      </v-row>
      
    
    </v-container>
  </v-form>
</template>


<script>

import {mapActions, mapGetters} from 'vuex'

export default {
  
  data() {

    return {

           files: [],

 uploadFieldName: 'file',
          tab_sexe:[
            {
            
            'number':1,
            'value' : 'Masculin'
          },
           {
             'number' : 0,
             'value' : 'Feminin'
           }
          
          ],
          btn_update_name:'Modifier',
          disabled:true,
    }
  },
 

  methods: {

    ...mapActions('users/profil', [
'updateUsersPersonalInfo'
      
    ]),

  onFileChange( file) { 
    console.log("file ", file)
     
              
        },

   async  updateAvatar () {

      let app =this

      console.log("file d'avant =" , this.files)

      let data = (await this.$axios.put('api/users/update_avatar', {
        avatar:app.files[0]
      })).data

      console.log("avatar updated = ", data)


    },

    enableForm:function() {

      
      
      if(this.disabled) {

        this.btn_update_name = "Terminer"
      }
      else {
        this.btn_update_name = "Modifier"

        // if(this.files !== []) {
        //   this.user.avatar = null
        //   this.user.avatar = this.files[0]
        // }

        this.updateUsersPersonalInfo(this)
      }

      this.disabled=!this.disabled
    }
  }
}
</script>