<template>
    <!-- nav -->
    <NavBar />


    <body class="position-relative">
        <div class="container-fluid">
            <div class="row">
                <CommunitySidebar></CommunitySidebar>
                <div class="col-2"></div>
                <div class="col-10 h-100" style="background-color: rgb(232, 251, 240);">

                    <h1 class="text-center py-3 text-muted" style="font-weight: bold;">Your Groups Page</h1>


                </div>

            </div>
        </div>









    </body>
    <footer>
        <!-- footer -->
    </footer>
</template>
<script>

import NavBar from "../components/Navbar.vue";
import CommunitySidebar from "../components/CommunitySidebar.vue";
import { useAuth0 } from '@auth0/auth0-vue';
import Share_badge from "../components/Share_badge.vue";
export default {

    data() {

    },
    components: {
        NavBar,
        CommunitySidebar,
        Share_badge
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
