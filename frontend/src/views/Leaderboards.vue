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
							<table class="table">
								<thead>
									<tr>
										<th>Rank</th>
										<th>Name</th>
										<th>Badges Earned</th>
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
										<!-- add pictures of badges-->
										<td>
											<span v-for="badge in user.badges" :key="badge.id">
												<img :src="badge.image" alt="Badge Image" width="50" height="50">
											</span>
											<!-- <img v-for="badge in badges" :key="badge.id" :src="'../src/assets/badges/' + badge.icon" width="30" height="30"> -->
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
			<!-- Friends leaderboard -->
			<div class="col-lg-12 mt-5">
				<div class="card">
					<div class="card-header">
						<h4 class="card-title">Friends Leaderboard</h4>
					</div>
					<div class="card-body">
						<div class="table-responsive">
							<table class="table">
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
									<tr v-for="(user, index) in friends" :key="user.email">
										{{ friends }}
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
import { ref, defineComponent, computed, reactive } from "vue";

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
		const friends = ref([]);

		return {
			users,
			userExp,
			expToNextLevel,
			userLvl,
			user,
			isAuthenticated,
			routes: [],
			friends,
			friendRequests: [],
			receivedRequests: [],
			sentRequests: [],
			badges: [],
		}
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
			this.fetchUser();
			this.fetchFriendStats(this.friends);
			this.fetchBadges();
			// this.fetchRoutes().then(() => {
			// 	this.drawChart();
			// });
			// this.fetchUser();
			// this.fetchFriendRequests();
		},
		// async fetchBadges() {
		// 	const url = `${import.meta.env.VITE_API_ENDPOINT}/users/iz/${encodeURIComponent(this.user.email)}/badges`;
		// 	const headers = {
		// 		"x-api-key": "PlanItIsTheBestProjectEverXYZ",
		// 	};

		// 	try {
		// 		const response = await axios.get(url, { headers });
		// 		this.badges = response.data.badges;
		// 		// console.log(this.friends);

		// 	} catch (error) {
		// 		console.error("Error fetching user", error);
		// 	}
		// },
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
				// console.log(this.friends);

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
		async fetchBadges() {
			const url = `${import.meta.env.VITE_API_ENDPOINT}/users/${encodeURIComponent(this.user.email)}/badges`;
			const headers = {
				"x-api-key": "PlanItIsTheBestProjectEverXYZ",
			};

			try {
				const response = await axios.get(url, { headers });
				this.badges = response.data.badges;

			} catch (error) {
				console.error("Error fetching badges", error);
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
				for (let user of this.users) {
					const badgeUrl = `${import.meta.env.VITE_API_ENDPOINT}/users/${user.email}/badges`;
					try {
						const badgeResponse = await axios.get(badgeUrl, { headers });
						user.badges = [];

						// user.badges = badgeResponse.data;
						// for every badge, fetch the details
						for (let badgeId of badgeResponse.data) {
							const badgeDetailsUrl = `${import.meta.env.VITE_API_ENDPOINT}/badges/${badgeId}`;
							try {
								const badgeDetailsResponse = await axios.get(badgeDetailsUrl, { headers });

								user.badges.push({
									id: badgeId,
									image: badgeDetailsResponse.data.image
								});
								console.log(user.badges)

							} catch (error) {
								console.error("Error fetching details for badge:", error);
							}
						}
					} catch (error) {
						console.error("Error fetching badges for user:", error);
					}
				}
			} catch (error) {
				console.error("Error fetching users:", error);
			}
		},
		async fetchFriendStats(friends) {
			try {
				console.log('Fetching friend data')
				console.log(friends)
				for (let friend of friends) {
					console.log('friend')
					const url = `${import.meta.env.VITE_API_ENDPOINT}/users/iz/${encodeURIComponent(friend)}`;
					const headers = {
						"x-api-key": "PlanItIsTheBestProjectEverXYZ",
					};
					const response = await axios.get(url, { headers });
					friend.stats = response.data;
					console.log(response.data)
				}
			} catch (error) {
				console.error("Error fetching friend stats:", error);
			}
		}


	},
};
</script>


