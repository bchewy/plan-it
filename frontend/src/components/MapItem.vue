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
	height: 100vh;
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

.toggle-button {
	position: absolute;
	bottom: 10px;
	right: 10px;
	z-index: 10000;
}

.top-right {
	position: absolute;
	top: 20px;
	right: 20px;
}

.autocomplete-container {
	position: relative;
}

.disable-overlay {
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	background-color: rgba(255, 255, 255, 0.5);
}
</style>

<template>
	<div class="map-container" ref="mapContainer">
		<!-- <div v-if="errorMessage" class="alert alert-danger" role="alert">
			{{ errorMessage }}
		</div> -->
		<!-- <button @click="toggleChat" class="position-fixed bottom-0 end-0 btn" style="z-index: 10000;">
			<img src="https://bchewy-images.s3.ap-southeast-1.amazonaws.com/plan-it/Travel+chat+icon.png" alt="chat" width="50" height="50" />
		</button>

		<Vue3DraggableResizable v-if="showChat" :w="500" :h="300" :x="x" :y="y" :z="10001" :parent="true" :minw="200" :minh="200" :resizable="true" :draggable="true" class="rounded">
			<iframe src="https://embed.fixie.ai/agents/a14a698f-4934-4410-a88a-67051418ed65?agentStartsConversation=1" allow="clipboard-write" class="h-100 w-100" />
		</Vue3DraggableResizable> -->

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

					<!-- Travel Mode -->
					<div class="col-sm-12 col-md-3 input-group mb-2">
						<!-- <span class="input-group-text font-weight-bold">Transporation</span> -->
						<select v-model="travelMode" class="form-control">
							<option value="" disabled selected>select transport</option>
							<option value="DRIVE">🚗 Drive</option>
							<!-- <option value="TWO_WHEELER">🏍️ Motorbike</option> -->
							<option value="TRANSIT">🚌 Public Transport</option>
							<option value="BICYCLE">🚲 Bicycle</option>
							<option value="WALK">🚶‍♂️ Walk</option>
						</select>
					</div>
					<!-- Start Location -->
					<div class="col-sm-12 col-md-3 input-group mb-2">
						<!-- <span class="input-group-text font-weight-bold" id="autocomplete-label">From</span> -->
						<!-- <GMapAutocomplete :ref="startLocationRef" v-model="startLocation.value" placeholder="Origin" :componentRestrictions="{ country: 'SG' }" @place_changed="setStartLocation" class="form-control" /> -->

						<GMapAutocomplete v-if="!isDisabled" :ref="startLocationRef" v-model="startLocation.value" placeholder="Origin" :componentRestrictions="{ country: 'SG' }" @place_changed="setStartLocation" class="form-control" />
						<input v-else :value="startLocation.value" :placeholder="placeholderText" class="form-control" disabled />

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
					<!-- Depature Time Field -->
					<div class="col-sm-12 col-md-3 input-group mb-3">
						<!-- <span class="input-group-text font-weight-bold"></span> -->
						<input type="time" v-model="departureTime" class="form-control">
						<!-- <button class="btn btn-green" type="button" @click="addMinutes(5)">+5m</button> -->
					</div>
				</div>
				<!-- Log Route Button -->
				<div class="mb-0 p-0">
					<button class="btn btn-green w-100" @click="fetchRouteDetails" :disabled="isButtonClicked" :title="isButtonClicked ? 'Please refresh the page to log more routes' : ''">Log Route</button>
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
					<div class="text-center">
						<img :src="randomGif" alt="Random Gif" class="mb-2">
						<p> Congratulations. You've logged your route! Please proceed to verify it later in <strong>Profile > Verify</strong> to get maximum EXP.</p>
						<div class="d-flex justify-content-center mt-3">
							<button data-bs-dismiss="modal" class="btn btn-primary rounded-pill shadow-sm" @click="$router.push('/verify')">
								Go to Verify Page
							</button>
						</div>
					</div>

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
						<span>{{ calculateCarbonEmission().toFixed(2) }} g CO2</span>
					</div>
					<hr>
					<h5 class="card-title mb-4">User Details</h5>

					<div class="d-flex justify-content-between">
						<span><strong>User Level:</strong></span>
						<span>{{ userLvl }}</span>
					</div>
					<div class="d-flex justify-content-between mb-2">
						<span><strong>Experience Added:</strong></span>
						<span>+{{ expAdded }}</span>
					</div>
					<div class="d-flex justify-content-between mb-2">
						<span><strong>Emission Savings:</strong></span>
						<span>{{ emissionSavings.toFixed(2) }} g CO2</span>
					</div>
					<!-- Open in GMaps/CityMapper -->
					<div class="d-flex justify-content-center">
						<button class="btn btn-primary shadow-sm" @click="openGoogleMaps">
							<i class="fas fa-map-marker-alt"></i> Open on Google Maps
						</button>
						<button class="btn btn-green shadow-sm" @click="openCityMapper">
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
import { ref, defineComponent, computed, reactive, watch, onMounted } from "vue";
import axios from "axios";
import { useAuth0 } from '@auth0/auth0-vue';
import Vue3DraggableResizable from 'vue3-draggable-resizable';
import { useGeolocation } from '@vueuse/core'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import Modal from 'bootstrap/js/dist/modal';



