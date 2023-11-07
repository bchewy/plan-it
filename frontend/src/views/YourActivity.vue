<template>
	<NavBar />
	<div class="container-fluid bg-supergreen pb-3 position-relative" style="background-color: #a8cfa8;">
		<div class="sticky-top border-bottom" style="background-color:#a8cfa8; z-index: 1;">
			<CommunitySidebar></CommunitySidebar>
			<div class="text-center h2 mb-3 pt-4">
				<span class="header text-muted" style="font-weight: bold;">Your Activity </span>
			</div>
		</div>
		<div class="row justify-content-center">
			
			<span  v-for="post in posts">
			<PostComponent :key="post._id" :username="post.username" :profileImage="post.userprofile" :timePosted="post.timestamp" :badge="post.badge" :taggedFriends="post.taggedfriends" :liked="post.likes" :content="post.content" :postID="post._id" :useremail="user.email"></PostComponent>
			<div class="col justify-content-center d-flex">
				<button type="button" class="btn btn-danger" :id="post._id">Delete post! </button>
				
			</div>
		</span>
		</div>
	</div>
</template>
<script>
import CreatePostComponent from "../components/CreatePostComponent.vue"
import CommunitySidebar from "../components/CommunitySidebar.vue";
import NavBar from "../components/Navbar.vue";
import PostComponent from '../components/PostComponent.vue'
import { ref, onMounted,watch } from "vue";
import { useAuth0 } from '@auth0/auth0-vue';
import axios from "axios";

export default {
	name: 'Community',
	components: {
		NavBar,
		CreatePostComponent,
		PostComponent,
		CommunitySidebar,
	},
	setup() {
		const { loginWithRedirect, user, isAuthenticated } = useAuth0();
		const headers = { "x-api-key": "PlanItIsTheBestProjectEverXYZ", };
		const posts = ref([]);

		const fetchPosts = async () => {
			const url = `${import.meta.env.VITE_API_ENDPOINT}/posts`;
			const headers = { "x-api-key": "PlanItIsTheBestProjectEverXYZ", }
			try {
				const response = await axios.get(url, { headers })
				for (let i of response.data){
					if(i.useremail==user.value.email){
						posts.value.push(i)
					}
				}
				
			}
			catch (error) {
				console.error("error", error)
			}
		}

		watch(user, async (newUser) => {
        if (newUser) {
            await fetchPosts();
        }
    }, { immediate: true });

		return {
			user,
			posts,
			fetchPosts,

		};
	}
}
</script>

<style scoped>
.beige-colour {
  color: rgb(68, 49, 4);
}
</style>