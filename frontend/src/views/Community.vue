<template>
	<NavBar />
	<div class="container-fluid bg-supergreen pb-3 vh-100 position-relative" style="background-color:#cbdbb7">

		<div class="sticky-top border-bottom" style="background-color:#cbdbb7; z-index: 1;">
			<CommunitySidebar></CommunitySidebar>

			<div class="text-center h2 mb-3 pt-4">
				<span class="header text-muted" style="font-weight: bold;">For You </span>
			</div>
		</div>
		<div v-if="IsbackendConnected" class="row justify-content-center bg-supergreen">
			<CreatePostComponent @postCreated="fetchPosts"></CreatePostComponent>
			<PostComponent v-for="post in posts" :key="post._id" :username="post.username" :profileImage="post.userprofile" :timePosted="post.timestamp" :badge="post.badge" :taggedFriends="post.taggedfriends" :liked="post.likes" :content="post.content" :postID="post._id" :useremail="user.email"></PostComponent>
		</div>
		<div v-else>
			<FailBackend></FailBackend>
		</div>
	</div>
</template>
<script>
import CreatePostComponent from "../components/CreatePostComponent.vue"
import CommunitySidebar from "../components/CommunitySidebar.vue";
import NavBar from "../components/Navbar.vue";
import PostComponent from '../components/PostComponent.vue'
import FailBackend from "../components/FailBackend.vue";
import { ref, onMounted } from "vue";
import { useAuth0 } from '@auth0/auth0-vue';
import axios from "axios";
// import { toast } from 'vue3-toastify';

export default {
	name: 'Community',
	components: {
		NavBar,
		CreatePostComponent,
		PostComponent,
		CommunitySidebar,
		FailBackend,
	},
	setup() {
		const { loginWithRedirect, user, isAuthenticated } = useAuth0();
		const headers = { "x-api-key": `${import.meta.env.VITE_API_KEY}`, };
		const posts = ref([]);
		const IsbackendConnected = ref(false);
		const fetchPosts = async () => {
			const url = `${import.meta.env.VITE_API_ENDPOINT}/posts`;
			try {
				const response = await axios.get(url, { headers })
				posts.value = response.data.reverse()
				console.log(posts.value)
				IsbackendConnected.value = true;
			}
			catch (error) {
				console.error("error", error);
				IsbackendConnected.value = false;
				// toast.error(`Encountered an error on the backend. ${error}. Please try again later.`, {
				// 	autoClose: 5000,
				// 	position: toast.POSITION.TOP_CENTER,
				// });

			}
		}

		// if (hasError.value) {
		// 	toast.error(`Encountered an error on the backend. ${error}. Please try again later.`, {
		// 		autoClose: 5000,
		// 		position: toast.POSITION.TOP_CENTER,
		// 	});
		// };

		onMounted(fetchPosts);

		return {
			user,
			posts,
			fetchPosts,
			IsbackendConnected,

		};
	}
}
</script>

<style scoped>
.beige-colour {
	color: rgb(68, 49, 4);
}

.bg-supergreen {
	background-color: #cbdbb7;
}
</style>