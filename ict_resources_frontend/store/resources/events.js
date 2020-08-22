export const state = () => ({


    events: [],
    tab_type_events: [],



})






export const mutations = {

    async GET_TYPE_EVENT(state) {

        let datas = (await this.$axios.$get('api/TypeScheduleView')).data
        state.tab_type_events = []


        state.tab_type_events = datas



    },
    /**
     * 
     * @param {*} state 
     * @param {*} params_load_event {by_type:"classe, level,salle,cours" , id_level, id_classe, cours}
     */
    async GET_EVENTS(state, params_load_event) {




        let data = (await this.$axios.$get('api/resources/', {
            params: params_load_event
        }))



        state.events = []



        let tab_event = data.data

        //

        let datas = (await this.$axios.get('api/getDepartmentFilierLevelId/' + params_load_event.id_department + '/?is_id_admin=guest')).data




        let tab_department = datas.department
        let tab_filiere = datas.filiere
        let tab_level = datas.level
        let tab_course = datas.course



        tab_event.forEach(event => {


            // on utilise i pour diminuer la profondeur


            let e = tab_course.filter(course => course.id == event.id_course)
            let e_level = tab_level.filter(level => level.id == event.id_level)

            // pour modifier la couleur verifions si c'est une reservation, si c'est une reservation on mettra une meme couleur



            let type_reservation = state.tab_type_events.filter(type_event => type_event.type == 6)[0] //6 = reservation

            let e_type_event = undefined
            if (type_reservation.type == params_load_event.id_type) {

                e_type_event = state.tab_type_events.filter(type_event => type_event.type == event.type_reservation)


            } else {
                e_type_event = state.tab_type_events.filter(type_event => type_event.type == event.id_type)

            }

            // je fais ca pour enleve le premier id de category
            let newFormElement = event
            newFormElement.id = event.id
            newFormElement.name = e[0].name
            newFormElement.code_course = e[0].code_course


            newFormElement.level_code = e_level[0].level_code


            newFormElement.color = e_type_event[0].color


            newFormElement.start = event.start
            newFormElement.end = event.end
            newFormElement.id_classe = event.id_classe






            state.events.push(newFormElement)



        })

        console.log("tab_event final = ", state.events)









    },




    async ADD_EVENT(state, eventInput) {



        if (eventInput.name && eventInput.start && eventInput.end && eventInput.details) {
            let data = (await this.$axios.post('api/resources/', eventInput)).data

            //   state.getEvents()

            let resources = (await this.$axios.get('api/resources/')).data
            state.events = []
            state.events = resources.data






        } else {
            alert('You must enter event name, start, and end time')
        }
    },



}


export const actions = {

    async getEvents({ commit }, params_load_event) {
        commit('GET_EVENTS', params_load_event)
    },
    addEvent({ commit }, eventInput) {
        commit('ADD_EVENT', eventInput)

    },

    getTypeEvent({ commit }) {
        commit('GET_TYPE_EVENT', )

    },

    deleteEvent({ commit }, id) {
        commit('DELETE_EVENT', id)
    },


}



export const getters = {


    events: state => state.events,
    tab_type_events: state => state.tab_type_events,



}