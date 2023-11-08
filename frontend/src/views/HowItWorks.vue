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
	color: #70484a;
	font-weight: bold;
}

h6 {
	text-decoration: underline;
}

.title{
	color: black;
	position:relative;
	text-decoration: none;
}

.title::before{
	content: '';
    position: absolute;
    width: 100%;
    height: 2px;
    border-radius: 4px;
    background-color: #18272F;
    bottom: 0;
    left: 0;
    transform-origin: right;
    transform: scaleX(0);
    transition: transform .3s ease-in-out;
}

.title:hover::before{
	color: #70484a;
	transform-origin: left;
  	transform: scaleX(1);
}

a{
	color: #70484a;
}

a:hover{
	color: #4a3c3c;
}

ul li{
	margin-left: 5px;
}

.block{
	padding-top: 10px;
}


</style>

<template>
	<Navbar />
	<div class="container-fluid pt-3 pb-3" style="background-color: ;">
		<div class="row justify-content-center">
			<div class="block col-lg-8">
				<h2 class="text-center"><a class="title">What is It?</a></h2>
				<!-- <img src="../assets/how-it-works.png" alt="How it works" class="img-fluid rounded mx-auto d-block"> -->
				<p id="whatisit" class="text-center mt-3">PlanIt is a <span>gamified </span>route planner app aimed at encouraging users to reduce transport carbon emissions. This can be done through the adoption of eco-friendly transport options, like <span>walking</span> or <span>taking public transport</span> over driving.</p>
			</div>
			<div class="block col-lg-8">
				<h2 class="text-center"><a class="title">Why PlanIt?</a></h2>
				<!-- <img src="../assets/how-it-works.png" alt="How it works" class="img-fluid rounded mx-auto d-block"> -->
				<h6>Carbon Emissions from Urban Transportation</h6>
				<ul>
					<li>Contributes to about <span>15% of total carbon emissions </span> in Singapore</li>
					<li>Government aims to <span> reduce transport emissions by 80% </span>(from 2016 levels) by mid-century</li>
				</ul>
				<h6>Growing Trend of Gamification</h6>
				<ul>
					<li>Gamification market in Singapore <span>projected to expand from 2023 - 2028</span></li>
					<li>New and innovative way to <span>drive awareness</span>,<span> motivation</span>, and <span>engagement</span></li>
				</ul>
			</div>
			<div class="block col-lg-8">
				<h2 class="text-center"><a class="title">How It Works</a></h2>
				<!-- <img src="../assets/how-it-works.png" alt="How it works" class="img-fluid rounded mx-auto d-block"> -->
				<img src="../assets/product_demo_real.gif" alt="How it works" class="img-fluid rounded mx-auto d-block">
				<p class="text-center mt-3">Our application provides a unique way to navigate your city. It uses advanced algorithms to find the most efficient routes, and it also includes a gamification system to make your journey more fun. Earn badges, level up, and compete with your friends!</p>
			</div>
			<div class="col-lg-8">
			<h6>Additional Reading Links</h6>
				<ol>
					<li>Land Transport Authority: <a href="https://www.lta.gov.sg/content/ltagov/en/newsroom/2022/3/news-releases/reducing-peak-land-transport-emissions-by-80-.html" target="_blank">Reducing Peak Land Transport Emissions by 80%</a></li>
					<li>Land Transpoer Authority: <a href="https://www.lta.gov.sg/content/ltagov/en/who_we_are/our_work/land_transport_master_plan_2040.html" target="_blank">Land Transport Master Plan 2040</a></li>
					<li>National Climate Change Secretariat Singapore: <a href="https://www.nccs.gov.sg/singapores-climate-action/mitigation-efforts/transport/#:~:text=TRANSPORT,A%20significant%20needle" target="_blank">Making Walk-Cycle-Ride the Preferred Mode to Travel</a></li>
				</ol>
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
			} catch (error) {
				console.error("Error fetching users:", error);
			}
		}

	},
};
</script>


