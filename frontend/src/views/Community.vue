<style scoped>
.container-fluid {
	min-height: 100vh;
	padding-top: 3rem;
	background-color: #d1f4d1;
}
</style>
<template>
	<!-- nav -->
	<NavBar />
	<div class="container-fluid pt-3 bg-supergreen pb-3">
		<div class="container-fluid" style="background-color: #d1f4d1">
			<div class="row">
				<CommunitySidebar></CommunitySidebar>
				<div class="col-2"></div>
				<div class="col-10 h-100" style="background-color: rgb(232, 251, 240);">
					<h1 class="text-center py-3 text-muted" style="font-weight: bold;">For You Page</h1>
					<div class="row justify-content-center">
						<div class="col-8 rounded border bg-white">
							<textarea class="my-3 form-control" placeholder="Share something with the community!"></textarea>
							<div class="row mb-3 justify-content-between">
								<span class="col-1"></span>
								<Share_badge></Share_badge>
								<button class="btn btn-secondary col-3" type="button"><font-awesome-icon icon="fa-solid fa-tag" /> Tag a friend</button>
								<button class="btn btn-secondary col-3" type="button"><font-awesome-icon icon="fa-solid fa-plus-square" /> Create post!</button>
								<span class="col-1"></span>
							</div>
						</div>
					</div>
					<div class="row justify-content-center my-4">
						<div class="col-8 rounded border bg-white"><font-awesome-icon icon="fa-solid fa-user" class="mt-3"></font-awesome-icon> User<br><br>
							<heart_btn></heart_btn>
							<p>Post text</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<footer>
		<!-- footer -->
	</footer>
</template>
<script>
import CommunitySidebar from "../components/CommunitySidebar.vue";
import NavBar from "../components/Navbar.vue";
import { useAuth0 } from '@auth0/auth0-vue';
import heart_btn from "../components/like_button.vue";
import Share_badge from "../components/Share_badge.vue";
export default {
	name: 'Community',
	data() {

	},
	components: {
		NavBar,
		Share_badge,
		heart_btn,
		CommunitySidebar
	},
	setup() {
		const { loginWithRedirect, user, isAuthenticated } = useAuth0();
		const badges = false

		console.log('Setup method is called');

		return {
			login: async () => {
				console.log('Login button clicked');
				try {
					await loginWithRedirect();
				} catch (e) {
					alert('Failed to login');
					console.error('Failed to login:', e);
				}
			},
			user,
			isAuthenticated,
			badges
		};
	}
}
</script>
