<template>
    <NavBar />
    <div class="container-fluid bg-supergreen pb-3 position-relative" style="background-color: rgb(200, 209, 191);">
        <div class="sticky-top border-bottom" style="background-color:rgb(200, 209, 191); z-index: 1;">
            <CommunitySidebar></CommunitySidebar>
            <div class="text-center h2 mb-3 pt-4">
                <span class="header" style="font-weight: bold;">Your Friends </span>
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
    name: 'FriendCommunity',
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
        const friends = ref([]);


        const fetchData = async () => {
            await fetchUser();
            await fetchFriendPosts();
        };

        const fetchPosts = async () => {
            const url = `https://api.bchwy.com/posts`;
            try {
                const response = await axios.get(url, { headers })
                // posts.value = response.data.reverse()
            }
            catch (error) {
                console.error("error", error)
            }
        };

        const fetchFriendPosts = async () => {
            console.log("Fetching friends")
            console.log(friends.value)
            for (let friend of friends.value) {
                const url = `https://api.bchwy.com/users/${encodeURIComponent(friend)}/posts`;
                try {
                    const response = await axios.get(url, { headers });
                    posts.value = [...posts.value, ...response.data.posts];
                } catch (error) {
                    console.error("Error fetching friend's posts", error);
                }
            }

        };

        const fetchUser = async () => {
            const url = `https://api.bchwy.com/users/iz/${encodeURIComponent(user.value.email)}`;
            const headers = {
                "x-api-key": "PlanItIsTheBestProjectEverXYZ",
            };

            try {
                const response = await axios.get(url, { headers });
                friends.value = response.data.friends;
                console.log(friends.value)

            } catch (error) {
                console.error("Error fetching user", error);
            }
        };

        onMounted(fetchData);

        return {
            user,
            posts,
            fetchPosts,

        };
    }
}
</script>
