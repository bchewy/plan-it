<template>
	<header>
		<!-- nav -->
		<NavBar />

	</header>
    <body>
<div class="container-fluid">
<div class="row">
<div class="sidebar" style="width:180px">
<ul class="nav nav-sidebar">
    <li class="active"><a href="#">For you page</a></li>
    <li><a href="#">Your groups</a></li>
    <li><a href="#">Your friends</a></li>

</ul>
</div>
<div class="col-sm-12 main">
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
