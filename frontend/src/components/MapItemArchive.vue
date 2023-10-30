<template>
	<div class="row">
		<div v-if="errorMessage" class="alert alert-danger" role="alert">
			{{ errorMessage }}
		</div>
		<div class="col-lg-8 col-md-12 p-0">
			<GMapMap class="w-100 vh-100" :center="center" :zoom="zoom" map-type-id="terrain">
				<GMapMarker v-if="startLocation.lat && startLocation.lng" :position="startLocation" />
				<GMapMarker v-if="destination.lat && destination.lng" :position="destination" />
				<GMapPolyline :path="decodedPolyline" :editable="false" ref="polyline" :options="{ strokeColor: '#00FF00' }" />
			</GMapMap>
		</div>
		<div class="col-lg-4 col-md-12 p-4 bg-supergreen">

			<div class="mb-4">
				<div class="input-group mb-3">
					<span class="input-group-text font-weight-bold" id="autocomplete-label">From</span>
					<GMapAutocomplete ref="autocomplete" v-model="startLocation.value" placeholder="Origin" :componentRestrictions="{ country: 'SG' }" @place_changed="setStartLocation" class="form-control" />
					<!-- <button class="btn btn-outline-secondary" type="button" @click="getUserLocation">Here</button> -->
				</div>
				<div class="input-group mb-3">
					<span class="input-group-text font-weight-bold" id="autocomplete-label">To</span>
					<GMapAutocomplete v-model="destination.value" placeholder="Destination" :componentRestrictions="{ country: 'SG' }" @place_changed="setDestination" class="form-control" />
				</div>
				<div class="input-group mb-3">
					<span class="input-group-text font-weight-bold">Transporation</span>
					<select v-model="travelMode" class="form-control">
						<option value="DRIVE">Drive</option>
						<option value="TWO_WHEELER">Motorbike</option>
						<option value="TRANSIT">Public Transport</option>
						<option value="BICYCLE">Bicycle</option>
						<option value="WALK">Walk</option>
					</select>
				</div>
				<div class="input-group mb-3">
					<span class="input-group-text font-weight-bold">Depature Time</span>
					<input type="time" v-model="departureTime" class="form-control">
					<!-- <button class="btn btn-green" type="button" @click="addMinutes(5)">+5m</button> -->
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

			<div class="mb-4">
				<button class="btn btn-green w-100" @click="fetchRouteDetails" data-bs-toggle="modal" data-bs-target="#progressModal">Log Route</button>
			</div>

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

		</div>
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