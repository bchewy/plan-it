<script>
import MapItem from '../components/MapItem.vue'
import Navbar from '../components/Navbar.vue';
import { useAuth0 } from '@auth0/auth0-vue';

export default {
	data() {
		const { user, isAuthenticated } = useAuth0();
		return {
			user,
			isAuthenticated
		}
	},
	components: {
		Navbar,
		MapItem
	}
}
</script>
<style scoped></style>

<template>
	<Navbar />
	<div class="container-fluid">
		<MapItem :userme="user" />

	</div>
</template>

