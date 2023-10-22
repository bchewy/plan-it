<template>
  <div>
    <div v-if="errorMessage" class="alert alert-danger" role="alert">
      {{ errorMessage }}
    </div>
    <div v-if="successMessage" class="alert alert-success" role="alert">
      {{ successMessage }}
    </div>
    <form @submit.prevent="sendFriendRequest" class="form-inline">
      <div class="form-group mb-2">
        <label for="friendEmail" class="sr-only">Friend's Email:</label>
        <input id="friendEmail" v-model="friendEmail" type="email" class="form-control" required placeholder="Friend's Email" />
      </div>
      <button type="submit" class="btn btn-primary mb-2">Send Friend Request</button>
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
    async sendFriendRequest() {
      if (!this.user.sub) {
        this.errorMessage = "User prop wasn't passed properly.";
        return;
      }
      try {
        const response = await axios.post(
          "http://127.0.0.1:5000/friend_requests",
          {
            sender_email: this.user.email,
            receiver_email: this.friendEmail,
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
          this.errorMessage = "Friend not found";
          this.successMessage = "";
        } else if (response.status === 400) {
          this.errorMessage = "You cannot send a friend request to yourself";
          this.successMessage = "";
        } else if (response.status === 201) {
          this.errorMessage = "";
          this.successMessage = "Friend request sent successfully.";
        } else {
          this.errorMessage = "Unexpected response.";
        }
      } catch (e) {
        this.errorMessage = "Please try again later. The backend may be down.";
      }
    }
  },
};
</script>
