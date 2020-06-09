<template>



    <!--display, and page processing (traitement), login-->
    <div style="width:100%">



        <div class="body-form">
            <h3 style="text-align: center;">Welcome to MyResource</h3>
            <br>

            <b-form @submit.prevent="register"  autocomplete="off">

                <b-form-group id="name"
                              label-for="User name"
                              :description="errors.username ? errors.username: ''">

                         <!--   <span v-if="hasError  && hasErrorName ">  errors.name </span>-->


                    <b-form-input id="name"
                                  type="text"
                                  v-model="data.username"
                                  required
                                  placeholder="enter name"

                    >
                    </b-form-input>
                    <!--<span class="floating-label">enter email</span>-->

                </b-form-group>

                <b-form-group id="email"
                              label-for="email"
                              :description="errors.email ? errors.email: ''">

                    <b-form-input id="email"
                                  type="email"
                                  v-model="data.email"
                                  required
                                  placeholder="enter email"
                    >
                    </b-form-input>
                  <!--  <span v-if="hasError && hasErrorEmail">errors.email</span>-->
                    <!--<span class="floating-label">enter email</span>-->

                </b-form-group>

                <b-form-group id="password"
                              label-for="pasword"
                              :description="errors.password ? errors.password: ''">

                    <b-form-input id="password"
                                  type="password"
                                  v-model="data.password"
                                  required
                                  placeholder="enter password"
                    >
                    </b-form-input>

                    <!--<span v-if="hasError && hasErrorPassword">errors.password</span>-->
                    <!-- <span class="floating-label">enter email</span>-->

                </b-form-group>




                <div class="form-group">
                    <Button type="submit" class="submit">Valider</Button>
                </div>
            </b-form>

            <b-row class="btn-auth" align-h="center"  >




                <h5 >pas encore inscrit?</h5>&nbsp

                <nuxt-link :to="{name:'auth-login'}">Connexion</nuxt-link>




            </b-row>



        </div>

    </div>



</template>

<script>




    export default {


        middleware: 'guest',
      layout: "auth",


       data() {
            return {




                data: {

                  username: '',
                  password: '',
                  email: ''
                }
            }
        },


        methods: {
          async register() {


              try {

               
                let response = await this.$axios.$post('http://localhost:8000/api/users/', this.data)

                this.$router.push({name :'auth-login'})
              } catch (err) {
                console.log("rreur une "+ err)
              }

          }
        },

        mounted() {

           //changement du nom de la page

            // this.$parent.namePageAuth="Inscription";





        }


    }

</script>

