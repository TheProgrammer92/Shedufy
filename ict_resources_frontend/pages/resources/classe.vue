<template>
<v-container fluid class="pa-4 text-center">





    <v-row class="fill-height flex flex-column"  v-for="(category, index) in tab_category"  :key="index">

    <h2 class="text-left">{{category.department_name}}</h2>

       <v-row>


      <!-- on verifie si la classe lié a la catérogry est dans le tableau des classe-->
        <template v-for="(item, i) in tab_classe"   >
        <v-col

        v-if="category.classe.indexOf(item.id) !== -1" 
          :key="i"
          cols="12"
          md="4"
          
    
          @click.prevent="showSchedule(item.id,category.id)"
        >
          <v-hover v-slot:default="{ hover }">
            <v-card
              :elevation="hover ? 12 : 2"
              :class="{ 'on-hover': hover }"
            >
              <v-img
                :src="img"
                height="225px"
              >
                <v-card-title class="title white--text">
                  <v-row
                    class="fill-height flex-column"
                    justify="space-between"
                  >
                    <p class="mt-4 subheading text-center">{{ item.code_classe }} id = {{item.id}}</p>

                    <div>
                      <p class="ma-0 body-1 font-weight-bold font-italic text-center">
                        {{ item.code_classe }}
                      </p>
                      <p class="caption font-weight-medium font-italic text-left">
                        {{ item.code_classe }}
                      </p>
                    </div>

                    
                  </v-row>
                </v-card-title>
              </v-img>
            </v-card>
          </v-hover>
        </v-col>
      </template>
       
       </v-row>
    </v-row>
  </v-container>
</template>

<script>


import {mapActions , mapGetters} from 'vuex'


export default {

   data() {
     return {

      
          loading: false,
          selection: 1,
              img: 'https://www.bienenseigner.com/wp-content/uploads/2019/02/decoration-salle-de-classe-780x470.jpg',



        
          transparent: 'rgba(255, 255, 255, 0.1)',



     
      
 
     }
   },

    computed: {

        ...mapGetters('resources/classes', [
            'tab_classe', 'tab_category',
        ]),
        
        ...mapGetters('resources/course', [
            'tab_course_category',
        ])
    },

    methods: {

    
     ...mapActions('resources/classes', ['getClasses','getClasseCategoryId','getAllCategoryClasse']),
     ...mapActions('resources/equipment',['getEquipments']),
     ...mapActions('resources/course',['getAllCourse','getCourse']),
     ...mapActions('resources/events',['getEvents']),
 
 


      reserve () {
        this.loading = true

        setTimeout(() => (this.loading = false), 2000)
      },


      showSchedule(id_classe,id_categ) {
        

        //on charge les eveement, les cours par categori et classe par categorie

      
        this.getEvents(id_classe)
        this.getClasseCategoryId(id_categ)
        this.getCourse()


        this.$router.push({name:'resources-schedule-id', params: {id:id_classe}})

        
      }
    },

    async mounted() {






        
    }
    
}
</script>