export default function({ store, redirect }) {

    if (!store.getters['is_teacher']) {
        redirect('/')
    }
}