<template>
	<div class="container-fluid">
		<div v-if="!isAuthenticated" class="row justify-content-center align-items-center" style="height: 100vh;">
			<h3 class="text-center p-5">Please log in to use this feature</h3>
		</div>
		<div v-else class="row">
			<div class="col-lg-8 col-md-12">
				<GMapMap :center="center" :zoom="12" map-type-id="terrain" style="width: 100%; height: 100vh;">
					<GMapMarker v-if="startLocation.lat && startLocation.lng" :position="startLocation" />
					<GMapMarker v-if="destination.lat && destination.lng" :position="destination" />
					<GMapPolyline :path="decodedPolyline" :editable="true" ref="polyline" />
				</GMapMap>
			</div>
			<div class="col-lg-4 col-md-12 p-4">
				<div class="input-group mb-3">
					<span class="input-group-text" id="autocomplete-label">Start Location</span>
					<GMapAutocomplete v-model="startLocation.value" placeholder="Starting point"
						:componentRestrictions="{ country: 'SG' }" @place_changed="setStartLocation" class="form-control" />
				</div>
				<div class="input-group mb-3">
					<span class="input-group-text" id="autocomplete-label">End Location</span>
					<GMapAutocomplete v-model="destination.value" placeholder="Destination"
						:componentRestrictions="{ country: 'SG' }" @place_changed="setDestination" class="form-control" />
				</div>
				<div class="input-group mb-3">
					<span class="input-group-text">Travel Mode</span>
					<select v-model="travelMode" class="form-control">
						<option value="DRIVE">Drive</option>
						<option value="TRANSIT">Public Transport</option>
					</select>
				</div>
				<button class="btn btn-primary mb-4" @click="fetchRouteDetails">Log Route</button>
				<div v-if="routeDetails">
					<p><strong>Distance:</strong> {{ routeDetails.distanceMeters }} meters</p>
					<p><strong>Duration:</strong> {{ routeDetails.duration }}</p>
					<div v-if="directionSteps.length > 0" style="max-height: 300px; overflow-y: auto;">
						<h2>Directions:</h2>
						<ol>
							<li v-for="(step, index) in directionSteps" :key="index">
								{{ step && step.navigationInstruction ? step.navigationInstruction.instructions : 'Step not available' }}
							</li>
						</ol>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import { ref, defineComponent, computed } from "vue";
import axios from "axios";
import { useAuth0 } from '@auth0/auth0-vue';
// import { useStore } from 'vuex';


