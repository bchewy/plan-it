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
			
			<div  v-for="post in posts">
			<PostComponent :key="post._id" :username="post.username" :profileImage="post.userprofile" :timePosted="post.timestamp" :badge="post.badge" :taggedFriends="post.taggedfriends" :liked="post.likes" :content="post.content" :postID="post._id" :useremail="user.email"></PostComponent>
			<div class="col justify-content-center d-flex">
				<button type="button" class="btn btn-danger" data-bs-toggle="modal" :data-bs-target="'#a'+post._id">Delete post! </button>
				<div class="modal fade" :id="'a'+post._id" tabindex="-1" :aria-labelledby="post._id" aria-hidden="true">
					<div class="modal-dialog">
						
						<div class="modal-content">
							
							
								
							
							<div class="modal-body fs-5 text-center">
								Are you sure you want to delete this post? <br>
								This action is <strong>irreversible</strong>!
							</div>
								<div class="modal-footer justify-content-center">
								<button type="button" class="btn btn-secondary col-3" data-bs-dismiss="modal" >Cancel</button>
								<button type="button" class="btn btn-danger col-3" data-bs-dismiss="modal" @click="deletePost(post._id)">Confirm</button>
								</div>
						</div>
					</div>
				</div>
			</div>
		</div>
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