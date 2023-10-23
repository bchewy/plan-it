<template>

		<!-- nav -->
		<NavBar />


<body class="position-relative"  style="background-color: rgb(232, 251, 240);">
<div class="container-fluid">
<div class="row">

<nav class="col-2 position-fixed h-100"  style="background-color: rgb(209, 244, 209)">
	
	<div class="container-fluid">
		<br>
		<span class="navbar-text h2 text-muted">Menu</span>
	<ul class="navbar-nav flex-column mt-3">
	
    <li class="active nav-item"><a class="nav-link" href="#">For you page</a></li>
	<hr>
    <li class="nav-item"><a class="nav-link" href="#">Groups</a></li>
	<hr>
    <li class="nav-item"><a class="nav-link" href="#">Friends</a></li>
	<hr>

</ul>
	</div>
</nav>
<div class="col-2"></div>
<div class="col-10 h-100">
<h1 class="text-center pb-2 text-muted">Plan-it Community</h1>
<div class="col-8 rounded">
	<input type="text" class="form-control" placeholder="Share something with the community!">
	
</div>
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
