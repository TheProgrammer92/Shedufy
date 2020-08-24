export const state = () => ({


    is_show_notification: false,
    tab_notification: [],
    notification_selected: {},
    focus_calendar_notification: Date.now()
})


export const mutations = {

    SET_SHOW_NOTIFICATION(state) {


        state.is_show_notification = !state.is_show_notification
    },

    async GET_NOTIFICATION_USER_ID(state, id_user) {


        let data = (await this.$axios.get('api/notifications/?id_user=' + id_user)).data


        state.tab_notification = []
        state.tab_notification = data.data

    },

    async GET_NOTIFICATION_ID(state, id) {



        let data = (await this.$axios.get('api/notifications/' + id + '/')).data


        state.notification_selected = []
        state.notification_selected = data.data



        let params_load_event = {
            id_type: state.notification_selected[0].id_type,
            id_level: state.notification_selected[0].id_level,
            by_type: "level",
            id_user: state.notification_selected[0].id_emetter,
            id_department: state.notification_selected[0].id_department,
            id_event: state.notification_selected[0].id_event,
            message: state.notification_selected[0].message

        }
        this.dispatch('resources/events/getEventId', params_load_event)




    },


    set_notification_selected(state, value) {

        state.notification_selected = value
    },

    set_focus_calendar_notification(state, value_date) {

        state.focus_calendar_notification = value_date

    }

}

export const actions = {


    set_show_notification({ commit }) {


        commit("SET_SHOW_NOTIFICATION")
    },
    set_notification_selected({ commit }, value) {


        commit("set_notification_selected", value)
    },

    get_notification_user_id({ commit }, id_user) {


        commit("GET_NOTIFICATION_USER_ID", id_user)
    },

    get_notification_id({ commit }, id_user) {


        commit("GET_NOTIFICATION_ID", id_user)
    },


    set_focus_calendar_notification({ commit }, value_date) {


        commit("set_focus_calendar_notification", value_date)
    },



}


export const getters = {



    is_show_notification: state => state.is_show_notification,
    tab_notification: state => state.tab_notification,
    notification_selected: state => state.notification_selected,
    focus_calendar_notification: state => state.focus_calendar_notification,



}