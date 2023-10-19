// import './assets/main.css'

// Importing bootstrap CSS and JS
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'

// Importing the main App component
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Google Maps
import VueGoogleMaps from '@fawmi/vue-google-maps'

// Auth0
import { createAuth0 } from '@auth0/auth0-vue';
import authConfig from "../auth_config.json";

// Font Awesome
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faArrowRightFromBracket, faCar, faCircleUser, faTruckFast } from '@fortawesome/free-solid-svg-icons'
library.add(faCar)
library.add(faCircleUser)
library.add(faTruckFast)
library.add(faArrowRightFromBracket)

// Prima Vue
import PrimeVue from 'primevue/config';



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
app.use(
	createAuth0({
		domain: authConfig.domain,
		clientId: authConfig.clientId,
		authorizationParams: {
			redirect_uri: window.location.origin,
		}
	})
);
app.use(PrimeVue);

app.component('font-awesome-icon', FontAwesomeIcon)
app.use(router)
app.mount('#app')