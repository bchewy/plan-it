<template>
	<div>
		<!-- Google Map -->
		<GoogleMap :api-key="apiKey" style="width: 100%; height: 750px;" :center="center" :zoom="10">
			<Marker :options="{ position: center }" />
		</GoogleMap>

		<!-- Input group for starting location and destination -->
		<div class="input-group mb-3">
			<span class="input-group-text" id="inputGroup-sizing-default">Start Location</span>
			<input type="text" v-model="startLocation" class="form-control" aria-label="Starting Location"
				aria-describedby="inputGroup-sizing-default">
		</div>

		<div class="input-group mb-3">
			<span class="input-group-text" id="inputGroup-sizing-default">Destination</span>
			<input type="text" v-model="destination" class="form-control" aria-label="Destination"
				aria-describedby="inputGroup-sizing-default">
		</div>
	</div>
</template>

<script>
import { ref, defineComponent } from "vue";
import { GoogleMap, Marker } from "vue3-google-map";

export default defineComponent({
	components: { GoogleMap, Marker },
	setup() {
		const apiKey = 'xyz'; // You can switch to using the imported API_KEY if you like
		const center = { lat: 1.3331, lng: 103.7428 };

		// Create refs for the input values
		const startLocation = ref("");
		const destination = ref("");

		return { center, startLocation, destination, apiKey };
	},
});
</script>

<style scoped>
/* Add any additional styling if needed */
</style>
