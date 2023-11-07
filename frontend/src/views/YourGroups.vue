<template>
    <!-- nav -->
    <NavBar />

    <CommunitySidebar></CommunitySidebar>


    <div class="container-fluid vh-100" style="background-color: #a8cfa8;">
        
        <div class="text-center h2 mb-3 pt-4">
				<span class="header text-muted" style="font-weight: bold;">Your Groups </span>
			</div>
            <div v-for="(groupArray, index) in groups" :key="index" class="row">
                <div v-for="group in groupArray" :key="group._id" class="col-md-4 mb-4">
                    <div class="card">
                        <img class="card-img-top" :src="group.group_image" alt="Group Image" v-if="group.group_image">
                        <div class="card-body">
                            <h5 class="card-title">{{ group.name }}</h5>
                            <p class="card-text">Owner: {{ group.owner_email }}</p>
                            
                            <p class="card-text">Members: {{ group.members.toString("\n") }}</p>
                        </div>
                    </div>
                </div>
            </div>
        


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
    onMounted(){
        // this.fetchData();
        this.getGroups()}
    ,
    setup() {
        const { loginWithRedirect, user, isAuthenticated } = useAuth0();
        const badges = false
        const groups = ref([]);

        // console.log('Setup method is called');

        const getGroups = async () => {
            try {
                console.log(user.value.email)
                const response = await axios.get(`${import.meta.env.VITE_API_ENDPOINT}/users/${encodeURIComponent(user.value.email)}/groups`, {
                    headers: {
                        'x-api-key': 'PlanItIsTheBestProjectEverXYZ'
                    }
                });
                // console.log(response);
                console.log(response.data.groups)
                groups.value = response.data.groups;
            } catch (error) {
                console.error(error);
            }
        }

        watch(user, (newUser) => {
            console.log(newUser); // Add this line
    if (newUser) {
        getGroups();
    }
});

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

<style scoped>

.beige-colour {
  color: rgba(236, 227, 206, 1);
}

</style>