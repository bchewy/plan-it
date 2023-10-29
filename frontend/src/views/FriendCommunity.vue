<template>
    <!-- nav -->
    <NavBar />
    <div class="position-relative">
        <div class="container-fluid">
            <div class="row">
                <CommunitySidebar></CommunitySidebar>
                <div class="col-10 vh-100" style="background-color: rgb(232, 251, 240);">

                    <h1 class="text-center py-3 text-muted" style="font-weight: bold;">Your Friends Page</h1>
                    <div class="row justify-content-center">
                        <div class="col-8 rounded border bg-white">
                            <textarea class="my-3 form-control" placeholder="Share something with the community!"></textarea>
                            <div class="row mb-3 justify-content-between">
                                <span class="col-1"></span>


                           
                                <button class="btn btn-secondary col-3" type="button"><font-awesome-icon icon="fa-solid fa-tag" /> Tag a friend</button>
                                <button class="btn btn-secondary col-3" type="button"><font-awesome-icon icon="fa-solid fa-plus-square" /> Create post!</button>
                                <span class="col-1"></span>
                            </div>

                        </div>
                    </div>

                    <div class="row justify-content-center mt-5">

                        <div class="col-8 rounded border bg-white"><font-awesome-icon icon="fa-solid fa-user" class="mt-3"></font-awesome-icon> User<br><br>
                            <p>Post text</p>
                        </div>

                    </div>


                </div>

            </div>
        </div>









    </div>
</template>
<script>

import NavBar from "../components/Navbar.vue";
import CommunitySidebar from "../components/CommunitySidebar.vue";
import { useAuth0 } from '@auth0/auth0-vue';


export default {

    data() {

    },
    components: {
        NavBar,
        CommunitySidebar,
        
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
