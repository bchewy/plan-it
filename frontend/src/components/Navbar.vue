<style scoped>
.bg-green {
  background-color: #3a5a40;
}

.bg-green2 {
  background-color: #a3b18a;
}

.text-evenlight {
  color: #a3b18a;
}

.text-evenlighter {
  color: white;
}

.text-supergreen {
  color: #a7c957;
}

.router-link-active {
  color: #a7c957;
}

.nav-item .dropdown-menu {
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  /* Add shadow to dropdown */
}

.nav-item .dropdown-menu .dropdown-item:hover {
  background-color: #006400;
}

.nav-item {
  margin: 0;
  /* Reset margin for nav item */
  padding: 0;
  /* Reset padding for nav item */
}


.navbar-nav .nav-link {
  display: block;
  /* Make sure the link takes up the full width and height of its container */
  line-height: 1.5;
  /* Adjust line height if necessary */
  padding: 0.5rem 1rem;
  /* Adjust padding as per your design */
  margin: 0;
  /* Reset margin for nav link */
  transition: background-color 0.3s, color 0.3s;
  /* Smooth hover transition */
}

.navbar-nav .nav-link:hover {
  /* background-color: #a3b18a; */
  color: #a7c957;
}

.dropdown-toggle::after {
  color: #a3b18a;
  /* Change dropdown arrow color */
}
</style>
<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-green">
    <div class="container">
      <a class="navbar-brand text-supergreen" href="#">
        <!-- <font-awesome-icon icon="fa-solid fa-car" bounce style="color: #a7c957" /> Plan-It -->
        <img src="https://bchewy-images.s3.ap-southeast-1.amazonaws.com/plan-it/bchewy+conscious+travel+mascot.png" class="img-fluid" style="max-height: 40px;"> Plan-It
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <router-link class="nav-link text-evenlighter" to="/">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link text-evenlighter" to="/about">
              About
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link text-evenlighter" to="/route">Routing</router-link>
          </li>

          <li class="nav-item">
            <router-link class="nav-link text-evenlighter" to="/community">
              Community
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link text-evenlighter" to="/leaderboard">
              Leaderboards
            </router-link>
          </li>
        </ul>

        <ul class="navbar-nav">
          <li v-if="!isAuthenticated" class="nav-item">
            <a class="nav-link text-evenlighter" @click.prevent="login">Login</a>
          </li>
          <li v-else class="nav-item dropdown">
            <a class="nav-link dropdown-toggle text-evenlighter d-flex align-items-center" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              <img :src="user.picture" alt="" class="rounded-circle me-2" style="width: 30px; height: 30px" />
              <span class="text-evenlighter">Welcome, {{ user.name }}!</span>
            </a>
            <!-- <div v-if="showGamification" class="text-evenlighter d-flex align-items-center">
              <div>Level: {{ userMe.value.level }}</div>
              <div class="progress">
                <div class="progress-bar" role="progressbar" :style="{ width: `${userMe.value.exp}%` }" aria-valuenow="user.progress" aria-valuemin="0" aria-valuemax="100">{{ userMe.value.exp }}%</div>
              </div>
            </div> -->
            <ul class="dropdown-menu bg-green2 text-evenlighter" aria-labelledby="navbarDropdown">
              <li>
                <router-link class="dropdown-item text-light" to="/profile">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(255, 255, 255, 1);transform: ;msFilter:;">
                    <path d="M12 2C6.579 2 2 6.579 2 12s4.579 10 10 10 10-4.579 10-10S17.421 2 12 2zm0 5c1.727 0 3 1.272 3 3s-1.273 3-3 3c-1.726 0-3-1.272-3-3s1.274-3 3-3zm-5.106 9.772c.897-1.32 2.393-2.2 4.106-2.2h2c1.714 0 3.209.88 4.106 2.2C15.828 18.14 14.015 19 12 19s-3.828-.86-5.106-2.228z"></path>
                  </svg> Profile</router-link>
              </li>
              <li>
                <router-link class="dropdown-item text-light" to="/verify">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(255, 255, 255, 1);transform: ;msFilter:;">
                    <circle cx="13" cy="4" r="2"></circle>
                    <path d="M13.978 12.27c.245.368.611.647 1.031.787l2.675.892.633-1.896-2.675-.892-1.663-2.495a2.016 2.016 0 0 0-.769-.679l-1.434-.717a1.989 1.989 0 0 0-1.378-.149l-3.193.797a2.002 2.002 0 0 0-1.306 1.046l-1.794 3.589 1.789.895 1.794-3.589 2.223-.556-1.804 8.346-3.674 2.527 1.133 1.648 3.675-2.528c.421-.29.713-.725.82-1.225l.517-2.388 2.517 1.888.925 4.625 1.961-.393-.925-4.627a2 2 0 0 0-.762-1.206l-2.171-1.628.647-3.885 1.208 1.813z"></path>
                  </svg> Verify</router-link>
              </li>
              <li v-if="user.email == 'brian@bchewy.com' || user.email == 'melody.wong.2022@smu.edu.sg' || user.email == 'ryanlee99324@gmail.com' || user.email == 'planituser27@gmail.com'">
                <router-link class=" dropdown-item text-light" to="/admin">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgb(255, 255, 255);transform: ;msFilter:;">
                    <path d="m2.344 15.271 2 3.46a1 1 0 0 0 1.366.365l1.396-.806c.58.457 1.221.832 1.895 1.112V21a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1v-1.598a8.094 8.094 0 0 0 1.895-1.112l1.396.806c.477.275 1.091.11 1.366-.365l2-3.46a1.004 1.004 0 0 0-.365-1.366l-1.372-.793a7.683 7.683 0 0 0-.002-2.224l1.372-.793c.476-.275.641-.89.365-1.366l-2-3.46a1 1 0 0 0-1.366-.365l-1.396.806A8.034 8.034 0 0 0 15 4.598V3a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v1.598A8.094 8.094 0 0 0 7.105 5.71L5.71 4.904a.999.999 0 0 0-1.366.365l-2 3.46a1.004 1.004 0 0 0 .365 1.366l1.372.793a7.683 7.683 0 0 0 0 2.224l-1.372.793c-.476.275-.641.89-.365 1.366zM12 8c2.206 0 4 1.794 4 4s-1.794 4-4 4-4-1.794-4-4 1.794-4 4-4z"></path>
                  </svg>
                  Admin</router-link>
              </li>
              <li>
                <!-- <router-link class="dropdown-item text-light" to="/settings">
                  <font-awesome-icon icon="fa-cog" />
                  Settings</router-link> -->
                <!-- <router-link class="dropdown-item" :to="`/profile/public/${user.email}`">
                  <font-awesome-icon icon="fa-solid fa-circle-user" />
                  Your Public Profile</router-link> -->
              </li>
              <!-- <hr class="dropdown-divider" /> -->

              <!-- <li>
                <button class="dropdown-item text-light" @click="toggleGamification">
                  Toggle Gamification
                </button>
              </li> -->
              <li>
                <hr class="dropdown-divider" />

              </li>
              <li>
                <a class="dropdown-item text-light" @click="logout">Logout
                  <font-awesome-icon icon="fa-solid fa-arrow-right-from-bracket" />
                </a>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
    <div class="overlay bg-white" style="height: 20px;"></div>
  </nav>
  <!-- User handle modal -->
  <!-- <div class="modal" tabindex="-1" role="dialog" id="handleModal">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Enter User Handle</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <p>Please enter a handle for your account:</p>
          <input type="text" class="form-control" v-model="userHandle" placeholder="Enter handle">
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" @click="saveHandle">Save changes</button>
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
  </div> -->
