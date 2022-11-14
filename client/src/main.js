import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import VueMask from 'v-mask';
import 'bootstrap/dist/css/bootstrap.css';

// to enable use on Vue
Vue.use(BootstrapVue);
Vue.use(VueMask);

Vue.config.productionTip = false;

// basic startup
new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
