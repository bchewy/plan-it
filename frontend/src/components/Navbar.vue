<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
      <a class="navbar-brand" href="#">
        <font-awesome-icon icon="fa-solid fa-car" bounce style="color: green" /> Plan-It
      </a>
      <!-- <font-awesome-icon icon="fa-solid fa-user-secret" /> -->

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <router-link class="nav-link" to="/" active-class="active">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/route" active-class="active">Routing</router-link>
          </li>
          <!-- <li class="nav-item">
            <router-link class="nav-link" to="/debug">Debug</router-link>
          </li> -->
          <li class="nav-item">
            <router-link class="nav-link" to="/community" active-class="active">Community</router-link>
          </li>
        </ul>
        <ul class="navbar-nav">
          <li v-if="!isAuthenticated" class="nav-item">
            <a class="nav-link" @click.prevent="login">Login</a>
          </li>
          <li v-else class="nav-item dropdown">
            <a class="nav-link dropdown-toggle d-flex align-items-center" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              <img :src="user.picture" alt="" class="rounded-circle me-2" style="width: 30px; height: 30px" />
              Welcome, {{ user.name }}!
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
              <li>
                <router-link class="dropdown-item" to="/profile">
                  <font-awesome-icon icon="fa-solid fa-circle-user" />
                  Profile</router-link>
              </li>
              <li>
                <router-link class="dropdown-item" to="/settings">
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
                <a class="dropdown-item" @click="logout">Logout
                  <font-awesome-icon icon="fa-solid fa-arrow-right-from-bracket" />
                </a>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
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
  // props: {
  //   pictureurl: String
  // },
  setup() {
    const { loginWithRedirect, user, isAuthenticated, logout } = useAuth0();
    const userHandle = ref('');
    // const pictureurl = user.picture

    watch(user, async (newValue) => {
      // If the user is authenticated
      if (newValue) {
        // Create or update the user in your database
        console.log('new value here', newValue)
        try {
          const handleResponse = await fetch(`http://127.0.0.1:5000/users/handle/${newValue.nickname}`, {
            method: 'GET',
            headers: {
              'x-api-key': 'PlanItIsTheBestProjectEverXYZ'
            }
          });
          const handleData = await handleResponse.json();
          if (handleData.message === "User not found.") {
            // If the user doesn't have a handle, prompt them to enter one
            console.log('handle not found')
            $('#handleModal').modal('show');
          }
        } catch (e) {
          console.error('Failed to check handle:', e);
        }
        try {
          const response = await fetch('http://127.0.0.1:5000/users', {
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
