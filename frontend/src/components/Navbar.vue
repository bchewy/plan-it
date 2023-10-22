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
          <!-- If user is not authenticated -->
          <li v-if="!isAuthenticated" class="nav-item">
            <a class="nav-link" @click.prevent="login">Log in</a>
          </li>
          <!-- <li v-if="!isAuthenticated" class="nav-item">
						<a class="nav-link" @click="signup">Sign up</a>
					</li> -->
          <!-- If user is authenticated -->
          <li v-else class="nav-item dropdown">
            <a class="nav-link dropdown-toggle d-flex align-items-center" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              <img :src="user.picture" alt="" class="rounded-circle me-2" style="width: 30px; height: 30px" />
              Welcome, {{ user.name }}
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
              <li>
                <router-link class="dropdown-item" to="/profile">
                  <font-awesome-icon icon="fa-solid fa-circle-user" />
                  Profile</router-link>
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
</template>


<script>
import { useAuth0 } from '@auth0/auth0-vue';
import { watch, computed, defineComponent } from 'vue';

export default defineComponent({
  name: 'NavBar',
  setup() {
    const { loginWithRedirect, user, isAuthenticated, logout } = useAuth0();
    watch(user, async (newValue) => {
      // If the user is authenticated
      if (newValue) {
        // Create or update the user in your database
        try {
          const response = await fetch('https://api.bchwy.com/users', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'x-api-key': 'PlanItIsTheBestProjectEverXYZ'
            },
            body: JSON.stringify({
              auth0_user_id: newValue.sub,
              email: newValue.email
            })
          });
          const data = await response.json();
          console.log('User upserted:', data);
        } catch (e) {
          console.error('Failed to upsert user:', e);
        }
      }
    });

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
    };
  }
});
</script>
