import TrieTabEvent from '../../plugins/utils'


export const state = () => ({


    events: [],
    tab_type_events: [],
    tab_event_selected: []



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
        let tab_course = []

        //

        if (this._vm.TYPE_TEACHER == params_load_event.id_type) {


            tab_course = (await this.$axios.$get('api/getCourse/')).data


        } else {
            let datas = (await this.$axios.get('api/getDepartmentFilierLevelId/' + params_load_event.id_department + '/?is_id_admin=guest')).data
            let tab_department = datas.department
            let tab_filiere = datas.filiere
            let tab_level = datas.level
            tab_course = datas.course
        }




        state.events = TrieTabEvent(tab_event, tab_course, state.tab_type_events, params_load_event, this._vm.TEACHER_TYPE)






    },

    async GET_EVENT_ID(state, params_load_event) {
        let data = (await this.$axios.$get('api/resources/' + params_load_event.id_event + '/')).data

        state.tab_event_selected = []


        let tab_event = data
        let tab_course = []

        //  



        let datas = (await this.$axios.get('api/getDepartmentFilierLevelId/' + params_load_event.id_department + '/?is_id_admin=guest')).data
        let tab_department = datas.department
        let tab_filiere = datas.filiere
        let tab_level = datas.level
        tab_course = datas.course





        state.tab_event_selected = TrieTabEvent(tab_event, tab_course, state.tab_type_events, params_load_event, this._vm.TEACHER_TYPE)



        // mettons le focus sur la date




        this.dispatch('resources/notifications/set_focus_calendar_notification', state.tab_event_selected[0].start)


    },



    async SET_TAB_EVENT(state, event) {



        state.events.push(event)
    },





}


export const actions = {

    async getEvents({ commit }, params_load_event) {
        commit('GET_EVENTS', params_load_event)
    },

    getEventId({ commit }, params_load_event) {
        commit('GET_EVENT_ID', params_load_event)
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
    set_tab_event({ commit }, event) {

        commit('SET_TAB_EVENT', event)
    },




}



export const getters = {


    events: state => state.events,
    tab_type_events: state => state.tab_type_events,
    tab_event_selected: state => state.tab_event_selected,



}