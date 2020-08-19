import Vue from 'vue';


import { mapGetters } from 'vuex';


const Validation = {

    install(Vue, options) {

        Vue.mixin({
            data() {
                return {

                }
            },
            computed: {

                ...mapGetters({

                    user: 'user',
                    is_teacher: 'is_teacher',
                    authenticated: "authenticated",
                    is_admin: "is_admin",

                }),

                RESERVATION() {

                    return 6
                },
                ETAT_ATTENTE() {

                    return 3
                }
            }
        })
    }
}

Vue.use(Validation);