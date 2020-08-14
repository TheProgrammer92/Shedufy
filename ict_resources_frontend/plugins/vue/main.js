import Vue from 'vue'
import { Datetime } from 'vue-datetime'
// You need a specific loader for CSS files
import 'vue-datetime/dist/vue-datetime.css'

import xmodal from "xmodal-vue";
// install xmodal


import PrettyCheckbox from 'pretty-checkbox-vue';

Vue.use(PrettyCheckbox);
Vue.use(xmodal);



Vue.use(Datetime)