export default defineComponent({
	props: ['userme'],
	setup(props) {
		// const store = useStore();
		const { user, isAuthenticated } = useAuth0();
		// console.log('is authenticated?', isAuthenticated)
		// console.log('user', user)
		const travelMode = ref("DRIVE");  // Default is "DRIVE"
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
		const decodedPolyline = ref([]);  // Decoded polyline data from the API
		const directionSteps = ref([]);  // Add this line at the beginning of your setup() method

		// original straight polyline
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
			let requestData = {
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
				travelMode: travelMode.value,
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
			if (travelMode.value === "DRIVE") {
				requestData.routingPreference = "TRAFFIC_AWARE";
			}

			try {
				const response = await axios.post("https://routes.googleapis.com/directions/v2:computeRoutes", requestData, {
					headers: {
						'Content-Type': 'application/json',
						'X-Goog-Api-Key': 'AIzaSyC6xTDY_NrDH0U1NSE2Ug6AnzuVsbRPFYM',
						'X-Goog-FieldMask': 'routes.duration,routes.distanceMeters,routes.polyline.encodedPolyline,routes.legs.steps'
					}
				});

				//Error Checking
				// console.log(JSON.stringify(response.data, null, 2));  // Log the entire API response
				// console.log("Steps from API:", response.data.routes[0]?.legs[0]?.steps);
				// console.log(startLocation.value)


				// if (response.data.routes[0]?.legs[0]?.steps) {
				// 	directionSteps.value = response.data.routes[0].legs[0].steps.map(step => step.html_instructions);
				// }

				if (response.data.routes[0]?.legs[0]?.steps) {
					directionSteps.value = response.data.routes[0].legs[0].steps;
				}

				// console.log('directionSteps:', JSON.stringify(directionSteps.value, null, 2));
				routeDetails.value = response.data.routes[0];  // Assuming the first route is what you want
				// Decode the encodedPolyline and update decodedPolyline
				const encodedPolyline = response.data.routes[0].polyline.encodedPolyline;
				decodedPolyline.value = decodePolyline(encodedPolyline);  // Assume decodePolyline is a function to decode the polyline

				// Directions
				directionSteps.value = response.data.routes[0].legs[0].steps.map(step => step);


				// Helper Function to get names
				const getLocationName = async (lat, lng) => {
					try {
						const response = await axios.get(`https://maps.googleapis.com/maps/api/geocode/json?latlng=${lat},${lng}&key=AIzaSyC6xTDY_NrDH0U1NSE2Ug6AnzuVsbRPFYM`);
						if (response.data.results && response.data.results.length > 0) {
							// Return the formatted address of the first result
							return response.data.results[0].formatted_address;
						}
					} catch (error) {
						console.error('Failed to fetch location name:', error);
					}
					return '';  // Return an empty string if the location name could not be fetched
				};

				// Completed Fetching processing plotting
				// Store in DB
				console.log('Attempting to store database in MongoDB')
				console.log('Loggin for user email', props.userme.name)
				const routeData = {
					route_id: 'route_1' + Date.now(),  // You will need a way to generate unique route IDs
					start_point_lat_lng: `Point(${startLocation.value.lat}, ${startLocation.value.lng})`,
					end_point_lat_lng: `Point(${destination.value.lat}, ${destination.value.lng})`,
					start_point_name: await getLocationName(startLocation.value.lat, startLocation.value.lng),
					end_point_name: await getLocationName(destination.value.lat, destination.value.lng),
					transport_mode: travelMode.value === 'DRIVE' ? 'car' : 'public transport',
					carbon_emission: 0,
					timestamp: new Date().toISOString(),
					user_id: props.userme.email
				};

				try {
					// Send a POST request to the server to store the route data
					console.log('Attempt store happenin...')
					await axios.post('https://api.bchwy.com/routes', routeData);  // Adjust the URL to match your server
				} catch (error) {
					console.error('Failed to store route data:', error);
				}

				console.log('Route data stored successfully.. we think?');
			} catch (error) {
				console.error("Failed to fetch route details:", error);
			}
		};

		const decodePolyline = (encoded) => {
			let index = 0;
			let lat = 0;
			let lng = 0;
			const coordinates = [];
			let char = 0;  // Declare char here

			while (index < encoded.length) {
				let shift = 0;
				let result = 0;

				do {
					char = encoded.charCodeAt(index++) - 63;  // Update char
					result |= (char & 0x1F) << shift;
					shift += 5;
				} while (char >= 0x20);

				const dlat = (result & 1 ? ~(result >> 1) : result >> 1);
				lat += dlat;

				shift = 0;
				result = 0;

				do {
					char = encoded.charCodeAt(index++) - 63;  // Update char
					result |= (char & 0x1F) << shift;
					shift += 5;
				} while (char >= 0x20);

				const dlng = (result & 1 ? ~(result >> 1) : result >> 1);
				lng += dlng;

				coordinates.push({ lat: lat / 1E5, lng: lng / 1E5 });
			}

			return coordinates;
		};



		return {
			center,
			startLocation,
			destination,
			setStartLocation,
			setDestination,
			fetchRouteDetails,
			routeDetails,
			polylinePath,
			decodedPolyline,
			travelMode,
			directionSteps,
			user,
			isAuthenticated,
			// user: computed(() => store.getters.user),
			// isAuthenticated: computed(() => store.getters.isAuthenticated)
		};
	}
});
</script>
