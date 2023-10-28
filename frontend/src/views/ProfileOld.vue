<template>
	<Navbar />
	<div class="container">
		<div class="row">
			<div class="col-12 text-center mt-5">
				<h1>User Profile</h1>
			</div>
		</div>
		<!-- User Profile and Routes -->
		<div class="row justify-content-center mt-5">
			<!-- User Profile Column -->
			<div class="col-lg-3 col-md-6 col-sm-12 mb-4">
				<div class="card">
					<div class="card-header">
						<h3>{{ user.name }}</h3>
					</div>
					<div class="card-body">
						<div class="text-center mb-3">
							<img :src="user.picture" class="rounded-circle" alt="User profile picture" width="128" height="128" />
						</div>
						<div class="mb-3"><b>Given Name:</b> {{ user.given_name }}</div>
						<div class="mb-3"><b>Family Name:</b> {{ user.family_name }}</div>
						<div class="mb-3"><b>Nickname:</b> {{ user.nickname }}</div>
						<div class="mb-3"><b>Email:</b> {{ user.email }}</div>
						<div class="mb-3"><b>Locale:</b> {{ user.locale }}</div>
						<div class="mb-3"><b>Last Updated:</b> {{ user.updated_at }}</div>
					</div>
				</div>
				<div class="card mt-4 mb-4">
					<div class="card-header">
						<h3 class="mb-0">Friends</h3>
					</div>
					<div class="card-body">
						<div v-for="friend in friends" :key="friend" class="mb-4">
							<h5>{{ friend }}</h5>
						</div>
					</div>
				</div>
			</div>
			<!-- Routes Column -->
			<div class="col-lg-9 col-md-6 col-sm-12 mb-4">
				<div class="card">
					<div class="card-header">
						<h3>Routes</h3>
					</div>
					<div class="card-body">
						<!-- Shows if empty -->
						<div v-if="routes && routes.length == 0">
							<p class="text-center text-muted">
								Your route list is empty. You need to commit more.
							</p>
						</div>
						<div v-for="route in paginatedRoutes" :key="route.route_id" class="mb-4">
							<h5>{{ route.start_point_name }} to {{ route.end_point_name }}</h5>
							<p><b>Mode of Transport:</b> {{ route.transport_mode }}</p>
							<p><b>Carbon Emission:</b> {{ route.carbon_emission }}</p>
							<p><b>Timestamp:</b> {{ new Date(route.timestamp).toLocaleString() }}</p>
						</div>
						<!-- Pagination controls -->
						<nav aria-label="Pagination-for-routes">
							<ul class="pagination justify-content-center">
								<li class="page-item" :class="{ disabled: currentPage === 1 }">
									<a class="page-link" href="#" @click.prevent="currentPage--">Previous</a>
								</li>
								<!-- Page count -->
								<li class="page-item disabled">
									<span class="page-link">{{ currentPage }} / {{ totalPages }}</span>
								</li>
								<li class="page-item" :class="{ disabled: currentPage >= totalPages }">
									<a class="page-link" href="#" @click.prevent="currentPage++">Next</a>
								</li>
							</ul>
						</nav>
					</div>
				</div>
			</div>
		</div>
		<!-- Friends -->
		<!-- <div class="row justify-content-center mt-5"> -->

		<div class="card mt-4 mb-4">
			<div class="card-header">
				<h3 class="mb-0">Friend Requests</h3>
			</div>
			<div class="card-body">
				<AddFriend :user="user" />
				<h4>Received Requests</h4>
				<FriendRequest v-for="request in receivedRequests" :key="request" :friend="request" :user="user" :receivedRequests="receivedRequests" type="received" />

				<h4>Sent Requests</h4>
				<FriendRequest v-for="request in sentRequests" :key="request" :friend="request" :user="user" :sentRequests="sentRequests" type="sent" />
			</div>
		</div>
		<!-- </div> -->

		<div class="card mt-4 mb-4">
			<div class="card-header">
				<h3 class="mb-0">Game Stats</h3>
			</div>
			<Badges></Badges>
		</div>


	</div>
</template>