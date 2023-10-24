<template>
	<header>
	  <!-- nav -->
	  <NavBar />
	</header>
  
	<!--showcase-->
	<section class="text-center col-12 m-0 p-0">
  <div class="container" style="background-color: rgb(209, 244, 209);">
    <h1>Plan-It!<br> Stay <span class="text-success"> Sustainable </span> . </h1>
  </div>
</section>

<!-- signup now-->
<section class="bg-success text-light">
  <div class="container">
    <div class="d-md-flex justify-content-between align-items-center mb-3 mb-md-0">
      <p class="news-input">Refer a friend now!</p> <!-- Apply the "news-input" class -->
      <div class="input-group news-input">
        <input
          type="text"
          class="form-control news-input" <!-- Apply the "news-input" class to adjust the width -->
          placeholder="Friend's Email Address"
          aria-label="Friend's Email Address"
          aria-describedby="button-addon2">
        <button class="btn btn-lg" <!-- Adjust button sizing as needed -->
          type="button"
          id="button-addon2">Send</button>
      </div>
    </div>
  </div>
</section>


  
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

<style scoped>
/* Other component-specific styles */

.news-input {
  width: 50%; /* Set the width to 50% */
}

/* Additional styles if needed */
</style>
