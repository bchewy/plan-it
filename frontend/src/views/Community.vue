<style scoped>
</style>

<template>
	<!-- nav -->
	<NavBar />
	<div class="container-fluid bg-supergreen pb-3 position-relative" style="background-color: rgb(200, 209, 191);">

		
		<div class="sticky-top border-bottom" style="background-color:rgb(200, 209, 191); z-index: 1;">
		<CommunitySidebar ></CommunitySidebar>
	
			
			<div class="text-center h2 mb-3 pt-4">
				<span class="header" style="font-weight: bold;">For You </span>
			</div>
		</div>	
		
		
	
		<div class="row justify-content-center">
			
			
				<CreatePostComponent></CreatePostComponent>
				
				<PostComponent v-for="post in posts" :username="post.username" 
				:profileImage="post.userprofile" 
				:timePosted="post.timestamp" 
				:badge="post.badge" 
				:taggedFriends="post.taggedfriends"
				:liked="post.likes"
				:content="post.content"
				></PostComponent>
	
				



	
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
import axios from "axios";




export default {
	name: 'Community',
	data(){
		return{
			posts:[]
		}
	}
	,

async created(){
	const url = `https://api.bchwy.com/posts`;
		const headers = {
		"x-api-key": "PlanItIsTheBestProjectEverXYZ",
	};
	try{
		const response=await axios.get(url,{headers})
		this.posts=response.data.reverse()
		console.log(this.posts)
	}
	catch(error){
		console.error("error",error)
	}

 }
 ,
	

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
