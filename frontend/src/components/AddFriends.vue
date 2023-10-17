<template>
  <div>
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
    // const { user } = useAuth0();

    return {
      // user,
    };
  },
  data() {
    return {
      friendEmail: "",
    };
  },
  methods: {
    async addFriend() {
      if (!this.user.sub) {
        // console.log(user);
        console.error("User is not defined");
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
          }
        );
        const data = response.data;
        console.log("Friend added:", data);
      } catch (e) {
        console.error("Failed to add friend:", e);
      }
    },
  },
};
</script>
