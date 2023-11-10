<style scoped>
.story-part {
	flex: 0 0 100vw;
	width: 100vw;
	padding: 20px;
	box-sizing: border-box;
	text-align: center;
	position: relative;
	display: flex;
	justify-content: center;
	align-items: center;
	flex-direction: column;
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
	opacity: 0.6;
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
	background-color: rgba(255, 248, 248, 0.92);
	/* White background with 70% opacity */
	border-radius: 10px;
	/* Optional: for rounded corners */
	padding: 20px;
	/* Add padding to avoid text touching the edges */
	margin: 10px;
	/* Add some margin if needed */
	max-width: 50%;
	/* Control the max width of the transparent background */
	box-sizing: border-box;
}

.text-background ul {
	padding: 0;
	/* Reset default padding */
	margin: 0;
	/* Reset default margin */
	list-style-type: none;
	/* Remove default list item bullets */
	/* Add more styling as needed */
}

.text-background ul li {
	/* Your styles for list items here */
	text-align: center;
	/* or 'center' as per your design */
}

.video-container {
	position: relative;
	width: 100%;
	padding-bottom: 56.25%;
	/* Aspect Ratio (height / width * 100%) */
}

.video-container video {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
}

@media (max-width: 768px) {

	/* Adjust the breakpoint as needed */
	.text-background {
		max-height: 100vh;
		overflow: auto;
		/* Add a scrollbar if the content exceeds the max height */
	}
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
				<div class="">
					<img class="img-fluid w-25" src="https://bchewy-images.s3.ap-southeast-1.amazonaws.com/plan-it/bchewy+conscious+travel+mascot.png" alt="PlanIt Logo">
					<div class="w-25 text-background justify-content-center mx-auto pb-5">
						<p class="text-center">Hello! I'm Planny:<br>Scroll to...</p>
						<h2 class="text-center"><span class="text-success element"></span></h2>
					</div>

					<!-- <h2>Welcome to PlanIt!</h2>
					<p>PlanIt helps you make sustainable transportation choices while exploring your city. Our app allows you to log and compare routes across different modes like walking, biking, driving, and public transit.</p> -->
					<!-- <img class="img-fluid" src="../assets/product_demo_real.gif" alt="Product Demo"> -->
				</div>
			</div>

			<!-- Section 2: Log Your Routes -->
			<div class="col-12 story-part">
				<div class="text-background">
					<h3>Log Your Routes</h3>
					<p class="text-muted">Easily log routes you take around the city by entering your starting point and destination. Select the route you took to add it to your log.</p>
					<div class="video-container">
						<video controls autoplay muted loop>
							<source src="https://bchewy-videos.s3.ap-southeast-1.amazonaws.com/routes.mov" type="video/mp4">
							Your browser does not support the video tag.
						</video>
					</div>
				</div>
			</div>

			<!-- Section 3: Compare Carbon Impact -->
			<div class="col-12 story-part">
				<div class="text-background">
					<h3>See Your Profile</h3>
					<p class="text-muted">View all your logged routes, earned badges, points, and current level on your profile. Compare stats with friends on the leaderboard.</p>
					<div class="video-container">
						<video controls autoplay muted loop>
							<source src="https://bchewy-videos.s3.ap-southeast-1.amazonaws.com/profile.mov" type="video/mp4">
							Your browser does not support the video tag.
						</video>
					</div>
				</div>
			</div>

			<!-- Section 4: Earn Points and Level Up -->
			<div class="col-12 story-part">
				<div class="text-background">

					<h3>Earn Points and Level Up</h3>
					<p class="text-muted">Gain XP points and advance levels for choosing low-carbon active transport like walking and biking. Unlock badges and rewards as you level up!</p>
					<div class="video-container">
						<video controls autoplay muted loop>
							<source src="https://bchewy-videos.s3.ap-southeast-1.amazonaws.com/game.mov" type="video/mp4">
							Your browser does not support the video tag.
						</video>
					</div>
				</div>
			</div>

			<!-- Section 6: Connect with Community -->
			<div class="col-12 story-part">
				<div class="text-background">

					<h3>Connect with Community</h3>
					<p class="text-muted">Join the conversation around sustainable transportation. Share route ideas, transit tips, and stories with other members.</p>
					<div class="video-container">
						<video controls autoplay muted loop>
							<source src="https://bchewy-videos.s3.ap-southeast-1.amazonaws.com/community.mov" type="video/mp4">
							Your browser does not support the video tag.
						</video>
					</div>
				</div>
			</div>

			<!-- Section 7: See Your Profile -->
			<div class="col-12 story-part">
				<div class="text-background">
					<h3>Built with <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(241, 18, 18, 1);transform: ;msFilter:;">
							<path d="M20.205 4.791a5.938 5.938 0 0 0-4.209-1.754A5.906 5.906 0 0 0 12 4.595a5.904 5.904 0 0 0-3.996-1.558 5.942 5.942 0 0 0-4.213 1.758c-2.353 2.363-2.352 6.059.002 8.412L12 21.414l8.207-8.207c2.354-2.353 2.355-6.049-.002-8.416z"></path>
						</svg></h3>
					<p>Our website fully runs on <a class="link-success" href="https://sustainability.aboutamazon.com/products-services/the-cloud">sustainable energy</a> thanks to AWS.</p>

					<div class="d-flex flex-wrap justify-content-between">
						<div class="mb-3">
							<img style="height: 35px;" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Vue.js_Logo_2.svg/2367px-Vue.js_Logo_2.svg.png" alt="Tool 1">
							<p>VueJS</p>
						</div>
						<div class="mb-3">
							<img style="height: 35px;" src="https://www.svgrepo.com/show/331488/mongodb.svg" alt="Tool 1">
							<p>MongoDB</p>
						</div>
						<div class="mb-3">
							<img style="height: 35px;" src="https://static-00.iconduck.com/assets.00/auth0-icon-458x512-8spyi0ve.png" alt="Tool 1">
							<p>Auth0</p>
						</div>
						<div class="mb-3">
							<img style="height: 35px;" src="../assets/ec2.png" alt="Tool 1">
							<p>EC2</p>
						</div>
						<div class="mb-3">
							<img style="height: 35px;" src="../assets/s3.png" alt="Tool 1">
							<p>S3</p>
						</div>
						<div class="mb-3">
							<img style="height: 35px;" src="../assets/cf.png" alt="Tool 1">
							<p>Cloudfront</p>
						</div>
						<div class="mb-3">
							<img style="height: 35px;" src="https://static-00.iconduck.com/assets.00/flask-icon-1594x2048-84mjydzf.png" alt="Tool 1">
							<p>Flask</p>
						</div>

					</div>


					<h3>Meet Our Team</h3>
					<ul class="d-flex flex-column">
						<li class="mb-1">
							<img style="height: 35px;" src="https://bchewy.s3.ap-southeast-1.amazonaws.com/code+block%60%60%60%3A+'Brian+Chew+LinkedIn.jpeg">&nbsp;
							<a class="link-success" href="https://github.com/bchewy">@bchewy</a>
						</li>
						<li class="mb-1">
							<img style="height: 35px;" src="../assets/ryan.jpg" alt="">&nbsp;

							<a class="link-success" href="https://github.com/ryan99324">@ryan99324</a>
						</li>
						<li class="mb-1">
							<img style="height: 35px;" src="..assets/melody.jpg" alt="">&nbsp;

							<a class="link-success" href="https://github.com/melodywong23">@melodywong23</a>
						</li>
						<li class="mb-1">
							<img style="height: 35px;" src="https://cdn.vectorstock.com/i/preview-1x/08/19/gray-photo-placeholder-icon-design-ui-vector-35850819.jpg">&nbsp;

							<a class="link-success" href="https://github.com/saphalex">@saphalex</a>
						</li>
					</ul>
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
import Typed from 'typed.js';

export default {
	data() {
		return {
			isTypedInitialized: false

		};
	},
	components: {
		Navbar,
	},
	mounted() {
		const element = document.querySelector('.element');
		const cursors = document.querySelectorAll('.typed-cursor');
		cursors.forEach(cursor => cursor.remove());  // Remove existing cursors

		if (!this.isTypedInitialized) {
			new Typed(element, {
				strings: ["Explore PlanIt!", "Get Started!", "Meet the team!"],
				typeSpeed: 30,
				backSpeed: 50,
				loop: true
			});
			this.isTypedInitialized = true;
		}
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


