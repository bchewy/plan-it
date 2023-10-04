<template>
	<div>
		<GMapMap :center="center" :zoom="7" map-type-id="terrain" style="width: 100vw; height: 900px">
			<!-- <GMapMarker v-if="startLocation.lat && startLocation.lng" :position="startLocation" />
			<GMapMarker v-if="destination.lat && destination.lng" :position="destination" /> -->
			<GMapMarker v-if="startLocation.lat && startLocation.lng" :position="startLocation" />
			<GMapMarker v-if="destination.lat && destination.lng" :position="destination" />
			<!-- <GMapMarker :position="{ lat: 1.3331, lng: 103.7428 }" /> -->

		</GMapMap>
		<div class="input-group m-2">
			<span class="input-group-text" id="autocomplete-label">Start Location</span>
			<GMapAutocomplete v-model="startLocation.value" placeholder="Starting point"
				:componentRestrictions="{ country: 'SG' }" @place_changed="setPlace" class="form-control" />
		</div>
		<div class="input-group m-2">
			<span class="input-group-text" id="autocomplete-label">End Location</span>
			<GMapAutocomplete v-model="destination.value" placeholder="Destination"
				:componentRestrictions="{ country: 'SG' }" @place_changed="setPlace" class="form-control" />
		</div>
	</div>
</template>

<script>
import { reactive, ref, defineComponent } from "vue";
export default defineComponent({
	setup() {
		const center = { lat: 1.3331, lng: 103.7428 };
		// const state = reactive({
		// 	startLocation: {
		// 		lat: null,
		// 		lng: null
		// 	},
		// 	destination: {
		// 		lat: null,
		// 		lng: null
		// 	}
		// })
		const startLocation = ref({
			lat: 0,
			lng: 0
		});

		const destination = ref({
			lat: 0,
			lng: 0
		});
		// console.log('setting up');

		const setPlace = (place) => {
			const lat = Number(place.geometry.location.lat());
			const lng = Number(place.geometry.location.lng());
			console.log('Place changed');

			if (!startLocation.value.lat && !startLocation.value.lng) {
				startLocation.value = { lat, lng };
			} else {
				destination.value = { lat, lng };
			}
		};

		return {
			center,
			startLocation,
			destination,
			setPlace
		};
	},
	methods: {
		// setPlace(place) {
		// 	const lat = Number(place.geometry.location.lat());
		// 	const lng = Number(place.geometry.location.lng());
		// 	// console.log(lat, lng);

		// 	console.log('Placed changed');
		// 	if (!startLocation.value.lat && !startLocation.value.lng) {
		// 		startLocation.value = { lat, lng };
		// 	} else {
		// 		destination.value = { lat, lng };
		// 	}

		// 	// Reactive
		// 	// 	if (!state.startLocation.lat && !state.startLocation.lng) {
		// 	// 		state.startLocation = { lat, lng }
		// 	// 	} else {
		// 	// 		state.destination = { lat, lng }
		// 	// 	}
		// }

	}
});
</script>
