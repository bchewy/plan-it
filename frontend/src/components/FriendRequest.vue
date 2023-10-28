<template>
	<div class="card mb-3">
		<div class="card-body">
			<h5 class="card-title">{{ friend }}</h5>
			<div class="d-flex justify-content-end" v-if="showButtons">
				<button class="btn btn-success me-2" @click="acceptRequest">Accept</button>
				<button class="btn btn-danger" @click="declineRequest">Decline</button>
			</div>
			<div v-if="showAlert" class="alert alert-success alert-dismissible fade show" role="alert">
				{{ alertMessage }}
				<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close" @click="showAlert = false"></button>
			</div>
		</div>
	</div>
</template>
<script>
import axios from 'axios';

export default {
	props: ['friend', 'user', 'receivedRequests', 'sentRequests', 'type'],
	data() {
		return {
			// data properties...
			showAlert: false,
			alertMessage: '',
			// email: this.user.email,
		};
	},
	computed: {
		showButtons() {
			return this.type === 'received';
		}
	},
	methods: {
		async acceptRequest() {
			try {
				const email = this.user.email;
				const url = `${import.meta.env.VITE_API_ENDPOINT}/users/${encodeURIComponent(email)}/friend_requests/accept`;
				const body = { friend_email: this.friend };
				const headers = {
					'Content-Type': 'application/json',
					'x-api-key': 'PlanItIsTheBestProjectEverXYZ'
				};
				const response = await axios.post(url, body, { headers });
				this.showAlert = true;
				this.alertMessage = 'Friend request accepted.';
				this.$emit('refresh');
			} catch (error) {
				console.error("Error accepting friend request", error);
			}
		},
		async declineRequest() {
			try {
				const email = this.user.email;
				const url = `${import.meta.env.VITE_API_ENDPOINT}/users/${encodeURIComponent(email)}/friend_requests/decline`;
				const body = { friend_email: this.friend };
				const headers = {
					'Content-Type': 'application/json',
					'x-api-key': 'PlanItIsTheBestProjectEverXYZ'
				};
				const response = await axios.post(url, body, { headers });
				this.showAlert = true;
				this.alertMessage = 'Friend request declined.';
				this.$emit('refresh');
			} catch (error) {
				console.error("Error declining friend request", error);
			}
		},
	},
};
</script>