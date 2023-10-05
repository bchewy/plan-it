<template>
	<nav class="navbar navbar-expand-lg navbar-light bg-light">
		<div class="container">

			<a class="navbar-brand" href="#">PlanIt</a>

			<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
				aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
				<span class="navbar-toggler-icon"></span>
			</button>

			<div class="collapse navbar-collapse" id="navbarNav">
				<ul class="navbar-nav me-auto">
					<li class="nav-item">
						<router-link class="nav-link" to="/">Home</router-link>
					</li>
					<li class="nav-item">
						<router-link class="nav-link" to="/route">Routing</router-link>
					</li>
				</ul>
				<ul class="navbar-nav">
					<!-- If user is not authenticated -->
					<li v-if="!isAuthenticated" class="nav-item">
						<a class="nav-link" @click="login">Log in</a>
					</li>
					<li v-if="!isAuthenticated" class="nav-item">
						<a class="nav-link" @click="signup">Sign up</a>
					</li>
					<!-- If user is authenticated -->
					<li v-else class="nav-item dropdown">
						<a class="nav-link dropdown-toggle d-flex align-items-center" href="#" id="navbarDropdown"
							role="button" data-bs-toggle="dropdown" aria-expanded="false">
							<img :src="user.picture" alt="User Image" class="rounded-circle me-2"
								style="width: 30px; height: 30px;">
							Welcome, {{ user.name }}
						</a>
						<ul class="dropdown-menu" aria-labelledby="navbarDropdown">
							<li><router-link class="dropdown-item" to="/profile">User Profile</router-link></li>
							<li><router-link class="dropdown-item" to="/journey">Journey</router-link></li>
							<li>
								<hr class="dropdown-divider">
							</li>
							<li><a class="dropdown-item" @click="logout">Logout</a></li>
						</ul>
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

		// console.log(user);

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