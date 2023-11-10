<template>
	<div class="row justify-content-center" style="background-color: #cbdbb7;">
		<div class="col-12 col-md-6 col-lg-4 mt-3">
			<div class="card text-center">
				<div class="card-body">
					<img class="img-fluid" src="../assets/fail.png">
					<h5 class="card-title">Oops!</h5>
					<p class="card-text">We are unable to connect to the backend. Please try again later.</p>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped></style>

<script>
export default {
	name: 'FailBackend',
}
</script>