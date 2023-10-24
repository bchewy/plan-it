
<template>
  <div>
    <header>
      <!-- nav -->
      <NavBar />
    </header>

    <div>
      <p class="text-center text-capitalize fs-1 fw-bold">Carbon-First Routing</p>
      <p class="text-secondary">Account for your own carbon footprint for your traffic taken, value-add and commit to reducing your carbon footprint and reduce your personal impact.</p>
      <a href="https://wad2.bchwy.com/route" class="btn text-uppercase text-light fw-bold px-sm-4 py-sm-3 Route">Route Now!</a>
    </div>

    <footer>
      <!-- footer -->
    </footer>
  </div>
</template>

<style>
  div {
    padding: 8px;
    position: relative;
  }

  p:first-child {
    color: #FFFF;
  }

  p {
    text-align: justify;
    line-height: 1.6;
  }

  .Route {
    background-color: rgb(209, 244, 209); /* Change the button color */
    border-radius: 10px; /* Add rounded corners */
    transition: outline 0.3s ease-in-out; /* Add transition for outline */
  }

  .Route:hover {
    outline: 2px solid #00FF00; /* Green outline on hover */
  }
</style>

<script>
import NavBar from '../components/Navbar.vue'
// import Login from '../components/Login.vue'
import { useAuth0 } from '@auth0/auth0-vue';

export default {
  name: 'Home',
  components: {
    NavBar,  // Register the NavBar component
    // Login
  },
  setup() {
    const { loginWithRedirect, user, isAuthenticated } = useAuth0();

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
    };
  }
}
</script>


