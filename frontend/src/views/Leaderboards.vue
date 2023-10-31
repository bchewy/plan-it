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
	<Navbar />
	<div class="container-fluid pt-3 bg-supergreen pb-3">
		<div class="row">
			<div class="col-lg-12">
				<div class="card">
					<div class="card-header">
						<h4 class="card-title">Global Leaderboard</h4>
					</div>
					<div class="card-body">
						<div class="table-responsive">
							<table class="table table-striped">
								<thead>
									<tr>
										<th>Rank</th>
										<th>Name</th>
										<th>Level</th>
										<!-- <th>EXP to next level</th> -->
										<th>CO2 Saved</th>
									</tr>
								</thead>
								<tbody>
									<tr v-for="(user, index) in users" :key="user.email">
										<td>{{ index + 1 }}</td>
										<td>
											<img :src="user.pictureurl" alt="User Image" width="50" height="50">
											<br><span>{{ user.handle }}</span>
										</td>
										<td>{{ user.level }}</td>
										<!-- <td>{{ user.exp }}</td> -->
										<td v-if="user.carbonsavings">{{ user.carbonsavings }} Co2 kg</td>
										<td v-else></td>
									</tr>
								</tbody>
							</table>
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
import { Chart, registerables } from 'chart.js/auto';
import 'chartjs-adapter-date-fns';
import { format } from 'date-fns';
import { ref, defineComponent, computed, reactive } from "vue";
Chart.register(...registerables);



export default {
	created() {
		this.fetchData();

	},
	watch: {
		activeTab: {
			immediate: true,
			handler(newVal, oldVal) {
				if (newVal === 'routes') {
					this.$nextTick(() => {
						this.fetchData();
					});
				}
			},
		},
	},
	data() {
		const { user, isAuthenticated } = useAuth0();
		const userExp = ref(0);
		const expToNextLevel = ref(0);
		const userLvl = ref(0)
		const users = [];

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
		async drawChart() {
			if (!Array.isArray(this.routes) || this.routes.length === 0) {
				console.error('No routes available.');
				return;
			}

			this.routes.sort((a, b) => new Date(a.timestamp) - new Date(b.timestamp));
			const labels = this.routes.map(route => new Date(route.timestamp).toISOString());
			const data = this.routes.map(route => parseFloat(route.carbon_emission.toFixed(1)));

			const canvas = document.getElementById('carbonFootprintChart');
			if (canvas) {
				const ctx = document.getElementById('carbonFootprintChart').getContext('2d');
				if (this.myChart) {
					this.myChart.destroy();
				}

				console.log('Labels:', labels);
				console.log('Count of Labels:', labels.length);
				console.log('Data:', data);
				console.log('Count of Data:', data.length);

				console.log('Fake Data', [2, 4, 3],)
				console.log('Fake Labels', ["2023-10-26T00:00:00.000Z", "2023-10-27T00:00:00.000Z", "2023-10-28T00:00:00.000Z"],)
				this.myChart = new Chart(ctx, {
					type: 'bar',
					// data: {
					//   labels: parsedLabels,
					//   datasets: [{
					//     label: 'Carbon Emission',
					//     data: data,
					//     backgroundColor: 'rgba(75, 192, 192, 0.2)',
					//     borderColor: 'rgba(75, 192, 192, 1)',
					//     borderWidth: 1
					//   }]
					// },
					data: {
						labels: labels,
						datasets: [{
							label: 'Carbon Emission',
							data: data,
							backgroundColor: 'rgba(75, 192, 192, 0.2)',
							borderColor: 'rgba(75, 192, 192, 1)',
							borderWidth: 1
						}]
					},
					options: {
						responsive: true,
						maintainAspectRatio: true,
						aspectRatio: 1,
						scales: {
							x: {
								type: 'time',
								time: {
									unit: 'day',
									displayFormats: {
										day: 'mmm d'
									},
								},
								bounds: 'data',
								ticks: {
									source: 'data',
									autoSkip: true,
									minUnit: 'day'
								}
							},
							y: {
								min: 0,
								suggestedMax: 5,
								ticks: {
									stepSize: 0.5
								}
							}
						},
					}
				});

				// Pie chart for travel mode
				const travelModes = this.routes.map(route => route.transport_mode);
				const travelModeCounts = {};
				travelModes.forEach(mode => {
					if (!travelModeCounts[mode]) {
						travelModeCounts[mode] = 1;
					} else {
						travelModeCounts[mode]++;
					}
				});
				const travelModeLabels = Object.keys(travelModeCounts);
				const travelModeData = Object.values(travelModeCounts);
				const travelModeCanvas = document.getElementById('travelCategoryChart');
				if (travelModeCanvas) {
					const travelModeCtx = document.getElementById('travelCategoryChart').getContext('2d');
					if (this.myTravelModeChart) {
						this.myTravelModeChart.destroy();
					}
					this.myTravelModeChart = new Chart(travelModeCtx, {
						type: 'pie',
						data: {
							labels: travelModeLabels,
							datasets: [{
								data: travelModeData,
								backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(255, 206, 86, 0.2)', 'rgba(75, 192, 192, 0.2)', 'rgba(153, 102, 255, 0.2)', 'rgba(255, 159, 64, 0.2)'],
								borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)', 'rgba(255, 206, 86, 1)', 'rgba(75, 192, 192, 1)', 'rgba(153, 102, 255, 1)', 'rgba(255, 159, 64, 1)'],
								borderWidth: 1
							}]
						},
						options: {
							responsive: true,
							maintainAspectRatio: true,
							aspectRatio: 2
						}
					});
				}


			}
		},
		fetchData() {
			this.fetchUsers();
			// this.fetchRoutes().then(() => {
			// 	this.drawChart();
			// });
			// this.fetchUser();
			// this.fetchFriendRequests();
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
				this.routes = response.data.reverse(); // Assign the fetched routes to the routes data property
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
				console.log('test');
			} catch (error) {
				console.error("Error fetching users:", error);
			}
		}

	},
};
</script>


