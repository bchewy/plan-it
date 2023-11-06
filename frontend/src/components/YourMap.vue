<template>
	<GMapMap :center="mapCenter" :zoom="10" style="width: 100%; height: 500px;" ref="gMap">
		<GMapPolyline v-for="(route, index) in routes" :key="index" :path="route.path" :options="polylineOptions(route)" @click="selectRoute(route)" />
	</GMapMap>
</template>

<script>
import { ref, defineComponent, computed, reactive, watch, onMounted } from "vue";
// import { GMapMap, GMapPolyline, useLoadScript } from 'vue3-google-maps';
import axios from "axios";
import { useAuth0 } from '@auth0/auth0-vue';
import Vue3DraggableResizable from 'vue3-draggable-resizable';
import { useGeolocation } from '@vueuse/core'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
// import Modal from 'bootstrap/js/dist/modal';

export default defineComponent({
	components: {
		GMapMap,
		GMapPolyline,
		Vue3DraggableResizable
	},
	setup() {
		const mapCenter = ref({ lat: 0, lng: 0 }); // Center the map around your routes
		const routes = ref([]); // Your routes data

		// You would call an API or somehow populate the routes data
		// Each route should have a 'path' property which is an array of LatLng objects or literal objects

		// Calculate polyline options based on emissions
		const polylineOptions = (route) => {
			const emissionIntensity = calculateEmissionIntensity(route.carbon_emission);
			return {
				strokeColor: emissionIntensity.color,
				strokeOpacity: 0.8,
				strokeWeight: emissionIntensity.weight,
			};
		};

		const calculateEmissionIntensity = (emission) => {
			// Define your logic here to determine color and weight of polyline
			// For example, higher emissions could have a darker color and thicker line
			const color = emission > 50 ? '#FF0000' : '#00FF00';
			const weight = emission > 50 ? 5 : 2;
			return { color, weight };
		};

		const selectRoute = (route) => {
			// Define what happens when you click on a route
			// You might set the selected route's data to show in an info window or a separate details view
		};

		useLoadScript({
			googleMapsApiKey: 'YOUR_API_KEY', // Replace with your API key
		});

		return {
			mapCenter,
			routes,
			polylineOptions,
			selectRoute,
		};
	},
});
</script>
