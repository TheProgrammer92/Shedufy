export const state = () => ({


    is_show_notification: true
})


export const mutations = {

    SET_SHOW_NOTIFICATION(state) {

        console.log("is show notification", state.is_show_notification)

        state.is_show_notification = !state.is_show_notification
    }

}

export const actions = {


    set_show_notification({ commit }) {


        commit("SET_SHOW_NOTIFICATION")
    },



}


export const getters = {



    is_show_notification: state => state.is_show_notification,



}