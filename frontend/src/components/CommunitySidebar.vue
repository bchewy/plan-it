<template>
	<nav class="col-2 position-fixed h-100">
		<div class="container-fluid">
			<br>
			<span class="h5 text-muted">Plan-it Community</span>
			<ul class="navbar-nav flex-column mt-5">
				<li class="active nav-item"><router-link class="h3 nav-link" to="/community">For you</router-link></li>
				<hr>
				<li class="nav-item dropdown"><a class="h3 nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown">Groups</a>
					<ul class="dropdown-menu bg-light">
						<li><router-link class="dropdown-item" to="/community/createGroup"><font-awesome-icon icon="fa-solid fa-plus" /> Create group</router-link></li>
						<li><router-link class="dropdown-item" to="/community/yourGroups"><font-awesome-icon icon="fa-solid fa-users" /> Your groups</router-link></li>
					</ul>
				</li>
				<hr>
				<li class="nav-item"><router-link class="h3 nav-link" to="/community/friendCommunity">Friends</router-link></li>
				<hr>
			</ul>
		</div>
	</nav>
</template>