<template>
    <!-- nav -->
    <NavBar />


    <body class="position-relative">
        <div class="container-fluid">
            <div class="row">
                <CommunitySidebar></CommunitySidebar>
                <div class="col-2"></div>
                <div class="col-10 h-100" style="background-color: rgb(232, 251, 240);">

                    <h1 class="text-center py-3 text-muted" style="font-weight: bold;">Create your very group!</h1>
                    <div class="row justify-content-center">
                        <div class="col-8 rounded border bg-white">
                            <div class="mb-3 mt-3">
                                <label for="grpName" class="form-label">Enter your group name:</label>
                                <input type="text" class="form-control" id="grpName" placeholder="Group name" name="grpName">
                            </div>
                            <div class="mb-3">
                                <label for="grpImg" class="form-label">Select your group profile image:</label>
                                <img src="../assets/badges/community_catalyst_icon.png"> <!--v-model for grpImg here-->
                                <select class="form-control" id="grpImg" name="grpImg">
                                    <option selected>1</option>
                                    <option>2</option>
                                </select>
                            </div>
                            <div class="form-check mb-3">
                                <label for="addFriends" class="form-label">Add your friends!</label>

                                <select class="form-control" id="addFriends" name="addFriends">
                                    <option selected>1</option>
                                    <option>2</option> <!--friends list-->
                                </select>
                            </div>

                            <button type="submit" class="btn btn-primary"><font-awesome-icon icon="fa-solid fa-plus-square"></font-awesome-icon> Create group!</button>
                        </div>
                    </div>




                </div>

            </div>
        </div>

    </body>
    <footer>
        <!-- footer -->
    </footer>
</template>

<script>
import CommunitySidebar from "../components/CommunitySidebar.vue";
import NavBar from "../components/Navbar.vue";
// import Login from '../components/Login.vue'
import { useAuth0 } from '@auth0/auth0-vue';

import Share_badge from "../components/Share_badge.vue";
export default {

    data() {

    },
    components: {
        NavBar,
        Share_badge,
        CommunitySidebar
    },
    setup() {
        const { loginWithRedirect, user, isAuthenticated } = useAuth0();
        const badges = false

        console.log('Setup method is called');

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
            badges
        };
    }
}
</script>
