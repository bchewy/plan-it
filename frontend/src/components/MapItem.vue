<template>
	<div class="container-fluid">
		<div v-if="!isAuthenticated" class="row justify-content-center align-items-center" style="height: 100vh;">
			<h3 class="text-center p-5">Please log in to use this feature</h3>
		</div>
		<div v-else class="row">
			<div v-if="errorMessage" class="alert alert-danger" role="alert">
				{{ errorMessage }}
			</div>
			<div class="col-lg-8 col-md-12 p-0">
				<GMapMap class="w-100 vh-100" :center="center" :zoom="zoom" map-type-id="terrain">
					<GMapMarker v-if="startLocation.lat && startLocation.lng" :position="startLocation" />
					<GMapMarker v-if="destination.lat && destination.lng" :position="destination" />
					<GMapPolyline :path="decodedPolyline" :editable="true" ref="polyline" />
				</GMapMap>
			</div>
			<div class="col-lg-4 col-md-12 p-4">

				<div class="mb-4">
					<!-- Start Location -->
					<div class="input-group mb-3">
						<span class="input-group-text font-weight-bold" id="autocomplete-label">Start Location</span>
						<GMapAutocomplete ref="autocomplete" v-model="startLocation.value" placeholder="Starting point" :componentRestrictions="{ country: 'SG' }" @place_changed="setStartLocation" class="form-control" />
						<button class="btn btn-outline-secondary" type="button" @click="getUserLocation">Here</button>
					</div>

					<!-- End Location -->
					<div class="input-group mb-3">
						<span class="input-group-text font-weight-bold" id="autocomplete-label">End Location</span>
						<GMapAutocomplete v-model="destination.value" placeholder="Destination" :componentRestrictions="{ country: 'SG' }" @place_changed="setDestination" class="form-control" />
					</div>

					<!-- Travel Mode -->
					<div class="input-group mb-3">
						<span class="input-group-text font-weight-bold">Travel Mode</span>
						<select v-model="travelMode" class="form-control">
							<option value="DRIVE">Drive</option>
							<option value="TWO_WHEELER">Motorbike</option>
							<option value="TRANSIT">Public Transport</option>
							<option value="BICYCLE">Bicycle</option>
							<option value="WALK">Walk</option>
						</select>
					</div>

					<!-- Departure Time -->
					<div class="input-group mb-3">
						<span class="input-group-text font-weight-bold">Departure Time</span>
						<input type="time" v-model="departureTime" class="form-control">
						<button class="btn btn-outline-secondary" type="button" @click="addMinutes(5)">+5m</button>
					</div>
				</div>

				<!-- Route Modifiers -->
				<div class="mb-4">
					<span class="d-block mb-2 font-weight-bold">Route Modifiers</span>
					<div class="form-check">
						<input class="form-check-input" type="checkbox" value="" id="avoidTolls" v-model="routeModifiers.avoidTolls">
						<label class="form-check-label" for="avoidTolls">Avoid Tolls</label>
					</div>
					<div class="form-check">
						<input class="form-check-input" type="checkbox" value="" id="avoidHighways" v-model="routeModifiers.avoidHighways">
						<label class="form-check-label" for="avoidHighways">Avoid Highways</label>
					</div>
					<div class="form-check">
						<input class="form-check-input" type="checkbox" value="" id="avoidFerries" v-model="routeModifiers.avoidFerries">
						<label class="form-check-label" for="avoidFerries">Avoid Ferries</label>
					</div>
				</div>

				<!-- Log Route Button -->
				<div class="mb-4">
					<button class="btn btn-primary w-100" @click="fetchRouteDetails">Log Route</button>
				</div>

				<div v-if="routeDetails" class="card border-0 shadow p-4">
					<div class="card-body">
						<h5 class="card-title mb-4">Route Details</h5>
						<div class="mb-2">
							<strong>Distance:</strong>
							<div class="row">
								<div class="col-6">Meters: {{ routeDetails.distanceMeters }}</div>
								<div class="col-6">Kilometers: {{ routeDetails.distanceMeters / 1000 }}</div>
							</div>
						</div>
						<div class="d-flex justify-content-between mb-2">
							<span><strong>Duration:</strong></span>
							<span>{{ routeDetails.duration }} seconds</span>
						</div>
						<div class="d-flex justify-content-between mb-3">
							<span><strong>Carbon Emission:</strong></span>
							<span>{{ calculateCarbonEmission() }} kg CO2</span>
						</div>
						<div class="d-flex justify-content-center">
							<button class="btn btn-primary rounded-pill shadow-sm" @click="openGoogleMaps">
								<i class="fas fa-map-marker-alt"></i> Open on Google Maps
							</button>
						</div>
					</div>
				</div>

			</div>
		</div>
	</div>
