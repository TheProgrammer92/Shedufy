export default function TrieTabEvent(tab_event, tab_course, tab_type_events, params_load_event, TEACHER_TYPE) {


    let events = []

    tab_event.forEach(event => {


        // on utilise i pour diminuer la profondeur


        let e = tab_course.filter(course => course.id == event.id_course)


        //  let e_level = tab_level.filter(level => level.id == event.id_level)*/




        // pour modifier la couleur verifions si c'est une reservation, si c'est une reservation on mettra une meme couleur



        let type_reservation = tab_type_events.filter(type_event => type_event.type == 6)[0] //6 = reservation

        let e_type_event = undefined
        if (type_reservation.type == params_load_event.id_type) {

            e_type_event = tab_type_events.filter(type_event => type_event.type == event.type_reservation)


        }
        //si c'est l'emploie du prof, 
        else if (TEACHER_TYPE = params_load_event.id_type) {

            e_type_event = tab_type_events.filter(type_event => type_event.type == event.id_type)


        } else {
            e_type_event = tab_type_events.filter(type_event => type_event.type == event.id_type)

        }

        // je fais ca pour enleve le premier id de category
        let newFormElement = event
        newFormElement.id = event.id
        newFormElement.name = e[0].name
        newFormElement.code_course = e[0].code_course


        // newFormElement.level_code = e_level[0].level_code

        newFormElement.color = e_type_event[0].color

        newFormElement.start = event.start
        newFormElement.end = event.end
        newFormElement.id_classe = event.id_classe
        newFormElement.message = e[0].code_course + "\n" + e[0].name + "\n" + params_load_event.message


        events.push(newFormElement)

        console.log("tab event final = ", events)

    })

    return events

}