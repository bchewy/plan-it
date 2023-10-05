<template>
	<nav class="navbar navbar-expand-lg navbar-light bg-light">
		<div class="container">
			<a class="navbar-brand" href="#">
				<font-awesome-icon icon="fa-solid fa-car" bounce style="color: green;" /> Plan-It
			</a>
			<!-- <font-awesome-icon icon="fa-solid fa-user-secret" /> -->

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
						<a class="nav-link" @click.prevent="login">Log in</a>
					</li>
					<!-- <li v-if="!isAuthenticated" class="nav-item">
						<a class="nav-link" @click="signup">Sign up</a>
					</li> -->
					<!-- If user is authenticated -->
					<li v-else class="nav-item dropdown">
						<a class="nav-link dropdown-toggle d-flex align-items-center" href="#" id="navbarDropdown"
							role="button" data-bs-toggle="dropdown" aria-expanded="false">
							<img :src="user.picture" alt="" class="rounded-circle me-2" style="width: 30px; height: 30px;">
							Welcome, {{ user.name }}
						</a>
						<ul class="dropdown-menu" aria-labelledby="navbarDropdown">
							<!-- <li><router-link class="dropdown-item" to="/profile">User Profile</router-link></li>
							<li><router-link class="dropdown-item" to="/journey">Journey</router-link></li> -->
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
import { watch, computed, defineComponent } from 'vue';
import { useStore } from 'vuex';


export default defineComponent({
	name: 'NavBar',
	setup() {
		const { loginWithRedirect, user, isAuthenticated, logout } = useAuth0();

		return {
			login: async () => {
				console.log('Login button clicked');
				try {
					await loginWithRedirect();
				} catch (e) {
					console.error('Failed to login:', e);
				}
			},
			logout: () => {
				logout({ logoutParams: { returnTo: window.location.origin } });
				// store.dispatch('updateUser', null);
			},
			// user: computed(() => store.getters.user),
			user,
			isAuthenticated,
			// isAuthenticated: computed(() => store.getters.isAuthenticated),
		};
	}
});

</script>
