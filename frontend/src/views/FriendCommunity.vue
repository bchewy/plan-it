<template>
    <NavBar />
    <div class="container-fluid pb-3 position-relative vh-100" style="background-color: #cbdbb7;">
        <div class="sticky-top border-bottom" style="background-color: #cbdbb7; z-index: 1;">
            <CommunitySidebar></CommunitySidebar>
            <div class="text-center h2 mb-3 pt-4" style="background-color: #cbdbb7;">
                <span class="header text-muted" style="font-weight: bold;">Your Friends</span>
            </div>
        </div>
        <div class="row justify-content-center" style="background-color: #cbdbb7;">
            <div v-if="posts">
                <PostComponent v-for=" post in posts" :key="post._id" :username="post.username" :profileImage="post.userprofile" :timePosted="post.timestamp" :badge="post.badge" :taggedFriends="post.taggedfriends" :liked="post.likes" :content="post.content" :postID="post._id" :useremail="user.email">
                </PostComponent>
            </div>
            <div v-else>
                You don't have any posts from your friends.
            </div>

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
import { toast } from 'vue3-toastify';

export default {
    name: 'FriendCommunity',
    components: {
        NavBar,
        CreatePostComponent,
        PostComponent,
        CommunitySidebar,
    },
    setup() {
        const { loginWithRedirect, user, isAuthenticated, isLoading } = useAuth0();
        const headers = { "x-api-key": `${import.meta.env.VITE_API_KEY}`, };
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
                posts.value = [...posts.value, ...response.data].sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
                // console.log(posts.value)
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
                "x-api-key": `${import.meta.env.VITE_API_KEY}`,
            };
            try {
                const response = await axios.get(url, { headers })
                // console.log(response.data)
            }
            catch (error) {
                console.error("error", error)
                toast.error(`${error.response.data.message}`, {
                    autoClose: 5000,
                    position: toast.POSITION.TOP_CENTER,
                });

            }
        }
    }
}
</script>
<style scoped>
.beige-colour {
    color: rgba(236, 227, 206, 1);
}

.bg-supergreen {
    background-color: #a8cfa8;
}
</style>