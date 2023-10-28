<template>
  <Navbar />
  <div class="container">
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

  },
};
</script>
  