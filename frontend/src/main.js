import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Google Maps
import VueGoogleMaps from 'bchewy-maps'

// Auth0
import { createAuth0 } from '@auth0/auth0-vue';

// animations
import 'animate.css'
import './components/likebuttontest.scss'

// Font Awesome
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faArrowRightFromBracket, faCar, faCircleUser, faTruckFast, faCog } from '@fortawesome/free-solid-svg-icons'
import { faPlusSquare, faShare, faTag, faPlus, faUsers, faUser } from '@fortawesome/free-solid-svg-icons'
import { faLeaf, faShoePrints, faBus, faHouse, faBars, faUserGroup, faPeopleGroup } from '@fortawesome/free-solid-svg-icons';
library.add(faCar)
library.add(faCircleUser)
library.add(faTruckFast)
library.add(faArrowRightFromBracket)
library.add(faCog)
library.add(faPlusSquare)
library.add(faPlus)
library.add(faShare)
library.add(faTag)
library.add(faUsers)
library.add(faUser)
library.add(faLeaf)
library.add(faShoePrints)
library.add(faBus)
library.add(faHouse)
library.add(faBars)
library.add(faUserGroup)
library.add(faPeopleGroup)

import PrimeVue from 'primevue/config';



const app = createApp(App)
app.use(VueGoogleMaps, {
	load: {
		key: `${import.meta.env.VITE_GMAPS_API_KEY}`,
		libraries: "places",
		componentRestrictions: {
			country: "SG"
		}
	}
})
app.use(
	createAuth0({
		domain: `${import.meta.env.VITE_AUTH0_DOMAIN}`,
		clientId: `${import.meta.env.VITE_AUTH0_CLIENTID}`,
		authorizationParams: {
			redirect_uri: window.location.origin,
		}
	})
);
app.use(PrimeVue);
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(router)
app.mount('#app')