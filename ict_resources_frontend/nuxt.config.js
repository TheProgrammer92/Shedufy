import colors from 'vuetify/es5/util/colors'

export default {
    mode: 'universal',
    /*
     ** Headers of the page
     */
    head: {
        titleTemplate: '%s - ' + process.env.npm_package_name,
        title: process.env.npm_package_name || '',
        meta: [
            { charset: 'utf-8' },
            { name: 'viewport', content: 'width=device-width, initial-scale=1' },
            { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
        ],

        script: [{
                src: '/dist/jquery.slim.min.js',
                type: "text/javascript"
            },


        ],
        link: [{
                rel: 'stylesheet',
                href: 'https://fonts.googleapis.com/css?family=Roboto:300,400&display=swap',
                rel: 'stylesheet',
                href: 'https://fonts.googleapis.com/icon?family=Material+Icons',
            }

        ],


        script: [
            { src: '/dist/jquery.slim.min.js' },
        ],
    },
    /*
     ** Customize the progress-bar color
     */
    loading: { color: '#fff' },
    /*
     ** Global CSS
     */
    css: [

        "@/assets/css/main.scss"
    ],
    /*
     ** Plugins to load before mounting the App
     */
    plugins: [

        '~/plugins/axios',
        '~/plugins/mixins/validation',
        '~/plugins/mixins/user',
        '~/plugins/vue/vueTextareaAutosize',
        '~/plugins/vue/main.js',
        '~/plugins/vue/vue-notify',

    ],




    /*
     ** Nuxt.js dev-modules
     */
    buildModules: [
        '@nuxtjs/vuetify',
    ],
    /*
     ** Nuxt.js modules
     */
    modules: [
        'bootstrap-vue/nuxt',
        '@nuxtjs/axios',
        '@nuxtjs/proxy',

        '@nuxtjs/auth'
    ],
    axios: {
        // See https://github.com/nuxt-community/axios-module#options
        baseURL: 'http://127.0.0.1:8000',

    },
    // proxy: {
    //   '/api/': 'http:localhost:8000',

    // },

    proxy: {
        '/api': {
            target: 'http://127.0.0.1:8000',
            pathRewrite: {
                '^/api': '/'
            }
        }
    },





    auth: {
        strategies: {
            local: {

                endpoints: {
                    login: { url: '/api/jwt/create/', method: 'post', propertyName: 'access' },

                    logout: { url: '/api/blacklist/', method: 'post' },
                    user: { url: '/api/users/me/', method: 'get', propertyName: false },

                },
                vuex: {
                    namespace: 'index'
                },

                autoFetchUser: false





            },



        },
        cookie: {

            options: {
                path: '/',
                expires: 1555555555555555555555555555555555555555555555555555555555
            }
        }
    },


    /*
     ** vuetify module configuration
     ** https://github.com/nuxt-community/vuetify-module
     */
    vuetify: {
        customVariables: ['~/assets/variables.scss'],
        theme: {
            dark: false,
            themes: {
                dark: {
                    primary: colors.blue.darken2,
                    accent: colors.grey.darken3,
                    secondary: colors.amber.darken3,
                    info: colors.teal.lighten1,
                    warning: colors.amber.base,
                    error: colors.deepOrange.accent4,
                    success: colors.green.accent3
                }
            }
        }
    },
    /*
     ** Build configuration
     */
    build: {
        /*
         ** You can extend webpack config here
         */
        extend(config, ctx) {}
    }
}