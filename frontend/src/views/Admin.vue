<style scoped>
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
</style>

<template>
	<Navbar />
	<div class="container-fluid pt-3 bg-supergreen pb-3">
		<!-- User Management ================================================== -->
		<div class="row">
			<div class="col-lg-12">
				<div class="card mt-4 mb-4">
					<div class="card-header">
						<h3 class="mb-0">User Management</h3>
					</div>
					<div class="container m-2">
						<div class="row">
							<div class="col-12 mt-5">
								<table class="table table-striped">
									<thead>
										<tr>
											<th scope="col">#</th>
											<th scope="col">Handle</th>
											<th scope="col">Progress</th>
											<th scope="col">Actions</th>
										</tr>
									</thead>
									<tbody>
										<tr v-for="(user, index) in users" :key="user">
											<th scope="row">{{ index + 1 }}</th>
											<td>@{{ user.handle }}</td>
											<td v-if="user.level">Lvl {{ user.level }}, EXP: {{ user.exp }}/100</td>
											<td v-else>-</td>
											<!-- <td>{{ user.email }}</td> -->
											<td>
												<button class="btn btn-primary" @click="openModal(user)" data-bs-toggle="modal" data-bs-target="#addUserModal">Edit</button>
												<button disabled class="btn btn-danger" @click="deleteUser(user.id)">Delete</button>
											</td>
										</tr>
									</tbody>
								</table>
							</div>
						</div>
					</div>
				</div>

			</div>
		</div>

		<div class="modal fade" id="addUserModal" tabindex="-1" aria-labelledby="addUserModalLabel" aria-hidden="true" ref="addUserModal">
			<div class="modal-dialog">
				<div class="modal-content">
					<div class="modal-header">
						<h5 class="modal-title" id="addUserModalLabel">Update User Level and EXP</h5>
						<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					</div>
					<div class="modal-body">
						<form @submit.prevent="updateUser">
							<div class="mb-3">
								<label for="user-level" class="form-label">Level</label>
								<input type="number" class="form-control" id="user-level" v-model="updatedUser.level">
							</div>
							<div class="mb-3">
								<label for="user-exp" class="form-label">EXP</label>
								<input disabled type="number" class="form-control" id="user-exp" v-model="updatedUser.exp">
							</div>
							<button type="submit" class="btn btn-primary">Update</button>
						</form>
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
import 'chartjs-adapter-date-fns';
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
			updatedUser: {
				email: '',
				level: 0,
				exp: 0,
			},
		};
	},
	computed: {},
	components: {
		Navbar,
		MapItem,
		AddFriend,
		FriendRequest,
		Badges,
	},
	methods: {
		openModal(user) {
			this.updatedUser.email = user.email;
			this.updatedUser.level = user.level;
			this.updatedUser.exp = user.exp;
		},
		updateUser() {
			const urlLevel = `${import.meta.env.VITE_API_ENDPOINT}/users/${this.updatedUser.email}/replace/level`;
			// const urlExp = `${import.meta.env.VITE_API_ENDPOINT}/users/${this.updatedUser.email}/exp`;
			const headers = {
				"x-api-key": "PlanItIsTheBestProjectEverXYZ",
			};

			// Update level
			axios.post(urlLevel, { level: this.updatedUser.level }, { headers })
				.then(response => {
					console.log(response.data);
					// let modal = new bootstrap.Modal(this.$refs.addUserModal);
					// modal.hide();
					this.fetchUsers();

				})
				.catch(error => {
					console.error("Error updating level:", error);
				});

			// // Update exp
			// axios.post(urlExp, { exp: this.updatedUser.exp }, { headers })
			// 	.then(response => {
			// 		console.log(response.data);
			// 	})
			// 	.catch(error => {
			// 		console.error("Error updating exp:", error);
			// 	});
		},
		fetchData() {
			this.fetchUsers();
			// this.fetchRoutes().then(() => {
			// 	this.drawChart();
			// });
			// this.fetchUser();
			// this.fetchFriendRequests();
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


