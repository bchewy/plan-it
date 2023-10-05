<template>
	<Navbar />
	<!-- {{ user }} -->
	<!-- <MapItem :userme="user" /> -->

	<div class="container">
		<div class="row">
			<div class="col-12 text-center mt-5">
				<h1>User Profile</h1>
			</div>
		</div>
		<div class="alert alert-info" role="alert">
			You are signed in with Google. Profile editing is disabled.
		</div>
		<div class="row justify-content-center mt-5">
			<!-- User Profile Column -->
			<div class="col-lg-3 col-md-6 col-sm-12 mb-4">
				<div class="card">
					<div class="card-header">
						<h3>{{ user.name }}</h3>
					</div>
					<div class="card-body">
						<div class="text-center mb-3">
							<img :src="user.picture" class="rounded-circle" alt="User profile picture" width="128"
								height="128" />
						</div>
						<div class="mb-3">
							<b>Given Name:</b> {{ user.given_name }}
						</div>
						<div class="mb-3">
							<b>Family Name:</b> {{ user.family_name }}
						</div>
						<div class="mb-3">
							<b>Nickname:</b> {{ user.nickname }}
						</div>
						<div class="mb-3">
							<b>Email:</b> {{ user.email }}
						</div>
						<div class="mb-3">
							<b>Locale:</b> {{ user.locale }}
						</div>
						<div class="mb-3">
							<b>Last Updated:</b> {{ user.updated_at }}
						</div>
					</div>
				</div>
			</div>
			<div class="col-lg-9 col-md-6 col-sm-12 mb-4">
				<div class="card">
					<div class="card-header">
						<h3>Routes</h3>
					</div>
					<div class="card-body">
						<div v-for="route in routes" :key="route.route_id" class="mb-4">
							<h5>{{ route.start_point_name }} to {{ route.end_point_name }}</h5>
							<p><b>Mode of Transport:</b> {{ route.transport_mode }}</p>
							<p><b>Carbon Emission:</b> {{ route.carbon_emission }}</p>
							<p><b>Timestamp:</b> {{ new Date(route.timestamp.$date).toLocaleString() }}</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import MapItem from '../components/MapItem.vue'
import Navbar from '../components/Navbar.vue';
import { useAuth0 } from '@auth0/auth0-vue';
import axios from 'axios';

export default {
	data() {
		const { user, isAuthenticated } = useAuth0();
		console.log('Profile.vue: is authenticated?', isAuthenticated)
		console.log('Profile.vue user', user)
		return {
			user,
			isAuthenticated,
			routes: [],
		}
	},
	components: {
		Navbar,
		MapItem
	},
	created() {
		this.fetchRoutes();
	},
	methods: {
		async fetchRoutes() {
			console.log('Fetching!')
			const email = this.user.email;  // Get the email from user object
			const url = `https://api.bchwy.com/routes/email?email=${encodeURIComponent(email)}`;
			try {
				const response = await axios.get(url);
				this.routes = response.data;  // Assign the fetched routes to the routes data property
			} catch (error) {
				console.error('Error fetching routes:', error);
			}
		}
	}
}

</script>