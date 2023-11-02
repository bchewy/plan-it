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

		<!-- Badges ================================================== -->
		<div class="row">
			<div class="col-lg-12">
				<div class="card mt-4 mb-4">
					<div class="card-header">
						<h3 class="mb-0">Badge Management</h3>
					</div>
					<div class="container m-2">
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
								<button class="btn btn-success mt-3" data-bs-toggle="modal" data-bs-target="#addBadgeModal">Add New Badge</button>
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

		<div class="modal fade" id="addBadgeModal" tabindex="-1" aria-labelledby="addBadgeModalLabel" aria-hidden="true" ref="addBadgeModal">
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
							<button type="submit" class="btn btn-primary">Add</button>
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
import Modal from 'bootstrap/js/dist/modal';

// import S3 from 'aws-sdk/clients/s3';

// import AWS from 'aws-sdk/dist/aws-sdk'

// AWS.config.update({
// 	region: 'ap-southeast-1',
// 	accessKeyId: `${process.env.VITE_APP_AWS_ACCESS_KEY_ID}`,
// 	secretAccessKey: `${process.env.VITE_APP_AWS_SECRET_ACCESS_KEY}`,
// });



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

			var myModalEl = document.getElementById('addBadgeModal');
			var myModal = new Modal(myModalEl);
			myModal.show();


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
			this.fetchBadges();
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
				this.fetchBadges();
			} catch (error) {
				console.error("Error deleting badge:", error);
			}
		},


	},
};
</script>


