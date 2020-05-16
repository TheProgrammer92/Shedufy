export const strict = false



export const getters = {


  authenticated(state){
      return state.auth.loggedIn
  },

  user (state) {

      return state.auth.user
  },

  urlApi(state) {

      return state.urlApi


  }
}

export const state = ()=> ({


  busy:false,
  loggedIn:false,
  stategy:"local",
  user:false


})
