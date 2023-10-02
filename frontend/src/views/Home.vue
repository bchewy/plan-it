<template>
	<header>
		<!-- nav -->
		<NavBar />

	</header>

	Welcome Home.

	<footer>
		<!-- footer -->
	</footer>
</template>
<script>
import NavBar from '../components/Navbar.vue'

export default {
    name: 'Home',
    components: {
        NavBar  // Register the NavBar component
    }
}
</script>