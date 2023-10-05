<template>
	<nav class="navbar navbar-expand-lg navbar-light bg-light">
		<div class="container">

			<a class="navbar-brand" href="#">Carbon-First</a>

			<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
				aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
				<span class="navbar-toggler-icon"></span>
			</button>

			<div class="collapse navbar-collapse" id="navbarNav">
				<ul class="navbar-nav">
					<li class="nav-item">
						<router-link class="nav-link" to="/">Home</router-link>
					</li>
					<li class="nav-item">
						<router-link class="nav-link" to="/route">Routing</router-link>
					</li>
					<!-- Login tiems here -->
					<li v-if="!isAuthenticated" class="nav-item">
						<a class="nav-link" @click="login">Log in</a>
					</li>
				</ul>
			</div>

		</div>
	</nav>
</template>
<script>
import { useAuth0 } from '@auth0/auth0-vue';

export default {
	name: 'NavBar',
	setup() {
		const { loginWithRedirect, user, isAuthenticated } = useAuth0();

		console.log('Setup method is called');

		return {
			login: async () => {
				console.log('Login button clicked');
				try {
					await loginWithRedirect();
					console.log('User:', user);
					console.log('Authenticated:', isAuthenticated);
				} catch (e) {
					console.error('Failed to login:', e);
				}
			},
			user,
			isAuthenticated,
		};
	}
}
</script>