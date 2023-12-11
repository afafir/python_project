import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import BootstrapVue from "bootstrap-vue";
import VueFilterDateFormat from '@vuejs-community/vue-filter-date-format';
import VueFilterDateParse from '@vuejs-community/vue-filter-date-parse';
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Vuex from 'vuex';
import setupInterceptors from "@/services/setupInterceptors";
import {library} from "@fortawesome/fontawesome-svg-core";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {faTelegram, faVk} from "@fortawesome/free-brands-svg-icons";
import {faEnvelope} from "@fortawesome/free-solid-svg-icons";


Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(VueFilterDateFormat);
Vue.use(VueFilterDateParse);
Vue.use(Vuex)
Vue.component('font-awesome-icon', FontAwesomeIcon);
library.add(faTelegram, faVk, faEnvelope);

setupInterceptors(store);
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
