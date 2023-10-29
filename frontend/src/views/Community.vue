<style scoped></style>
<template>
	<!-- nav -->
	<NavBar />
	<div class="container-fluid bg-supergreen pb-3 position-relative" style="background-color: rgb(232, 251, 240);">

		
		<div class="row">
			<div style="position:sticky">
			<div class="col">
			<CommunitySidebar></CommunitySidebar>
			</div>
			<span class="text-center py-3 text-muted h3" style="font-weight: bold;">For You</span>
			</div>
				<CreatePostComponent></CreatePostComponent>
				
	
				
				<div class="row justify-content-center my-4">
					
					<div class="col-11 rounded border bg-white"><font-awesome-icon icon="fa-solid fa-user" class="mt-3"></font-awesome-icon> User<br><br>
						<heart_btn></heart_btn>
						<p>Post text</p>
					</div>
				</div>

				<div class="row justify-content-center my-4">
					<div class="col-11 rounded border bg-white"><font-awesome-icon icon="fa-solid fa-user" class="mt-3"></font-awesome-icon> User<br><br>
						<heart_btn></heart_btn>
						<p>Post text</p>
					</div>
				</div>

				<div class="row justify-content-center my-4">
					<div class="col-11 rounded border bg-white"><font-awesome-icon icon="fa-solid fa-user" class="mt-3"></font-awesome-icon> User<br><br>
						<heart_btn></heart_btn>
						<p>Post text</p>
					</div>
				</div>

				<div class="row justify-content-center my-4">
					<div class="col-11 rounded border bg-white"><font-awesome-icon icon="fa-solid fa-user" class="mt-3"></font-awesome-icon> User<br><br>
						<heart_btn></heart_btn>
						<p>Post text</p>
					</div>
				</div>
			</div>
		</div>
	<footer>
		<!-- footer -->
	</footer>
</template>
<script>
import CreatePostComponent from "../components/CreatePostComponent.vue"
import CommunitySidebar from "../components/CommunitySidebar.vue";
import NavBar from "../components/Navbar.vue";
import { useAuth0 } from '@auth0/auth0-vue';
import heart_btn from "../components/like_button.vue";


export default {
	name: 'Community',
	data() {

	},
	components: {
		NavBar,
		CreatePostComponent,
		heart_btn,
		CommunitySidebar,
	
		
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
