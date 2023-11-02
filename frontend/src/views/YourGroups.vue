<template>
    <!-- nav -->
    <NavBar />

    <CommunitySidebar></CommunitySidebar>


    <div class="container-fluid vh-100" style="background-color: rgb(232, 251, 240);">
        <section class="py-5">
            <h1 class="text-center mb-5" style="font-weight: bold; color: #4CAF50;">Your Groups</h1>
            <div v-for="(groupArray, index) in groups" :key="index" class="row">
                <div v-for="group in groupArray" :key="group._id" class="col-md-4 mb-4">
                    <div class="card">
                        <img class="card-img-top" :src="group.group_image" alt="Group Image" v-if="group.group_image">
                        <div class="card-body">
                            <h5 class="card-title">{{ group.name }}</h5>
                            <p class="card-text">Owner: {{ group.owner_email }}</p>
                            <p class="card-text">Members: {{ group.members.join(', ') }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>


    </div>


    <footer>
        <!-- footer -->
    </footer>
</template>
<script>

import NavBar from "../components/Navbar.vue";
import CommunitySidebar from "../components/CommunitySidebar.vue";
import { useAuth0 } from '@auth0/auth0-vue';
import axios from "axios";
import { ref, defineComponent, computed, reactive, watch, onMounted } from "vue";

export default {
    components: {
        NavBar,
        CommunitySidebar

    },
    created() {

    },
    setup() {
        const { loginWithRedirect, user, isAuthenticated } = useAuth0();
        const badges = false
        const groups = ref([]);

        console.log('Setup method is called');

        const getGroups = async () => {
            try {
                console.log(user.value.email)
                const email = user.value.email;
                const response = await axios.get(`${import.meta.env.VITE_API_ENDPOINT}/users/${encodeURIComponent(user.value.email)}/groups`, {
                    headers: {
                        'x-api-key': 'PlanItIsTheBestProjectEverXYZ'
                    }
                });
                // console.log(response);
                groups.value = response.data;
            } catch (error) {
                console.error(error);
            }
        }

        watch(user, (newUser, oldUser) => {
            if (newUser !== null) {
                getGroups();
            }
        }, { immediate: false });

        return {
            login: async () => {
                console.log('Login button clicked');
                try {
                    await loginWithRedirect();
                    // console.log('User:', user);
                    // console.log('Authenticated:', isAuthenticated);
                } catch (e) {
                    alert('Failed to login');
                    console.error('Failed to login:', e);
                }
            },
            user,
            isAuthenticated,
            badges,
            getGroups,
            groups
        };
    }
}
</script>
