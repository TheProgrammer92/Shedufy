export const state = () => ({


    clipped: true,
    drawer_left: true,

    drawer_sidebar_global: false,
    right_sidebar_global: true,
    clipped_sidebar_global: false,
})


export const mutations = {

    set_clipped(state) {


        state.clipped = !state.clipped
    },

    set_drawer_left(state) {


        state.drawer_left = !state.drawer_left
    },
    SET_DRAWER_SIDEBAR_GLOBAL(state) {


        console.log("voici drawer global", state.drawer_sidebar_global)

        state.drawer_sidebar_global = !state.drawer_sidebar_global


    },

    set_clipped_sidebar_global(state) {

        console.log("cliped global set")

        state.clipped_sidebar_global = !state.clipped_sidebar_global

    },

    set_direct_value_drawer_sidebar_global(state, value) {


        state.drawer_sidebar_global = value
        console.log("cliped direc value", state.drawer_sidebar_global)

    }
}

export const actions = {


    set_clipped({ commit }) {


        commit("set_clipped")
    },
    set_drawer_left({ commit }) {

        commit('set_drawer_left')
    },


    set_clipped_sidebar_global({ commit }) {


        commit("set_clipped_sidebar_global")
    },
    set_drawer_sidebar_global({ commit }) {


        commit('SET_DRAWER_SIDEBAR_GLOBAL')
    },
    set_direct_value_drawer_sidebar_global({ commit }, value) {

        console.log("voici direct drawer global", state.drawer_sidebar_global)

        commit('set_direct_value_drawer_sidebar_global', value)
    }



}


export const getters = {



    clipped: state => state.clipped,
    drawer_left: state => state.drawer_left,
    drawer_sidebar_global: state => state.drawer_sidebar_global,
    right_sidebar_global: state => state.right_sidebar_global,
    clipped_sidebar_global: state => state.clipped_sidebar_global,




}