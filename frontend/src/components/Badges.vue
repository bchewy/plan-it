<template>
  <div v-if="isLoading" class="loading-screen">
    <div>Loading...</div>
  </div>
  <div v-else class="container">
    <div class="row">
      <div class="col-12 text-center mt-5">
        <h1>My Badges</h1>
      </div>
    </div>
    <!-- All Badges -->
    <div class="row justify-content-center mt-5">
      <div v-for="(badge, index) in badgesLoaded" :key=index class="card" style="width: 18rem; margin:0.5rem">

        <img :src="'../src/assets/badges/' + badge.icon" class="card-img-top">
        <div class="card-body d-flex flex-column">
          <h5 class="card-title">{{ badge.name }}</h5>
          <p class="card-text">{{ badge.description }}</p>
          <a href="community" class="btn btn-primary mt-auto">Share Badge</a>
        </div>
      </div>
      <button v-if="this.length == 3" @click="loadMore()" class="btn btn-link">Load More</button>
      <button v-else @click="showLess()" class="btn btn-link">Show Less</button>
    </div>
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import axios from "axios";

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
					try {
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
		}
	},
};
</script>

