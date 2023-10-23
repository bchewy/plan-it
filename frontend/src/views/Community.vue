<template>

		<!-- nav -->
		<NavBar />


<body class="position-relative" >
<div class="container-fluid">
<div class="row">

<nav class="col-2 position-fixed h-100"  style="background-color: rgb(209, 244, 209)">
	
	<div class="container-fluid">
		<br>
		<span class="h5 text-muted">Plan-it Community</span>
		
	<ul class="navbar-nav flex-column mt-5">
	
    <li class="active nav-item"><a class="h3 nav-link" href="#">For you</a></li>
	<hr>
    <li class="nav-item dropdown"><a class="h3 nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown">Groups</a>
	<ul class="dropdown-menu">
		<li><font-awesome-icon icon="fa-solid fa-plus"/><a class="dropdown-item" href="#">  Create group</a></li>
		<li><font-awesome-icon icon="fa-solid fa-users"/><a class="dropdown-item" href="#">  Your groups</a></li>
	</ul>
	</li>
	<hr>
    <li class="nav-item"><a class="h3 nav-link" href="#">Friends</a></li>
	<hr>

</ul>
	</div>
</nav>
<div class="col-2"></div>
<div class="col-10 h-100" style="background-color: rgb(232, 251, 240);">
	
<h1 class="text-center py-3 text-muted" style="font-weight: bold;">For you page</h1>
<div class="row justify-content-center">
<div class="col-8 rounded border bg-white">
	<input type="text" class="my-3 form-control" placeholder="Share something with the community!">
	<div class="row mb-3 justify-content-between">
	<span class="col-1"></span>
	
	<button class="btn btn-secondary col-3" type="button"><font-awesome-icon icon="fa-solid fa-share"/>  Share a badge</button>
	<button class="btn btn-secondary col-3" type="button"><font-awesome-icon icon="fa-solid fa-tag"/>  Tag a friend</button>
	<button class="btn btn-secondary col-3" type="button"><font-awesome-icon  icon="fa-solid fa-plus-square"/>  Create post!</button>
	<span class="col-1"></span>
	</div>

</div>
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
