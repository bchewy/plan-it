// import './assets/main.css'

// Importing bootstrap CSS and JS
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'

// Importing the main App component
import { createApp } from 'vue'
import App from './App.vue'
import router from './router' // The router is for navigating to other pages
import VueGoogleMaps from '@fawmi/vue-google-maps'
import { createAuth0 } from '@auth0/auth0-vue';



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
		domain: "bchewy.auth0.com",
		clientId: "YlYuClzH0InCceiP77CP230U9AHuMp2j",
		authorizationParams: {
			redirect_uri: window.location.origin
		}
	})
);

app.use(router)
app.mount('#app')
