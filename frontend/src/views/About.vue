<style scoped>
.story-part {
	flex: 0 0 100vw;
	/* This prevents the sections from growing or shrinking */
	width: 100vw;
	/* This makes each section the full width of the viewport */
	/* height: 100vh; */
	/* Adjust the height as needed */
	padding: 20px;
	box-sizing: border-box;
	/* This ensures padding is included in the width */
	text-align: center;
	position: relative;
	/* For positioning the journey line or other absolute elements */
}

.row {
	display: flex;
	flex-direction: row;
	height: 100vh;
	overflow-x: auto;
	overflow-y: hidden;
}

.full-height {
	display: flex;
	flex-direction: column;
	height: 100vh;
	overflow: auto;
}
</style>

<template>
	<div class="full-height">
		<Navbar />
		<div class="row g-0 row overflow-x-auto flex-nowrap vh-100">

			<!-- Section 1: Welcome -->
			<div class="col-12 story-part">
				<h2>Welcome to PlanIt!</h2>
				<p>PlanIt helps you make sustainable transportation choices while exploring your city. Our app allows you to log and compare routes across different modes like walking, biking, driving, and public transit.</p>
			</div>

			<!-- Section 2: Log Your Routes -->
			<div class="col-12 story-part">
				<h3>Log Your Routes</h3>
				<p>Easily log routes you take around the city by entering your starting point and destination. We'll show route options with distance and emissions for modes like walking, biking, driving, or public transit. Select the route you took to add it to your log.</p>
			</div>

			<!-- Section 3: Compare Carbon Impact -->
			<div class="col-12 story-part">
				<h3>Compare Carbon Impact</h3>
				<p>See at a glance how much CO2 each route option produces. Opting for walking, biking or public transit over driving can significantly reduce your carbon footprint from transportation.</p>
			</div>

			<!-- Section 4: Earn Points and Level Up -->
			<div class="col-12 story-part">
				<h3>Earn Points and Level Up</h3>
				<p>Gain XP points and advance levels for choosing low-carbon active transport like walking and biking. Unlock badges and rewards as you level up!</p>
			</div>

			<!-- Section 5: Track Your Impact -->
			<div class="col-12 story-part">
				<h3>Track Your Impact</h3>
				<p>Monitor your transport carbon footprint over time. See how smaller sustainable choices add up to make a real difference!</p>
			</div>

			<!-- Section 6: Connect with Community -->
			<div class="col-12 story-part">
				<h3>Connect with Community</h3>
				<p>Join the conversation around sustainable transportation. Share route ideas, transit tips, and stories with other members.</p>
			</div>

			<!-- Section 7: See Your Profile -->
			<div class="col-12 story-part">
				<h3>See Your Profile</h3>
				<p>View all your logged routes, earned badges, points, and current level on your profile. Compare stats with friends on the leaderboard.</p>
			</div>

			<!-- Journey Line -->
			<div class="journey-line"></div>

		</div>
	</div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import { onMounted, onBeforeUnmount } from 'vue';

export default {
	components: {
		Navbar,
	},
	setup() {
		let horizontalScroll = (e) => {
			document.querySelector('.row').scrollLeft += e.deltaY;
			e.preventDefault();
		};

		onMounted(() => {
			document.querySelector('.row').addEventListener('wheel', horizontalScroll);
		});

		onBeforeUnmount(() => {
			document.querySelector('.row').removeEventListener('wheel', horizontalScroll);
		});
	},
};
</script>


