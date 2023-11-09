// import './assets/main.css'

// Importing bootstrap CSS and JS
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'

// import 'bootstrap'
// Importing the main App component
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Google Maps
// import VueGoogleMaps from '@fawmi/vue-google-maps'
// import VueGOogleMaps from '@bchewy/vue3-gmaps'
// import VueGoogleMaps from 'vue-google-maps-community-fork'
import VueGoogleMaps from 'bchewy-maps'

// Auth0
import { createAuth0 } from '@auth0/auth0-vue';
import authConfig from "../auth_config.json";

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


// Prima Vue
import PrimeVue from 'primevue/config';
// import VueParallaxJs from 'vue-parallax-js'
// import { MotionPlugin } from '@vueuse/motion'

// AWS
// import AWS from 'aws-sdk';

// AWS.config.update({
// 	region: 'ap-southeast-1',
// 	accessKeyId: `${process.env.VITE_APP_AWS_ACCESS_KEY_ID}`,
// 	secretAccessKey: `${process.env.VITE_APP_AWS_SECRET_ACCESS_KEY}`,
// });



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
// app.use(MotionPlugin)
app.use(PrimeVue);
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(router)
app.mount('#app')