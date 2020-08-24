export const state = () => ({


    tab_department: [],

    tab_department_category: [],
    tab_filiere: [],
    tab_level: [],
    tab_course: [],
    tab_teacher: [],
    tab_type_reservation_prof: [],


    //les variable séléctionné pour la recherche
    filiere_selected: undefined,
    cours_selected: undefined,
    level_selected: undefined,
    salle_selected: undefined,
    type_schedule_selected: undefined, //on selectionne les cours par defaut
    department_selected: undefined,
    tab_type_reservation_prof: [],
    by_type_selected: 'level'

})




export const mutations = {

    // Les classe

    async GET_ALL_DEPARTMENT(state) {

        //on charge les departement pour tous le sprofesseur, 
        //quand il vont selectionner un departement on actuelise juste les data

        let datas = (await this.$axios.get('api/getAllDepartment/')).data
        state.tab_department = datas.data



    },



    async GET_DEPARTMENT_FILIERE_LEVEL_ID(state, params) {
        let data;

        if (params.what_action == "click") { //s'il a juste cliqué pour changer de depart

            data = (await this.$axios.get('api/getDepartmentFilierLevelId/' + params.id_depart + '/?is_id_admin=guest')).data


        } else {


            // s'il est un admin, o recherche son departement, on charge son depart au debut


            data = (await this.$axios.get('api/getDepartmentFilierLevelId/' + params.id_user + '/?is_id_admin=admin')).data

            state.tab_department = data.department

            //mise a  jour du select departement

            state.department_selected = state.tab_department[0].id


        }

        state.tab_classe_category_selected = []



        state.tab_filiere = data.filiere
        state.tab_level = data.level
        state.tab_course = data.course
        state.tab_teacher = data.teacher





    },

    SET_FILIERE(state, value) {
        state.filiere_selected = value
    },
    SET_COURS(state, value) {
        state.cours_selected = value
    },
    SET_SALLE(state, value) {

        state.salle_selected = value
    },

    SET_LEVEL(state, value) {

        state.level_selected = value
    },
    SET_TYPE_SCHEDULE(state, value) {
        state.type_schedule_selected = value
    },

    SET_DEPARTMENT(state, value) {

        state.department_selected = value
    },


    SET_BY_TYPE(state, value) {

        state.by_type_selected = value
    },



}


export const actions = {


    //classe


    getDepartmentFilierLevelId({ commit }, params) {
        commit('GET_DEPARTMENT_FILIERE_LEVEL_ID', params)
    },

    getAllDepartment({ commit }) {

        commit('GET_ALL_DEPARTMENT')
    },

    set_filiere({ commit }, filiere) {

        commit("SET_FILIERE", filiere)
    },
    set_level({ commit }, level) {

        commit("SET_LEVEL", level)
    },
    set_cours({ commit }, cours) {

        commit("SET_COURS", cours)
    },

    set_salle({ commit }, salle) {

        commit("SET_SALLE", salle)
    },
    set_type_schedule({ commit }, type) {

        commit("SET_TYPE_SCHEDULE", type)
    },
    set_by_type({ commit }, value) {

        commit("SET_BY_TYPE", value)
    },

    set_department({ commit }, type) {

        commit("SET_DEPARTMENT", type)


        //on charge les donnée lié a ce departement
        let params = {}
        params.what_action = "click"
        params.id_depart = type
        commit('GET_DEPARTMENT_FILIERE_LEVEL_ID', params)
    },


}



export const getters = {



    tab_filiere: state => state.tab_filiere,
    tab_department: state => state.tab_department,
    tab_level: state => state.tab_level,
    tab_course: state => state.tab_course,
    tab_teacher: state => state.tab_teacher,

    filiere_selected: state => state.filiere_selected,
    cours_selected: state => state.cours_selected,
    level_selected: state => state.level_selected,
    salle_selected: state => state.salle_selected,
    type_schedule_selected: state => state.type_schedule_selected,
    department_selected: state => state.department_selected,
    by_type_selected: state => state.by_type_selected,

}