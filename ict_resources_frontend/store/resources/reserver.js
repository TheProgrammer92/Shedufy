import { nth, monthFormatter } from "./reserver.func.js"

async function get_event(state) {


    console.log("call get Event")

    let data = (await state.$axios.get('api/resources/')).data

    let dataEach = data.data

    let events = []
    dataEach.forEach(element => {

        events.push(element)
    })

    return events


}

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
        end_date: ""
    }
})


export const mutations = {


    async GET_EVENTS(state) {

        console.log("call get Event")

        let data = (await this.$axios.get('api/resources/')).data
        state.events = []
        let dataEach = data.data


        dataEach.forEach(element => {

            state.events.push(element)
        })


        console.log("event = ", state.events)

    },

    async ADD_EVENT(state, eventInput) {



        console.log("demare event", eventInput)
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

    async UPDATE_EVENT(state, ev) {
        await db.collection('calEvent').doc(this.currentlyEditing).update({
            details: ev.details
        })
        this.selectedOpen = false,
            this.currentlyEditing = null
    },
    async DELETE_EVENT(state, id) {

        console.log("je vais delete , selected id = ", id)
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
        console.log("ayaaaaaaaaaa set dialog update")
        state.dialogUpdate = !state.dialogUpdate
    },


    SET_DIALOG_DATE(state, date) {

        console.log("set me dialog date")
        state.dialogDate = true
        state.focus = date
    },

    SET_DIALOG(state) {


        state.dialog = !state.dialog

    },





}

export const actions = {

    getEvents({ commit }) {
        commit('GET_EVENTS')
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

    eventInput: state => state.eventInput

}