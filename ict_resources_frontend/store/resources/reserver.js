import { nth, monthFormatter } from "./reserver.func.js"



export const state = () => ({


    events: [],
    dialog: false,
    dialogDate: false,
    dialogUpdate: false,


    eventInput: {
        name: "",
        details: "",
        start_date: "",
        color: "#1976D2",
        end_date: "",
        id_classe: ""
    },

    tab_classe: [],
    tab_equipment: []
})


export const mutations = {


    async GET_EVENTS(state, id) {

        console.log("avoir les event = ", id)

        let data = (await this.$axios.get('api/resources/' + id + '/')).data
        state.events = []
        let dataEach = data.data


        console.log("event sget =", dataEach)


        dataEach.forEach(element => {

            state.events.push(element)
        })





    },

    async GET_CLASSES(state) {

        let data = (await this.$axios.get('api/classe/')).data
        state.tab_classe = []

        state.tab_classe = data.data



    },

    async GET_EQUIPMENTS(state) {

        let data = (await this.$axios.get('api/equipment/')).data
        state.tab_equipment = []

        state.tab_equipment = data.data

        console.log("tab_equipment = ", state.tab_equipment)

    },

    async ADD_EVENT(state, eventInput) {



        if (eventInput.name && eventInput.start && eventInput.end && eventInput.details) {
            let data = (await this.$axios.post('api/resources/', eventInput)).data

            //   state.getEvents()

            let resources = (await this.$axios.get('api/resources/')).data
            state.events = []
            let dataEach = resources.data


            dataEach.forEach(element => {

                state.events.push(element)
            })




        } else {
            alert('You must enter event name, start, and end time')
        }
    },



    async DELETE_EVENT(state, id) {


        let data = (await this.$axios.delete('api/resources/' + id + '/')).data




    },
    SHOW_EVENT(state, { nativeEvent, event }) {
        const open = () => {
            this.selectedEvent = event
            this.selectedElement = nativeEvent.target
            setTimeout(() => this.selectedOpen = true, 10)
        }
        if (this.selectedOpen) {
            this.selectedOpen = false
            setTimeout(open, 10)
        } else {
            open()
        }
        nativeEvent.stopPropagation()
    },

    SET_DIALOG_UPDATE(state) {
        state.dialogUpdate = !state.dialogUpdate
    },


    SET_DIALOG_DATE(state, date) {

        state.dialogDate = true
        state.focus = date
    },

    SET_DIALOG(state) {


        state.dialog = !state.dialog

    },





}

export const actions = {

    //classe


    getClasses({ commit }) {

        commit('GET_CLASSES')
    },

    // equipement

    getEquipments({ commit }) {

        commit('GET_EQUIPMENTS')
    },


    getEvents({ commit }, id) {
        commit('GET_EVENTS', id)
    },
    addEvent({ commit }, eventInput) {
        commit('ADD_EVENT', eventInput)

    },


    deleteEvent({ commit }, id) {
        commit('DELETE_EVENT', id)
    },




    setDialogUpdate({ commit }) {

        commit('SET_DIALOG_UPDATE')
    },


    setDialogDate({ commit }, date) {

        commit('SET_DIALOG_DATE', date)
    },

    setDialog({ commit }) {

        commit('SET_DIALOG')
    },





}


export const getters = {


    events: state => state.events,
    details: state => state.details,
    dialogDate: state => state.dialogDate,
    dialogUpdate: state => state.dialogUpdate,

    dialog: state => state.dialog,
    tab_classe: state => state.tab_classe,
    tab_equipment: state => state.tab_equipment,

    eventInput: state => state.eventInput

}