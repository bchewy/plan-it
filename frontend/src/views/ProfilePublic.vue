<template>
  <Navbar />
  <div v-if="isLoading || !isAuthenticated" class="loading-screen">
    <div v-if="isLoading">Loading...</div>
    <div v-else class="row justify-content-center align-items-center" style="height: 100vh">
      <h3 class="text-center p-5">Please log in to use this feature</h3>
    </div>
  </div>
  <div v-else class="container">
    <div class="row">
      <div class="col-12 text-center mt-5">
        <h1>User Profile</h1>
      </div>
    </div>
    <!-- User Profile -->
    <div class="row justify-content-center mt-5">
      <!-- User Profile Column -->
      <div class="col-lg-3 col-md-6 col-sm-12 mb-4">
        <div class="card">
          <div class="card-header">
            <h3>{{ user.name }}</h3>
          </div>
          <div class="card-body">
            <div class="text-center mb-3">
              <img :src="user.picture" class="rounded-circle" alt="User profile picture" width="128" height="128" />
            </div>
            <div class="mb-3"><b>Given Name:</b> {{ user.given_name }}</div>
            <div class="mb-3"><b>Family Name:</b> {{ user.family_name }}</div>
            <div class="mb-3"><b>Nickname:</b> {{ user.nickname }}</div>
            <div class="mb-3"><b>Locale:</b> {{ user.locale }}</div>
            <div class="mb-3"><b>Last Updated:</b> {{ user.updated_at }}</div>
          </div>
        </div>
      </div>
    </div>
    <!-- Friends -->
    <div class="card mt-4 mb-4">
      <div class="card-header">
        <h3 class="mb-0">Friends</h3>
      </div>
      <div class="card-body">
        <div v-for="friend in friends" :key="friend" class="mb-4">
          <h5>{{ friend }}</h5>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import { useAuth0 } from "@auth0/auth0-vue";
import axios from "axios";

export default {
  created() {
    this.fetchData();
  },
  mounted() {
    this.fetchData();
  },
  watch: {
    isAuthenticated: {
      immediate: true,
      handler() {
        this.fetchData();
      },
    },
    user: {
      immediate: true,
      handler() {
        this.fetchData();
      },
    },
  },
  data() {
    const { user, isAuthenticated } = useAuth0();
    return {
      isLoading: false,
      user,
      isAuthenticated,
      friends: [],
    };
  },
  components: {
    Navbar,
  },
  methods: {
    fetchData() {
      this.isLoading = true;
      if (this.isAuthenticated) {
        this.fetchUser();
      }
      this.isLoading = false;
    },
    async fetchUser() {
      const url = `https://api.bchwy.com/users/${encodeURIComponent(this.user.email)}`;
      const headers = {
        "x-api-key": "PlanItIsTheBestProjectEverXYZ",
      };

      try {
        const response = await axios.get(url, { headers });
        console.log('Response received from fetching user.')
        this.friends = response.data.friends;

      } catch (error) {
        console.error("Error fetching user", error);
      }
    },
  },
};
</script>

