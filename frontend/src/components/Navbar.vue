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
        <font-awesome-icon icon="fa-solid fa-car" bounce style="color: #a7c957" /> Plan-It
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
            <router-link class="nav-link text-evenlighter" to="/route">Routing</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link text-evenlighter" to="/community">Community</router-link>
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
            <ul class="dropdown-menu bg-green2 text-evenlighter" aria-labelledby="navbarDropdown">
              <li>
                <router-link class="dropdown-item text-light" to="/profile">
                  <font-awesome-icon icon="fa-solid fa-circle-user" />
                  Profile</router-link>
              </li>
              <li>
                <router-link class="dropdown-item text-light" to="/settings">
                  <font-awesome-icon icon="fa-cog" />
                  Settings</router-link>
                <!-- <router-link class="dropdown-item" :to="`/profile/public/${user.email}`">
                  <font-awesome-icon icon="fa-solid fa-circle-user" />
                  Your Public Profile</router-link> -->
              </li>
              <!-- <li><router-link class="dropdown-item" to="/journey">
								<font-awesome-icon icon="fa-solid fa-truck-fast" />
								Journey</router-link>
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
  <div class="modal" tabindex="-1" role="dialog" id="handleModal">
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
  </div>
</template>


<script>
import { useAuth0 } from '@auth0/auth0-vue';
import { watch, computed, defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'NavBar',

  setup() {
    const { loginWithRedirect, user, isAuthenticated, logout } = useAuth0();
    const userHandle = ref('');
    watch(user, async (newValue) => {
      if (newValue) {
        console.log('new value here', newValue)
        try {
          const handleResponse = await fetch(`${import.meta.env.VITE_API_ENDPOINT}/users/handle/${newValue.nickname}`, {
            method: 'GET',
            headers: {
              'x-api-key': 'PlanItIsTheBestProjectEverXYZ'
            }
          });
          const handleData = await handleResponse.json();
          if (handleData.message === "User not found.") {
            console.log('handle not found')
            $('#handleModal').modal('show');
          }
        } catch (e) {
          console.error('Failed to check handle:', e);
        }
        try {
          const response = await fetch('${import.meta.env.VITE_API_ENDPOINT}/users', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'x-api-key': 'PlanItIsTheBestProjectEverXYZ'
            },
            body: JSON.stringify({
              auth0_user_id: newValue.sub,
              email: newValue.email,
              handle: newValue.nickname,
              pictureurl: newValue.picture,
            })
          });
          const data = await response.json();
          console.log('User upserted:', data);
        } catch (e) {
          console.error('Failed to upsert user:', e);
        }
      }
    });

    const saveHandle = async () => {
      user.nickname = userHandle.value;
      $('#handleModal').modal('hide');
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
      saveHandle,
    };
  }
});
</script>
