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

span{
	color: #3a5a40;
}

h6{
	text-decoration: underline;
}
</style>

<template>
	<Navbar />
	<div class="container-fluid pt-3 bg-supergreen pb-3">
		<div class="row justify-content-center">
			<div class="col-lg-8">
				<h2 class="text-center">What is It?</h2>
				<!-- <img src="../assets/how-it-works.png" alt="How it works" class="img-fluid rounded mx-auto d-block"> -->
				<p id="whatisit" class="text-center mt-3">PlanIt is a <span>gamified </span>route planner app aimed at encouraging users to reduce transport carbon emissions. This can be done through the adoption of eco-friendly transport options, like walking, or taking public transport over driving.</p>
			</div>
			<div class="col-lg-8">
				<h2 class="text-center">Why PlanIt?</h2>
				<!-- <img src="../assets/how-it-works.png" alt="How it works" class="img-fluid rounded mx-auto d-block"> -->
				<h6>Carbon Emissions from Urban Transportation</h6>
				<ul>
					<li>Contributes to about 15% of total carbon emissions in Singapore</li>
					<li>Government aims to reduce transport emissions by 80% (from 2016 levels) by mid-century</li>
				</ul>
				<h6>Growing Trend of Gamification</h6>
				<ul>
					<li>Gamification market in Singapore projected to expand from 2023 - 2028</li>
					<li>New and innovative way to drive awareness, motivation, and engagement</li>
				</ul>
			</div>
			<div class="col-lg-8">
				<h2 class="text-center">How It Works</h2>
				<!-- <img src="../assets/how-it-works.png" alt="How it works" class="img-fluid rounded mx-auto d-block"> -->
				<img src="../assets/product_demo_real.gif" alt="How it works" class="img-fluid rounded mx-auto d-block">
				<p class="text-center mt-3">Our application provides a unique way to navigate your city. It uses advanced algorithms to find the most efficient routes, and it also includes a gamification system to make your journey more fun. Earn badges, level up, and compete with your friends!</p>
			</div>
		</div>
		<div class="container-fluid pt-3 bg-supergreen pb-3">
			<h6>Additional Reading Links</h6>
			<ol>
				<li><a href="https://www.lta.gov.sg/content/ltagov/en/newsroom/2022/3/news-releases/reducing-peak-land-transport-emissions-by-80-.html">Land Transport Authority: Reducing Peak Land Transport Emissions by 80%</a></li>
				<li><a href="https://www.nccs.gov.sg/singapores-climate-action/mitigation-efforts/transport/#:~:text=TRANSPORT,A%20significant%20needle">National Climate Change Secretariat Singapore: Making Walk-Cycle-Ride the Preferred Mode to Travel</a></li>
			</ol>
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


