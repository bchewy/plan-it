<style scoped></style>
<template>
	<!-- nav -->
	<NavBar />
	<div class="container-fluid bg-supergreen pb-3 position-relative" style="background-color: rgb(211, 233, 220);">

		
		<div class="sticky-top border-bottom" style="background-color: rgb(211, 233, 220); z-index: 1;">
		<CommunitySidebar ></CommunitySidebar>
	
			
			<div class="text-center h2 mb-3 py-4">
				<span class="text-muted" style="font-weight: bold;">For You</span>
			</div>
		</div>	
		
		
	
		<div class="row justify-content-center">
			
			
				<CreatePostComponent></CreatePostComponent>
				
				<PostComponent :username="sampleData.username" 
				:profileImage="sampleData.profileImage" 
				:timePosted="sampleData.timePosted" 
				:badge="sampleData.badge" 
				:taggedFriends="sampleData.taggedFriends"
				:liked="sampleData.liked"
				>Check out my new badge!</PostComponent>
	
				



		<div class="row justify-content-center my-4">

			<div class="col-10 rounded border bg-white"><font-awesome-icon icon="fa-solid fa-user" class="mt-3"></font-awesome-icon> User<br><br>
				<heart_btn></heart_btn>
				<p>Post text</p>
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
import PostComponent from '../components/PostComponent.vue'



export default {
	name: 'Community',
	data() {
		return{
			sampleData:{
				username:"Ryan",
				profileImage: "https://lh3.googleusercontent.com/a/ACg8ocJMqVngf0XBxJRe4tnMG_Q_kzEvs4Ier5N5-7V3fvw5=s96-c",
				timePosted: "13/10/2023 6:25pm",
				badge:"0",
				taggedFriends:["Brian","Melody","Saph"],
				liked:["email1","email2","email3"],
				comments:[{user:"Brian",comment:"Awesome stuff!"},{user:"Melody",comment:"Love to see that!"}]

			}
      
		

	}},
	components: {
		NavBar,
		CreatePostComponent,
		PostComponent,
		CommunitySidebar,


	},
	setup() {
		const { loginWithRedirect, user, isAuthenticated } = useAuth0();


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

		};
	}
}
</script>
