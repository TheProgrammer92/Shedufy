import Vue from 'vue';


import { mapGetters } from 'vuex';


const Validation = {

    install(Vue, options) {

        Vue.mixin({
            computed: {

                ...mapGetters({

                    user: 'user',
                    is_teacher: 'is_teacher',
                    authenticated: "authenticated",
                    is_admin: "is_admin"

                })
            }
        })
    }
}

Vue.use(Validation);