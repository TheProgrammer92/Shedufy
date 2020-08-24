export const state = () => ({



    dialog: false,
    dialogDate: false,
    dialogUpdate: false,




    tab_reservation_valid: [],
    tab_reservation_refus: [],
    tab_reservation_attente: [],
    tab_reservation_annulle: [],
})


export const mutations = {
    async GET_ALL_RESERVATION_SCHEDULE(state) {

        let data = (await this.$axios.get('api/reservationschedule/')).data


        state.tab_reservation_valid = []
        state.tab_reservation_refus = []
        state.tab_reservation_attente = []
        state.tab_reservation_annulle = []



        //on recupere les type de reservation
        state.tab_reservation_valid = data.reservation_valid
        state.tab_reservation_refus = data.reservation_refus
        state.tab_reservation_attente = data.reservation_attente
        state.tab_reservation_annulle = data.reservation_annulle



    },
    async GET_ALL_RESERVATION_SCHEDULE_TEACHER(state, id_teacher) {




        let data = (await this.$axios.get('api/reservationschedule/' + id_teacher + '/')).data
        state.tab_reservation_valid = []
        state.tab_reservation_refus = []
        state.tab_reservation_attente = []
        state.tab_reservation_annulle = []



        //on recupere les type de reservation
        state.tab_reservation_valid = data.reservation_valid
        state.tab_reservation_refus = data.reservation_refus
        state.tab_reservation_attente = data.reservation_attente
        state.tab_reservation_annulle = data.reservation_annulle



    },




    SET_DIALOG_UPDATE(state) {

        console.log("dialog update is", state.dialogUpdate)
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



    dialog: state => state.dialog,
    dialogUpdate: state => state.dialogUpdate,
    dialogDate: state => state.dialogDate,
    tab_reservation_valid: state => state.tab_reservation_valid,
    tab_reservation_refus: state => state.tab_reservation_refus,
    tab_reservation_attente: state => state.tab_reservation_attente,
    tab_reservation_annulle: state => state.tab_reservation_annulle,



}