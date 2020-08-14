<template>
    <div>


            <h4>Department </h4>

             
         <v-row>
         
            <v-col class="d-flex" cols="12" sm="6">
                <v-select
                :items="tab_department"
                :item-value="'id'"
                :item-text="'department_name'"

                label="Department"
                filled
                chips
                :value="department_selected"
                @change="set_department"
                ></v-select>
            </v-col>
        </v-row>



       <h4>Filiere</h4>

          
         <v-row>
         
            <v-col class="d-flex" cols="12" sm="6">
                <v-select
                :items="tab_filiere"
                :item-value="'id'"
                :item-text="'filiere_code'"

                label="Filiere"
                filled
                chips
                :value="filiere_selected"
                @change="set_filiere"
                ></v-select>
            </v-col>
        </v-row>


          <h4>Niveau</h4>
         <v-row>
         
            <v-col class="d-flex" cols="12" sm="6">
                <v-select
                :items="tab_level"
                :item-value="'id'"
                :item-text="'level_code'"
                label="Niveau"
                filled
                chips
                 :value="level_selected"

                @change="set_level"
                ></v-select>
            </v-col>
        </v-row>



          <h4>Cours</h4>
         <v-row>
         
            <v-col class="d-flex" cols="12" sm="6">
                <v-select
                :items="tab_course"
                :item-value="'id'"
                :item-text="'name'"
                label="Cours"
                filled
                chips
                :value="cours_selected"
                 @change="set_cours"

                ></v-select>
            </v-col>
        </v-row>




              <h4>Salles</h4>
         <v-row>
         
            <v-col class="d-flex" cols="12" sm="6">
             

                  <v-select
                  item-text="code_classe"
              item-value="id"
              :items="tab_classe"
              filled
              label="Classe"
              :value="salle_selected"

              @change="set_salle"
             
            >
    </v-select>
            </v-col>


        </v-row>

        

   


   

   
            
    </div>
</template>



<script>
import {mapActions, mapGetters} from 'vuex'

  export default {
      layout:'layout-schedule-params',
    data: () => ({
    
      content_filiere: ['Foo', 'Bar', 'Fizz', 'Buzz'],

      items: [
        {
          id: 1,
          name: 'Applications :',
          children: [
            { id: 2, name: 'Calendar : app' },
            { id: 3, name: 'Chrome : app' },
            { id: 4, name: 'Webstorm : app' },
          ],
        },
        {
          id: 5,
          name: 'Documents :',
          children: [
            {
              id: 6,
              name: 'vuetify :',
              children: [
                {
                  id: 7,
                  name: 'src :',
                  children: [
                    { id: 8, name: 'index : ts' },
                    { id: 9, name: 'bootstrap : ts' },
                  ],
                },
              ],
            },
            {
              id: 10,
              name: 'material2 :',
              children: [
                {
                  id: 11,
                  name: 'src :',
                  children: [
                    { id: 12, name: 'v-btn : ts' },
                    { id: 13, name: 'v-card : ts' },
                    { id: 14, name: 'v-window : ts' },
                  ],
                },
              ],
            },
          ],
        },
        {
          id: 15,
          name: 'Downloads :',
          children: [
            { id: 16, name: 'October : pdf' },
            { id: 17, name: 'November : pdf' },
            { id: 18, name: 'Tutorial : html' },
          ],
        },
        {
          id: 19,
          name: 'Videos :',
          children: [
            {
              id: 20,
              name: 'Tutorials :',
              children: [
                { id: 21, name: 'Basic layouts : mp4' },
                { id: 22, name: 'Advanced techniques : mp4' },
                { id: 23, name: 'All about app : dir' },
              ],
            },
            { id: 24, name: 'Intro : mov' },
            { id: 25, name: 'Conference introduction : avi' },
          ],
        },
      ],
    }),

    computed: {

  ...mapGetters('resources/utils', ['tab_filiere' ,'tab_department' , 
  'tab_level', 'tab_course','cours_selected','level_selected', 
  'salle_selected','filiere_selected', 'type_schedule_selected','department_selected']),
  ...mapGetters('resources/classes', [
    'tab_classe'
  ])
    },
    methods: {

      ...mapActions('resources/utils', ['set_salle','set_filiere','set_type_schedule','set_level','set_cours','set_department'])
    }
  }
</script>