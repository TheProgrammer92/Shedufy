export const state = () => ({


    tab_course_category: [],
    tab_course: [],
})


export const mutations = {

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

}

export const actions = {


    //course

    //course avec modification du tableau pour afficher dans le select
    getCourse({ commit }, ) {

        commit('GET_COURSE')
    },

    //tous les cours sans modification du tableau
    getAllCourse({ commit }, ) {

        commit('GET_ALL_COURSE')
    },




}


export const getters = {



    tab_course_category: state => state.tab_course_category,

    tab_course: state => state.tab_course,



}