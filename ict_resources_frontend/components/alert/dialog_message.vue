<template>
    
   <v-dialog
      v-model="dialog_message_teacher"
      max-width="290"
    >
      <v-card>
        <v-card-title class="headline">Nous vous remercions</v-card-title>

        <v-card-text>
            Nous vous prions, de patienter , pour l'envoie de ce timing  aux administrateur, aussitot, ils feront une validation
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="green darken-1"
            text
            @click="dialog_message_teacher=false"
          >
            Ok
          </v-btn>

          
        </v-card-actions>
      </v-card>
    </v-dialog>


</template>


<script>
export default {

    props: {

        dialog_message_teacher:Boolean
    }
    
}
</script>