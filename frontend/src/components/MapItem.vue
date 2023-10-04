<template>
	<div>
		<GMapMap :center="center" :zoom="7" map-type-id="terrain" style="width: 100vw; height: 900px">
			<GMapMarker v-if="startLocation.lat && startLocation.lng" :position="startLocation" />
			<GMapMarker v-if="destination.lat && destination.lng" :position="destination" />
			<!-- Polyline here -->
			<GMapPolyline :path="polylinePath" :editable="true" ref="polyline" />

		</GMapMap>
		<div class="input-group m-2">
			<span class="input-group-text" id="autocomplete-label">Start Location</span>
			<GMapAutocomplete v-model="startLocation.value" placeholder="Starting point"
				:componentRestrictions="{ country: 'SG' }" @place_changed="setStartLocation" class="form-control" />
		</div>
		<div class="input-group m-2">
			<span class="input-group-text" id="autocomplete-label">End Location</span>
			<GMapAutocomplete v-model="destination.value" placeholder="Destination"
				:componentRestrictions="{ country: 'SG' }" @place_changed="setDestination" class="form-control" />
		</div>
		<button @click="fetchRouteDetails">Get Route Details</button>
		<div v-if="routeDetails">
			<p>Distance: {{ routeDetails.distanceMeters }} meters</p>
			<p>Duration: {{ routeDetails.duration }}</p>
		</div>
	</div>
</template>

<script>
import { ref, defineComponent, computed } from "vue";
import axios from "axios";

export default defineComponent({
	setup() {
		const center = { lat: 1.3331, lng: 103.7428 };
		const startLocation = ref({
			lat: 0,
			lng: 0
		});
		const destination = ref({
			lat: 0,
			lng: 0
		});
		const routeDetails = ref(null);
		const polylinePath = computed(() => {
			if (startLocation.value.lat && startLocation.value.lng && destination.value.lat && destination.value.lng) {
				return [startLocation.value, destination.value];
			}
			return [];
		});

		const setStartLocation = (place) => {
			const lat = Number(place.geometry.location.lat());
			const lng = Number(place.geometry.location.lng());
			startLocation.value = { lat, lng };
		};

		const setDestination = (place) => {
			const lat = Number(place.geometry.location.lat());
			const lng = Number(place.geometry.location.lng());
			destination.value = { lat, lng };
		};

		const fetchRouteDetails = async () => {
			const requestData = {
				origin: {
					location: {
						latLng: {
							latitude: startLocation.value.lat,
							longitude: startLocation.value.lng
						}
					}
				},
				destination: {
					location: {
						latLng: {
							latitude: destination.value.lat,
							longitude: destination.value.lng
						}
					}
				},
				travelMode: "DRIVE",
				routingPreference: "TRAFFIC_AWARE",
				// departureTime: new Date().toISOString(),
				// 30 mins later!	
				departureTime: new Date(Date.now() + 30 * 60 * 1000).toISOString(),
				computeAlternativeRoutes: false,
				routeModifiers: {
					avoidTolls: false,
					avoidHighways: false,
					avoidFerries: false
				},
				languageCode: "en-US",
				units: "IMPERIAL"
			};

			try {
				const response = await axios.post("https://routes.googleapis.com/directions/v2:computeRoutes", requestData, {
					headers: {
						'Content-Type': 'application/json',
						'X-Goog-Api-Key': 'AIzaSyC6xTDY_NrDH0U1NSE2Ug6AnzuVsbRPFYM',
						'X-Goog-FieldMask': 'routes.duration,routes.distanceMeters,routes.polyline.encodedPolyline'
					}
				});
				routeDetails.value = response.data.routes[0];  // Assuming the first route is what you want
			} catch (error) {
				console.error("Failed to fetch route details:", error);
			}
		};

		return {
			center,
			startLocation,
			destination,
			setStartLocation,
			setDestination,
			fetchRouteDetails,
			routeDetails,
			polylinePath
		};
	}
});
</script>
