<template>
		<!-- nav -->
		<NavBar />


<body class="position-relative" >
<div class="container-fluid">
<div class="row">

<div class=" text-center" style="margin-bottom:0">
  <h1>PLAN-IT!</h1>
  <p>Singapore's Best Carbon-efficient Travel Planner</p> 
</div>


</div>
</div>
</body>
	<footer>
		<!-- footer -->
	</footer>
</template>


<script>
import NavBar from '../components/Navbar.vue'
// import Login from '../components/Login.vue'
import { useAuth0 } from '@auth0/auth0-vue';

export default {
	name: 'Home',
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