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

/* This changes the chart sizes. */
/* .pr-4.pb-3.pb-md-0 {
  flex: 2;
}
*/

/* Settings Styles */
.checkbox-label {
  display: flex;
  align-items: center;
}

.checkbox-label input[type="checkbox"] {
  appearance: none;
  width: 32px;
  height: 14px;
  background-color: #cadcca;
  border-radius: 14px;
  position: relative;
}

.checkbox-label input[type="checkbox"]::before {
  content: "";
  width: 14px;
  /* Width of the switch handle */
  height: 14px;
  /* Height of the switch handle */
  background-color: #ebedf0;
  /* Color of the switch handle */
  border-radius: 50%;
  /* Make it a circle */
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  left: 2px;
  /* Adjust the position as needed */
  transition: 0.4s;
  /* Add a smooth transition effect */
}

.checkbox-label input[type="checkbox"]:checked {
  background-color: #4CAF50;
  /* Background color for the "on" state */
}

.checkbox-label input[type="checkbox"]:checked::before {
  left: calc(100% - 14px);
  /* Position the handle to the right when checked */
}

.checkbox-label label {
  margin-left: 8px;
}
</style>

<template>
  <Navbar />
  <div class="container-fluid pt-3 bg-supergreen">
    <div class="row">
      <!-- Left Sidebar: Tabs -->
      <div class="col-md-2">
        <ul class="nav flex-column nav-pills" id="myTabs" role="tablist">
          <li class="nav-item">
            <a class="nav-link" :class="{ 'active': activeTab === 'profile' }" @click="activeTab = 'profile'" href="#" role="tab">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(236, 227, 206, 1);transform: scaleX(-1);msFilter:progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1);">
                <path d="M12 10c1.151 0 2-.848 2-2s-.849-2-2-2c-1.15 0-2 .848-2 2s.85 2 2 2zm0 1c-2.209 0-4 1.612-4 3.6v.386h8V14.6c0-1.988-1.791-3.6-4-3.6z"></path>
                <path d="M19 2H5c-1.103 0-2 .897-2 2v13c0 1.103.897 2 2 2h4l3 3 3-3h4c1.103 0 2-.897 2-2V4c0-1.103-.897-2-2-2zm-5 15-2 2-2-2H5V4h14l.002 13H14z"></path>
              </svg> My Profile</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" :class="{ 'active': activeTab === 'myactivity' }" @click="activeTab = 'myactivity'" href="#" role="tab">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(236, 227, 206, 1);transform: ;msFilter:;">
                <path d="M20 2H4c-1.103 0-2 .897-2 2v18l4-4h14c1.103 0 2-.897 2-2V4c0-1.103-.897-2-2-2zM9 12a2 2 0 1 1 .001-4.001A2 2 0 0 1 9 12zm6 0a2 2 0 1 1 .001-4.001A2 2 0 0 1 15 12z"></path>
              </svg>
              My Activity</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" :class="{ 'active': activeTab === 'routes' }" @click="activeTab = 'routes'" href="#" role="tab"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(236, 227, 206, 1);transform: ;msFilter:;">
                <path d="m21.447 6.105-6-3a1 1 0 0 0-.895 0L9 5.882 3.447 3.105A1 1 0 0 0 2 4v13c0 .379.214.725.553.895l6 3a1 1 0 0 0 .895 0L15 18.118l5.553 2.776a.992.992 0 0 0 .972-.043c.295-.183.475-.504.475-.851V7c0-.379-.214-.725-.553-.895zM10 7.618l4-2v10.764l-4 2V7.618zm-6-2 4 2v10.764l-4-2V5.618zm16 12.764-4-2V5.618l4 2v10.764z"></path>
              </svg> My Routes</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" :class="{ 'active': activeTab === 'progress' }" @click="activeTab = 'progress'" href="#" role="tab"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(236, 227, 206, 1);transform: ;msFilter:;">
                <path d="M4.035 15.479A3.976 3.976 0 0 0 4 16c0 2.378 2.138 4.284 4.521 3.964C9.214 21.198 10.534 22 12 22s2.786-.802 3.479-2.036C17.857 20.284 20 18.378 20 16c0-.173-.012-.347-.035-.521C21.198 14.786 22 13.465 22 12s-.802-2.786-2.035-3.479C19.988 8.347 20 8.173 20 8c0-2.378-2.143-4.288-4.521-3.964C14.786 2.802 13.466 2 12 2s-2.786.802-3.479 2.036C6.138 3.712 4 5.622 4 8c0 .173.012.347.035.521C2.802 9.214 2 10.535 2 12s.802 2.786 2.035 3.479zm1.442-5.403 1.102-.293-.434-1.053A1.932 1.932 0 0 1 6 8c0-1.103.897-2 2-2 .247 0 .499.05.73.145l1.054.434.293-1.102a1.99 1.99 0 0 1 3.846 0l.293 1.102 1.054-.434C15.501 6.05 15.753 6 16 6c1.103 0 2 .897 2 2 0 .247-.05.5-.145.73l-.434 1.053 1.102.293a1.993 1.993 0 0 1 0 3.848l-1.102.293.434 1.053c.095.23.145.483.145.73 0 1.103-.897 2-2 2-.247 0-.499-.05-.73-.145l-1.054-.434-.293 1.102a1.99 1.99 0 0 1-3.846 0l-.293-1.102-1.054.434A1.935 1.935 0 0 1 8 18c-1.103 0-2-.897-2-2 0-.247.05-.5.145-.73l.434-1.053-1.102-.293a1.993 1.993 0 0 1 0-3.848z"></path>
                <path d="m15.742 10.71-1.408-1.42-3.331 3.299-1.296-1.296-1.414 1.414 2.704 2.704z"></path>
              </svg> My Badges</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" :class="{ 'active': activeTab === 'settings' }" @click="activeTab = 'settings'" href="#" role="tab">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(236, 227, 206, 1);transform: ;msFilter:;">
                <path d="m2.344 15.271 2 3.46a1 1 0 0 0 1.366.365l1.396-.806c.58.457 1.221.832 1.895 1.112V21a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1v-1.598a8.094 8.094 0 0 0 1.895-1.112l1.396.806c.477.275 1.091.11 1.366-.365l2-3.46a1.004 1.004 0 0 0-.365-1.366l-1.372-.793a7.683 7.683 0 0 0-.002-2.224l1.372-.793c.476-.275.641-.89.365-1.366l-2-3.46a1 1 0 0 0-1.366-.365l-1.396.806A8.034 8.034 0 0 0 15 4.598V3a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v1.598A8.094 8.094 0 0 0 7.105 5.71L5.71 4.904a.999.999 0 0 0-1.366.365l-2 3.46a1.004 1.004 0 0 0 .365 1.366l1.372.793a7.683 7.683 0 0 0 0 2.224l-1.372.793c-.476.275-.641.89-.365 1.366zM12 8c2.206 0 4 1.794 4 4s-1.794 4-4 4-4-1.794-4-4 1.794-4 4-4z"></path>
              </svg> Settings</a>
          </li>
        </ul>
      </div>

      <!-- Main Content Area -->
      <div class="col-md-10 my-4">
        <!-- Profile tab -->
        <div v-if="activeTab === 'profile'" class="tab-pane show active">
          <!-- Profile Content -->
          <div class="profile-container bg-light p-3 rounded d-flex flex-column flex-md-row mb-4">
            <!-- User Profile Image -->
            <div class="pb-3 pb-md-0">
              <img :src="user.picture" class="img-fluid px-3" alt="User profile picture">
            </div>
            <div class="pl-md-4">
              <h3 class="mb-2 glowing-text">{{ user.name }}</h3>
              <p class="mb-2"><b>Level:</b> {{ userLvl }}</p>
              <div class="progress stylish-progress-bar mb-4">
                <div v-if="userExp" class="progress-bar bg-supergreen" role="progressbar" :style="{ width: `${userExp.toFixed(2)}%` }" aria-valuenow="" aria-valuemin="0" aria-valuemax="100">{{ userExp.toFixed(2) }}%</div>
                <div v-else="userExp" class="progress-bar bg-supergreen" role="progressbar"></div>
              </div>
              <p class="mb-2"><b>Handle:</b> @{{ user.nickname }}</p>
              <p class="mb-2"><b>Email:</b> {{ user.email }}</p>
            </div>

          </div>
          <!-- Friends Section -->
          <div class="bg-white rounded-3 shadow-sm p-3">
            <h3 class="mb-0">Friends</h3>
            <div class="mt-3">
              <div v-for="friend in friends" :key="friend" class="mb-3 p-2 bg-light rounded">
                <h5 class="m-0">{{ friend }}</h5>
              </div>
            </div>
          </div>

          <!-- Friend Request Section -->
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

        <!-- Routes tab -->
        <div v-if="activeTab === 'routes'" class="tab-pane">
          <div class="pr-4 pb-3 pb-md-0 bg-white p-3 rounded shadow-sm">

            <h3 class="mb-2">Your Routes</h3>
            <!-- <div class="container bg-white">
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
                  <p><b>Timestamp:</b> {{ route.timestamp }}</p>
                </div>
              </div>
            </div>
            <nav aria-label="Pagination-for-routes">
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


            <!-- Display carbon emisisons total here in a nice graphic -->
            <div class="container">
              <div class="row">
                <!-- Card for Calories -->
                <div class="col">
                  <div class="card text-center">
                    <div class="card-body">
                      <img src="https://bchewy-images.s3.ap-southeast-1.amazonaws.com/plan-it/Cool+animals.png" alt="Levels" class="card-img-top" style="width: 60px; height: auto;">
                      <h5 class="card-title">{{ userLvl }}</h5>
                      <p class="card-text">Levels gained!</p>
                    </div>
                  </div>
                </div>
                <!-- Card for CO2 Saved -->
                <div class="col">
                  <div class="card text-center">
                    <div class="card-body">
                      <img src="https://bchewy-images.s3.ap-southeast-1.amazonaws.com/plan-it/code+block%0AGreen+cute+space.png" alt="CO2 Saved" class="card-img-top" style="width: 60px; height: auto;">
                      <h5 class="card-title">{{ carbonSavings.toFixed(2) }}g</h5>
                      <p class="card-text">CO2 Saved</p>
                    </div>
                  </div>
                </div>
                <!-- Card for Money Saved -->
                <div class="col">
                  <div class="card text-center">
                    <div class="card-body">
                      <img src="https://bchewy-images.s3.ap-southeast-1.amazonaws.com/plan-it/Distance+icons.gif" alt="Distance travelled" class="card-img-top" style="width: 60px; height: auto;">
                      <h5 class="card-title">{{ totalKM.toFixed(2) }}km</h5>
                      <p class="card-text">travelled</p>
                    </div>
                  </div>
                </div>
              </div>




            </div>
            <!-- Other graphs here -->
            <div class="chart-container mt-2">
              <h5 class="mb-2">Carbon Savings(g) over Distance Travelled (km)</h5>
              <canvas id="carbonFootprintChart"></canvas>
            </div>

            <div class="chart-container mt-4">
              <h5 class="mb-2">Travel modes</h5>
              <canvas id="travelCategoryChart"></canvas>
            </div>

            <!-- <Compare v-if="user" :user="user"></Compare> -->


          </div>

        </div>
        <div v-if="activeTab === 'progress'" class="tab-pane">
          <div class="card mt-4 mb-4">
            <div class="card-header">
              <h3 class="mb-0">Game Stats</h3>
            </div>
            <Badges></Badges>
          </div>
        </div>
        <div v-if="activeTab === 'settings'" class="tab-pane">
          <div class="card mt-4 mb-4">
            <div class="card-header">
              <h3 class="mb-0">Settings</h3>
            </div>
            <div class="container m-2">
              <div class="row">
                <div class="col-12 m2-2">
                  <h1>Notification Settings</h1>
                </div>
              </div>
              <div v-if="this.isSubmitted" class="alert alert-info" role="alert" style="margin: 1rem 1rem 1rem 0rem;">
                Settings saved!
              </div>
              <div class="control-group col-12">
                <div class="controls">
                  <div class="checkbox-label">
                    <input type="checkbox" v-model="newFriends" />
                    <label>Notify me about new friends who signed up with my friend code</label>
                  </div>
                  <br>
                  <div class="checkbox-label">
                    <input type="checkbox" v-model="newFeatures" />
                    <label>Notify me about new features of PlanIt!</label>
                  </div>
                  <br>
                  <div class="checkbox-label">
                    <input type="checkbox" v-model="lostPlace" />
                    <label>Notify me if I lose my place in the leaderboard</label>
                  </div>
                </div>
                <button class="border border-success btn btn-light m-1 mt-3 mb-2" @click="reset()">Clear All</button>
                <button class="border border-success btn btn-success m-1 mt-3 mb-2" @click="submit()">Save</button>
              </div>
            </div>
            <!-- <Badges></Badges> -->
          </div>

        </div>
        <div v-if="activeTab === 'myactivity'" class="tab-pane">
          <div class="card mt-4 mb-4">
            <div class="card-header">
              <h3 class="mb-0">Your Activity</h3>
            </div>


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
import Compare from "../components/Compare.vue";
import Badges from '../components/Badges.vue';

