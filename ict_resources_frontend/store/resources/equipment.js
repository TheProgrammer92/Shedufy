export const state = () => ({


    tab_equipment: [],

})




export const mutations = {
    /**
     * 
     * @param {*} state 
     * les equipement 
     */
    async GET_EQUIPMENTS(state) {

        let data = (await this.$axios.get('api/equipment/')).data
        state.tab_equipment = []

        state.tab_equipment = data.data


    },


}

export const actions = {

    // equipement

    getEquipments({ commit }) {

        commit('GET_EQUIPMENTS')
    },


}

export const getters = {



    tab_equipment: state => state.tab_equipment,


}