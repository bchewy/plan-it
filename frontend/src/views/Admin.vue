<template>
	<header>
		<NavBar />
	</header>
	<div v-if="user.email == `brian@bchewy.com`">
		<div class="d-flex justify-content-center mt-5">
			<div class="col-md-6">
				<form @submit.prevent="createPost" class="form-inline">
					<div class="form-group mb-2">
						<label for="postContent" class="sr-only">New Post:</label>
						<input id="postContent" v-model="postContent" type="text" class="form-control" placeholder="New Post" required>
					</div>
					<button type="submit" class="btn btn-primary mb-2">Create Post</button>
				</form>
			</div>
		</div>
	</div>
	<div v-else>
		You're not an admin. Sorry You have no permissions.
	</div>
	<footer>
	</footer>
</template>
<script>
import { ref } from 'vue';
import NavBar from '../components/Navbar.vue'
import { useAuth0 } from '@auth0/auth0-vue';
import axios from 'axios';

export default {
	name: 'Home',
	components: {
		NavBar,
	},
	setup() {
		const { loginWithRedirect, user, isAuthenticated } = useAuth0();
		const postContent = ref('');

		console.log('Setup method is called');

		const createPost = async () => {
			try {
				const response = await axios.post('/users/' + user.email + '/posts', { content: postContent.value });
				console.log(response);
			} catch (e) {
				console.error('Failed to create post:', e);
			}
		};

		return {
			login: async () => {
				try {
					await loginWithRedirect();
				} catch (e) {
					alert('Failed to login');
					console.error('Failed to login:', e);
				}
			},
			user,
			isAuthenticated,
			postContent,
		};
	}
}
</script>