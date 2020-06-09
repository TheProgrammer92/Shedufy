import { nth, monthFormatter } from "./reserver.func.js"



export const state = () => ({


    events: [],
    dialog: false,
    dialogDate: false,
    dialogUpdate: false,


    eventInput: {
        id_course: "",
        start_date: "",
        color: "#1976D2",
        end_date: "",
        id_classe: 1,
        id_equipment: "",
        id_teacher: ""
    },

    tab_classe: [],
    tab_equipment: [],
    tab_category: [],
    tab_classe_category_selected: [],


    tab_course_category: [],
    tab_course: [],
    tab_reservation_valid: [],
    tab_reservation_failed: []
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

    //les cours

    async GET_COURSE(state) {

        let data_course = (await this.$axios.get('api/getCourse/')).data
        let data_category_course = (await this.$axios.get('api/getCategoryCourse/')).data



        let tab_course = data_course.data
        let tab_category_course = data_category_course.data


        state.tab_course_category = []



        tab_category_course.forEach(category => {




            state.tab_course_category.push({ header: category.group })

            for (let index = 0; index < category.course.length; index++) {

                // on utilise i pour diminuer la profondeur


                let e = tab_course.filter(course => course.id == category.course[index])

                // je fais ca pour enleve le premier id de category
                let newFormElement = {}
                newFormElement.group = category.group
                newFormElement.id = e[0].id
                newFormElement.name = e[0].name
                newFormElement.code_course = e[0].code_course






                state.tab_course_category.push(newFormElement)



            }




        })








    },

    async GET_CATEGORY_COURSE(state) {

        let data = (await this.$axios.get('api/getCategoryCourse/')).data
        state.tab_category_course = []

        state.tab_category_course = data.data



    },

    async GET_ALL_COURSE(state) {

        let data = (await this.$axios.get('api/getCourse/')).data
        state.tab_course = []

        state.tab_course = data.data



    },


    /**
     * 
     * @param {*} state 
     * les equipement 
     */
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
            state.events = resources.data






        } else {
            alert('You must enter event name, start, and end time')
        }
    },







    async GET_ALL_RESERVATION_SCHEDULE(state) {

        let data = (await this.$axios.get('api/reservationSchedule/')).data
        state.tab_reservation_valid = []
        state.tab_reservation_failed = []




        state.tab_reservation_valid = data.data_valid



        state.tab_reservation_failed = data.data_failed



    },
    async GET_ALL_RESERVATION_SCHEDULE_TEACHER(state, id_teacher) {


        let data = (await this.$axios.get('api/reservationSchedule/' + id_teacher + '/')).data
        state.tab_reservation_valid = []
        state.tab_reservation_failed = []



        state.tab_reservation_valid = data.data_valid



        state.tab_reservation_failed = data.data_failed



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
    getClasseCategoryId({ commit }, id_category) {

        commit('GET_CLASSE_CATEGORY_ID', id_category)
    },

    getAllCategoryClasse({ commit }, ) {

        commit('GET_ALL_CATEGORY_CLASSE')
    },



    //course

    //course avec modification du tableau pour afficher dans le select
    getCourse({ commit }, ) {

        commit('GET_COURSE')
    },

    //tous les cours sans modification du tableau
    getAllCourse({ commit }, ) {

        commit('GET_ALL_COURSE')
    },




    // equipement

    getEquipments({ commit }) {

        commit('GET_EQUIPMENTS')
    },


    getEvents({ commit }, id_classe) {
        commit('GET_EVENTS', id_classe)
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



    //reservation

    getAllReservationSchedule({ commit }) {

        commit("GET_ALL_RESERVATION_SCHEDULE")

    },

    getAllReservationScheduleTeacher({ commit }, id_teacher) {

        commit("GET_ALL_RESERVATION_SCHEDULE_TEACHER", id_teacher)

    },







}


export const getters = {


    events: state => state.events,
    details: state => state.details,
    dialogDate: state => state.dialogDate,
    dialogUpdate: state => state.dialogUpdate,

    dialog: state => state.dialog,
    tab_classe: state => state.tab_classe,
    tab_category: state => state.tab_category,
    tab_classe_category_selected: state => state.tab_classe_category_selected,
    tab_course_category: state => state.tab_course_category,
    tab_equipment: state => state.tab_equipment,
    tab_reservation_valid: state => state.tab_reservation_valid,
    tab_reservation_failed: state => state.tab_reservation_failed,
    tab_course: state => state.tab_course,

    eventInput: state => state.eventInput,


}