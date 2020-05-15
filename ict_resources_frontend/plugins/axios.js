export default function ({ $axios, store}) {
  $axios.onRequest(config => {
    console.log('petit je fais une request' + config.url)

    store.dispatch('validation/clearErrors');
  })

  $axios.onError(error => {
    const code = parseInt(error.response && error.response.status)

    if(error.response.data) {

      store.dispatch('validation/setErrors', error.response.data)

    }


    console.log("errur on errors", error.response)
    if (code === 400) {
      // redirect('/400')
    }


    return Promise.reject(error);
  })
}

