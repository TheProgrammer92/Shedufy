export default function({ $axios, store, redirect }) {
    $axios.onRequest(config => {
        // console.log('petit je fais une request' + config.url)

        store.dispatch('validation/clearErrors');
    })

    $axios.onError(error => {


        const code = parseInt(error.response && error.response.status)

        if (error.response.data) {

            store.dispatch('validation/setErrors', error.response.data)

        }



        if (code === 400) {
            // redirect('/400')
        }

        if (code === 401) {

            alert("Vous devez vous connecter")
            redirect('/auth/login')
        }


        return Promise.reject(error);
    })

    $axios.onResponse(response => {




        if (response.config.url === "/api/users/me/") {



        }
    })
}