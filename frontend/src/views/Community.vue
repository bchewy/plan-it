<template>
	<header>
		<!-- nav -->
		<NavBar />

	</header>
    <body>
	<div class="container-fluid">
		<div class="card flex justify-content-center">
    <Sidebar v-model:visible="visible">
        <h2>Community</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
    </Sidebar>
    <Button icon="pi pi-arrow-right" @click="visible = true" />
		</div>

	

				</div>

    
        
	

    
    </body>
	<footer>
		<!-- footer -->
	</footer>
</template>
<script>
import { createApp } from 'vue';
import PrimeVue from 'primevue/config';
import Sidebar from 'primevue/sidebar';
const app = createApp(App);
app.use(PrimeVue);
import NavBar from "../components/Navbar.vue";
// import Login from '../components/Login.vue'
import { useAuth0 } from '@auth0/auth0-vue';

export default {
	name: 'Community',
	components: {
		NavBar,  // Register the NavBar component
		// Login
	},
	setup() {
		const { loginWithRedirect, user, isAuthenticated } = useAuth0();

		console.log('Setup method is called');

		return {
			login: async () => {
				console.log('Login button clicked');
				try {
					await loginWithRedirect();
					// console.log('User:', user);
					// console.log('Authenticated:', isAuthenticated);
				} catch (e) {
					alert('Failed to login');
					console.error('Failed to login:', e);
				}
			},
			user,
			isAuthenticated,
		};
	}
}
</script>
