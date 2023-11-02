<style scoped>
.profile-container {
	box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.bg-supergreen {
	background-color: #739072;
}

.nav-pills .nav-link.active {
	background-color: #4F6F52;
	/* Replace with the background color you want */
	color: #ECE3CE;
	/* Replace with the text color you want */
}

.nav-pills .nav-link {
	/* background-color: ; */
	color: #ECE3CE;
}

.nav-pills .nav-item {
	margin-bottom: 20px;
}

.container-fluid {
	min-height: 100vh;
	padding-top: 3rem;
	background-color: #739072;
}

.pr-4.pb-3.pb-md-0 {
	flex: 2;
	/* Adjust as needed */
}
</style>

<template>
	<keep-alive>
		<Navbar />
	</keep-alive>
	<!-- <Navbar /> -->
	<div class="container-fluid pt-3 bg-supergreen pb-3">
		<div class="row">
			<div class="col-lg-12">
				<div class="card">
					<div class="card-header">
						<h4 class="card-title">Invalid Routes</h4>
					</div>
					<div class="card-body">
						<div class="table-responsive">
							<table class="table table-striped">
								<thead>
									<tr>
										<!-- <th>Route ID</th> -->
										<!-- <th>Time</th> -->
										<th>Start Location</th>
										<th>End Location</th>
										<!-- <th>Distance</th> -->
										<th>Carbon Emission</th>
										<th>Transport Mode</th>
										<th>Validated</th>
										<th>Checked Start Location</th>
									</tr>
								</thead>
								<tbody v-if="routes">
									<tr v-for=" route  in  routes " :key="route.id">
										<td>{{ route.start_point_name }}</td>
										<td>{{ route.end_point_name }}</td>
										<td>{{ route.carbon_emission }}</td>
										<td>{{ route.transport_mode }}</td>
										<td>
											{{ route.validated }}
											<button @click="checkEndLocation(route)">Check Location</button>
										</td>
										<td>{{ route.checkedStartLocation }}</td>
									</tr>
								</tbody>
							</table>
						</div>
					</div>
				</div>


				<!-- Success Modal template -->
				<div class="modal fade" id="modalGood" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
					<div class="modal-dialog">
						<div class="modal-content">
							<div class="modal-header">
								<h5 class="modal-title" id="exampleModalLabel">Congratulations!</h5>
								<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
							</div>
							<div class="modal-body">
								You have validated this route. EXP has been added into your profile.
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-success" data-bs-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
				<!-- Failure Modal template -->
				<div class="modal fade" id="modalBad" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
					<div class="modal-dialog">
						<div class="modal-content">
							<div class="modal-header">
								<h5 class="modal-title" id="exampleModalLabel">Uh oh!</h5>
								<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
							</div>
							<div class="modal-body">
								You don't seem to be telling the truth...
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>


	</div>
</template>

<script>
import MapItem from "../components/MapItem.vue";
import AddFriend from "../components/AddFriends.vue";
import Navbar from "../components/Navbar.vue";
import FriendRequest from '../components/FriendRequest.vue';
import Badges from '../components/Badges.vue';
import { useAuth0 } from "@auth0/auth0-vue";
import axios from "axios";
// import { Chart, registerables } from 'chart.js/auto';
// import 'chartjs-adapter-date-fns';
// import { format } from 'date-fns';
import { ref, defineComponent, computed, reactive } from "vue";
import { UseGeolocation } from '@vueuse/components'
import { useGeolocation } from '@vueuse/core'
import Modal from 'bootstrap/js/dist/modal';

// Chart.register(...registerables);

export default {
	components: {
		UseGeolocation,
	},
	created() {
		this.fetchData();

	},
	watch: {

	},
	data() {
		const { user, isAuthenticated } = useAuth0();
		const userExp = ref(0);
		const expToNextLevel = ref(0);
		const userLvl = ref(0)
		const users = [];
		const { coords, locatedAt, error, resume, pause } = useGeolocation()
		// const { latitude, longitude } = coords;

		return {
			users,
			userExp,
			expToNextLevel,
			userLvl,
			activeTab: 'profile',
			isLoading: false,
			currentPage: 1,
			itemsPerPage: 3,
			user,
			isAuthenticated,
			routes: [],
			friends: [],
			friendRequests: [],
			receivedRequests: [],
			sentRequests: [],
			coords,
		};
	},
	computed: {
		// For pagination
		paginatedRoutes() {
			const start = (this.currentPage - 1) * this.itemsPerPage;
			const end = start + this.itemsPerPage;
			return this.routes.slice(start, end);
		},
		// Total pages
		totalPages() {
			return Math.ceil(this.routes.length / this.itemsPerPage);
		},
	},
	components: {
		Navbar,
		MapItem,
		AddFriend,
		FriendRequest,
		Badges,
	},
	methods: {
		fetchData() {
			this.fetchUsers();
			this.fetchRoutes();
			// this.fetchRoutes().then(() => {
			// 	this.drawChart();
			// });
			// this.fetchUser();
			// this.fetchFriendRequests();
		},
		haversineDistance(coords1, coords2, isMiles = false) {
			function toRad(x) {
				return x * Math.PI / 180;
			}

			var lon1 = coords1[1];
			var lat1 = coords1[0];

			var lon2 = coords2[1];
			var lat2 = coords2[0];

			var R = 6371; // km

			var x1 = lat2 - lat1;
			var dLat = toRad(x1);
			var x2 = lon2 - lon1;
			var dLon = toRad(x2)
			var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
				Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) *
				Math.sin(dLon / 2) * Math.sin(dLon / 2);
			var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
			var d = R * c;

			if (isMiles) d /= 1.60934;

			return d;
		},

		async fetchUser() {
			const url = `${import.meta.env.VITE_API_ENDPOINT}/users/iz/${encodeURIComponent(this.user.email)}`;
			const headers = {
				"x-api-key": "PlanItIsTheBestProjectEverXYZ",
			};

			try {
				const response = await axios.get(url, { headers });
				this.friends = response.data.friends;
				this.userLvl = response.data.level;
				this.userExp = response.data.exp;

			} catch (error) {
				console.error("Error fetching user", error);
			}
		},
		async fetchFriendRequests() {
			const url = `${import.meta.env.VITE_API_ENDPOINT}/users/${encodeURIComponent(this.user.email)}/friend_requests`;
			const headers = {
				"x-api-key": "PlanItIsTheBestProjectEverXYZ",
			};

			try {
				const response = await axios.get(url, { headers });
				this.receivedRequests = response.data.received;
				this.sentRequests = response.data.sent;

			} catch (error) {
				console.error("Error fetching friend requests", error);
			}

		},
		async fetchRoutes() {
			const email = this.user.email; // Get the email from user object
			const url = `${import.meta.env.VITE_API_ENDPOINT}/routes/email?email=${encodeURIComponent(email)}`;
			const headers = {
				"x-api-key": "PlanItIsTheBestProjectEverXYZ", // Replace with your actual API key
			};
			try {
				const response = await axios.get(url, { headers });
				const unvalidatedRoutes = response.data.filter(route => !route.validated);
				this.routes = unvalidatedRoutes.reverse(); // Assign the fetched routes to the routes data property
			} catch (error) {
				console.error("Error fetching routes:", error);
			}
		},
		async fetchUsers() {
			const url = `${import.meta.env.VITE_API_ENDPOINT}/users`;
			const headers = {
				"x-api-key": "PlanItIsTheBestProjectEverXYZ",
			};

			try {
				const response = await axios.get(url, { headers });
				this.users = response.data;
			} catch (error) {
				console.error("Error fetching users:", error);
			}
		},
		// This method is only used to validate a route
		async updateRoute(routeId) {
			const url = `${import.meta.env.VITE_API_ENDPOINT}/routes/${routeId}/validate`;
			const headers = {
				"x-api-key": "PlanItIsTheBestProjectEverXYZ", // Replace with your actual API key
			};
			try {
				const response = await axios.put(url, {}, { headers });
				return response.data;
			} catch (error) {
				console.error("Error updating route:", error);
			}
		},

		calculateCarbonEmissionForEXP(distance, travelMode) {
			const distanceInKm = distance
			let carbonEmissionPerKm;
			switch (travelMode) {
				case 'driving':
					carbonEmissionPerKm = 0.12;  // Assume 0.12 kg CO2 emitted per km for a car
					break;
				case 'BICYCLE':
					carbonEmissionPerKm = 0;
					break;
				case 'WALK':
					carbonEmissionPerKm = 0;
					break;
				case 'TRANSIT':
					carbonEmissionPerKm = 0;
					break
				default:
					carbonEmissionPerKm = 0.12;  // Default to car emission if travel mode is not recognized


					const carbonFootprintDriving = distanceInKm * 0.12;
					const carbonFootprint = distanceInKm * carbonEmissionPerKm;
					return [carbonFootprint, carbonFootprintDriving];
			}
		},
		addExpBasedOnCarbonEmission(carbonList) {
			const emissionSavings = ref(0);
			emissionSavings.value = carbonList[1] - carbonList[0];
			const BASE_EXP = 10; // is 1 on the routing page
			const BONUS_EXP_PER_SAVED_KG = 1; // is 1 on the routing page

			// Calculate the total EXP to add based on the base EXP and the bonus for saved emissions
			const expToAdd = Math.ceil(BASE_EXP + (emissionSavings.value * BONUS_EXP_PER_SAVED_KG));
			expAdded.value = expToAdd


			axios.post(`${import.meta.env.VITE_API_ENDPOINT}/users/${user.value.email}/carbonsavings`, { carbonsavings: emissionSavings.value }, {
				headers: {
					'X-Api-Key': 'PlanItIsTheBestProjectEverXYZ'
				}
			})
				.then(response => {
					console.log(response.data.message);
					logUserActivity(`saved :${emissionSavings.value} co2`)
				})
				.catch(error => {
					console.error(error);
				});

			// Update the user exp in the backend
			axios.post(`${import.meta.env.VITE_API_ENDPOINT}/users/${user.value.email}/exp`, { exp: expToAdd }, {
				headers: {
					'X-Api-Key': 'PlanItIsTheBestProjectEverXYZ'
				}
			})
				.then(response => {
					console.log(response.data.message);
					logUserActivity(`gained ${expToAdd} exp`)
				})
				.catch(error => {
					console.error(error);
				});
		},
		checkEndLocation(route) {
			const { latitude, longitude } = this.coords;

			// Get the route's end location
			const [endLat, endLng] = route.end_point_lat_lng.split(', ').map(Number);

			// Calculate the distance between the two locations in kilometers
			const distance = this.haversineDistance([latitude, longitude], [endLat, endLng]);

			// Check if the distance is less than 0.5 kilometers (500 meters)
			if (distance < 0.5) {
				console.log('User is within 500 meters of the end location');
				var myModalEl = document.getElementById('modalGood');
				var myModal = new Modal(myModalEl);
				myModal.show();

				// Update the route to validated true:
				this.updateRoute(route.route_id, true)
				// Remove route from routes array
				this.routes = this.routes.filter(r => r.route_id !== route.route_id);

				// Final addition for EXP
				this.addExpBasedOnCarbonEmission(this.calculateCarbonEmissionForEXP(route.distance, route.transport_mode))

			} else {
				console.log('User is not within 500 meters of the end location');
				var myModalEl = document.getElementById('modalBad');
				var myModal = new Modal(myModalEl);
				myModal.show();
			}

			myModalEl.addEventListener('hidden.bs.modal', function () {
				// When the modal is hidden, remove the 'modal-open' class from the body
				document.body.classList.remove('modal-open');
				// Remove padding-right added by Bootstrap modal
				document.body.style.removeProperty('padding-right');
				// Remove padding-right from fixed navbar if exists
				let fixedNavbar = document.querySelector('.navbar.fixed-top');
				if (fixedNavbar) {
					fixedNavbar.style.removeProperty('padding-right');
				}
			});


			// if (route.end_point_name === `${latitude}, ${longitude}`) {
			// 	console.log('User is at the end location');
			// } else {
			// 	console.log('users current coords', this.coords.latitude, this.coords.longitude)
			// 	console.log('validating against route lat lng', route.end_point_lat_lng)
			// 	console.log('User is not at the end location');
			// }
		},



	},
};
</script>


