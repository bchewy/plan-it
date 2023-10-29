<template>
  <div>
    <label for="friendSelector">Select a Friend: </label>
    <select v-model="selectedFriend" id="friendSelector" @change="updateChart">
      <option value="user">You</option>
      <option value="friend">Friend</option>
    </select>
    <canvas id="carbonEmissionComparisonChart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js/auto';
import 'chartjs-adapter-date-fns';
import { ref, onMounted, watch } from 'vue';

export default {
  setup() {
    const carbonEmissionChart = ref(null);
    const selectedFriend = ref('user'); // Default selection

    onMounted(() => {

      const data = []; //fill this in (ask brian)

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

      watch(selectedFriend, (newFriend) => {
        if (newFriend === 'friend') {
          setTimeout(() => {
            friendData.data = [/* ask brian abt api */];
            carbonEmissionChart.value.update(); 
          }, 1000); 
        } else {
          friendData.data = []; // Clear friend's data
          carbonEmissionChart.value.update(); // Update the chart
        }
      });
    });

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
    };
  },
};
</script>
