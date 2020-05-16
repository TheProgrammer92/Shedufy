<template>

    <div>




        <div class="sidebar-auth float-right fixed"  >


            <b-row align-v="center" align-h="center" class="row-auth" >



                <nuxt/>
            </b-row>


        </div>


    </div>


</template>

<script>


    export default {

         middleware: 'guest',



        mounted(){



               $('body').css('background','url(../img/fond2.jpg) center center /cover')

        },




        beforeRouteLeave(to , from , next){

            $('body').css('background','#eee').css('background-image','unset');


            next()

        },




        beforeRouteEnter(to ,from, next) {

            $(function () {



                $('body').css('background','url(../img/fond1.jpg) center center /cover')


            });

            next()
        }

    }
</script>

