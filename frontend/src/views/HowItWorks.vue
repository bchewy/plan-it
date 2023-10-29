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
		<div class="row justify-content-center">
			<div class="col-lg-8">
				<h2 class="text-center">How It Works</h2>
				<img src="../assets/how-it-works.png" alt="How it works" class="img-fluid rounded mx-auto d-block">
				<p class="text-center mt-3">Our application provides a unique way to navigate your city. It uses advanced algorithms to find the most efficient routes, and it also includes a gamification system to make your journey more fun. Earn badges, level up, and compete with your friends!</p>
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


