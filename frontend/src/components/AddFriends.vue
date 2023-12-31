<template>
  <div>
    <!-- <div v-if="errorMessage" class="alert alert-danger" role="alert">
      {{ errorMessage }}
    </div>
    <div v-if="successMessage" class="alert alert-success" role="alert">
      {{ successMessage }}
    </div> -->
    <form @submit.prevent="sendFriendRequest" class="d-flex flex-column flex-md-row align-items-start align-items-md-center">
      <div class="form-group mb-2 me-md-2 flex-grow-1">
        <label for="friendEmail" class="sr-only">Friend's Email:</label>
        <input id="friendEmail" v-model="friendEmail" type="email" class="form-control" required placeholder="Friend's Email" @input="searchFriends">
        <div v-if="searchResults.length" class="dropdown-menu show">
          <a v-for="result in searchResults" class="dropdown-item" @click="selectFriend(result)">{{ result.email }}</a>
        </div>
      </div>
      <button type="submit" class="btn btn-primary mb-2 flex-shrink-0">Send Friend Request</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import { useAuth0 } from "@auth0/auth0-vue";
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

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
      searchResults: [],
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
          `${import.meta.env.VITE_API_ENDPOINT}/users/${this.user.email}/friend_requests/send`,
          {
            friend_email: this.friendEmail,
          },
          {
            headers: {
              "Content-Type": "application/json",
              "x-api-key": `${import.meta.env.VITE_API_KEY}`, // Replace with your actual API key
            },
            validateStatus: function (status) {
              return status >= 200 && status < 500; // Resolve only if the status code is less than 500
            },
          }
        );
        if (response.status === 200) {
          this.successMessage = "Friend request sent successfully.";
          toast.success(`Friend request sent successfully.`, {
            autoClose: 5000,
            position: toast.POSITION.TOP_CENTER,
          });
          this.$emit('friendRequestSent'); // Emit an event to the parent component to update the page
        } else if (response.status === 400) {
          this.errorMessage = "Friend request already sent.";
          toast.error(`Friend request already sent!.`, {
            autoClose: 5000,
            position: toast.POSITION.TOP_CENTER,
          });
        } else if (response.status === 404) {
          this.errorMessage = "Friend not found.";
          toast.error(`Friend not found.`, {
            autoClose: 5000,
            position: toast.POSITION.TOP_CENTER,
          });
        }
      } catch (e) {
        this.errorMessage = "Please try again later. The backend may be down.";
        toast.error(`Please try again later. The backend may be down.`, {
          autoClose: 5000,
          position: toast.POSITION.TOP_CENTER,
        });
      }
      this.searchResults = []; // Clear the search results after sending the friend request
    },
    async searchFriends() {
      try {
        const response = await axios.get(
          `${import.meta.env.VITE_API_ENDPOINT}/users/search/${this.friendEmail}`,
          {
            headers: {
              "Content-Type": "application/json",
              "x-api-key": `${import.meta.env.VITE_API_KEY}`, // Replace with your actual API key
            },
          }
        );
        this.searchResults = response.data;
      } catch (e) {
        console.error(e);
      }
    },
    selectFriend(friend) {
      this.friendEmail = friend.email;
      this.searchResults = [];
    },
  },
};
</script>
