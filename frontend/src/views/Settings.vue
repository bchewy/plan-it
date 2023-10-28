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
      <div class="col-12 mt-5">
        <h1>Notification Settings</h1>
      </div>
    </div>
    <div v-if="this.isSubmitted" class="alert alert-info" role="alert">
      Settings saved!
    </div>
    <div class="control-group col-12 mt-5">
      <div class="controls">
        <label><input type="checkbox" v-model="newFriends" />Notify me about new friends who signed up with my friend code </label>
        <br>
        <label><input type="checkbox" v-model="newFeatures" />Nofity me about new features of PlanIt! </label>
        <br>
        <label><input type="checkbox" v-model="lostPlace" />Notify me if I lose my place in the leaderboard</label>
      </div>
      <button class="btn btn-light" @click="reset()">Reset</button>
      <button class="btn btn-success" @click="submit()">Save</button>
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
    // console.log('Profile.vue: is authenticated?', isAuthenticated)
    // console.log('Profile.vue user', user)
    return {
      isLoading: false,
      currentPage: 1,
      itemsPerPage: 3,
      user,
      isAuthenticated,
      routes: [],
      friends: [],

      isSubmitted: false,
      newFriends: true,
      newFeatures: true,
      lostPlace: true,

    };
  },
  computed: {
  },
  components: {
    Navbar,
    MapItem,
    AddFriend,
  },
  methods: {
    submit() {
      this.isSubmitted = true;

    },
    reset() {
      this.newFriends = true;
      this.newFeatures = true;
      this.lostPlace = true;
    },


    fetchData() {
      this.isLoading = true;
      if (this.isAuthenticated) {
        this.fetchRoutes();
        this.fetchFriends();
      }
      this.isLoading = false;
    },
    async fetchRoutes() {
      console.log("Fetchin Routes!");
      const email = this.user.email; // Get the email from user object
      const url = `${import.meta.env.VITE_API_ENDPOINT}/routes/email?email=${encodeURIComponent(email)}`;
      const headers = {
        "x-api-key": "PlanItIsTheBestProjectEverXYZ", // Replace with your actual API key
      };
      try {
        const response = await axios.get(url, { headers });
        this.routes = response.data; // Assign the fetched routes to the routes data property
        console.log("Fetched routes!", response.data)
      } catch (error) {
        console.error("Error fetching routes:", error);
      }
    },
    async fetchFriends() {
      console.log("Fetching Friends!");
      const email = this.user.email; // Get the email from user object
      const url = `${import.meta.env.VITE_API_ENDPOINT}/friends?email=${encodeURIComponent(email)}`;
      const headers = {
        "x-api-key": "PlanItIsTheBestProjectEverXYZ", // Replace with your actual API key
      };
      try {
        const response = await axios.get(url, { headers });
        console.log('Fetched Friends!', response.data)
        this.friends = response.data; // Assign the fetched friends to the friends data property
      } catch (error) {
        console.error("Error fetching friends:", error);
      }
    },
  },
};
</script>
  