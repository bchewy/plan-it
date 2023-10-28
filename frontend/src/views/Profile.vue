<style scoped>
.profile-container {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.bg-supergreen {
  background-color: #d1f4d1;
}
</style>

<template>
  <Navbar />
  <div class="container-fluid mt-5">
    <div class="row">
      <!-- Left Sidebar: Tabs -->
      <div class="col-md-3">
        <ul class="nav flex-column nav-pills" id="myTabs" role="tablist">
          <li class="nav-item">
            <a class="nav-link" :class="{ 'active': activeTab === 'profile' }" @click="activeTab = 'profile'" href="#" role="tab">Profile</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" :class="{ 'active': activeTab === 'routes' }" @click="activeTab = 'routes'" href="#" role="tab">Routes</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" :class="{ 'active': activeTab === 'friends' }" @click="activeTab = 'friends'" href="#" role="tab">Friends</a>
          </li>
        </ul>
      </div>

      <!-- Main Content Area -->
      <div class="col-md-9">
        <div v-if="activeTab === 'profile'" class="tab-pane show active">
          <!-- Profile Content -->
          <div class="profile-container bg-light p-3 rounded d-flex flex-column flex-md-row">
            <!-- User Profile Image -->
            <div class="pr-4 pb-3 pb-md-0">
              <img :src="user.picture" class="img-fluid px-3" alt="User profile picture">
            </div>
            <div class="pl-md-4">
              <h3 class="mb-2 glowing-text">{{ user.name }}</h3>
              <p class="mb-2"><b>Handle:</b> @{{ user.nickname }}</p>
              <p class="mb-2"><b>Email:</b> {{ user.email }}</p>
            </div>
          </div>
        </div>
        <div v-if="activeTab === 'routes'" class="tab-pane">
          <!-- Routes Content -->
          <div class="bg-light p-3 rounded d-flex flex-column flex-md-row">
            <!-- User Routes -->
            <div class="pr-4 pb-3 pb-md-0">
              <h3 class="mb-2">Your Routes</h3>
              <!-- Here you can add the code to display the user's routes -->
              <div class="chart-container">
                <canvas id="carbonFootprintChart"></canvas>
              </div>

              <div v-if="routes && routes.length == 0">
                <p class="text-center">
                  Your route list is empty. You need to commit more.
                </p>
              </div>
              <div v-else>
                <div v-for="route in paginatedRoutes" :key="route.route_id" class="route-item">
                  <h4>{{ route.start_point_name }} to {{ route.end_point_name }}</h4>
                  <p><b>Mode of Transport:</b> {{ route.transport_mode }}</p>
                  <p><b>Carbon Emission:</b> {{ route.carbon_emission }}</p>
                  <p><b>Timestamp:</b> {{ new Date(route.timestamp).toLocaleString() }}</p>
                </div>
              </div>
            </div>
          </div>
          <div class="pl-md-4">
            <!-- Here you can add the code to display details about the selected route -->
          </div>
          <nav aria-label="Pagination-for-routes">
            <ul class="pagination justify-content-center">
              <li class="page-item" :class="{ disabled: currentPage === 1 }">
                <a class="page-link" href="#" @click.prevent="currentPage--">Previous</a>
              </li>
              <!-- Page count -->
              <li class="page-item disabled">
                <span class="page-link">{{ currentPage }} / {{ totalPages }}</span>
              </li>
              <li class="page-item" :class="{ disabled: currentPage >= totalPages }">
                <a class="page-link" href="#" @click.prevent="currentPage++">Next</a>
              </li>
            </ul>
          </nav>
        </div>
        <div v-if="activeTab === 'friends'" class="tab-pane">
          <!-- Friends Content -->

        </div>
      </div>

    </div>
  </div>
</template>

<script>
import MapItem from "../components/MapItem.vue";
import AddFriend from "../components/AddFriends.vue";
import Navbar from "../components/Navbar.vue";
import FriendRequest from '../components/FriendRequest.vue';
import Badges from '../components/Badges.vue';
import { useAuth0 } from "@auth0/auth0-vue";
import axios from "axios";
import { Chart, registerables } from 'chart.js/auto';
import 'chartjs-adapter-date-fns';
import { format } from 'date-fns';

Chart.register(...registerables);



export default {
  created() {
    this.fetchData();

  },
  watch: {
    activeTab: {
      immediate: true,
      handler(newVal, oldVal) {
        if (newVal === 'routes') {
          this.$nextTick(() => {
            this.fetchData();
          });
        }
      },
    },
  },
  data() {
    const { user, isAuthenticated } = useAuth0();
    return {
      activeTab: 'profile',
      isLoading: false,
      currentPage: 1,
      itemsPerPage: 6,
      user,
      isAuthenticated,
      routes: [],
      friends: [],
      friendRequests: [],
      receivedRequests: [],
      sentRequests: [],
    };
  },
  computed: {
    // For pagination
    paginatedRoutes() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      const end = start + this.itemsPerPage;
      return this.routes.slice(start, end);
    },
    // Total pages
    totalPages() {
      return Math.ceil(this.routes.length / this.itemsPerPage);
    },
  },
  components: {
    Navbar,
    MapItem,
    AddFriend,
    FriendRequest,
    Badges,
  },
  methods: {
    async drawChart() {

      this.routes.sort((a, b) => new Date(a.timestamp) - new Date(b.timestamp));

      const labels = this.routes.map(route => format(new Date(route.timestamp), 'yyyy-MM-dd HH:mm:ss'));
      const data = this.routes.map(route => parseFloat(route.carbon_emission.toFixed(1)));

      console.log(labels)
      console.log(data)
      const canvas = document.getElementById('carbonFootprintChart');
      if (canvas) {
        const ctx = document.getElementById('carbonFootprintChart').getContext('2d');


        if (this.myChart) {
          this.myChart.destroy();
        }
        this.myChart = new Chart(ctx, {
          type: 'line',
          data: {
            labels: labels,
            datasets: [{
              label: 'Carbon Emission',
              data: data,
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 1
            }]
          },
          options: {
            scales: {
              x: {
                type: 'time',
                time: {
                  unit: 'hour',  // Changed from 'day' to 'hour'
                  displayFormats: {
                    hour: 'HH:mm'
                  }
                },
                ticks: {
                  source: 'data'
                }
              },
              y: {
                min: 0,
                suggestedMax: 5,
                ticks: {
                  stepSize: 0.5
                }
              }
            }
          }
        });
      }
    },
    fetchData() {
      this.fetchRoutes().then(() => {
        this.drawChart();
      });
      this.fetchUser();
      this.fetchFriendRequests();
    },
    async fetchUser() {
      const url = `${import.meta.env.VITE_API_ENDPOINT}/users/iz/${encodeURIComponent(this.user.email)}`;
      const headers = {
        "x-api-key": "PlanItIsTheBestProjectEverXYZ",
      };

      try {
        const response = await axios.get(url, { headers });
        this.friends = response.data.friends;

      } catch (error) {
        console.error("Error fetching user", error);
      }
    },
    async fetchFriendRequests() {
      const url = `${import.meta.env.VITE_API_ENDPOINT}/users/${encodeURIComponent(this.user.email)}/friend_requests`;
      const headers = {
        "x-api-key": "PlanItIsTheBestProjectEverXYZ",
      };

      try {
        const response = await axios.get(url, { headers });
        this.receivedRequests = response.data.received;
        this.sentRequests = response.data.sent;

      } catch (error) {
        console.error("Error fetching friend requests", error);
      }

    },
    async fetchRoutes() {
      const email = this.user.email; // Get the email from user object
      const url = `${import.meta.env.VITE_API_ENDPOINT}/routes/email?email=${encodeURIComponent(email)}`;
      const headers = {
        "x-api-key": "PlanItIsTheBestProjectEverXYZ", // Replace with your actual API key
      };
      try {
        const response = await axios.get(url, { headers });
        this.routes = response.data.reverse(); // Assign the fetched routes to the routes data property
        console.log('Successfully fetched routes.')
      } catch (error) {
        console.error("Error fetching routes:", error);
      }
    },
  },
};
</script>


