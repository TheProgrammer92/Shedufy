<template>
    <div class="container-notification">
  <div class="notification">
    <transition name="fadeStart" v-cloak>
      <div v-if="is_show_notification" class="tooltips">
        <div id="heading">
          <div class="heading-left">
            <h6 class="heading-title">Notifications</h6>
          </div>
            <div class="heading-right">

              <nuxt-link to="/notifications" class="notification-link">
               See all          
               </nuxt-link>

            </div>

        </div>
        <ul class="notification-list">
          <li class="notification-item " style="cursor:pointer" v-for="(notify,keys)
          of tab_notification" :key="keys" @click.prevent="goToNotify(notify)">
          <template >
            <div class="img-left">
              <img class="user-photo" alt="User Photo" src="https://img.favpng.com/25/7/23/computer-icons-user-profile-avatar-image-png-favpng-LFqDyLRhe3PBXM0sx2LufsGFU.jpg" />
            </div>
            <div class="user-content">
              <p class="user-info"><span class="name">{{notify.message}}</span> cliquer ici.</p>
              <p class="time">1 hour ago</p>
            </div>
          </template>
            
          </li>
        </ul>
      </div>
    </transition>
  </div>
</div>
</template>


<script>

import {mapActions, mapGetters} from 'vuex'
export default {
    
    data: () => ({
    users: [],
    error: [],
    show: true
  }),
    computed: {

        ...mapGetters(
          'resources/notifications', [
            'is_show_notification','tab_notification' ,'notification_selected'
        ])

    },

    async fetch() {


         setInterval(this.getAllNotification, 3000);

      
    },

    fetchOnServer:false,
  mounted () {
  },

  methods: {
      ...mapActions('resources/notifications',['set_show_notification','get_notification_user_id','set_notification_selected']),
      ...mapActions('resources/events',['getEventId']),

  getAllNotification() {this.get_notification_user_id(this.user.id)
   },

   goToNotify(notify) {


     this.set_notification_selected(notify)

       

  
     this.$router.push({ path: `/notifications/${notify.id}` }) // -> /user/123

   }
   
  },

  filters: {
    capitalize: function (value) {
      if (!value) return ''
      value = value.toString()
      return value.charAt(0).toUpperCase() + value.slice(1)
    }
  }
}
</script>

<style lang="scss" scoped>


@import url('https://fonts.googleapis.com/css?family=Roboto:400,500');

* {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  &:before, &:after {
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
  }
}

.notification{
    position:relative
}


.container-notification {
  width: 20rem;
  grid-area: main;
  -ms-flex-item-align: center;
  align-self: center;
  justify-self: center;
  position: absolute;
  right:0
}

h2 {
  font-size: 1.6rem;
  font-weight: 400;
  line-height: 2rem;
  color: #1f2022;
}

ul {
  list-style-type: none;
  padding: 0.5rem 1rem;
  margin: 0 0 0.5rem;
}

li {
  display: inline-block;
  padding: 0.85rem 1rem;
  color: #1f2022;
}

h6 {
  font-size: 1rem;
  font-weight: 500;
  line-height: 1.1;
  margin: 0.45rem 0;
}

a {
  color: #4aaee7;
  background: transparent;
  outline: 0;
  text-decoration: none;
  cursor: pointer;
}

.notification {
  position: absolute;
}

.tooltip-bell {
  position: absolute;
  display: block;
  left: 9rem;
  color: #a5a6a8;
}

.tooltips {
  &::before {
    content: '';
    position: absolute;
    top: -0.4rem;
    right: 8.3rem;
    border-left: 2rem solid transparent;
    border-right: 2rem solid transparent;
    border-bottom: 1.5rem solid #fff;
  }
  position: absolute;
  top: 2.2rem;
  line-height: 1.5;
  color: #27303d;
  width: 20rem;
  max-height: 700px;
  overflow-y: auto;
  background: #fff;
  border-radius: 5px;
  -webkit-box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
}

#circle {
  position: absolute;
  top: 0;
  left: 0.75rem;
  width: 0.75rem;
  height: 0.75rem;
  border-radius: 100%;
  background: #f07379;
}

.notification-item {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: start;
  -ms-flex-align: start;
  align-items: flex-start;
  display: -ms-grid;
  display: grid;
  padding: 0.65rem 0;
}

#heading {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: start;
  -ms-flex-align: start;
  align-items: flex-start;
  display: -ms-grid;
  display: grid;
  padding: 0.5rem 1rem;
  border-bottom: 0.01rem solid #eee;
}

.notification-link {
  position: absolute;
  margin: 0.4rem 0;
}

.heading-left, .img-left {
  -ms-flex-preferred-size: auto;
  flex-basis: auto;
  -webkit-box-flex: 0;
  -ms-flex-positive: 0;
  flex-grow: 0;
  -ms-flex-negative: 0;
  flex-shrink: 0;
  -ms-grid-row: 1;
  grid-row: 1;
  margin: 0 1rem 0 0;
}

.heading-left, .user-content {
  grid-column: span 9;
  width: 14rem;
}

.heading-right, .img-left {
  grid-column: auto;
}

.heading-right, .user-content {
  -ms-flex-preferred-size: auto;
  flex-basis: auto;
  -webkit-box-flex: 1;
  -ms-flex-positive: 1;
  flex-grow: 1;
  -ms-flex-negative: 1;
  flex-shrink: 1;
  -ms-grid-row: 1;
  grid-row: 1;
}

.heading-right {
  width: 2.5rem;
}

.img-left {
  width: 3rem;
}

.user-photo {
  display: inline-block;
  vertical-align: middle;
  height: 3rem;
  width: 3rem;
  margin: 0 0.5rem 0 0;
  border-radius: 50%;
  max-width: 100%;
}

p {
  &.user-info {
    margin: 0.15rem 0 0;
  }
  &.time {
    margin: 0;
    color: #9da4ae;
  }
}

span.name {
  font-weight: 500;
}

.fadeStart-enter-active {
  -webkit-animation: fadeStart .2s both ease-in-out;
  animation: fadeStart .2s both ease-in-out;
}

.fadeStart-leave-active {
  -webkit-animation: fadeEnd .2s both ease-in-out;
  animation: fadeEnd .2s both ease-in-out;
}

[v-cloak] > * {
  display: none;}


@-webkit-keyframes fadeStart {
  0% {
    opacity: 0;
    -webkit-transform: translate3d(0, 5px, 0);
    transform: translate3d(0, 5px, 0);
  }

  to {
    opacity: 1;
    -webkit-transform: translateZ(0);
    transform: translateZ(0);
    display: block;
  }
}


@keyframes fadeStart {
  0% {
    opacity: 0;
    -webkit-transform: translate3d(0, 5px, 0);
    transform: translate3d(0, 5px, 0);
  }

  to {
    opacity: 1;
    -webkit-transform: translateZ(0);
    transform: translateZ(0);
    display: block;
  }
}


@-webkit-keyframes fadeEnd {
  0% {
    opacity: 1;
    -webkit-transform: translateZ(0);
    transform: translateZ(0);
  }

  to {
    opacity: 0;
    -webkit-transform: translate3d(0, 5px, 0);
    transform: translate3d(0, 5px, 0);
  }
}


@keyframes fadeEnd {
  0% {
    opacity: 1;
    -webkit-transform: translateZ(0);
    transform: translateZ(0);
  }

  to {
    opacity: 0;
    -webkit-transform: translate3d(0, 5px, 0);
    transform: translate3d(0, 5px, 0);
  }
}
</style>