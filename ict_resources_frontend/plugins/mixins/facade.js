import Vue from 'vue';




import { mapActions, mapGetters } from 'vuex'
export default {
    data() {

        return {


        }
    },

    computed: {


    },

    methods: {
        getInfoUserId(id, params, tab_user) {



            try {


                let u = tab_user.find(user => user.id == id)


                switch (params) {
                    case 'email':
                        return u.email
                        break;
                    case 'username':
                        return u.username

                    default:
                        break;
                }


            } catch (error) {
                return undefined
            }





        }
    },

}