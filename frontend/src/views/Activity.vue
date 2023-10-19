<template>
  <header>
    <!-- nav -->
    <NavBar />
  </header>
  <!-- <Friends v-if="user" :user="user" /> -->

  <footer>
    <!-- footer -->
  </footer>
</template>
<script>
import NavBar from "../components/Navbar.vue";
// import Friends from "../components/Friends.vue";
import { useAuth0 } from "@auth0/auth0-vue";

export default {
  name: "Home",
  components: {
    NavBar,
    // Friends,
  },
  setup() {
    const { loginWithRedirect, user, isAuthenticated } = useAuth0();

    console.log("Setup method is called");
    console.log("user is here", user);
    return {
      login: async () => {
        console.log("Login button clicked");
        try {
          await loginWithRedirect();
          // console.log('User:', user);
          // console.log('Authenticated:', isAuthenticated);
        } catch (e) {
          alert("Failed to login");
          console.error("Failed to login:", e);
        }
      },
      user,
      isAuthenticated,
    };
  },
};
</script>
