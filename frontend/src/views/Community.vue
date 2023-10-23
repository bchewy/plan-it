

<template>
<head>
	<link rel="stylesheet" href="community_css.css">
</head>
	<header>
		<!-- nav -->
		<NavBar />

	</header>
    <body>
<nav class="navbar sidebarbackground">

<div class="container-fluid">

  <ul class="navbar-nav">
	<li class="nav-item">
	  <a class="nav-link" href="#">For you page</a>
	</li>
	<li class="nav-item">
	  <a class="nav-link" href="#">Your groups</a>
	</li>
	<li class="nav-item">
	  <a class="nav-link" href="#">Your friends</a>
	</li>
  </ul>
</div>

</nav>

    
        
	

    
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
