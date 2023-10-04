// import './assets/main.css'

// Importing bootstrap CSS and JS
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'

// Importing the main App component
import { createApp } from 'vue'
import App from './App.vue'
import router from './router' // The router is for navigating to other pages
import VueGoogleMaps from '@fawmi/vue-google-maps'



const app = createApp(App)
app.use(VueGoogleMaps, {
	load: {
		key: "AIzaSyC6xTDY_NrDH0U1NSE2Ug6AnzuVsbRPFYM",
		libraries: "places",
		componentRestrictions: {
			country: "SG"
		}
	}
})
app.use(router)
app.mount('#app')
