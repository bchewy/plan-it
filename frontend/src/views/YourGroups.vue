<template>
    <!-- nav -->
    <NavBar />

    <CommunitySidebar></CommunitySidebar>



    <div class="container-fluid vh-100 bg-supergreen pb-3 position-relative" style="background-color: #cbdbb7;">
        <div class="sticky-top border-bottom" style="background-color:#cbdbb7; z-index: 1;">
            <CommunitySidebar></CommunitySidebar>
            <div class="text-center h2 mb-3 pt-4">
                <span class="header text-muted" style="font-weight: bold;">Your Groups </span>
            </div>
        </div>
        <div class="row" style="background-color: #cbdbb7;">


            <div v-if="loading">Loading...</div>

            <div v-else v-for="(group, index) in groups" :key="index" class="col-md-4 mb-4" style="background-color: #cbdbb7;">
                <div :key="group._id">

                    <div class="card">
                        <img class="card-img-top" :src="group.group_image" alt="Group Image" v-if="group.group_image">
                        <div class="card-body">

                            <h5 class="card-title fs-2 text-center">{{ group.name }}</h5>
                            <br>

                            <p class="card-text"> <span class="fw-bold">Owner:</span></p>
                            <p>{{ group.owner_email }}</p>

                            <p class="card-text"> <span class="fw-bold">Members:</span></p>
                            <ul class="list-group">
                                <li v-for="member in group.members " class="list-group-item bg-light">{{ member }}</li>
                            </ul> <br>

                            <div v-if="group.badges">
                                <p class="card-text"><span class="fw-bold">Badges:</span></p>


                                <div v-for="badge in group.badges" class="col-11 bg-light text-center rounded border mb-2">
                                    <img :src="badge.image" class="w-75 rounded-circle mb-3 mt-3"><br>
                                    <button class="btn btn-secondary mb-3" data-bs-toggle="modal" :data-bs-target="'#a' + badge._id">More info</button>

                                    <div class="modal fade" :id="'a' + badge._id" tabindex="-1" :aria-labelledby="badge._id" aria-hidden="true">
                                        <div class="modal-dialog">
                                            <div class="modal-content">
                                                <div class="modal-header">
                                                    <h5 class="modal-title" :id="badge.name">Badge Info</h5>
                                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                                </div>
                                                <div class="modal-body">
                                                    <div class="row">
                                                        <div class="col justify-content-end">
                                                            <img :src="badge.image" class="w-100">
                                                        </div>
                                                        <div class="col align-items-center d-flex">
                                                            <div> <span class="fw-bold fs-4">{{ badge.name }} </span><br><br> {{ badge.description }} <br><br><strong>Milestone:</strong> {{ badge.milestone }}</div>

                                                        </div>
                                                    </div>
                                                    <div class="modal-footer">

                                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                    </div>

                                </div>


                            </div>
                            <div v-else>
                                <p class="card-text"><span class="fw-bold">Badges:</span> None</p>
                            </div>
                        </div>
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

    }
    ,
    setup() {
        const loading = ref(true)
        const { loginWithRedirect, user, isAuthenticated, isLoading } = useAuth0();
        const badges = false
        const groups = ref([]);


        // console.log('Setup method is called');


        const getGroups = async () => {
            while (isLoading.value) {
                await new Promise(resolve => setTimeout(resolve, 100));
            }

            console.log(user.value.email)
            const response = await axios.get(`${import.meta.env.VITE_API_ENDPOINT}/users/${encodeURIComponent(user.value.email)}/groups`, {
                headers: {
                    'x-api-key': `${import.meta.env.VITE_API_KEY}`
                }
            });
            // console.log(response);
            console.log("groups")
            console.log(response.data.groups)
            groups.value = response.data.groups;
            // clearTimeout(timeoutId)
            // loading.value = false
        }

        onMounted(() => {
            getGroups();
            loading.value = false;
        });

        // const timeoutId = setTimeout(() => {
        //     loading.value = false;
        // }, 5000);

        // watch(user, async (newUser) => {
        //     if (newUser) {
        //         await getGroups();
        //     }
        // }, { immediate: true });

        return {
            user,
            isAuthenticated,
            loading,
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