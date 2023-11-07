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

.badge-select {
	display: flex;
	align-items: center;
  }
  
  .badge-select input[type="checkbox"]{
	appearance: none;
	width: 32px;
	height: 14px;
	background-color: #c67074;
	border-radius: 14px;
	position: relative;
  }
  .badge-select input[type="checkbox"]::before {
	content: "";
	width: 14px; /* Width of the switch handle */
	height: 14px; /* Height of the switch handle */
	background-color: #ebedf0; /* Color of the switch handle */
	border-radius: 50%; /* Make it a circle */
	position: absolute;
	top: 50%;
	transform: translateY(-50%);
	left: 1px; /* Adjust the position as needed */
	transition: 0.4s; /* Add a smooth transition effect */
  }
  
  .badge-select input[type="checkbox"]:checked {
	background-color: #4CAF50; /* Background color for the "on" state */
  }
  
  .badge-select input[type="checkbox"]:checked::before {
	left: calc(100% - 15px); /* Position the handle to the right when checked */
  }
  
  .badge-select label{
	margin-left: 8px;
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
					<div class="container p-0">
						<div class="row">
							<div class="col-12 mt-5">
								<table class="table table-responsive">
									<thead>
										<tr>
											<th scope="col">#</th>
											<th scope="col">Handle</th>
											<th scope="col">Progress</th>
											<th scope="col">Badges</th>
											<th scope="col">Actions</th>
										</tr>
									</thead>
									<tbody>
										<tr v-for="(user, index) in users" :key="user">
											<th scope="row">{{ index + 1 }}</th>
											<td><img :src="user.pictureurl" alt="User Image" width="50" height="50"><br> @{{ user.handle }}</td>
											<td v-if="user.level">Lvl {{ user.level }}, EXP: {{ user.exp }}/100</td>
											<td v-else>-</td>
											<td>
												<div v-for="badge in badges" :key="badge._id" class="badge-select">
													<input type="checkbox" :value="badge._id" :checked="hasBadge(user, badge._id)" @change="handleBadgeChange(user, badge._id)">
													<label>{{ badge.name }}</label>
													<img :src="badge.image" class="badge-image" style="width: 30px;">
												</div>
											</td>
											<td>
												<button class="btn btn-success" @click="openModal(user)" data-bs-toggle="modal" data-bs-target="#addUserModal">Edit</button>
												<!-- <button disabled class="btn btn-danger" @click="deleteUser(user.id)">Delete</button> -->

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

		<!-- Badges ================================================== -->
		<div class="row">
			<div class="col-lg-12">
				<div class="card mt-4 mb-4">
					<div class="card-header">
						<h3 class="mb-0">Badge Management</h3>
					</div>
					<div class="container p-0">
						<div class="row">
							<div class="col-12 mt-5">
								<table class="table table-striped">
									<thead>
										<tr>
											<th scope="col">#</th>
											<th scope="col">Badge</th>
											<th scope="col">Description</th>
											<th scope="col">Actions</th>
										</tr>
									</thead>
									<tbody>
										<tr v-for="(badge, index) in badges" :key="badge">
											<th scope="row">{{ index + 1 }}</th>
											<td>
												{{ badge.name }}
											</td>
											<td> <img :src="badge.image" class="w-25 h-25">
												{{ badge.description }}
											</td>
											<td>
												<!-- <button class="btn btn-primary" @click="openBadgeModal(badge)" data-bs-toggle="modal" data-bs-target="#editBadgeModal">Edit</button> -->
												<button class="btn btn-danger" @click="deleteBadge(badge._id)">Delete</button>
											</td>
										</tr>
									</tbody>
								</table>
								<button class="btn btn-success mt-3 mb-2" @click="addBadge">Add New Badge</button>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<!-- Modal for updating user level and exp ================================================== -->
		<div class="modal" id="addUserModal" tabindex="-1" aria-labelledby="addUserModalLabel" aria-hidden="true" ref="addUserModal">
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
							<button type="submit" class="btn btn-success" data-bs-dismiss="modal">Update</button>
						</form>
					</div>
				</div>
			</div>
		</div>

		<!-- Modal for adding badges ================================================== -->
		<div class="modal" id="addBadgeModal" tabindex="-1" aria-labelledby="addBadgeModalLabel" aria-hidden="true" ref="addBadgeModal">
			<div class="modal-dialog">
				<div class="modal-content">
					<div class="modal-header">
						<h5 class="modal-title" id="addBadgeModalLabel">Add New Badge</h5>
						<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					</div>
					<div class="modal-body">
						<form @submit.prevent="addBadge">
							<div class="mb-3">
								<label for="badge-name" class="form-label">Name</label>
								<input type="text" class="form-control" id="badge-name" v-model="newBadge.name">
							</div>
							<div class="mb-3">
								<label for="badge-description" class="form-label">Description</label>
								<input type="text" class="form-control" id="badge-description" v-model="newBadge.description">
							</div>
							<div class="mb-3">
								<label for="badge-image" class="form-label">Image</label>
								<input type="file" class="form-control" id="badge-image" @change="handleFileUpload" accept=".png, .jpg, .jpeg">
							</div>
							<button type="submit" class="btn btn-success" data-bs-dismiss="modal">Add</button>
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
import { ref, defineComponent, computed, reactive } from "vue";
// import Modal from 'bootstrap/js/dist/modal';
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import * as bootstrap from 'bootstrap';

export default {
	async created() {
		await this.fetchData();
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
			user,
			badges: [],
			isAuthenticated,
			updatedUser: {
				email: '',
				level: 0,
				exp: 0,
			},
			newBadge: {
				name: '',
				description: '',
				image: null,
			},
			selectedBadges: reactive({}),
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
		hasBadge(user, badgeId) {
			return user && user.badges && user.badges.includes(badgeId);
		},
		toggleBadge(user, badgeId) {
			if (this.hasBadge(user, badgeId)) {
				// remove badge
				const index = user.badges.indexOf(badgeId);
				if (index > -1) {
					user.badges.splice(index, 1);
				}
			} else {
				// add badge
				user.badges.push(badgeId);
			}
		},
		handleBadgeChange(user, badgeId) {
			if (this.hasBadge(user, badgeId)) {
				// remove badge
				this.unassignBadges(user.email, badgeId);
			} else {
				// add badge
				this.assignBadges(user.email, [badgeId]);
			}
		},
		async assignBadges(email, badges) {
			const url = `${import.meta.env.VITE_API_ENDPOINT}/users/${email}/badges`;
			const headers = {
				"x-api-key": "PlanItIsTheBestProjectEverXYZ",
			};

			try {
				await axios.put(url, { badges }, { headers });
				console.log("Badges assigned successfully");
				this.fetchUsers(); // Refresh the user list
			} catch (error) {
				console.error("Error assigning badges:", error);
			}
		},
		async unassignBadges(email, badge) {
			const url = `${import.meta.env.VITE_API_ENDPOINT}/users/${email}/badges/${badge}`;
			const headers = {
				"x-api-key": "PlanItIsTheBestProjectEverXYZ",
			};

			try {
				await axios.delete(url, { headers });
				console.log("Badge unassigned successfully");
				this.fetchUsers(); // Refresh the user list
			} catch (error) {
				console.error("Error unassigning badge:", error);
			}
		},
		// handle file upload
		handleFileUpload(event) {
			this.newBadge.image = event.target.files[0];
		},
		openModal(user) {
			this.updatedUser.email = user.email;
			this.updatedUser.level = user.level;
			this.updatedUser.exp = user.exp;
		},
		async addBadge() {

			let myModalEl = document.getElementById('addBadgeModal');
			let myModal = new bootstrap.Modal(myModalEl);
			myModal.show();

			if (!this.newBadge.name || !this.newBadge.description || !this.newBadge.image) {
				toast.error(`Please fill in all fields.`, {
					autoClose: 5000,
					position: toast.POSITION.TOP_CENTER,
				});
				return;
			}

			console.log("Adding badge");
			console.log(this.newBadge);
			console.log(this.newBadge.image);
			const formData = new FormData();

			formData.append('name', this.newBadge.name);
			formData.append('description', this.newBadge.description);
			formData.append('image', this.newBadge.image);

			try {
				const response = await axios.post(`${import.meta.env.VITE_API_ENDPOINT}/badges`, formData, {
					headers: {
						// 'Content-Type': 'application/json',
						'x-api-key': 'PlanItIsTheBestProjectEverXYZ' // replace with your actual API key
					}
				});
				console.log(response.data.message);
				myModal.hide();
				this.badges = [];
				this.fetchBadges();
			} catch (error) {
				console.error(error);
			}
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
		},
		fetchData() {
			this.fetchUsers();
			this.fetchBadges();
		},
		async fetchUsers() {
			const url = `${import.meta.env.VITE_API_ENDPOINT}/users`;
			const headers = { "x-api-key": "PlanItIsTheBestProjectEverXYZ" };

			try {
				const response = await axios.get(url, { headers });
				this.users = response.data;

				for (let user of this.users) {
					const badgeUrl = `${import.meta.env.VITE_API_ENDPOINT}/users/${user.email}/badges`;
					const badgeResponse = await axios.get(badgeUrl, { headers });
					user.badges = badgeResponse.data;
					this.selectedBadges[user.email] = user.badges.map(badge => badge._id);

				}
			} catch (error) {
				console.error("Error fetching data:", error);
			}
		},
		async fetchBadges() {
			const url = `${import.meta.env.VITE_API_ENDPOINT}/badges`;
			const headers = {
				"x-api-key": "PlanItIsTheBestProjectEverXYZ",
			};

			try {
				const response = await axios.get(url, { headers });
				this.badges = response.data;
			} catch (error) {
				console.error("Error fetching badges:", error);
			}
		},
		async deleteBadge(badgeId) {
			const url = `${import.meta.env.VITE_API_ENDPOINT}/badges/${badgeId}`;
			const headers = {
				"x-api-key": "PlanItIsTheBestProjectEverXYZ",
			};

			try {
				await axios.delete(url, { headers });
				console.log("Badge deleted");
				this.badges = [];
				this.fetchBadges();
			} catch (error) {
				console.error("Error deleting badge:", error);
			}
		},


	},
};
</script>


