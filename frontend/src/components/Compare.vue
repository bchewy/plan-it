<template>
  <div>
    <label for="friendSelector">Select a Friend: </label>
    <select v-model="selectedFriend" id="friendSelector" @change="updateChart">
      <option v-for="(friend, index) in friends" :key="index" :value="friend.email">{{ friend }}</option>
    </select>
    <canvas id="carbonEmissionComparisonChart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js/auto';
import 'chartjs-adapter-date-fns';
import { ref, onMounted, watch, reactive } from 'vue';
import axios from 'axios';

export default {
  props: ["user"],
  data() {
    const state = reactive({
      friends: {},
      carbonSavings: 0,
    });

    return {
      state,
    }
  },
  setup(props) {
    const carbonEmissionChart = ref(null);
    const selectedFriend = ref('user'); // Default selection
    const data = ref({});
    const friends = ref({});
    const carbonSavings = ref(0);

    const userData = {
      label: 'You',
      data,
      backgroundColor: '#ECE3CE',
      borderColor: '#ECE3CE',
      borderWidth: 1,
    };
    const friendData = {
      label: 'Friend',
      data: [],
      backgroundColor: 'rgb(209, 244, 209)',
      borderColor: 'rgb(209, 244, 209)',
      borderWidth: 1,
    };
    const chartData = {
      labels: [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
      ],
      datasets: [userData, friendData],
    };

    onMounted(() => {
      const ctx = document.getElementById('carbonEmissionComparisonChart').getContext('2d');
      carbonEmissionChart.value = new Chart(ctx, {
        type: 'bar',
        data: chartData,
        options: {
          scales: {
            x: {
              barPercentage: 0.5,
              categoryPercentage: 0.5,
            },
            y: {
              min: 0,
            },
          },
        },
      });
    });


    const fetchUser = async () => {
      console.log("Fetching user")
      console.log(props.user)
      const url = `${import.meta.env.VITE_API_ENDPOINT}/users/iz/${encodeURIComponent(props.user.email)}`;
      const headers = {
        "x-api-key": "PlanItIsTheBestProjectEverXYZ",
      };

      try {
        const response = await axios.get(url, { headers });
        friends.value = response.data.friends;
        carbonSavings.value = response.data.carbonsavings;

        console.log('friends here')
        console.log(response.data.friends);
        console.log(response.data.carbonsavings);


      } catch (error) {
        console.error("Error fetching user", error);
      }
    }
    onMounted(fetchUser);

    const updateData = () => {
      userData.data = this.user.carbonSavings;
      carbonEmissionChart.value.update();

    }

    // watch(selectedFriend, (newFriend) => {
    //   if (newFriend === 'friend') {
    //     setTimeout(() => {
    //       friendData.data = this.friends
    //       carbonEmissionChart.value.update();
    //     }, 1000);
    //   } else {
    //     friendData.data = []; // Clear friend's data
    //     carbonEmissionChart.value.update(); // Update the chart
    //   }
    // });


    const updateChart = () => {
      if (selectedFriend.value === 'friend') {
        setTimeout(() => {
          // Update 'friendData' with friend's carbon emissions data
          friendData.data = [/* Ask brian */];
          carbonEmissionChart.value.update(); // Update the chart
        }, 1000);
      }
    };

    return {
      carbonEmissionChart,
      selectedFriend,
      updateChart,
      updateData,
      friends,
      carbonSavings,
    };
  },
};
</script>
