<template>
  <!-- Profile page bugs: -->

  <!--  Fix the issue with the routes not being loaded after a refresh -->
  <Navbar />

  <div
    v-if="!isAuthenticated"
    class="row justify-content-center align-items-center"
    style="height: 100vh"
  >
    <h3 class="text-center p-5">Please log in to use this feature</h3>
  </div>
  <div v-else class="container">
    <div class="row">
      <div class="col-12 text-center mt-5">
        <h1>User Profile</h1>
      </div>
    </div>
    <div class="alert alert-info" role="alert">
      You are signed in with Google. Profile editing is disabled.
    </div>
    <div class="row justify-content-center mt-5">
      <!-- User Profile Column -->
      <div class="col-lg-3 col-md-6 col-sm-12 mb-4">
        <div class="card">
          <div class="card-header">
            <h3>{{ user.name }}</h3>
          </div>
          <div class="card-body">
            <div class="text-center mb-3">
              <img
                :src="user.picture"
                class="rounded-circle"
                alt="User profile picture"
                width="128"
                height="128"
              />
            </div>
            <div class="mb-3"><b>Given Name:</b> {{ user.given_name }}</div>
            <div class="mb-3"><b>Family Name:</b> {{ user.family_name }}</div>
            <div class="mb-3"><b>Nickname:</b> {{ user.nickname }}</div>
            <div class="mb-3"><b>Email:</b> {{ user.email }}</div>
            <div class="mb-3"><b>Locale:</b> {{ user.locale }}</div>
            <div class="mb-3"><b>Last Updated:</b> {{ user.updated_at }}</div>
          </div>
        </div>
      </div>
      <div class="col-lg-9 col-md-6 col-sm-12 mb-4">
        <div class="card">
          <div class="card-header">
            <h3>Routes</h3>
          </div>
          <div class="card-body">
            <!-- Shows if empty -->
            <div v-if="routes && routes.length == 0">
              <p class="text-center text-muted">
                Your route list is empty. You need to commit more.
              </p>
            </div>
            <div v-for="route in paginatedRoutes" :key="route.route_id" class="mb-4">
              <h5>{{ route.start_point_name }} to {{ route.end_point_name }}</h5>
              <p><b>Mode of Transport:</b> {{ route.transport_mode }}</p>
              <p><b>Carbon Emission:</b> {{ route.carbon_emission }}</p>
              <p><b>Timestamp:</b> {{ new Date(route.timestamp).toLocaleString() }}</p>
            </div>
            <!-- Pagination controls -->
            <nav aria-label="Pagination-for-routes">
              <ul class="pagination justify-content-center">
                <li class="page-item" :class="{ disabled: currentPage === 1 }">
                  <a class="page-link" href="#" @click.prevent="currentPage--"
                    >Previous</a
                  >
                </li>
                <!-- Page count -->
                <li class="page-item disabled">
                  <span class="page-link">{{ currentPage }} / {{ totalPages }}</span>
                </li>
                <li class="page-item" :class="{ disabled: currentPage >= totalPages }">
                  <a class="page-link" href="#" @click.prevent="currentPage++">Next</a>
                </li>
              </ul>
            </nav>
          </div>
        </div>
      </div>
    </div>
    <!-- Friends Section -->
    <div class="row justify-content-center mt-5">
      <div class="col-lg-9 col-md-6 col-sm-12 mb-4">
	  	<AddFriend :user="user"/>
        <div class="card">
          <div class="card-header">
            <h3>Friends</h3>
          </div>
          <div class="container"></div>
          <div class="card-body">
            <!-- Shows if empty -->
            <div v-if="friends && friends.length == 0">
              <p class="text-center text-muted">
                Your friends list is empty. Add some friends!
              </p>
            </div>
            <div v-for="friend in friends" :key="friend.friend_email" class="mb-4">
              <h5>{{ friend }}</h5>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MapItem from "../components/MapItem.vue";
import AddFriend from "../components/AddFriends.vue";
import Navbar from "../components/Navbar.vue";
// import NotAuthenticated from '../components/NotAuthenticated.vue';
import { useAuth0 } from "@auth0/auth0-vue";
import axios from "axios";

export default {
  data() {
    const { user, isAuthenticated } = useAuth0();
    // console.log('Profile.vue: is authenticated?', isAuthenticated)
    // console.log('Profile.vue user', user)
    return {
      currentPage: 1,
      itemsPerPage: 3,
      user,
      isAuthenticated,
      routes: [],
      friends: [],
    };
  },
  computed: {
    // For pagination
    paginatedRoutes() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      const end = start + this.itemsPerPage;
      return this.routes.slice(start, end);
    },
    // Total pages
    totalPages() {
      return Math.ceil(this.routes.length / this.itemsPerPage);
    },
  },
  components: {
    Navbar,
    MapItem,
	AddFriend,
  },
  // Could be replaced with setup() or etc so that it refreshes on reset
  created() {
    if (this.isAuthenticated) {
      this.fetchRoutes();
      this.fetchFriends();
    }
  },
  methods: {
    async fetchRoutes() {
      console.log("Fetching!");
      const email = this.user.email; // Get the email from user object
      const url = `https://api.bchwy.com/routes/email?email=${encodeURIComponent(email)}`;
      const headers = {
        "x-api-key": "PlanItIsTheBestProjectEverXYZ", // Replace with your actual API key
      };
      try {
        const response = await axios.get(url, { headers });
        this.routes = response.data; // Assign the fetched routes to the routes data property
      } catch (error) {
        console.error("Error fetching routes:", error);
      }
    },
    async fetchFriends() {
      console.log("Fetching Friends!");
      const email = this.user.email; // Get the email from user object
      const url = `https://api.bchwy.comfriends?email=${encodeURIComponent(email)}`;
      const headers = {
        "x-api-key": "PlanItIsTheBestProjectEverXYZ", // Replace with your actual API key
      };
      try {
        const response = await axios.get(url, { headers });
		console.log('fetching friends but data tho',response.data)
        this.friends = response.data; // Assign the fetched friends to the friends data property
      } catch (error) {
        console.error("Error fetching friends:", error);
      }
    },
  },
};
</script>
