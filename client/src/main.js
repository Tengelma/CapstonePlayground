import Vue from 'vue'
import App from './App.vue'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import axios from 'axios'
import fs from 'fs'

Vue.use(VueMaterial)
Vue.config.productionTip = false
Vue.prototype.$http = axios
Vue.use(fs)

new Vue({
  render: h => h(App),
}).$mount('#app')
