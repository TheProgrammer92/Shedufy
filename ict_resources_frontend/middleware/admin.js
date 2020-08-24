export default function({ store, redirect }) {

    if (!store.getters['is_admin']) {
        alert("vous n'ete pas admin")
        redirect('/')
    }
}