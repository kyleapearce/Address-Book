import Vue from 'vue';
import Router from 'vue-router';
import Contacts from '../components/Contacts.vue';
import Ping from '../components/Ping.vue';

Vue.use(Router);

// deploy different components to be used at different pages
export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Contacts',
      component: Contacts,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
