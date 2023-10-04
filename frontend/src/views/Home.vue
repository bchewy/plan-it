<template>
	<header>
		<!-- nav -->
		<NavBar />

	</header>

	Welcome Home.
	<button @click="login">Log in</button>
	<button @click="register">Register</button>

	<footer>
		<!-- footer -->
	</footer>
</template>
<script>
import NavBar from '../components/Navbar.vue'
import { useAuth0 } from '@auth0/auth0-vue';

export default {
	name: 'Home',
	components: {
		NavBar  // Register the NavBar component
	},
	setup() {
		const { loginWithRedirect } = useAuth0();

		return {
			login: () => {
				loginWithRedirect();
			}
		};
	}
}
</script>