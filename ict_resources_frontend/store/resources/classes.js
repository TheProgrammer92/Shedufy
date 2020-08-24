export const state = () => ({


    tab_category: [],
    tab_classe_category_selected: [],



    tab_classe: []
})




export const mutations = {

    // Les classe

    async GET_CLASSE_CATEGORY_ID(state, id_category) {



        let data = (await this.$axios.get('api/getClasseCategoryId/' + id_category + '/')).data
        state.tab_classe_category_selected = []


        state.tab_classe_category_selected = data.data



    },

    async GET_ALL_CATEGORY_CLASSE(state) {

        let data = (await this.$axios.get('api/getCategoryClasse/')).data
        state.tab_category = []
        state.tab_category = data.data



    },

    async GET_CLASSES(state) {

        let data = (await this.$axios.get('api/getClasse/')).data
        state.tab_classe = []

        state.tab_classe = data.data



    },

}


export const actions = {


    //classe


    getClasses({ commit }) {

        commit('GET_CLASSES')
    },
    getClasseCategoryId({ commit }, id_category) {

        commit('GET_CLASSE_CATEGORY_ID', id_category)
    },

    getAllCategoryClasse({ commit }, ) {

        commit('GET_ALL_CATEGORY_CLASSE')
    },


}



export const getters = {



    tab_classe: state => state.tab_classe,
    tab_classe_category_selected: state => state.tab_classe_category_selected,
    tab_category: state => state.tab_category,

}