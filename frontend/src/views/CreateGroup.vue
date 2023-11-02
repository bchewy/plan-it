<template>
    <!-- nav -->
    <NavBar />
    <CommunitySidebar></CommunitySidebar>
    <div class="container-fluid" style="background-color: rgb(232, 251, 240);">
        <div class="row justify-content-center">

            <div class="col-10 vh-100">

                <h1 class="text-center py-3 text-muted" style="font-weight: bold;">Create your very group!</h1>
                <div class="row justify-content-center">

                    <form class="col-8 rounded border bg-white p-3" @submit.prevent="onSubmit">
                        <div class="mb-3 mt-3">
                            <label for="grpName" class="form-label">Enter your group name:</label>
                            <input type="text" class="form-control" id="grpName" placeholder="Group name" v-model="groupName">
                        </div>
                        <div class="mb-3">
                            <label for="grpImg" class="form-label">Select your group profile image:</label>
                            <input class="form-control" type="file" id="grpImg" @change="onFileChange">
                        </div>
                        <!-- <div class="form-check mb-3">
                            <label for="addFriends" class="form-label">Add your friends!</label>
                            <select class="form-control" id="addFriends" name="addFriends">
                                <option selected>1</option>
                                <option>2</option> 
                            </select>
                            </div> -->

                        <button type="submit" class="btn btn-primary"><font-awesome-icon icon="fa-solid fa-plus-square"></font-awesome-icon> Create group!</button>

                    </form>
                </div>




            </div>

        </div>
    </div>
</template>

<script>
import CommunitySidebar from "../components/CommunitySidebar.vue";
import NavBar from "../components/Navbar.vue";
import { useAuth0 } from '@auth0/auth0-vue';
import { ref, defineComponent, computed, reactive, watch, onMounted } from "vue";
import axios from "axios";
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

export default {
    data() {
        return {
            users: [],
            badges: []
        };
    },
    components: {
        NavBar,
        CommunitySidebar
    },
    setup() {
        const { loginWithRedirect, user, isAuthenticated } = useAuth0();
        const badges = false
        const groupName = ref('');
        const groupImage = ref(null);

        const createGroup = async (userEmail, groupName, groupImage) => {
            const url = `${import.meta.env.VITE_API_ENDPOINT}/users/${userEmail}/groups`;
            const formData = new FormData();
            formData.append('group_name', groupName);
            formData.append('group_image', groupImage);
            const response = await axios.post(url, formData, {
                headers: {
                    'X-Api-Key': 'PlanItIsTheBestProjectEverXYZ'
                }
            });
            const result = response.data;
            if (response.status === 200) {
                toast.success(`Group has been successfully created!`, {
                    autoClose: 5000,
                    position: toast.POSITION.TOP_CENTER,
                });
                document.getElementById('createGroupForm').reset();
                return result;

            } else {
                // alert(result.message);
                throw new Error(result.message);
            }
        };

        const onFileChange = (e) => {
            groupImage.value = e.target.files[0];
        };

        const onSubmit = async () => {
            try {
                const result = await createGroup(user.value.email, groupName.value, groupImage.value);
                // console.log(result);
            } catch (error) {
                console.error(error.response.data.message);
                toast.error(`${error.response.data.message}`, {
                    autoClose: 5000,
                    position: toast.POSITION.TOP_CENTER,
                });
            }
        };


        return {
            login: async () => {
                console.log('Login button clicked');
                try {
                    await loginWithRedirect();
                } catch (e) {
                    alert('Failed to login');
                    console.error('Failed to login:', e);
                }
            },
            user,
            isAuthenticated,
            badges,
            groupName,
            groupImage,
            onFileChange,
            onSubmit,
            createGroup
        };
    }
}
</script>
