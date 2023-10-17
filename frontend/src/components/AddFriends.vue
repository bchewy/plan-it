<template>
  <div>
    <div v-if="errorMessage" class="alert alert-danger" role="alert">
      {{ errorMessage }}
    </div>
    <div v-if="successMessage" class="alert alert-success" role="alert">
      {{ successMessage }}
    </div>
    <form @submit.prevent="addFriend">
      <label for="friendEmail">Friend's Email:</label>
      <input id="friendEmail" v-model="friendEmail" type="text" required />
      <button type="submit">Add Friend</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import { useAuth0 } from "@auth0/auth0-vue";

export default {
  props: ["user"],
  setup() {
    return {};
  },
  data() {
    return {
      friendEmail: "",
      errorMessage: "",
      successMessage: "",
    };
  },
  methods: {
    async addFriend() {
      if (!this.user.sub) {
        this.errorMessage = "User prop wasn't passed properly.";
        return;
      }
      try {
        const response = await axios.post(
          "http://127.0.0.1:5000/friends",
          {
            user_id: this.user.sub,
            user_email: this.user.email,
            friend_email: this.friendEmail,
          },
          {
            headers: {
              "Content-Type": "application/json",
              "x-api-key": "PlanItIsTheBestProjectEverXYZ", // Replace with your actual API key
            },
            validateStatus: function (status) {
              return status >= 200 && status < 500; // Resolve only if the status code is less than 500
            },
          }
        );
        if (response.status === 404) {
          this.errorMessage = "Friend not found in database.";
          this.successMessage = "";
        } else if (response.status === 400) {
          if (response.data.message === "You can't add yourself!") {
            this.errorMessage = "Cannot add self.";
          } else {
            this.errorMessage = "Friend already added.";
          }
          this.successMessage = "";
        } else if (response.status === 201) {
          this.errorMessage = "";
          this.successMessage = "Friend added successfully.";
        } else {
          this.errorMessage = "Unexpected response.";
        }
      } catch (e) {
        this.errorMessage = "Please try again later. The backend may be down.";
      }
    },
  },
};
</script>
