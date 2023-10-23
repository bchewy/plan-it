<template>
	<header>
		<!-- nav -->
		<NavBar />

	</header>
    <body>
<div class="container-fluid">
<div class="row">
<nav class="col-3 position-fixed"  style="background-color: rgb(177, 237, 177)">
	<div class="container-fluid">
	<ul class="navbar-nav flex-column">
    <li class="active nav-item"><a href="#">For you page</a></li>
    <li class="nav-item"><a href="#">Your groups</a></li>
    <li class="nav-item"><a href="#">Your friends</a></li>

</ul>
	</div>
</nav>
<div class="col-9">
<h1 class="page-header">Community</h1>
</div>
</div>
</div>

    
        
	

    
    </body>
	<footer>
		<!-- footer -->
	</footer>
</template>
<script>

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
