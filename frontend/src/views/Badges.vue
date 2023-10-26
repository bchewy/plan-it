<template>
  <Navbar />
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
      <div v-for="badge in badges" class="card" style="width: 18rem; margin:0.5rem">
        
        <img :src="'src/assets/badges/' + badge.icon"  class="card-img-top">
        <div class="card-body d-flex flex-column">
          <h5 class="card-title">{{badge.name}}</h5>
          <p class="card-text">{{badge.description}}</p>
          <button class="btn btn-primary mt-auto">Share Badge</button>
          <Share_badge></Share_badge>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import Share_badge from "../components/Share_badge.vue";
import axios from "axios";

export default {
  data() {
    return {
      isLoading: false,
      badges: [
    {
      "description": "Congratulations on taking your first step toward a greener planet!",
      "icon": "green_newbie_icon.png",
      "id": "badge_1",
      "milestone": "First carbon footprint calculation",
      "name": "Green Newbie"
    },
    {
      "description": "You've offset the carbon footprint of your travels for one month!",
      "icon": "eco_friendly_traveler_icon.png",
      "id": "badge_2",
      "milestone": "Offset one month of travel",
      "name": "Eco-Friendly Traveler"
    },
    {
      "description": "One week of sustainable eating choices. Way to go!",
      "icon": "foodprint_fighter_icon.png",
      "id": "badge_3",
      "milestone": "One week of sustainable food choices",
      "name": "Foodprint Fighter"
    },
    {
      "description": "You've converted to using solar energy at home.",
      "icon": "solar_superstar_icon.png",
      "id": "badge_4",
      "milestone": "Switch to solar energy",
      "name": "Solar Superstar"
    },
    {
      "description": "Recycled items for 30 consecutive days!",
      "icon": "recycle_ranger_icon.png",
      "id": "badge_5",
      "milestone": "30 days of recycling",
      "name": "Recycle Ranger"
    },
    {
      "description": "You've inspired 5 friends to join the app and start tracking their footprint.",
      "icon": "community_catalyst_icon.png",
      "id": "badge_6",
      "milestone": "Refer 5 friends",
      "name": "Community Catalyst"
    },
    {
      "description": "Achieved a zero-waste lifestyle for one month.",
      "icon": "zero_waste_warrior_icon.png",
      "id": "badge_7",
      "milestone": "One month of zero-waste",
      "name": "Zero-Waste Warrior"
    }
  ]

    };
  },
  created() {
    //this.fetchData();
  },
  components: {
    Navbar,
    Share_badge
  },
  methods: {
    fetchData() {
      this.isLoading = true;
      this.fetchBadges();
      this.isLoading = false;
    },
    async fetchBadges() {
      const url = `http://127.0.0.1:5000/users/ez/${this.$route.params.userEmail}/badges`;
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

