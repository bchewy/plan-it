<style scoped>
.btn-green {
	background-color: #a7c957;
	color: white;
}

.bg-supergreen {
	background-color: #739072;
}

.map-container {
	position: relative;
}

.map {
	width: 100%;
	height: 100vh;
}

.form-overlay {
	position: absolute;
	top: 10px;
	right: 10px;
	width: 100%;
	background-color: #739072;
	padding: 7px;
	/* border-radius: 5px; */
}

.top-right {
	position: absolute;
	top: 20px;
	right: 20px;
}
</style>

<template>
	<div class="map-container" ref="mapContainer">
		<div v-if="errorMessage" class="alert alert-danger" role="alert">
			{{ errorMessage }}
		</div>
		<GMapMap class="map" :center="center" :zoom="zoom" map-type-id="terrain">
			<GMapMarker v-if="startLocation.lat && startLocation.lng" :position="startLocation" />
			<GMapMarker v-if="destination.lat && destination.lng" :position="destination" />
			<GMapPolyline :path="decodedPolyline" :editable="false" ref="polyline" :options="{ strokeColor: '#00FF00' }" />
		</GMapMap>

		<!-- <div class="form-overlay" draggable="true" @dragstart="dragStart" @dragend="dragEnd"> -->
		<!-- <vue-draggable-resizable :zIndex="1000"> -->
		<Vue3DraggableResizable v-if="show" :x="20" :y="0" :w="300" :h="200" :z="1" :draggable="true" :resizable="false" :referenceLineVisible="false">
			<div class="form-overlay rounded">
				<div class="row p-0 my-1 mx-1">
					<!-- Start Location -->
					<div class="col-sm-12 col-md-3 input-group mb-2">
						<!-- <span class="input-group-text font-weight-bold" id="autocomplete-label">From</span> -->
						<GMapAutocomplete ref="autocomplete" v-model="startLocation.value" placeholder="Origin" :componentRestrictions="{ country: 'SG' }" @place_changed="setStartLocation" class="form-control" />
						<button class="btn btn-green" type="button" @click="getUserLocation">
							<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(255, 255, 255, 1);transform: ;msFilter:;">
								<circle cx="12" cy="12" r="4"></circle>
								<path d="M13 4.069V2h-2v2.069A8.01 8.01 0 0 0 4.069 11H2v2h2.069A8.008 8.008 0 0 0 11 19.931V22h2v-2.069A8.007 8.007 0 0 0 19.931 13H22v-2h-2.069A8.008 8.008 0 0 0 13 4.069zM12 18c-3.309 0-6-2.691-6-6s2.691-6 6-6 6 2.691 6 6-2.691 6-6 6z"></path>
							</svg>
						</button>
					</div>
					<!-- Destination Field -->
					<div class="col-sm-12 col-md-3 input-group mb-2">
						<!-- <span class="input-group-text font-weight-bold" id="autocomplete-label">To</span> -->
						<GMapAutocomplete v-model="destination.value" placeholder="Destination" :componentRestrictions="{ country: 'SG' }" @place_changed="setDestination" class="form-control" />
					</div>
					<!-- Travel Mode -->
					<div class="col-sm-12 col-md-3 input-group mb-2">
						<!-- <span class="input-group-text font-weight-bold">Transporation</span> -->
						<select v-model="travelMode" class="form-control">
							<option value="" disabled selected>select transport</option>
							<option value="DRIVE">Drive</option>
							<option value="TWO_WHEELER">Motorbike</option>
							<option value="TRANSIT">Public Transport</option>
							<option value="BICYCLE">Bicycle</option>
							<option value="WALK">Walk</option>
						</select>
					</div>
					<div class="col-sm-12 col-md-3 input-group mb-3">
						<!-- <span class="input-group-text font-weight-bold"></span> -->
						<input type="time" v-model="departureTime" class="form-control">
						<!-- <button class="btn btn-green" type="button" @click="addMinutes(5)">+5m</button> -->
					</div>
				</div>
				<div class="mb-0 p-0">
					<button class="btn btn-green w-100" @click="fetchRouteDetails" data-bs-toggle="modal" data-bs-target="#progressModal">Log Route</button>
				</div>
			</div>


			<!-- Route modifiers -->
			<!-- <div class="mb-4">
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
			</div> -->



			<!-- <div v-if="routeDetails" class="card border-0 shadow p-4">
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
			</div> -->
			<!-- </vue-draggable-resizable> -->
		</Vue3DraggableResizable>

	</div>
	<!-- Modal for log completion -->
	<div class="modal fade" id="progressModal" tabindex="-1" aria-labelledby="progressModalLabel" aria-hidden="true">
		<div class="modal-dialog">
			<div v-if="routeDetails" class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="progressModalLabel">Progress</h5>
					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<div class="modal-body">
					<h5 class="card-title mb-4">Route Details</h5>
					<div class="d-flex justify-content-between mb-2">
						<strong>Distance:</strong>
						{{ routeDetails.distanceMeters.toFixed(0) }}m / {{ (routeDetails.distanceMeters / 1000).toFixed(2) }}km
					</div>
					<div class="d-flex justify-content-between mb-2">
						<span><strong>Duration:</strong></span>
						<span>{{ routeDetails.duration }} seconds</span>
					</div>
					<div class="d-flex justify-content-between mb-3">
						<span><strong>Carbon Emission:</strong></span>
						<span>{{ calculateCarbonEmission().toFixed(2) }} kg CO2</span>
					</div>
					<hr>
					<div class="d-flex justify-content-between mb-3">
						<span><strong>User Level:</strong></span>
						<span>{{ userLvl }}</span>
					</div>
					<div class="d-flex justify-content-between mb-3">
						<!-- <span><strong>Experience Progress:</strong></span>
						<span>{{ userExp }} / 100</span> -->

					</div>
					<div class="d-flex justify-content-between mb-3">
						<span><strong>Experience Added:</strong></span>
						<span>+{{ expAdded }}</span>
					</div>
					<div class="d-flex justify-content-between mb-3">
						<span><strong>Emission Savings:</strong></span>
						<span>{{ emissionSavings.toFixed(2) }} kg CO2</span>
					</div>
					<div class="d-flex justify-content-center">
						<button class="btn btn-primary rounded-pill shadow-sm" @click="openGoogleMaps">
							<i class="fas fa-map-marker-alt"></i> Open on Google Maps
						</button>
						<button class="btn btn-green rounded-pill shadow-sm" @click="openCityMapper">
							<i class="fas fa-map-marker-alt"></i> Open on CityMapper
						</button>
					</div>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
					<!-- <button type="button" class="btn btn-secondary" @click="location.reload()">Refresh</button> -->
				</div>
			</div>
		</div>
	</div>