export default defineComponent({
	mounted() {
		this.parentWidth = this.$refs.mapContainer.clientWidth;
	},
	components: {
		Vue3DraggableResizable
	},
	methods: {
		openGoogleMaps() {
			window.open(this.googleMapsUrl, '_blank');
		},
		openCityMapper() {
			window.open(this.citymapperUrl, '_blank');
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
		const showIframe = ref(false);
		// Call to check user's exp and level, if any.
		axios.get(`${import.meta.env.VITE_API_ENDPOINT}/users/ez/${props.userme.email}`)
			.then(response => {
				userExp.value = response.data.exp;
				expToNextLevel.value = 100 - userExp.value;
				userLvl.value = response.data.level;
			})
			.catch(error => {
				console.error(error);
				toast.error(`${error.response.data.message}`, {
					autoClose: 5000,
					position: toast.POSITION.TOP_CENTER,
				});
			});

		const errorMessage = ref('');
		const { user, isAuthenticated } = useAuth0();
		const travelMode = ref("");
		const zoom = ref(13);
		const center = reactive({ lat: 1.3331, lng: 103.7428 });
		const startLocation = ref({
			lat: 0,
			lng: 0,
			value: ''
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
		const { coords, locatedAt, error, resume, pause } = useGeolocation()
		const isDisabled = ref(false) // Set this to true when you want to disable the input
		const placeholderText = ref('Origin')
		const totalKm = ref(0)
		const API_KEY = `${import.meta.env.VITE_GMAPS_API_KEY}`

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


		// # ================================================================================================================================================================================================================================================================================================


		const fetchRouteDetails = async () => {
			if (!startLocation.value.lat || !destination.value.lat) {
				console.log("hello")
				toast.error(`You did not select any locations!`, {
					autoClose: 5000,
					position: toast.POSITION.TOP_CENTER,
				});
			}
			if (startLocation.value.lat && startLocation.value.lng && destination.value.lat && destination.value.lng) {
				if (!travelMode.value) {
					toast.error(`Please select a valid travel mode.`, {
						autoClose: 5000,
						position: toast.POSITION.TOP_CENTER,
					});
					return;
				}
				// Check for user attempting to log the button more...
				isButtonClicked.value = true;

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

				// Declare values for GoogleAPI, traffic aware routing
				if (travelMode.value === "DRIVE") {
					requestData.routingPreference = "TRAFFIC_AWARE";
					requestData.departureTime = departureTimeISO;
				}

				try {
					const response = await axios.post("https://routes.googleapis.com/directions/v2:computeRoutes", requestData, {
						headers: {
							'Content-Type': 'application/json',
							'X-Goog-Api-Key': `${import.meta.env.VITE_GMAPS_API_KEY}`,
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
							const response = await axios.get(`https://maps.googleapis.com/maps/api/geocode/json?latlng=${lat},${lng}&key=${import.meta.env.VITE_GMAPS_API_KEY_API_KEY}`);
							if (response.data.results && response.data.results.length > 0) {
								// Return the formatted address of the first result
								return response.data.results[0].formatted_address;
							}
						} catch (error) {
							console.error('Failed to fetch location name:', error);
							toast.error(`${error.response.data.message}`, {
								autoClose: 5000,
								position: toast.POSITION.TOP_CENTER,
							});
						}
						return '';  // Return an empty string if the location name could not be fetched
					};

					const carbonEms = calculateCarbonEmission(travelMode.value, routeDetails.value.distanceMeters)
					const distanceInKm = routeDetails.value.distanceMeters / 1000;
					const routeData = {
						route_id: 'route_' + Date.now(),  // You will need a way to generate unique route IDs
						distance: distanceInKm,
						start_point_lat_lng: `${startLocation.value.lat},${startLocation.value.lng}`,
						end_point_lat_lng: `${destination.value.lat}, ${destination.value.lng}`,
						start_point_name: await getLocationName(startLocation.value.lat, startLocation.value.lng),
						end_point_name: await getLocationName(destination.value.lat, destination.value.lng),
						transport_mode: travelMode.value,
						carbon_emission: carbonEms,
						timestamp: new Date().toISOString(),
						user_id: props.userme.email,
						validated: false, // Validation here is for users to confirm the route via GeoLocation
						checkedStartLocation: isDisabled.val //Validation here is for users to ensure that they selected currentLocation as start location.
					};


					// Update our route database (backend Call)
					// Update user's EXP based on carbon emission calculation
					try {
						const headers = {
							'x-api-key': 'PlanItIsTheBestProjectEverXYZ'
						};


						await axios.post(`${import.meta.env.VITE_API_ENDPOINT}/routes`, routeData, { headers });


						totalKm.value += distanceInKm;
						// EXP Given here is not the most and incomplete.
						await addExpBasedOnCarbonEmission(calculateCarbonEmissionForEXP(), distanceInKm, travelMode.value);
						showModal();



					} catch (error) {
						console.error('Failed to store route data:', error);
						// errorMessage.value = error.message += ' Please try again.';
						toast.error(`${error.response.data.message}`, {
							autoClose: 5000,
							position: toast.POSITION.TOP_CENTER,
						});


					}
				}
				catch (error) {
					console.error("Failed to fetch route details:", error);
					errorMessage.value = error.message += ' Please try again.';
					toast.error(`${error.response.data.message}`, {
						autoClose: 5000,
						position: toast.POSITION.TOP_CENTER,
					});


				}
			}
		};

		const fetchPolylineOnly = async () => {
			if (startLocation.value.lat && startLocation.value.lng && destination.value.lat && destination.value.lng) {
				if (!travelMode.value) {
					toast(`${error.response.data.message}`, {
						autoClose: 5000,
						position: toast.POSITION.TOP_CENTER,
					});
					return;
				}
				try {
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
						travelMode: travelMode.value
					};
					const response = await axios.post("https://routes.googleapis.com/directions/v2:computeRoutes", requestData, {
						headers: {
							'Content-Type': 'application/json',
							'X-Goog-Api-Key': `${import.meta.env.VITE_GMAPS_API_KEY}`,
							'X-Goog-FieldMask': 'routes.polyline.encodedPolyline'
						}
					});
					if (response.data.routes && response.data.routes.length > 0) {
						const route = response.data.routes[0];
						const polyline = route.polyline.encodedPolyline;
						decodedPolyline.value = decodePolyline(polyline);
					}
				} catch (error) {
					console.error('Failed to fetch polyline:', error);
				}
			}
		};

		const startLocationRef = ref(null);

		const getUserLocation = async () => {
			const lat = coords.value.latitude;
			const lng = coords.value.longitude;
			try {
				url = `https://maps.googleapis.com/maps/api/geocode/json?latlng=${lat},${lng}&key=${import.meta.env.VITE_GMAPS_API_KEY}`
				const response = await axios.get(url);
				if (response.data.results && response.data.results.length > 0) {
					startLocation.value = { lat, lng };
					isDisabled.value = true;
					placeholderText.value = response.data.results[0].formatted_address;
				} else {
					console.error('No results found');
				}
			} catch (error) {
				console.error('Error making request:', error);
			}
		};

		// # ================================================================================================================================================================================================================================================================================================

		const randomGif = ref('');
		const fetchRandomGif = async () => {
			const url = `https://api.giphy.com/v1/gifs/random?api_key=${import.meta.env.VITE_GIFY_API_KEY}&tag=congratulations&rating=g`;

			try {
				const response = await axios.get(url);
				randomGif.value = response.data.data.images.fixed_height.url;
				// console.log(randomGif.value);
			} catch (error) {
				console.error('Error fetching random gif:', error);
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
			const BASE_EXP = 1; //previously 10
			const BONUS_EXP_PER_SAVED_KG = 1; //previously 10

			// Calculate the total EXP to add based on the base EXP and the bonus for saved emissions
			const expToAdd = Math.ceil(BASE_EXP + (emissionSavings.value * BONUS_EXP_PER_SAVED_KG));
			expAdded.value = expToAdd

			// Update the user's total km travelled
			axios.post(`${import.meta.env.VITE_API_ENDPOINT}/users/${user.value.email}/total_km`, { total_km: totalKm.value }, {
				headers: {
					'X-Api-Key': 'PlanItIsTheBestProjectEverXYZ'
				}
			})
				.then(response => {
					console.log(response.data.message);
					// logUserActivity(`travelled ${distanceInKm} km`)
				})
				.catch(error => {
					console.error(error);
				});



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

		const showModal = () => {
			const modalElement = document.getElementById('progressModal');
			const modalInstance = new Modal(modalElement);
			modalInstance.show();
		};

		// Auto update as long as destination is updated.
		// travelMode needs to be set.
		watch(destination, fetchPolylineOnly);


		// FixieAI items
		const x = ref(0);
		const y = ref(0);
		const showChat = ref(false);

		onMounted(async () => {
			x.value = window.innerWidth - 510; // 500 (width of the component) + 10 (right margin)
			y.value = window.innerHeight - 310; // 300 (height of the component) + 10 (bottom margin)
			await fetchRandomGif();

		});

		const toggleChat = () => {
			showChat.value = !showChat.value;
		};


		// Button Validation
		const isButtonClicked = ref(false);

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
			getUserLocation,
			coords,
			parentWidth: 0,
			componentWidth: 300,
			startLocationRef,
			isDisabled,
			placeholderText,
			x,
			y,
			showChat,
			toggleChat,
			isButtonClicked,
			randomGif
		};
	}
});
</script>

