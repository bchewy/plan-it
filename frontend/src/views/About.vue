<style scoped>
.story-part {
	flex: 0 0 100vw;
	width: 100vw;
	padding: 20px;
	box-sizing: border-box;
	text-align: center;
	position: relative;
	display: flex;
	/* Add this */
	justify-content: center;
	/* Add this */
	align-items: center;
	/* Add this */
	flex-direction: column;
	/* Add this */
}

.row {
	position: relative;
	display: flex;
	flex-direction: row;
	height: 100vh;
	overflow-x: auto;
	overflow-y: hidden;
}

.row::-webkit-scrollbar {
	display: none;
}

.row::before {
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	width: 600vw;
	/* Adjust this value to match the total width of your content */
	height: 100%;
	background-image: url('../assets/aboutfinal.png');
	background-size: auto 100%;
	background-repeat: no-repeat;
	z-index: -1;
}

.full-height {
	display: flex;
	flex-direction: column;
	height: 100vh;
	overflow: auto;
}

.text-background {
	background-color: rgba(255, 255, 255, 0.7);
	/* White background with 70% opacity */
	border-radius: 10px;
	/* Optional: for rounded corners */
	padding: 20px;
	/* Add padding to avoid text touching the edges */
	margin: 10px;
	/* Add some margin if needed */
	max-width: 80%;
	/* Control the max width of the transparent background */
	box-sizing: border-box;
}

/* .section-1 {
	background-image: url('https://bchewy-images.s3.ap-southeast-1.amazonaws.com/plan-it/aboutf.png');
	/* background-size: cover;
	background-position: center; 
}*/
</style>

<template>
	<div class="full-height">
		<Navbar />
		<div class="row g-0 row overflow-x-auto flex-nowrap vh-100">

			<!-- Section 1: Welcome -->
			<div class="col-12 story-part ">
				<div class="text-background">
					<h2>Welcome to PlanIt!</h2>
					<p>PlanIt helps you make sustainable transportation choices while exploring your city. Our app allows you to log and compare routes across different modes like walking, biking, driving, and public transit.</p>
					<img class="img-fluid" src="../assets/product_demo_real.gif" alt="Product Demo">
				</div>
			</div>

			<!-- Section 2: Log Your Routes -->
			<div class="col-12 story-part">
				<div class="text-background">
					<h3>Log Your Routes</h3>
					<p>Easily log routes you take around the city by entering your starting point and destination. We'll show route options with distance and emissions for modes like walking, biking, driving, or public transit. Select the route you took to add it to your log.</p>
				</div>
			</div>

			<!-- Section 3: Compare Carbon Impact -->
			<div class="col-12 story-part">
				<div class="text-background">
					<h3>See Your Profile</h3>
					<p>View all your logged routes, earned badges, points, and current level on your profile. Compare stats with friends on the leaderboard.</p>
				</div>
			</div>

			<!-- Section 4: Earn Points and Level Up -->
			<div class="col-12 story-part">
				<div class="text-background">

					<h3>Earn Points and Level Up</h3>
					<p>Gain XP points and advance levels for choosing low-carbon active transport like walking and biking. Unlock badges and rewards as you level up!</p>
				</div>
			</div>

			<!-- Section 6: Connect with Community -->
			<div class="col-12 story-part">
				<div class="text-background">

					<h3>Connect with Community</h3>
					<p>Join the conversation around sustainable transportation. Share route ideas, transit tips, and stories with other members.</p>
				</div>
			</div>

			<!-- Section 7: See Your Profile -->
			<div class="col-12 story-part">
				<div class="text-background">
					<h3>Built with <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(241, 18, 18, 1);transform: ;msFilter:;">
							<path d="M20.205 4.791a5.938 5.938 0 0 0-4.209-1.754A5.906 5.906 0 0 0 12 4.595a5.904 5.904 0 0 0-3.996-1.558 5.942 5.942 0 0 0-4.213 1.758c-2.353 2.363-2.352 6.059.002 8.412L12 21.414l8.207-8.207c2.354-2.353 2.355-6.049-.002-8.416z"></path>
						</svg></h3>
					<p>Our platform is fully built to run on sustainable energy on AWS</p>

					<img style="height: 50px;" src="https://www.svgrepo.com/show/331488/mongodb.svg" alt="Tool 1">
					<p>MongoDB</p>

					<img style="height: 50px;" src="https://static-00.iconduck.com/assets.00/auth0-icon-458x512-8spyi0ve.png" alt="Tool 1">
					<p>Auth0</p>

					<img style="height: 50px;" src="https://static-00.iconduck.com/assets.00/aws-ec2-icon-423x512-iaajemnx.png" alt="Tool 1">
					<p>AWS EC2</p>

					<img style="height: 50px;" src="https://www.outsystems.com/blog/-/media/images/blog/posts/aws-service-list/amazon-s3-bp-aws-services-list.png?updated=20210415092723" alt="Tool 1">
					<p>AWS S3</p>

					<img style="height: 50px;" src="https://pbs.twimg.com/profile_images/1189603938137280512/Xy_sEdeN_400x400.jpg" alt="Tool 1">
					<p>AWS Cloudfront</p>


					<h3>Contributors</h3>
					<p>@bchewy - frontend/backend</p>
					<p>@ryan - frontend/backend</p>
					<p>@melody - frontend</p>
					<p>@saph - frontend</p>
				</div>
			</div>

			<!-- Journey Line -->
			<!-- <div class="journey-line"></div> -->

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