</template>



<script>
import { ref, defineComponent, computed, reactive } from "vue";
import axios from "axios";
import { useAuth0 } from '@auth0/auth0-vue';

export default defineComponent({
	components: {
	},
	methods: {
		triggerConfetti() {
			confetti({
				particleCount: 100,
				spread: 70,
				origin: { y: 0.6 }
			});
		},
		openGoogleMaps() {
			window.open(this.googleMapsUrl, '_blank');
		},
		getUserLocation() {
			if (navigator.geolocation) {
				navigator.geolocation.getCurrentPosition((position) => {
					const lat = position.coords.latitude;
					const lng = position.coords.longitude;
					const locationString = `${lat}, ${lng}`;

					this.$refs.autocomplete.$el.querySelector('input').value = locationString;
					this.$refs.autocomplete.$el.querySelector('input').dispatchEvent(new Event('input'));
				});
			} else {
				this.errorMessage = "Geolocation is not supported by this browser.";
			}
		}
	},
	computed: {
		// Open up on google maps
		googleMapsUrl() {
			const origin = `${this.startLocation.lat},${this.startLocation.lng}`;
			const destination = `${this.destination.lat},${this.destination.lng}`;
			let travelmode = this.travelMode.toLowerCase();
			if (travelmode === 'drive') travelmode = 'driving';
			if (travelmode === 'two_wheeler') travelmode = 'driving';
			return `https://www.google.com/maps/dir/?api=1&origin=${origin}&destination=${destination}&travelmode=${travelmode}`;
		},
	},
	props: ['userme'],
	setup(props) {
		const errorMessage = ref('');
		const { user, isAuthenticated } = useAuth0();
		const travelMode = ref("DRIVE");  // Default is "DRIVE"
		const confetti = ref(null);
		const zoom = ref(12);  // Default zoom level
		const center = reactive({ lat: 1.3331, lng: 103.7428 });
		const startLocation = ref({
			lat: 0,
			lng: 0
		});
		const destination = ref({
			lat: 0,
			lng: 0
		});
		const routeModifiers = ref({
			avoidTolls: false,
			avoidHighways: false,
			avoidFerries: false
		});
		const routeDetails = ref(null);
		const decodedPolyline = ref([]);
		const directionSteps = ref([]);
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
			center.lat = lat;
			center.lng = lng;
			if (destination.value.lat && destination.value.lng) {
				const distance = getDistance(startLocation.value, destination.value);
				zoom.value = getZoomLevel(distance);
			}

		};

		function getDistance(location1, location2) {
			const R = 6371e3; // metres
			const φ1 = location1.lat * Math.PI / 180; // φ, λ in radians
			const φ2 = location2.lat * Math.PI / 180;
			const Δφ = (location2.lat - location1.lat) * Math.PI / 180;
			const Δλ = (location2.lng - location1.lng) * Math.PI / 180;

			const a = Math.sin(Δφ / 2) * Math.sin(Δφ / 2) +
				Math.cos(φ1) * Math.cos(φ2) *
				Math.sin(Δλ / 2) * Math.sin(Δλ / 2);
			const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

			const distance = R * c; // in metres
			return distance;
		}

		function getZoomLevel(distance) {
			if (distance > 10000) return 10;
			if (distance > 5000) return 12;
			if (distance > 2000) return 12;
			if (distance > 1000) return 12;
			if (distance > 500) return 12;
			return 18;
		}

		const setDestination = (place) => {
			const lat = Number(place.geometry.location.lat());
			const lng = Number(place.geometry.location.lng());
			destination.value = { lat, lng };
			if (startLocation.value.lat && startLocation.value.lng) {
				const distance = getDistance(startLocation.value, destination.value);
				zoom.value = getZoomLevel(distance);
			}
		};

		const getCurrentTime = () => {
			const now = new Date();
			const hours = String(now.getHours()).padStart(2, '0');
			const minutes = String(now.getMinutes()).padStart(2, '0');
			return `${hours}:${minutes}`;
		};

		const addFiveMinutesToCurrentTime = () => {
			const now = new Date();
			now.setMinutes(now.getMinutes() + 5);
			const hours = String(now.getHours()).padStart(2, '0');
			const minutes = String(now.getMinutes()).padStart(2, '0');
			return `${hours}:${minutes}`;
		};
		const departureTime = ref(addFiveMinutesToCurrentTime());

		const addMinutes = (minutesToAdd) => {
			const [hours, minutes] = departureTime.value.split(':').map(Number);
			const currentTimeInMinutes = hours * 60 + minutes;
			const newTimeInMinutes = currentTimeInMinutes + minutesToAdd;

			const newHours = Math.floor(newTimeInMinutes / 60) % 24;
			const newMinutes = newTimeInMinutes % 60;

			departureTime.value = `${String(newHours).padStart(2, '0')}:${String(newMinutes).padStart(2, '0')}`;
		};
		const fetchRouteDetails = async () => {
			// this.triggerConfetti();
			const [hours, minutes] = departureTime.value.split(':').map(Number);
			const departureDate = new Date();
			departureDate.setHours(hours);
			departureDate.setMinutes(minutes);
			const departureTimeISO = departureDate.toISOString();

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
				departureTime: departureTimeISO,
				computeAlternativeRoutes: false,
				routeModifiers: {
					avoidTolls: routeModifiers.value.avoidTolls,
					avoidHighways: routeModifiers.value.avoidHighways,
					avoidFerries: routeModifiers.value.avoidFerries
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

				if (response.data.routes[0]?.legs[0]?.steps) {
					directionSteps.value = response.data.routes[0].legs[0].steps;
				}

				routeDetails.value = response.data.routes[0];
				const encodedPolyline = response.data.routes[0].polyline.encodedPolyline;
				decodedPolyline.value = decodePolyline(encodedPolyline);

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

				// Store in DB
				console.log("Route stored in the database for this user.")
				const routeData = {
					route_id: 'route_' + Date.now(),  // You will need a way to generate unique route IDs
					start_point_lat_lng: `Point(${startLocation.value.lat}, ${startLocation.value.lng})`,
					end_point_lat_lng: `Point(${destination.value.lat}, ${destination.value.lng})`,
					start_point_name: await getLocationName(startLocation.value.lat, startLocation.value.lng),
					end_point_name: await getLocationName(destination.value.lat, destination.value.lng),
					transport_mode: travelMode.value,
					carbon_emission: calculateCarbonEmission(travelMode.value, routeDetails.value.distanceMeters),  // Assume calculateCarbonEmission is a function to calculate the carbon emission
					timestamp: new Date().toISOString(),
					user_id: props.userme.email
				};

				try {
					// Send a POST request to the server to store the route data
					const headers = {
						'x-api-key': 'PlanItIsTheBestProjectEverXYZ'
					};
					await axios.post(`${import.meta.env.VITE_API_ENDPOINT}/routes`, routeData, { headers });
				} catch (error) {
					console.error('Failed to store route data:', error);
					errorMessage.value = error.message += ' Please try again.';


				}
			} catch (error) {
				console.error("Failed to fetch route details:", error);
				errorMessage.value = error.message += ' Please try again.';


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

		const calculateCarbonEmission = () => {
			const distanceInKm = routeDetails.value.distanceMeters / 1000;
			let carbonEmissionPerKm;

			switch (travelMode.value) {
				case 'driving':
					carbonEmissionPerKm = 0.12;  // Assume 0.12 kg CO2 emitted per km for a car
					break;
				case 'bicycling':
				case 'walking':
					carbonEmissionPerKm = 0;  // No carbon emission for bicycling or walking
					break;
				default:
					carbonEmissionPerKm = 0.12;  // Default to car emission if travel mode is not recognized
			}

			const carbonFootprint = distanceInKm * carbonEmissionPerKm;
			return carbonFootprint;
		};


		return {
			calculateCarbonEmission,
			addMinutes,
			departureTime,
			routeModifiers,
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
			zoom,
			errorMessage,
		};
	}
});
</script>

