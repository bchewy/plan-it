<template>
	<NavBar />
	<div class="container-fluid bg-supergreen pb-3 position-relative" style="background-color: rgb(232, 251, 240);">
		<div class="sticky-top border-bottom" style="background-color:rgb(232, 251, 240); z-index: 1;">
			<CommunitySidebar></CommunitySidebar>
			<div class="text-center h2 mb-3 pt-4">
				<span class="header text-muted" style="font-weight: bold;">For You </span>
			</div>
		</div>
		<div class="row justify-content-center">
			<CreatePostComponent @postCreated="fetchPosts"></CreatePostComponent>
			<PostComponent v-for="post in posts" :key="post._id" :username="post.username" :profileImage="post.userprofile" :timePosted="post.timestamp" :badge="post.badge" :taggedFriends="post.taggedfriends" :liked="post.likes" :content="post.content" :postID="post._id" :useremail="user.email"></PostComponent>
		</div>
	</div>
</template>
<script>
import CreatePostComponent from "../components/CreatePostComponent.vue"
import CommunitySidebar from "../components/CommunitySidebar.vue";
import NavBar from "../components/Navbar.vue";
import PostComponent from '../components/PostComponent.vue'
import { ref, onMounted } from "vue";
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
			try {
				const response = await axios.get(url, { headers })
				posts.value = response.data.reverse()
				console.log(posts.value)
			}
			catch (error) {
				console.error("error", error)
			}
		}

		onMounted(fetchPosts);

		return {
			user,
			posts,
			fetchPosts,

		};
	}
}
</script>
