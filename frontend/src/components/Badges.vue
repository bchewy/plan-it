<template>
	<div class="container">
		<div class="row">
			<div class="col-12 text-center mt-5">
				<h1>My Badges</h1>
			</div>
		</div>
		<!-- All Badges -->
		<div class="row justify-content-center mt-5">

			<!-- Display badges here in badges.value -->
			<div class="col-12 col-md-6 col-lg-4" v-for="badge in badges" :key="badge.id">
				<div class="card mb-3">
					<img :src="badge.badgesimg" class="card-img-top" alt="...">
					<div class="card-body">
						<h5 class="card-title">{{ badge.name }}</h5>
						<p class="card-text">{{ badge.description }}</p>
						<p class="card-text">Milestone: {{ badge.milestone }}</p>
					</div>
				</div>


				<!-- <button v-if="this.length == 3" @click="loadMore()" class="btn btn-link">Load More</button> -->
				<!-- <button v-else @click="showLess()" class="btn btn-link">Show Less</button> -->
			</div>
		</div>
	</div>
</template>

<script>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useAuth0 } from "@auth0/auth0-vue";

export default {
	setup() {
		const { user, isAuthenticated } = useAuth0();
		const badges = ref([]);
		const headers = { "x-api-key": "PlanItIsTheBestProjectEverXYZ", };

		const fetchUsersBadges = async () => {
			const url = `${import.meta.env.VITE_API_ENDPOINT}/users/${encodeURIComponent(user.value.email)}/badges`;
			try {
				const response = await axios.get(url, { headers });
				badges.value = response.data;
				// console.log("printing values")
				// console.log(badges.value)

				// For each badge, fetch it's corresponding image and details and put it into the same badges array.
				for (let i = 0; i < badges.value.length; i++) {
					const badge = badges.value[i];
					const badgeDetailsUrl = `${import.meta.env.VITE_API_ENDPOINT}/badges/${badge}`;
					const badgeDetailsResponse = await axios.get(badgeDetailsUrl, { headers });

					// Update the badge in the array
					badges.value[i] = {
						id: badge,
						badgesimg: badgeDetailsResponse.data.image,
						name: badgeDetailsResponse.data.name,
						description: badgeDetailsResponse.data.description,
						milestone: badgeDetailsResponse.data.milestone,
					};
				}

			} catch (error) {
				console.error("Error fetching badges", error);
			}


			// console.log("printing values")
			// console.log(badges.value)


		};

		const fetchData = async () => {
			await fetchUsersBadges();
		};

		onMounted(fetchData);

		return {
			user,
			isAuthenticated,
			badges,
		}

	},
};
</script>

