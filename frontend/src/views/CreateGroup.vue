<template>
    <!-- nav -->
    <NavBar />
    <CommunitySidebar></CommunitySidebar>
    <div class="container-fluid" style="background-color: #a8cfa8;">
        <div class="row justify-content-center">

            <div class="col-10 vh-100">

                <h2 class="text-center py-3 text-colour" style="font-weight: bold;">Create your very group!</h2>
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
                        
                            <div class="mb-3">
                                <button class="btn btn-secondary col" type="button" data-bs-target="#friendsOverlay" data-bs-toggle="modal"><font-awesome-icon icon="fa-solid fa-plus" /> Select your members!</button>
				<!--tag friend model-->
				<div class="modal fade" id="friendsOverlay" tabindex="-1" aria-labelledby="friendsOverlayLabel" aria-hidden="true">
					<div class="modal-dialog">
						<div class="modal-content">
							<div class="modal-header">
								<h5 class="modal-title" id="TagFriendsModalLabel">Your friends</h5>
								<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
							</div>
							<div class="modal-body">
								<ul class="list-group">
                                    
									<li v-for="friend in friends" class="list-group-item bg-light"> <input type="checkbox" :value="friend.email" v-model="groupMembers" class="me-2">{{ friend.handle }} </li>

								</ul>
							</div>
							<div class="modal-footer">
								<button type="button" class="btn btn-secondary" data-bs-dismiss="modal" @click="groupMembers = []">Cancel</button>
								<button type="button" class="btn btn-primary" data-bs-dismiss="modal">Confirm</button>
							</div>
						</div>
					</div>
				</div>
                        </div>


                        <button type="submit" class="btn btn-success"><font-awesome-icon icon="fa-solid fa-plus-square"></font-awesome-icon> Create group!</button>

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
        const groupMembers=ref([]);
        const friends=ref([])

        const friendList= async()=>{
            
            const url = `${import.meta.env.VITE_API_ENDPOINT}/users/iz/${user.value.email}`
            
            const headers={
                    'X-Api-Key': 'PlanItIsTheBestProjectEverXYZ'
                }
            const response= await axios.get(url,{headers})
            for (let friend of response.data.friends){
                const friendDetailsURL = `${import.meta.env.VITE_API_ENDPOINT}/users/iz/${encodeURIComponent(friend)}`
				try {
					const friendDetailsResponse = await axios.get(friendDetailsURL, { headers });
					friends.value.push({ handle: "@" + friendDetailsResponse.data.handle, email: friendDetailsResponse.data.email})
				}
				catch (error) {
					console.error("error", error)
				}

            }
            console.log(friends)
        }
        
        const createGroup = async (userEmail, groupName, groupImage,groupMembers) => {
            const url = `${import.meta.env.VITE_API_ENDPOINT}/users/${userEmail}/groups`;
            const formData = new FormData();
            
            formData.append('group_name', groupName);
            formData.append('group_image', groupImage);
            formData.append('group_members',groupMembers)
            const response = await axios.post(url, formData,{
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
                
                const result = await createGroup(user.value.email, groupName.value, groupImage.value,groupMembers.value);
                // console.log(result);
            } catch (error) {
                console.error(error.response.data.message);
                toast.error(`${error.response.data.message}`, {
                    autoClose: 5000,
                    position: toast.POSITION.TOP_CENTER,
                });
            }
        };
        watch(user, async (newUser) => {
        if (newUser) {
            await friendList();
        }
    }, { immediate: true });


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
            groupMembers,
            friends,
            onFileChange,
            onSubmit,
            createGroup,
            friendList
        };
    }
}
</script>


<style scoped>

.beige-colour {
  color: rgba(236, 227, 206, 1);
}

</style>
