export const state = () => ({


    clipped: true,
    drawer_left: true,
})


export const mutations = {

    set_clipped(state) {


        state.clipped = !state.clipped
    },

    set_drawer_left(state) {


        state.drawer_left = !state.drawer_left
    },

}

export const actions = {


    set_clipped({ commit }) {


        commit("set_clipped")
    },
    set_drawer_left({ commit }) {

        commit('set_drawer_left')
    }



}


export const getters = {



    clipped: state => state.clipped,
    drawer_left: state => state.drawer_left,



}