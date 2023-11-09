<template>
  <Navbar />
  <div v-if="isLoading" class="loading-screen">
    <div>Loading...</div>
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
              <img :src="user.pictureurl" class="rounded-circle" alt="User profile picture" width="128" height="128" />
            </div>
            <div class="mb-3"><b>Email:</b> {{ user.email }}</div>
            <div class="mb-3"><b>Experience:</b> {{ user.exp }}</div>
            <div class="mb-3"><b>Level:</b> {{ user.level }}</div>
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
          <h5>
            <router-link :to="`/profile/public/${friend}`">{{ friend }}</router-link>
          </h5>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import axios from "axios";

export default {
  data() {
    return {
      isLoading: false,
      user: {},
      friends: [],
    };
  },
  created() {
    this.fetchData();
  },
  components: {
    Navbar,
  },
  methods: {
    fetchData() {
      this.isLoading = true;
      this.fetchUser();
      this.isLoading = false;
    },
    async fetchUser() {
      const url = `${import.meta.env.VITE_API_ENDPOINT}/users/ez/${this.$route.params.userEmail}`;
      const headers = {
        "x-api-key": `${import.meta.env.VITE_API_KEY}`,
      };

      try {
        const response = await axios.get(url, { headers });
        this.user = response.data;
        this.friends = response.data.friends;

      } catch (error) {
        console.error("Error fetching user", error);
      }
    },
  },
};
</script>

