<template>
	<div>
		<!-- Bootstrap progress bar container -->
		<div v-if="userExp !== undefined" class="progress" style="position: relative;">
			<div class="progress-bar bg-success" role="progressbar" :style="{ width: userExp + '%', minWidth: '1em' }" aria-valuenow="userExp" aria-valuemin="0" aria-valuemax="100">
				<!-- Text inside progress bar -->
				<span v-if="userExp >= 20" class="progress-bar-text">{{ formattedExp }}%</span>
			</div>
			<!-- Text outside progress bar for small percentages -->
			<span v-if="userExp < 20" class="text-muted">&nbsp;{{ userExp }}%</span>

		</div>
	</div>
</template>

<script>
export default {
	name: 'ExpProgressBar',
	props: {
		userExp: {
			type: Number,
			required: true
		}
	},
	computed: {
		formattedExp() {
			console.log(this.userExp);
			return this.userExp ? this.userExp.toFixed(0) : '0.00';
		}
	}
};
</script>

<style scoped>
.progress-bar-text {
	color: white;
	/* Ensure the text is visible on the progress bar */
}
</style>
