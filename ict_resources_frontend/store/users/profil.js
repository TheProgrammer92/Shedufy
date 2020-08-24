export const state = () => ({


    tab_user: []

})


export const mutations = {




    async UPDATE_USERS_PERSONAL_INFO(state) {


        let data = (await this.$axios.put('api/users/update_personnal_info')).data


        vm.$snotify.success('Mise a jour effectués', {
            timeout: 5000,
            showProgressBar: true,
            closeOnClick: true,
            pauseOnHover: true
        });


    },


    async GET_ALL_USER(state) {



        let data = (await this.$axios.get('api/users/getAllUser')).data

        state.tab_user = []

        state.tab_user = data.data



    },






}

export const actions = {

    //classe


    updateUsersPersonalInfo({ commit }, user) {

        commit('UPDATE_USERS_PERSONAL_INFO', user)
    },

    getAllUser({ commit }) {

        commit('GET_ALL_USER')
    },






}


export const getters = {


    events: state => state.events,
    tab_user: state => state.tab_user,


}