</template>


<script>
import { useAuth0 } from '@auth0/auth0-vue';
import { watch, computed, defineComponent, ref } from 'vue';
import axios from "axios";

export default defineComponent({
  name: 'NavBar',
  setup() {
    const { loginWithRedirect, user, isAuthenticated, logout } = useAuth0();
    const userHandle = ref('');
    const showGamification = ref(false);
    const userMe = ref({});


    const toggleGamification = () => {
      fetchUser();
      showGamification.value = !showGamification.value;
    };

    watch(user, async (newValue) => {
      if (newValue) {
        // console.log('new value here', newValue)

        // Check Handle Code
        // try {
        //   const handleResponse = await fetch(`${import.meta.env.VITE_API_ENDPOINT}/users/handle/${newValue.nickname}`, {
        //     method: 'GET',
        //     headers: {
        //       'x-api-key': `${import.meta.env.VITE_API_KEY}`
        //     }
        //   });
        //   const handleData = await handleResponse.json();
        //   if (handleData.message === "User not found.") {
        //     console.log('handle not found')
        //     $('#handleModal').modal('show');
        //   }
        // } catch (e) {
        //   console.error('Failed to check handle:', e);
        // }


        try {
          let requestBody = {
            auth0_user_id: newValue.sub,
            email: newValue.email,
            handle: newValue.nickname,
            pictureurl: newValue.picture,
          };

          // Always do initial check to see if user exists
          const response1 = await axios.get(`${import.meta.env.VITE_API_ENDPOINT}/users/ez/${encodeURIComponent(newValue.email)}`, {
            headers: {
              'x-api-key': `${import.meta.env.VITE_API_KEY}`
            }
          });
          const msg = await response1.data;
          console.log(response1.data)
          if (response1.status === 200) {
            // Initialize exp and level if it does not exist on first-time creation.
            console.log('User not found in the database');
            requestBody.exp = 0;
            requestBody.level = 0;
            requestBody.total_km = 0;
            // When user is not found we create it.
            const response = await fetch(`${import.meta.env.VITE_API_ENDPOINT}/users`, {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
                'x-api-key': `${import.meta.env.VITE_API_KEY}`
              },
              body: JSON.stringify(requestBody)

            });
            const data = await response.json();
            console.log('User upserted:', data);

          } else {
            console.log('User found in the database');
          }
        } catch (e) {
          console.error('Failed to upsert user on the Backend:', e);
        }
      }
    });

    // const saveHandle = async () => {
    //   user.nickname = userHandle.value;
    //   // $('#handleModal').modal('hide');
    // };

    // Initial API call to check if the user exists. (for @handle checking)
    const fetchUser = async () => {
      const url = `${import.meta.env.VITE_API_ENDPOINT}/users/iz/${encodeURIComponent(user.value.email)}`;
      const headers = {
        "x-api-key": `${import.meta.env.VITE_API_KEY}`,
      };

      try {
        const response = await axios.get(url, { headers });
        userMe.value = response.data;

      } catch (error) {
        console.error("Error fetching user", error);
      }
    };


    return {
      login: async () => {
        try {
          await loginWithRedirect({
            appState: { targetUrl: window.location.pathname }
          });
        } catch (e) {
          console.error('Failed to login:', e);
        }
      },
      logout: () => {
        logout({ logoutParams: { returnTo: window.location.origin } });
      },
      user,
      isAuthenticated,
      userHandle,
      // saveHandle,
      showGamification,
      toggleGamification,
      fetchUser,
      userMe,
    };
  }
});
</script>
