export default function({ store, redirect }) {

    if (!store.getters['is_teacher']) {
        alert("vous n'ete pas professeur")
        redirect('/')
    }
}