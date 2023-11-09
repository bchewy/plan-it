<style scoped>
.profile-container {
	box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.map-container {
	width: 80%;
	/* or any other preferred percentage */
	height: 200px;
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
						<h4 class="card-title text-center">Invalid Routes</h4>
						<p class="card-text">The invalid routes here do not have their end locations verified. <strong>Verify your end locations</strong> before the time limit to get more EXP.</p>
					</div>
					<div class="card-body">
						<div class="table-responsive">
							<table class="table table-striped">
								<thead>
									<tr>
										<!-- <th>Route ID</th> -->
										<!-- <th>Time</th> -->
										<th>Map</th>
										<!-- <th>Start Location</th> -->
										<!-- <th>End Location</th> -->
										<!-- <th>Distance</th> -->
										<!-- <th>Carbon Emission</th> -->
										<!-- <th>Transport Mode</th> -->
										<th>Details</th>
										<!-- <th>Checked Start Location</th> -->
									</tr>
								</thead>
								<tbody v-if="routes">
									<tr v-for=" route  in  routes " :key="route.id">
										<td class="col-9">
											<GMapMap :center="{ lat: Number(route.start_point_lat_lng.split(',')[0]), lng: Number(route.start_point_lat_lng.split(',')[1]) }" :zoom="10" map-type-id="terrain" style="width: 100%; height: 200px;">
												<GMapMarker :position="{ lat: Number(route.start_point_lat_lng.split(',')[0]), lng: Number(route.start_point_lat_lng.split(',')[1]) }" />
												<GMapMarker :position="{ lat: Number(route.end_point_lat_lng.split(',')[0]), lng: Number(route.end_point_lat_lng.split(',')[1]) }" />
											</GMapMap>
										</td>
										<td>
											Start: <b>{{ route.start_point_name }} </b><br>
											End: <b>{{ route.end_point_name }} </b><br>
											<button class="btn btn-primary" @click="checkEndLocation(route)">Validate Route</button><br>

										</td>
										<!-- <td>{{ route.checkedStartLocation }}</td> -->
									</tr>
								</tbody>
							</table>
						</div>
					</div>
				</div>
			</div>
		</div>

		<!-- Success Modal template -->
		<div class="modal fade" id="modalGood" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
			<div class="modal-dialog">
				<div class="modal-content">
					<!-- <div class="modal-header">
						<h5 class="modal-title" id="exampleModalLabel"></h5>
						<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					</div> -->
					<div class="modal-body">
						<!-- <p>You have validated this route. EXP has been added into your profile.</p> -->
						<!-- <img src="../assets/levelup.png" alt="level up" width="100px" height="100px"> -->
						<!-- <div v-if="dancingGif"> -->
						<div class="text-center">
							<img :src="dancingGif" alt="Dancing Gif"><br>
							<h2>Congratulations!</h2>
						</div>


						<table class="table table-hover">
							<tr>
								<td>Your current EXP:</td>
								<!-- <td><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(0, 0, 0, 1);transform: ;msFilter:;">
										<path d="M5 21h14c1.103 0 2-.897 2-2V5c0-1.103-.897-2-2-2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zm5-14 6 5-6 5V7z"></path>
									</svg></td> -->
								<td>{{ userExp }}/100</td>
							</tr>
							<tr>
								<td>Your new EXP:</td>
								<!-- <td><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(0, 0, 0, 1);transform: ;msFilter:;">
										<path d="M5 21h14c1.103 0 2-.897 2-2V5c0-1.103-.897-2-2-2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zm5-14 6 5-6 5V7z"></path>
									</svg></td> -->
								<td>{{ userExp + expToAddG }}/100 (+ {{ expToAddG }})</td>
							</tr>
							<!-- <tr>
								<td>Level Progress:</td>
								<td>{{ userLvl }}</td>
							</tr> -->
						</table>

						<!-- <p>{{ expToAddG }}exp has been added to your progress!</p> -->

						<div class="progress">
							<div class="progress-bar bg-supergreen" role="progressbar" :style="{ width: userExp + expToAddG + '%' }" aria-valuenow="userExp" aria-valuemin="0" aria-valuemax="userLvl * 100">{{ ((userExp + expToAddG)).toFixed(2) }}%</div>
						</div>
						<!-- <p>Current Level: {{ userLvl }}</p> -->
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
					<!-- <div class="modal-header">
						<h5 class="modal-title" id="exampleModalLabel">Uh oh!</h5>
						<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					</div> -->
					<div class="modal-body text-center">
						<!-- <div v-if="dancingGif"> -->
						<img :src="dancingGif" alt="Dancing Gif"><br>
						<!-- </div> -->
						It appears there may be some inaccuracies in your routes...
					</div>
					<div class="modal-footer">
						<button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
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
import { ref, defineComponent, computed, reactive, watch } from "vue";
import { useGeolocation } from '@vueuse/core'
import Modal from 'bootstrap/js/dist/modal';

export default {
	components: {
		Navbar,
		MapItem,
		AddFriend,
		FriendRequest,
		Badges,
	},
	watch: {
		userLvl: {
			handler() {
				this.fetchUser();
			},
			immediate: true,
		},

	},
	created() {
		this.fetchData();
	},
	data() {
		const { user, isAuthenticated } = useAuth0();
		const userExp = ref(0);
		const userLvl = ref(0)
		const { coords, locatedAt, error, resume, pause } = useGeolocation()
		const emissionSavings = ref(0);
		const expToAddG = ref(0);
		const dancingGif = ref(null);


		return {
			userExp,
			userLvl,
			user,
			isAuthenticated,
			routes: [],
			coords,
			emissionSavings,
			expToAddG,
			dancingGif,
		};
	},
	methods: {
		fetchData() {
			this.fetchRoutes();
			this.fetchRandomGif();
			this.fetchUser();
		},

		// Method for calculating distance between two points
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


		async fetchRandomGif() {
			const url = `https://api.giphy.com/v1/gifs/random?api_key=${import.meta.env.VITE_GIFY_API_KEY}&tag=dancing&rating=g`;

			try {
				const response = await axios.get(url);
				this.dancingGif = response.data.data.images.fixed_height.url;
				console.log(this.dancingGif);

			} catch (error) {
				console.error('Error fetching random gif:', error);
			}
		},
		// ==================================================================================================
		async fetchUser() {
			const url = `${import.meta.env.VITE_API_ENDPOINT}/users/iz/${encodeURIComponent(this.user.email)}`;
			const headers = {
				"x-api-key": `${import.meta.env.VITE_API_KEY}`,
			};

			try {
				const response = await axios.get(url, { headers });
				// this.friends = response.data.friends;
				this.userLvl = response.data.level;
				this.userExp = response.data.exp;

			} catch (error) {
				console.error("Error fetching user", error);
			}
		},

		// Method for fetching routes from the backend
		async fetchRoutes() {
			const email = this.user.email; // Get the email from user object
			const url = `${import.meta.env.VITE_API_ENDPOINT}/routes/email?email=${encodeURIComponent(email)}`;
			const headers = {
				"x-api-key": `${import.meta.env.VITE_API_KEY}`, // Replace with your actual API key
			};
			try {
				const response = await axios.get(url, { headers });
				const unvalidatedRoutes = response.data.filter(route => !route.validated);
				this.routes = unvalidatedRoutes.reverse(); // Assign the fetched routes to the routes data property
			} catch (error) {
				console.error("Error fetching routes:", error);
			}
		},

		// This method is only used to validate a route
		// ==================================================================================================
		async updateRoute(routeId) {
			const url = `${import.meta.env.VITE_API_ENDPOINT}/routes/${routeId}/validate`;
			const headers = {
				"x-api-key": `${import.meta.env.VITE_API_KEY}`, // Replace with your actual API key
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
			}
			const carbonFootprintDriving = distanceInKm * 0.12;
			const carbonFootprint = distanceInKm * carbonEmissionPerKm;
			// console.log("Carbon Footprint:", carbonFootprint);
			// console.log("Carbon Footprint Driving:", carbonFootprintDriving);
			return [carbonFootprint, carbonFootprintDriving];
		},
		addExpBasedOnCarbonEmission(carbonList) {
			// console.log("Entering the addEXP Function now...")

			this.emissionSavings = carbonList[1] - carbonList[0];
			// console.log("Emission Savings:", this.emissionSavings);

			const BASE_EXP = 10; // is 1 on the routing page
			const BONUS_EXP_PER_SAVED_KG = 10; // is 1 on the routing page

			// Calculate the total EXP to add based on the base EXP and the bonus for saved emissions
			const expToAdd = Math.ceil(BASE_EXP + (this.emissionSavings * BONUS_EXP_PER_SAVED_KG));

			// console.log("EXP added here:", expToAdd);
			// expAdded.value = expToAdd;
			this.expToAddG += expToAdd;

			// Update the user's carbon savings in the backend
			axios.post(`${import.meta.env.VITE_API_ENDPOINT}/users/${this.user.email}/carbonsavings`, { carbonsavings: this.emissionSavings }, {
				headers: {
					'X-Api-Key': `${import.meta.env.VITE_API_KEY}`
				}
			})
				.then(response => {
					console.log(response.data.message);
					// logUserActivity(`saved :${this.emissionSavings} co2`)
				})
				.catch(error => {
					console.error(error);
				});

			// Update the user exp in the backend
			axios.post(`${import.meta.env.VITE_API_ENDPOINT}/users/${this.user.email}/exp`, { exp: this.expToAddG }, {
				headers: {
					'X-Api-Key': `${import.meta.env.VITE_API_KEY}`
				}
			})
				.then(response => {
					console.log(response.data.message);
					// logUserActivity(`gained ${this.expToAddG} exp`)
				})
				.catch(error => {
					console.error(error);
				});
		},

		// Method for checking if the user is within 500 meters of the end location
		checkEndLocation(route) {
			// console.log("Route being checked:", route);
			// console.log("Route distance", route.distance);
			// console.log("Route travel mode", route.transport_mode);
			const { latitude, longitude } = this.coords;

			// Get the route's end location
			const [endLat, endLng] = route.end_point_lat_lng.split(', ').map(Number);

			// Calculate the distance between the two locations in kilometers
			const distance = this.haversineDistance([latitude, longitude], [endLat, endLng]);

			// Check if the distance is less than 0.5 kilometers (500 meters)
			if (distance < 0.5) {
				console.log('User is within 500 meters of the end location');

				this.updateRoute(route.route_id, true)
				this.routes = this.routes.filter(r => r.route_id !== route.route_id);
				this.addExpBasedOnCarbonEmission(this.calculateCarbonEmissionForEXP(route.distance, route.transport_mode))

				console.log('Added EXP:', this.expToAddG)
				var myModalEl = document.getElementById('modalGood');
				var myModal = new Modal(myModalEl);
				myModal.show();

				// Update the route to validated true:



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

		// ==================================================================================================


	},
};
</script>


