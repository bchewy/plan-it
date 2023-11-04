<template>
  <link rel="stylesheet" href="likebuttontest.scss">
  <button :class="['heart-btn', { liked: this.liked }]" @click="heartit">
    <svg class="heart heart_icon" viewBox="0 0 32 29.6">
      <path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2
      c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z" />
    </svg>
  </button>
</template>
<script>
import axios from 'axios';
import { defineComponent } from 'vue';


export default defineComponent(
  {
    name: 'heart_btn',
    props: {
      postID: String,
      useremail: String
    },
    emits: ['updateLikes'],  // Declare the custom events


    data() {
      return {
        liked: false
      }
    },
    async created() {
      const url = `https://api.bchwy.com/posts/${this.postID}`
      const headers = {
        "x-api-key": "PlanItIsTheBestProjectEverXYZ",
      };
      try {
        const response = await axios.get(url, { headers })
        if (response.data.likes.includes(this.useremail)) {
          this.liked = true
        }
        else {
          this.liked = false
        }
      }
      catch (error) {
        console.error("error", error)
      }
    }
    ,


    methods: {
      heartit: async function (e) {
        const hearts = document.createElement('div');
        hearts.innerHTML = '<svg class="heart heart-pop one" viewBox="0 0 32 29.6"><path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z"/></svg><svg class="heart heart-pop two" viewBox="0 0 32 29.6"><path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z"/></svg><svg class="heart heart-pop three" viewBox="0 0 32 29.6"><path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z"/></svg><svg class="heart heart-pop four" viewBox="0 0 32 29.6"><path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z"/></svg><svg class="heart heart-pop five" viewBox="0 0 32 29.6"><path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z"/></svg><svg class="heart heart-pop six" viewBox="0 0 32 29.6"><path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z"/></svg><svg class="heart heart-pop seven" viewBox="0 0 32 29.6"><path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z"/></svg><svg class="heart heart-pop eight" viewBox="0 0 32 29.6"><path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z"/></svg><svg class="heart heart-pop nine" viewBox="0 0 32 29.6"><path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z"/></svg>';
        e.target.appendChild(hearts);
        // Call the corresponding backend method when the heart button is clicked
        if (!this.liked) {
          const response = await this.likePost();
          if (response.status === 200) {
            this.liked = true;
            this.$emit('updateLikes', response.data.likes_count);
            console.log("liked");
            console.log(response.data.likes_count);


          }
        } else {
          const response = await this.unlikePost();
          if (response.status === 200) {
            this.liked = false;
            this.$emit('updateLikes', response.data.likes_count);
            console.log("unliked");
            console.log(response.data.likes_count);

          }
        }
        // Remove the hearts after 3 seconds
        setTimeout(function () {
          e.target.removeChild(hearts);
        }, 3000);
      },

      likePost: async function () {
        const url = `http://127.0.0.1:5000/posts/${this.postID}/likes/add`
        const headers = {
          "x-api-key": "PlanItIsTheBestProjectEverXYZ",
          "Content-Type": "application/x-www-form-urlencoded"

        };
        return axios.post(url, `user_email=${encodeURIComponent(this.useremail)}`, { headers });

      },
      unlikePost: async function () {
        const url = `http://127.0.0.1:5000/posts/${this.postID}/likes/remove`
        const headers = {
          "x-api-key": "PlanItIsTheBestProjectEverXYZ",
          "Content-Type": "application/x-www-form-urlencoded"

        };
        return axios.post(url, `user_email=${encodeURIComponent(this.useremail)}`, { headers });
      }


    },
    mounted() {
      document.body.addEventListener('mousedown', function () {
        document.body.classList.add('using-mouse');
      });
      document.body.addEventListener('keydown', function () {
        document.body.classList.remove('using-mouse');
      });
    }
  })



</script>