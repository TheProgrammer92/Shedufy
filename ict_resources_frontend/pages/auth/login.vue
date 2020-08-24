<template>



    <!--display, and page processing (traitement), login-->
    <div style="width:100%">



        <div class="body-form">
            <h3 style="text-align: center;">  Welcome to MyResource </h3>
            <br>

            <p v-if="errors.detail">  {{errors.detail }} </p>

            <b-form @submit.prevent="login"  autocomplete="off">

                <b-form-group
                              label-for="User email"
                              :description="errors.email ? errors.email: ''">

                         <!--   <span v-if="hasError  && hasErrorName ">  errors.name </span>-->


                    <b-form-input
                                  type="email"
                                  v-model="data.email"
                                  required
                                  placeholder="enter email"

                    >
                    </b-form-input>
                    <!--<span class="floating-label">enter email</span>-->

                </b-form-group>



                <b-form-group
                              label-for="pasword"
                              :description="errors.password ? errors.password: null">

                    <b-form-input
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
                    <Button type="submit" class="submit">Se connecter</Button>
                </div>
            </b-form>

            <b-row class="btn-auth" align-h="center"  >




                <h5 >pas encore inscrit?</h5>&nbsp

                <nuxt-link :to="{name:'auth-register'}">Inscription</nuxt-link>




            </b-row>



        </div>

    </div>



</template>

<script>





    export default {
   middleware: 'guest',

      layout:'auth',





       data() {
            return {




                data: {

                  email: '',
                  password: '',

                }
            }
        },


        methods: {
          async login() {





              let app = this;



              try {

                let form =  {

                email: app.data.email,
                password: app.data.password

              }


                let response =  await this.$auth.login({ data: form })



                if(response.data) {

                   console.log("response data",response)

                 this.$auth.$storage.setLocalStorage("refresh_token", response.data.refresh)





              }


            window.location.reload();

              app.$router.push({name:'index'})
              } catch (error) {

                  console.log("erreur sur login" , error.response)
              }


                }








        },
  mounted() {
      
     

  }



    }

</script>

