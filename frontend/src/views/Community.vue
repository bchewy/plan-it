<template>

		<!-- nav -->
		<NavBar />
<div v-if="isLoading || !isAuthenticated" class="loading-screen">
    <div v-if="isLoading">Loading...</div>
    <div v-else class="row justify-content-center align-items-center" style="height: 100vh">
      <h3 class="text-center p-5">Please log in to use this feature</h3>
    </div>
  </div>

<div v-else class="position-relative" >
<div class="container-fluid">
<div class="row">

<nav class="col-2 position-fixed h-100"  style="background-color: rgb(209, 244, 209)">
	
	<div class="container-fluid">
		<br>
		<span class="h5 text-muted">Plan-it Community</span>
		
	<ul class="navbar-nav flex-column mt-5">
	
    <li class="active nav-item"><router-link class="h3 nav-link" to="/community">For you</router-link></li>
	<hr>
    <li class="nav-item dropdown"><a class="h3 nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown">Groups</a>
	<ul class="dropdown-menu bg-light">
		<li><router-link class="dropdown-item" to="/community/createGroup" ><font-awesome-icon icon="fa-solid fa-plus"/>   Create group</router-link></li>
		<li><router-link class="dropdown-item" to="/community/yourGroups" ><font-awesome-icon icon="fa-solid fa-users"/>   Your groups</router-link></li>
	</ul>
	</li>
	<hr>
    <li class="nav-item"><router-link class="h3 nav-link" to="/community/friendCommunity">Friends</router-link></li>
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
	<heart_btn></heart_btn><p>Post text</p></div>

</div>


</div>

</div>
</div>




    
        
	

    
</div>
	<footer>
		<!-- footer -->
	</footer>
</template>
<script>

import NavBar from "../components/Navbar.vue";
// import Login from '../components/Login.vue'
import { useAuth0 } from '@auth0/auth0-vue';
import heart_btn from "../components/like_button.vue";
import Share_badge from "../components/Share_badge.vue";
export default {
	name: 'Community',
	data(){

	},
	components: {
		NavBar,  // Register the NavBar component
		// Login
		Share_badge,
		heart_btn
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
