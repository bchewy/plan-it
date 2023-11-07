<template>
    <NavBar />
    
    <div class="container-fluid bg-supergreen pb-3 position-relative" style="background-color: #a8cfa8;">
        <div class="sticky-top border-bottom" style="background-color: #a8cfa8; z-index: 1;">
            <CommunitySidebar></CommunitySidebar>
            <div class="text-center h2 mb-3 pt-4">
                <span class="header text-muted" style="font-weight: bold;">Your Friends </span>
            </div>
        </div>
        <div class="row justify-content-center" style = "background-color:  #a8cfa8 ;">
            <CreatePostComponent @postCreated="fetchData"></CreatePostComponent>
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
    name: 'FriendCommunity',
    components: {
        NavBar,
        CreatePostComponent,
        PostComponent,
        CommunitySidebar,
    },
    created() {
        this.fetchData();
    },
    setup() {
        const { loginWithRedirect, user, isAuthenticated, isLoading } = useAuth0();
        const headers = { "x-api-key": "PlanItIsTheBestProjectEverXYZ", };
        const posts = ref([]);
        const friends = ref([]);

        const fetchData = async () => {

            // Debug Statements

            // Fixes a bug where refreshing the page does not retrieve users
            while (isLoading.value) {
                await new Promise(resolve => setTimeout(resolve, 100));
            }


            const url = `${import.meta.env.VITE_API_ENDPOINT}/users/iz/${encodeURIComponent(user.value.email)}`;
            const response = await axios.get(url, { headers });
            friends.value = response.data.friends;
            // Fetch posts per badge
            for (let friend of friends.value) {
                console.log("Fetching posts for friend", friend)
                const url = `${import.meta.env.VITE_API_ENDPOINT}/users/${encodeURIComponent(friend)}/posts`;
                const response = await axios.get(url, { headers });
                posts.value = [...posts.value, ...response.data].sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));;
            }


        };

        onMounted(fetchData);

        return {
            user,
            posts,
            friends,
            fetchData,
        };
    },

    computed: {
        async friendslist() {
            const url = `https://api.bchwy.com/users/${encodeURIComponent(this.user.email)}`
            const headers = {
                "x-api-key": "PlanItIsTheBestProjectEverXYZ",
            };
            try {
                const response = await axios.get(url, { headers })
                console.log(response.data)
            }

            catch (error) {
                console.error("error", error)

            }
        }
    }
}
</script>
<style scoped>

.beige-colour {
  color: rgba(236, 227, 206, 1);
}

</style>