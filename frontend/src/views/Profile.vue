<style scoped>
.profile-container {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.bg-supergreen {
  background-color: #739072;
}

.nav-pills .nav-link.active {
  background-color: #4F6F52;
  /* Replace with the background color you want */
  color: #ECE3CE;
  /* Replace with the text color you want */
}

.nav-pills .nav-link {
  /* background-color: ; */
  color: #ECE3CE;
}

.nav-pills .nav-item {
  margin-bottom: 20px;
}

.container-fluid {
  min-height: 100vh;
  padding-top: 3rem;
  background-color: #739072;
}
</style>

<template>
  <Navbar />
  <div class="container-fluid pt-3 bg-supergreen">
    <div class="row">
      <!-- Left Sidebar: Tabs -->
      <div class="col-md-3">
        <ul class="nav flex-column nav-pills" id="myTabs" role="tablist">
          <li class="nav-item">
            <a class="nav-link" :class="{ 'active': activeTab === 'profile' }" @click="activeTab = 'profile'" href="#" role="tab">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(236, 227, 206, 1);transform: scaleX(-1);msFilter:progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1);">
                <path d="M12 10c1.151 0 2-.848 2-2s-.849-2-2-2c-1.15 0-2 .848-2 2s.85 2 2 2zm0 1c-2.209 0-4 1.612-4 3.6v.386h8V14.6c0-1.988-1.791-3.6-4-3.6z"></path>
                <path d="M19 2H5c-1.103 0-2 .897-2 2v13c0 1.103.897 2 2 2h4l3 3 3-3h4c1.103 0 2-.897 2-2V4c0-1.103-.897-2-2-2zm-5 15-2 2-2-2H5V4h14l.002 13H14z"></path>
              </svg> My Profile</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" :class="{ 'active': activeTab === 'routes' }" @click="activeTab = 'routes'" href="#" role="tab"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(236, 227, 206, 1);transform: ;msFilter:;">
                <path d="m21.447 6.105-6-3a1 1 0 0 0-.895 0L9 5.882 3.447 3.105A1 1 0 0 0 2 4v13c0 .379.214.725.553.895l6 3a1 1 0 0 0 .895 0L15 18.118l5.553 2.776a.992.992 0 0 0 .972-.043c.295-.183.475-.504.475-.851V7c0-.379-.214-.725-.553-.895zM10 7.618l4-2v10.764l-4 2V7.618zm-6-2 4 2v10.764l-4-2V5.618zm16 12.764-4-2V5.618l4 2v10.764z"></path>
              </svg> My Routes</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" :class="{ 'active': activeTab === 'progress' }" @click="activeTab = 'progress'" href="#" role="tab"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(236, 227, 206, 1);transform: ;msFilter:;">
                <circle cx="17" cy="4" r="2"></circle>
                <path d="M15.777 10.969a2.007 2.007 0 0 0 2.148.83l3.316-.829-.483-1.94-3.316.829-1.379-2.067a2.01 2.01 0 0 0-1.272-.854l-3.846-.77a1.998 1.998 0 0 0-2.181 1.067l-1.658 3.316 1.789.895 1.658-3.317 1.967.394L7.434 17H3v2h4.434c.698 0 1.355-.372 1.715-.971l1.918-3.196 5.169 1.034 1.816 5.449 1.896-.633-1.815-5.448a2.007 2.007 0 0 0-1.506-1.33l-3.039-.607 1.772-2.954.417.625z"></path>
              </svg> My Progress</a>
          </li>
        </ul>
      </div>

      <!-- Main Content Area -->
      <div class="col-md-9">
        <div v-if="activeTab === 'profile'" class="tab-pane show active">
          <!-- Profile Content -->
          <div class="profile-container bg-light p-3 rounded d-flex flex-column flex-md-row mb-4">
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
          <div class="bg-white rounded-3 shadow-sm p-3">
            <h3 class="mb-0">Friends</h3>
            <div class="mt-3">
              <div v-for="friend in friends" :key="friend" class="mb-3 p-2 bg-light rounded">
                <h5 class="m-0">{{ friend }}</h5>
              </div>
            </div>
          </div>
          <div class="bg-white rounded shadow-sm p-3 mt-4 mb-4">
            <h3 class="mb-0">Friend Requests</h3>
            <div class="mt-3">
              <AddFriend :user="user" />
              <h4 class="mt-2">Received Requests</h4>
              <div v-for="request in receivedRequests" :key="request" class="mb-2 p-2 bg-light rounded">
                <FriendRequest :friend="request" :user="user" :receivedRequests="receivedRequests" type="received" />
              </div>

              <h4 class="mt-2">Sent Requests</h4>
              <div v-for="request in sentRequests" :key="request" class="mb-2 p-2 bg-light rounded">
                <FriendRequest :friend="request" :user="user" :sentRequests="sentRequests" type="sent" />
              </div>
            </div>
          </div>
        </div>
        <div v-if="activeTab === 'routes'" class="tab-pane">
          <!-- Routes Content -->
          <div class="bg-light p-3 rounded d-flex flex-column flex-md-row mb-2">
            <!-- User Routes -->
            <div class="pr-4 pb-3 pb-md-0">
              <h3 class="mb-2">Your Routes</h3>
              <!-- Here you can add the code to display the user's routes -->
              <div class="chart-container">
                <h4 class="mb-2">Carbon emissions</h4>
                <canvas id="carbonFootprintChart"></canvas>
              </div>

              <div class="chart-container mt-4">
                <h4 class="mb-2">Travel modes</h4>
                <canvas id="travelCategoryChart"></canvas>
              </div>

              <!-- <div v-if="routes && routes.length == 0">
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
              </div> -->
            </div>
          </div>
          <!-- <nav aria-label="Pagination-for-routes">
            <ul class="pagination justify-content-center">
              <li class="page-item" :class="{ disabled: currentPage === 1 }">
                <a class="page-link" href="#" @click.prevent="currentPage--">Previous</a>
              </li>
              <li class="page-item disabled">
                <span class="page-link">{{ currentPage }} / {{ totalPages }}</span>
              </li>
              <li class="page-item" :class="{ disabled: currentPage >= totalPages }">
                <a class="page-link" href="#" @click.prevent="currentPage++">Next</a>
              </li>
            </ul>
          </nav> -->
        </div>
        <div v-if="activeTab === 'progress'" class="tab-pane">
          <!-- Friends Content -->
          <div class="card mt-4 mb-4">
            <div class="card-header">
              <h3 class="mb-0">Game Stats</h3>
            </div>
            <Badges></Badges>
          </div>

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
      itemsPerPage: 3,
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
      const canvas = document.getElementById('carbonFootprintChart');
      if (canvas) {
        const ctx = document.getElementById('carbonFootprintChart').getContext('2d');
        if (this.myChart) {
          this.myChart.destroy();
        }
        this.myChart = new Chart(ctx, {
          type: 'bar',
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
            responsive: true,
            maintainAspectRatio: true,
            aspectRatio: 1,
            scales: {
              x: {
                type: 'category',
                time: {
                  unit: 'hour', // Changed from 'hour' to 'minute'
                  displayFormats: {
                    hour: 'HH:mm'
                  }
                },
                ticks: {
                  source: 'data',
                  autoSkip: false // Force it to display all data points
                },
                distribution: 'linear'  // Set to linear for even distribution of ticks
              },
              y: {
                min: 0,
                suggestedMax: 5,
                ticks: {
                  stepSize: 0.5
                }
              }
            },
          }
        });

        // Pie chart for travel mode
        const travelModes = this.routes.map(route => route.transport_mode);
        const travelModeCounts = {};
        travelModes.forEach(mode => {
          if (!travelModeCounts[mode]) {
            travelModeCounts[mode] = 1;
          } else {
            travelModeCounts[mode]++;
          }
        });
        const travelModeLabels = Object.keys(travelModeCounts);
        const travelModeData = Object.values(travelModeCounts);
        const travelModeCanvas = document.getElementById('travelCategoryChart');
        if (travelModeCanvas) {
          const travelModeCtx = document.getElementById('travelCategoryChart').getContext('2d');
          if (this.myTravelModeChart) {
            this.myTravelModeChart.destroy();
          }
          this.myTravelModeChart = new Chart(travelModeCtx, {
            type: 'pie',
            data: {
              labels: travelModeLabels,
              datasets: [{
                data: travelModeData,
                backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(255, 206, 86, 0.2)', 'rgba(75, 192, 192, 0.2)', 'rgba(153, 102, 255, 0.2)', 'rgba(255, 159, 64, 0.2)'],
                borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)', 'rgba(255, 206, 86, 1)', 'rgba(75, 192, 192, 1)', 'rgba(153, 102, 255, 1)', 'rgba(255, 159, 64, 1)'],
                borderWidth: 1
              }]
            },
            options: {
              responsive: true,
              maintainAspectRatio: true,
              aspectRatio: 2
            }
          });
        }


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
      } catch (error) {
        console.error("Error fetching routes:", error);
      }
    },
  },
};
</script>


