<template>
  <div class="row justify-content-center my-4 ">
    <div class="col-10 rounded border bg-white position-relative px-4 pt-3">
      <div class="row">
        <div class="col d-flex align-items-center px-2">
          <img :src="profileImage" class="rounded-circle" style="width:40px;">
          <span class="fw-bold ms-2"> {{ username }} </span>
        </div>
      </div>
      <br>
      <div class="mx-1">
        <span v-html="content"></span>
        <div v-if="taggedFriends.length != 0"><br><span style="font-size: smaller;font-style: italic;" v-for="friend in taggedFriends"> {{ friend.handle }} &nbsp; </span></div>
      </div>
      <div v-if="badge != ''">
        <div class="border-rounded border mt-3 " style="background-color: rgb(218, 239, 216);">
          <div class="row">
            <div class="col-3 justify-content-end d-flex my-3 ms-3">
              <br> <img :src="badgeDetails.image" style="width:100%" class="rounded-circle">
            </div>
            <div class="col ms-2 mt-2 align-items-center d-flex">
              <p class="fs-5"><span class="fw-bold fs-3">{{ badgeDetails.name }} </span><br><br> {{ badgeDetails.description }} <br><br> <strong>Milestone:</strong> {{ badgeDetails.milestone }}</p>
            </div>
          </div>
        </div>
      </div>
      <br>
      <span class="text-muted">{{ timePosted }}</span>
      <hr>
      <div class="text-muted fw-bold mb-2">{{ likesCount.value }} likes</div>
      <heart_btn :postID="postID" :useremail="useremail" @updateLikes="updateLikes"></heart_btn>
      <br><br>
    </div>
  </div>
</template>


<script>
import { defineComponent, reactive } from 'vue';
import heart_btn from './like_button.vue'
import axios from 'axios';


export default defineComponent({
  name: 'PostComponent',
  components: {
    heart_btn
  },
  data() {
    const likesCount = reactive({ value: this.liked.length });
    return {
      badgeDetails: {},
      likesCount,
    }
  },
  props: {
    username: String,
    badge: String,
    taggedFriends: Array,
    profileImage: String,
    timePosted: String,
    content: String,
    liked: Array,
    comments: Array,
    postID: String,
    useremail: String
  },
  async created() {
    if (this.badge != '') {
      const url = `${import.meta.env.VITE_API_ENDPOINT}/badges/${this.badge}`;
      const headers = {
        "x-api-key": "PlanItIsTheBestProjectEverXYZ",
      };
      try {
        const response = await axios.get(url, { headers })
        this.badgeDetails = {
          id: this.badge,
          name: response.data.name,
          image: response.data.image,
          description: response.data.description,
          milestone: response.data.milestone
        }
      }
      catch (error) {
        console.error("error", error)
      }

    }
  },
  methods: {
    updateLikes(newLikesCount) {
      this.likesCount.value = newLikesCount;
    }
  }


})




</script>