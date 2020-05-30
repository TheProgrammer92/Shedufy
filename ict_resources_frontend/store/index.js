export const strict = false



export const getters = {


    authenticated(state) {
        return state.auth.loggedIn
    },

    user(state) {

        return state.auth.user
    },

    urlApi(state) {

        return state.urlApi
    },

    is_teacher(state) {



        let is_teacher = state.auth.user.is_staff == 1
        return is_teacher
    }
}

export const mutations = {

    SET_USER(state, user) {

        state.user = user

    }
}

export const actions = {

    setUser({ commit }, user) {
        commit('SET_USER', user)
    }
}

export const state = () => ({


    busy: false,
    loggedIn: false,
    stategy: "local",
    user: {

    },
    is_teacher: false


})