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
	<ul class="dropdown-menu bg-light">
		<li><a class="dropdown-item" href="https://wad2.bchwy.com/createGroup"><font-awesome-icon icon="fa-solid fa-plus"/>   Create group</a></li>
		<li><a class="dropdown-item" href="https://wad2.bchwy.com/yourGroups"><font-awesome-icon icon="fa-solid fa-users"/>   Your groups</a></li>
	</ul>
	</li>
	<hr>
    <li class="nav-item"><a class="h3 nav-link" href="https://wad2.bchwy.com/friendCommunity">Friends</a></li>
	<hr>

</ul>
	</div>
</nav>
<div class="col-2"></div>
<div class="col-10 h-100" style="background-color: rgb(232, 251, 240);">
	
<h1 class="text-center py-3 text-muted" style="font-weight: bold;">For You Page</h1>
<div class="row justify-content-center">
<div class="col-8 rounded border bg-white">
	<textarea class="my-3 form-control" placeholder="Share something with the community!"></textarea>
	<div class="row mb-3 justify-content-between">
	<span class="col-1"></span>
	
	<button class="btn btn-secondary col-3" type="button" @click="badges=!badges"><font-awesome-icon icon="fa-solid fa-share"/>  Share a badge</button>
	<Share_badge></Share_badge>
	<button class="btn btn-secondary col-3" type="button"><font-awesome-icon icon="fa-solid fa-tag"/>  Tag a friend</button>
	<button class="btn btn-secondary col-3" type="button"><font-awesome-icon  icon="fa-solid fa-plus-square"/>  Create post!</button>
	<span class="col-1"></span>
	</div>

</div>
</div>

<div class="row justify-content-center mt-5">

	<div class="col-8 rounded border bg-white"><font-awesome-icon icon="fa-solid fa-user" class="mt-3"></font-awesome-icon> User<br><br>
	<p>Post text</p></div>

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

import Share_badge from "../components/Share_badge.vue";
export default {
	name: 'Community',
	data(){

	},
	components: {
		NavBar,  // Register the NavBar component
		// Login
		Share_badge
	},
	setup() {
		const { loginWithRedirect, user, isAuthenticated } = useAuth0();
		const badges=false

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
			badges
		};
	}
}
</script>
