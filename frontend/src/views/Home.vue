<template>
	<header>
	  <!-- nav -->
	  <NavBar />
	</header>
  
	<!--showcase-->
	<section class="text-center col-12 m-0 p-0">
  <div class="container" style="background-color: rgb(209, 244, 209);">
    <h1>Plan-It!</h1>
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
          class="form-control news-input" 
          placeholder="Friend's Email Address"
          aria-label="Friend's Email Address"
          aria-describedby="button-addon2">
        <button class="btn btn-lg" 
          id="button-addon2">Send</button>
      </div>
    </div>
  </div>
</section>

<!--flexbox thingy!-->
<section class="text-muted p-5 text-center">
	<div class = "container">
		<div class = "d-sm-flex">
			<div>
				<h1><span class= "text-success">Carbon-First </span> Routing.</h1>
				<p class= "lead">
					Account for your own carbon footprint for your traffic taken, value-add and commit to reducing your carbon footprint and reduce your personal impact.
				</p>
			</div>
			<img class="img-fluid w-50" src = "frontend/src/assets/Homepage pictures/ehotel_Co2-Fussabdruck-header_750x500-750x500.jpg" alt="">
		</div>
	</div>
    <h1>Plan-It!</h1>
</section>

<!--Boxes-->
<section class="p-5">
	<div class = "container">
		<div class= "row text-center">
			<div class = "col-md">
				<div class = "card text-muted" style = "outline-color: darkgreen;">
				<div class = "card-body text-center">
					<div class="h1 mb-3>">
					<font-awesome-icon icon="fa-solid fa-leaf"></font-awesome-icon>
				</div>
				<h3 class = "card-title mb-3">
					Eco-friendly Navigation
				</h3>
				<p class="card-text">
					this is so great and green! change writeup at the end.
				</p>
				<a href = "#" class = "btn btn-success"> Learn More</a>
				</div>
				</div>
			</div>
			<div class = "col-md">
				<div class = "card text-muted" style = "outline-color: darkgreen;">
				<div class = "card-body text-center">
					<div class="h1 mb-3>">
					<font-awesome-icon icon="fa-solid fa-shoe-prints"></font-awesome-icon>
				</div>
				<h3 class = "card-title mb-3">
					Traffic Optimisation
				</h3>
				<p class="card-text">
					This reduces our carbon footprint.
				</p>
				<a href = "#" class = "btn btn-success"> Learn More</a>
				</div>
				</div>
			</div>

			<div class = "col-md">
				<div class = "card text-muted" style = "outline-color: darkgreen;">
				<div class = "card-body text-center">
					<div class="h1 mb-3>">
						<font-awesome-icon icon="fa-solid fa-bus"></font-awesome-icon>
				</div>
				<h3 class = "card-title mb-3">
					Incentivising Public Transport
				</h3>
				<p class="card-text">
					Encourages more people to take the public transport through badges.
				</p>
				<a href = "#" class = "btn btn-success"> Learn More</a>
				</div>
				</div>
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