// Others
import { useAuth0 } from "@auth0/auth0-vue";
import axios from "axios";
import { ref, defineComponent, computed, reactive } from "vue";

// Chart JS 
import { Chart, registerables } from 'chart.js/auto';
import 'chartjs-adapter-date-fns';
import { format } from 'date-fns';
import ChartDataLabels from "chartjs-plugin-datalabels";
Chart.register(...registerables);
Chart.register(ChartDataLabels);



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
    const userExp = ref(0);
    const expToNextLevel = ref(0);
    const userLvl = ref(0)
    const carbonSavings = ref(0);
    const totalKM = ref(0);
    return {
      userExp,
      expToNextLevel,
      userLvl,
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
      isSubmitted: false,
      newFriends: false,
      newFeatures: false,
      lostPlace: false,
      carbonSavings,
      totalKM,
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
    Compare,
  },
  methods: {
    async drawChart() {
      if (!Array.isArray(this.routes) || this.routes.length === 0) {
        console.error('No routes available.');
        return;
      }

      // this.routes.sort((a, b) => new Date(a.timestamp) - new Date(b.timestamp));
      // const labels = this.routes.map(route => new Date(route.timestamp).toISOString());
      // const data = this.routes.map(route => parseFloat(route.carbon_emission.toFixed(1)));


      const dateEmissionsMap = this.routes.reduce((acc, route) => {
        const date = new Date(route.timestamp).toISOString().split('T')[0];
        if (!acc[date]) {
          acc[date] = 0;
        }
        acc[date] += parseFloat(route.carbon_emission.toFixed(1));
        return acc;
      }, {});
      const dateDistanceMap = this.routes.reduce((acc, route) => {
        const date = new Date(route.timestamp).toISOString().split('T')[0];
        if (!acc[date]) {
          acc[date] = 0;
        }
        acc[date] += route.distance; // Assuming distance is a number
        return acc;
      }, {});

      const labels = Object.keys(dateEmissionsMap).sort();
      const data = labels.map(label => dateEmissionsMap[label]);
      const distanceData = labels.map(label => dateDistanceMap[label]);

      const canvas = document.getElementById('carbonFootprintChart');




      if (canvas) {
        const ctx = document.getElementById('carbonFootprintChart').getContext('2d');
        if (this.myChart) {
          this.myChart.destroy();
        }

        // Carbon Emissions Chart
        const routes = this.routes;
        this.myChart = new Chart(ctx, {
          type: 'bar',
          data: {
            labels: labels,
            datasets: [{
              label: 'Carbon Emission',
              data: data,
              // datalabels: {
              //   color: '#444',
              //   backgroundColor: 'rgba(255,255,255,0.75)',
              //   borderColor: 'grey',
              //   borderRadius: 4,
              //   borderWidth: 1,
              //   padding: 4
              // },
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 1
            },
            {
              label: 'Distance Travelled',
              data: distanceData,
              // Additional dataset styling goes here
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: true,
            aspectRatio: 1,
            scales: {
              y: {
                beginAtZero: true,
                title: {
                  display: true,
                  text: 'Carbon emissions (g CO₂e)'
                }
              },
              x: {
                title: {
                  display: true,
                  text: 'Date'
                },
                ticks: {
                  autoSkip: true,
                  maxTicksLimit: 20 // Adjust this number based on your preference and space
                }
              }
            },
            // tooltip: { //tool tip is deprac
            //   callbacks: {
            //     label: function (tooltipItem, data) {
            //       const emission = data.datasets[0].data[tooltipItem.index].toFixed(2);
            //       const distance = data.datasets[1].data[tooltipItem.index].toFixed(2);
            //       return `${emission}g CO₂e, ${distance} km`; // Format as per your preference
            //     }
            //   }
            // },
            plugins: {
              datalabels: {
                align: 'end',
                anchor: 'end',
                formatter: (value, context) => {
                  // Check the dataset index
                  // If the current dataset is for carbon emissions (index 0), format the label for emissions
                  if (context.datasetIndex === 0) {
                    return `${value.toFixed(2)} g CO₂e`;
                  }
                  // If the current dataset is for distance (index 1), format the label for distance
                  else if (context.datasetIndex === 1) {
                    return `${value.toFixed(2)} km`; // Replace 'km' with your unit for distance if necessary
                  }
                  return null; // Return null for any other dataset to avoid displaying a label
                }
              }
            }
          },


        });
      }


      // Travel category chart
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
        this.userLvl = response.data.level;
        this.userExp = response.data.exp;
        this.userEmail = response.data.email
        this.carbonSavings = response.data.carbonsavings;
        this.totalKM = response.data.total_km;
        // console.log(response.data);

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
    submit() {
      this.isSubmitted = true;
    },
    reset() {
      this.newFeatures = false;
      this.newFriends = false;
      this.lostPlace = false;
    }
  },
};
</script>


