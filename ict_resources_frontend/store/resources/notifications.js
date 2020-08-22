export const state = () => ({


    is_show_notification: false,
    tab_notification: []
})


export const mutations = {

    SET_SHOW_NOTIFICATION(state) {


        state.is_show_notification = !state.is_show_notification
    },

    async GET_NOTIFICATION_USER_ID(state, id_user) {


        let data = (await this.$axios.get('api/notifications/' + id_user + '/')).data


        state.tab_notification = []
        state.tab_notification = data.data

    }

}

export const actions = {


    set_show_notification({ commit }) {


        commit("SET_SHOW_NOTIFICATION")
    },

    get_notification_user_id({ commit }, id_user) {


        commit("GET_NOTIFICATION_USER_ID", id_user)
    },



}


export const getters = {



    is_show_notification: state => state.is_show_notification,
    tab_notification: state => state.tab_notification,



}