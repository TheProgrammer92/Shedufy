export const state = () => ({
    errors: "fsdf",


    urlApi: 'http://upgradeeducation.local/api/'
})


export const mutations = {

    SET_VALIDATION_ERRORS(state, errors) {



        state.errors = errors

    }

}

export const actions = {

    setErrors({ commit }, errors) {




        commit('SET_VALIDATION_ERRORS', errors)

    },

    clearErrors({ commit }) {

        commit('SET_VALIDATION_ERRORS', {})
    },

    urlApi(state) {

        return state.urlAxios


    }


}


export const getters = {

    errors(state) {

        return state.errors
    }
}