</template>


<script>
import { ref, defineComponent, computed, reactive, watch } from "vue";
import axios from "axios";
import { useAuth0 } from '@auth0/auth0-vue';
import Vue3DraggableResizable from 'vue3-draggable-resizable';


export default defineComponent({
	data() {
		return {
			parentWidth: 0,
			componentWidth: 300,
		}
	},
	mounted() {
		this.parentWidth = this.$refs.mapContainer.clientWidth;
	},
	components: {
		// VueDraggableResizable
		Vue3DraggableResizable
	},
	methods: {
		openGoogleMaps() {
			window.open(this.googleMapsUrl, '_blank');
		},
		openCityMapper() {
			window.open(this.citymapperUrl, '_blank');

		},
		getUserLocation() {
			const geoLoc = navigator.geolocation;

			// Clear the cache
			if (navigator.geolocation.clearWatch) {
				navigator.geolocation.clearWatch(0);
			}
			geoLoc.getCurrentPosition(async (position) => {
				const lat = position.coords.latitude;
				const lng = position.coords.longitude;
				try {
					// Ensure lat and lng are valid numbers
					if (typeof lat === 'number' && typeof lng === 'number') {
						const response = await axios.get(`https://maps.googleapis.com/maps/api/geocode/json?latlng=${lat},${lng}&key=AIzaSyC6xTDY_NrDH0U1NSE2Ug6AnzuVsbRPFYM`);

						if (response.data.results && response.data.results.length > 0) {
							this.startLocation.value = response.data.results[0].formatted_address;
						} else {
							console.error('No results found');
						}
					} else {
						console.error('Invalid lat or lng values');
					}
				} catch (error) {
					console.error('Error making request:', error);
				}
			});
		},
	},
	computed: {
		// External API calls for displaying on map apps
		googleMapsUrl() {
			const origin = `${this.startLocation.lat},${this.startLocation.lng}`;
			const destination = `${this.destination.lat},${this.destination.lng}`;
			let travelmode = this.travelMode.toLowerCase();
			if (travelmode === 'drive') travelmode = 'driving';
			if (travelmode === 'two_wheeler') travelmode = 'driving';
			return `https://www.google.com/maps/dir/?api=1&origin=${origin}&destination=${destination}&travelmode=${travelmode}`;
		},
		citymapperUrl() {
			const origin = `${this.startLocation.lat},${this.startLocation.lng}`;
			const destination = `${this.destination.lat},${this.destination.lng}`;
			return `https://citymapper.com/directions?startcoord=${origin}&endcoord=${destination}`;
		},

		// Used for the vue3 drag and drop
		computedX() {
			// For smaller screens, we adjust the component width to fit the parent width
			if (window.innerWidth <= 768) {
				this.componentWidth = this.parentWidth;
			}
			// For medium screens, we adjust the component width to be 3/4 of the parent width
			else if (window.innerWidth <= 1024) {
				this.componentWidth = this.parentWidth * 0.75;
			}
			// For larger screens, we adjust the component width to be 1/2 of the parent width
			else {
				this.componentWidth = this.parentWidth * 0.5;
			}
			return this.parentWidth - this.componentWidth;
		}
	},
	props: ['userme'],
	setup(props) {
		const emissionSavings = ref(0);
		const userExp = ref(0);
		const expToNextLevel = ref(0);
		const userLvl = ref(0)
		const expAdded = ref(0)
		const show = ref(true);
		axios.get(`${import.meta.env.VITE_API_ENDPOINT}/users/ez/${props.userme.email}`)
			.then(response => {
				userExp.value = response.data.exp;
				expToNextLevel.value = 100 - userExp.value;
				userLvl.value = response.data.level;
			})
			.catch(error => {
				console.error(error);
			});
		const errorMessage = ref('');
		const { user, isAuthenticated } = useAuth0();
		const travelMode = ref("");
		const zoom = ref(13);
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
			if (distance > 10000) return 12;
			if (distance > 5000) return 13;
			if (distance > 2000) return 13;
			if (distance > 1000) return 13;
			if (distance > 500) return 13;
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
			if (startLocation.value.lat && startLocation.value.lng && destination.value.lat && destination.value.lng) {
				if (!travelMode.value) {
					alert('Please select a valid travel mode.');
					return;
				}
				const [hours, minutes] = departureTime.value.split(':').map(Number);
				const departureDate = new Date();
				departureDate.setHours(hours);
				departureDate.setMinutes(minutes);
				const departureTimeISO = departureDate.toISOString();

				// Google Routes Request Data
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

					// Retrieve direction steps, but we don't use this
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

					const carbonEms = calculateCarbonEmission(travelMode.value, routeDetails.value.distanceMeters)
					const distanceInKm = routeDetails.value.distanceMeters / 1000;
					const routeData = {
						route_id: 'route_' + Date.now(),  // You will need a way to generate unique route IDs
						start_point_lat_lng: `${startLocation.value.lat},${startLocation.value.lng}`,
						end_point_lat_lng: `${destination.value.lat}, ${destination.value.lng}`,
						start_point_name: await getLocationName(startLocation.value.lat, startLocation.value.lng),
						end_point_name: await getLocationName(destination.value.lat, destination.value.lng),
						transport_mode: travelMode.value,
						carbon_emission: carbonEms,
						timestamp: new Date().toISOString(),
						user_id: props.userme.email
					};

					// Update our route database (backend call)
					// Update user's EXP based on carbon emission calculation
					try {
						const headers = {
							'x-api-key': 'PlanItIsTheBestProjectEverXYZ'
						};
						await axios.post(`${import.meta.env.VITE_API_ENDPOINT}/routes`, routeData, { headers });
						await addExpBasedOnCarbonEmission(calculateCarbonEmissionForEXP(), distanceInKm, travelMode.value);


					} catch (error) {
						console.error('Failed to store route data:', error);
						errorMessage.value = error.message += ' Please try again.';


					}
				} catch (error) {
					console.error("Failed to fetch route details:", error);
					errorMessage.value = error.message += ' Please try again.';


				}
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

		const calculateCarbonEmissionForEXP = () => {
			const distanceInKm = routeDetails.value.distanceMeters / 1000;
			let carbonEmissionPerKm;
			switch (travelMode.value) {
				case 'driving':
					carbonEmissionPerKm = 0.12;  // Assume 0.12 kg CO2 emitted per km for a car
					break;
				case 'BICYCLE':
					carbonEmissionPerKm = 0;
					break;
				case 'WALK':
					carbonEmissionPerKm = 0;
					break;
				case 'TRANSIT':
					carbonEmissionPerKm = 0;
					break
				default:
					carbonEmissionPerKm = 0.12;  // Default to car emission if travel mode is not recognized
			}

			const carbonFootprintDriving = distanceInKm * 0.12;
			const carbonFootprint = distanceInKm * carbonEmissionPerKm;
			return [carbonFootprint, carbonFootprintDriving];
		};

		const addExpBasedOnCarbonEmission = (carbonList) => {
			emissionSavings.value = carbonList[1] - carbonList[0];
			const BASE_EXP = 10;
			const BONUS_EXP_PER_SAVED_KG = 10;

			// Calculate the total EXP to add based on the base EXP and the bonus for saved emissions
			const expToAdd = Math.ceil(BASE_EXP + (emissionSavings.value * BONUS_EXP_PER_SAVED_KG));
			expAdded.value = expToAdd


			axios.post(`${import.meta.env.VITE_API_ENDPOINT}/users/${user.value.email}/carbonsavings`, { carbonsavings: emissionSavings.value }, {
				headers: {
					'X-Api-Key': 'PlanItIsTheBestProjectEverXYZ'
				}
			})
				.then(response => {
					console.log(response.data.message);
					logUserActivity(`saved :${emissionSavings.value} co2`)
				})
				.catch(error => {
					console.error(error);
				});

			// Update the user exp in the backend
			axios.post(`${import.meta.env.VITE_API_ENDPOINT}/users/${user.value.email}/exp`, { exp: expToAdd }, {
				headers: {
					'X-Api-Key': 'PlanItIsTheBestProjectEverXYZ'
				}
			})
				.then(response => {
					console.log(response.data.message);
					logUserActivity(`gained ${expToAdd} exp`)
				})
				.catch(error => {
					console.error(error);
				});
		};

		const logUserActivity = (activity) => {
			axios.post(`${import.meta.env.VITE_API_ENDPOINT}/users/${user.value.email}/log`, { activity: activity }, {
				headers: {
					'X-Api-Key': 'PlanItIsTheBestProjectEverXYZ'
				}
			})
				.then(response => {
					console.log(response.data.message);
				})
				.catch(error => {
					console.error(error);
				});
		};


		// Auto update as long as destination is updated.
		// travelMode needs to be set.
		// watch(destination, fetchRouteDetails);



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
			emissionSavings,
			userExp,
			expToNextLevel,
			userLvl,
			expAdded,
			show,
		};
	}
});
</script>

