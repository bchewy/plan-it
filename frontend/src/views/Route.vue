<script>
import MapItem from '../components/MapItem.vue'
import Navbar from '../components/Navbar.vue';
import { useAuth0 } from '@auth0/auth0-vue';

export default{
	data(){
		const { user, isAuthenticated } = useAuth0();
		console.log('Route.vue: is authenticated?', isAuthenticated)
		console.log('Route.vue user', user)
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


<template>
	<Navbar />
	<MapItem :userme="user" />
</template>

