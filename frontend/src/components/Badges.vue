<template>
  <div v-if="isLoading" class="loading-screen">
    <div>Loading...</div>
  </div>
  <div v-else class="container">
    <div class="row">
      <div class="col-12 text-center mt-5">
        <h1>My Badges</h1>
      </div>
    </div>
    <!-- All Badges -->
    <div class="row justify-content-center mt-5">
      <div v-for="(badge, index) in badgesLoaded" :key=index class="card" style="width: 18rem; margin:0.5rem">

        <img :src="'../src/assets/badges/' + badge.icon" class="card-img-top">
        <div class="card-body d-flex flex-column">
          <h5 class="card-title">{{ badge.name }}</h5>
          <p class="card-text">{{ badge.description }}</p>
          <a href="community" class="btn btn-primary mt-auto">Share Badge</a>
        </div>
      </div>
      <button v-if="this.length == 3" @click="loadMore()" class="btn btn-link">Load More</button>
      <button v-else @click="showLess()" class="btn btn-link">Show Less</button>
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
      length: 3,
      badges: []
    };
  },
  created() {
    this.fetchData();
  },
  components: {
    Navbar
  },
  computed: {
    badgesLoaded() {
      return this.badges.slice(0, this.length);
    }
  },
  methods: {
    fetchData() {
      this.isLoading = true;
      this.fetchBadges();
      this.isLoading = false;
    },
    loadMore() {
      console.log(this.length)
      console.log(this.badges.length)
      this.length = this.badges.length;
      console.log(this.length)
    },
    showLess() {
      this.length = 3;
    },
    async fetchBadges() {
			const url = `${import.meta.env.VITE_API_ENDPOINT}/users/${encodeURIComponent(this.user.email)}/badges`;
			const headers = {
				"x-api-key": "PlanItIsTheBestProjectEverXYZ",
			};

			try {
				const response = await axios.get(url, { headers });
				this.badges = response.data.badges;

			} catch (error) {
				console.error("Error fetching badges", error);
			}
		},
  },
};
</script>

