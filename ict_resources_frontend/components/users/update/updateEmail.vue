<template>
    <v-card
    class="overflow-hidden"
    color="purple lighten-1"
    dark

    width="700"
  >
    <v-toolbar
      flat
      color="purple"
    >
      <v-icon>mdi-account</v-icon>
      <v-toolbar-title class="font-weight-light">User Email</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        color="purple darken-3"
        fab
        small
        @click="isEditing = !isEditing"
      >
        <v-icon v-if="isEditing">mdi-close</v-icon>
        <v-icon v-else>mdi-pencil</v-icon>
      </v-btn>
    </v-toolbar>
    <v-card-text>
      <v-text-field
     
        color="white"
        label="Email"
      ></v-text-field>
      <v-autocomplete
     
        :items="states"
        :filter="customFilter"
        color="white"
        item-text="name"
        label="State"
      ></v-autocomplete>
    </v-card-text>
    <v-divider></v-divider>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
  
        color="success"
        @click="save"
      >
        Save
      </v-btn>
    </v-card-actions>
    <v-snackbar
      v-model="hasSaved"
      :timeout="2000"
      absolute
      bottom
      left
    >
      Your profile has been updated
    </v-snackbar>
  </v-card>
</template>