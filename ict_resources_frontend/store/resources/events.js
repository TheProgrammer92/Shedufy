export const state = () => ({


    events: [],



})






export const mutations = {



    async GET_EVENTS(state, id_classe) {


        let data = (await this.$axios.get('api/resources/' + id_classe + '/')).data
        state.events = []
        let dataEach = data.data

        let tab_event = dataEach


        let data_course = (await this.$axios.get('api/getCourse/')).data



        let tab_course = data_course.data




        tab_event.forEach(event => {


            // on utilise i pour diminuer la profondeur


            let e = tab_course.filter(course => course.id == event.id_course)

            // je fais ca pour enleve le premier id de category
            let newFormElement = event
            newFormElement.id = e[0].id
            newFormElement.name = e[0].name
            newFormElement.code_course = e[0].code_course
            newFormElement.code_course = e[0].code_course
            newFormElement.start = event.start
            newFormElement.end = event.end
            newFormElement.color = event.color
            newFormElement.id_classe = event.id_classe
            newFormElement.id_equipment = event.id_equipment






            state.events.push(newFormElement)



        })










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

    getEvents({ commit }, id_classe) {
        commit('GET_EVENTS', id_classe)
    },
    addEvent({ commit }, eventInput) {
        commit('ADD_EVENT', eventInput)

    },

    deleteEvent({ commit }, id) {
        commit('DELETE_EVENT', id)
    },


}



export const getters = {


    events: state => state.events,



}