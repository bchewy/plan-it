<template>
	<div v-if="!isAuthenticated">
		<h3 class="text-center p-5">Please log in to use this feature</h3>
	</div>
	<div v-else >
		<GMapMap :center="center" :zoom="12" map-type-id="terrain" style="width: 100vw; height: 900px">
			<GMapMarker v-if="startLocation.lat && startLocation.lng" :position="startLocation" />
			<GMapMarker v-if="destination.lat && destination.lng" :position="destination" />
			<!-- Polyline here -->
			<!-- <GMapPolyline :path="polylinePath" :editable="true" ref="polyline" /> -->
			<GMapPolyline :path="decodedPolyline" :editable="true" ref="polyline" />


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
		<div class="input-group m-2">
			<span class="input-group-text">Travel Mode</span>
			<select v-model="travelMode" class="form-control">
				<option value="DRIVE">Drive</option>
				<option value="TRANSIT">Public Transport</option>
			</select>
		</div>
		<button @click="fetchRouteDetails">Log Route</button>
		<div v-if="routeDetails">
			<p>Distance: {{ routeDetails.distanceMeters }} meters</p>
			<p>Duration: {{ routeDetails.duration }}</p>
			<div v-if="directionSteps.length > 0">
				<h2>Directions:</h2>
				<ol>
					<li v-for="(step, index) in directionSteps" :key="index">
						{{ step && step.navigationInstruction ? step.navigationInstruction.instructions : 'Step not available' }}
					</li>
				</ol>
			</div>

		</div>
	</div>
</template>