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
										<th>CO2 Saved</th>
									</tr>
								</thead>
								<tbody>
									<tr v-for="(user, index) in users" :key="user.email">
										<td>{{ index + 1 }}</td>
										<td>
											<img :src="user.pictureurl" alt="User Image" width="50" height="50">&nbsp;
											<span>@{{ user.handle }}</span>
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
										<th>Badges Earned</th>
										<th>Level</th>
										<th>CO2 Saved</th>
									</tr>
								</thead>
								<tbody>
									<tr v-for="(user, index) in friendStats" :key="user.email">
										<td>{{ index + 1 }}</td>
										<td>
											<img :src="user.stats.pictureurl" alt="User Image" width="50" height="50">&nbsp;
											<span>@{{ user.stats.handle }}</span>
										</td>
										<td>
											<span v-for="badge in user.stats.badges" :key="badge.id">
												<img :src="badge.badgesimg" alt="Badge Image" width="50" height="50">
											</span>
										</td>
										<!-- You can now access the stats data for each user -->
										<td>{{ user.stats.level }}</td>
										<td>{{ user.stats.carbonsavings }} Co2 Kg</td>
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
		const friendStats = ref([]);

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
			friendStats,

		}
	},
	components: {
		Navbar,
		MapItem,
		AddFriend,
		FriendRequest,
		Badges,
	},
	methods: {
		async fetchData() {
			this.fetchUsers();
			await this.fetchUser();
			this.fetchFriendStats(this.friends);
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
		// This call fetch the iniital users in the leaderboard page.
		async fetchUsers() {
			const url = `${import.meta.env.VITE_API_ENDPOINT}/users`;
			const headers = {
				"x-api-key": "PlanItIsTheBestProjectEverXYZ",
			};

			try {
				const response = await axios.get(url, { headers });
				this.users = response.data;
				for (let user of this.users) {
					try {
						// console.log(user);
						const badgeUrl = `${import.meta.env.VITE_API_ENDPOINT}/users/${user.email}/badges`;
						const badgeResponse = await axios.get(badgeUrl, { headers });
						const badgeIds = badgeResponse.data;

						// Initialize an empty array for user badges
						user.badges = [];

						// Fetch each badge details
						for (let badgeId of badgeIds) {
							try {
								const badgeDetailsUrl = `${import.meta.env.VITE_API_ENDPOINT}/badges/${badgeId}`;
								const badgeDetailsResponse = await axios.get(badgeDetailsUrl, { headers });

								// Add the badge details to the user badges array
								// console.log(badgeDetailsResponse.data);
								user.badges.push({
									id: badgeId,
									image: badgeDetailsResponse.data.image,
								});
							} catch (error) {
								console.error(`Error fetching details for badge with ID ${badgeId}:`, error);
							}
						}
					} catch (error) {
						console.error(`Error fetching badges for user with email ${user.email}:`, error);
					}
				}
			} catch (error) {
				console.error("Error fetching users:", error);
			}
		},

		// This call fetches the friends in the leaderboard page.
		async fetchFriendStats(friends) {
			// console.log("Fetching friend stats")
			// console.log(friends)
			try {
				const stats = [];
				for (let friend of friends) {
					// console.log(friend)
					// console.log("Fetching our friend here.")
					const url = `${import.meta.env.VITE_API_ENDPOINT}/users/iz/${encodeURIComponent(friend)}`;
					const headers = {
						"x-api-key": "PlanItIsTheBestProjectEverXYZ",
					};
					const response = await axios.get(url, { headers });
					stats.push({
						...friend,
						stats: {
							...response.data,
							badges: [],
						},
					});

					// console.log(response.data.badges)
					if (Array.isArray(response.data.badges)) {
						for (let badge of response.data.badges) {
							const badgeDetailsUrl = `${import.meta.env.VITE_API_ENDPOINT}/badges/${badge}`;
							const badgeDetailsResponse = await axios.get(badgeDetailsUrl, { headers });

							// Add the badge details to the user badges array
							stats[stats.length - 1].stats.badges.push({
								id: badge,
								badgesimg: badgeDetailsResponse.data.image,
							});
						}
					}


				}
				this.friendStats = stats;
				// console.log(this.friendStats)
			} catch (error) {
				console.error("Error fetching friend stats:", error);
			}
		}


	},
};
</script>


