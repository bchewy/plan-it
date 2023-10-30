<template>

	<Sidebar v-model:visible="visible" style="background-color: #739072">
		
		<div class="p-sidebar-content px-3 pt-3">
			<span class="h5 text-light">Plan-it Community <font-awesome-icon icon="fa-solid fa-house"></font-awesome-icon></span>
			
			<ul class="navbar-nav flex-column mt-5">
				<li class="active nav-item"><router-link class="h3 nav-link text-light" to="/community"><font-awesome-icon icon="fa-solid fa-user"></font-awesome-icon> For You</router-link></li>
				<hr>
				<li class="nav-item dropdown"><a class="h3 nav-link dropdown-toggle text-light" href="#" data-bs-toggle="dropdown"><font-awesome-icon icon="fa-solid fa-people-group"></font-awesome-icon>  Groups</a>
					<ul class="dropdown-menu bg-light">
						<li><router-link class="dropdown-item" to="/community/createGroup"><font-awesome-icon icon="fa-solid fa-plus" /> Create group</router-link></li>
						<li><router-link class="dropdown-item" to="/community/yourGroups"><font-awesome-icon icon="fa-solid fa-users" /> Your groups</router-link></li>
					</ul>
				</li>
				<hr>
				<li class="nav-item"><router-link class="h3 nav-link text-light" to="/community/friendCommunity"><font-awesome-icon icon="fa-solid fa-user-group"></font-awesome-icon>  Your Friends</router-link></li>
				<hr>
			</ul>
	
		</div>
	</Sidebar>
	
	<button class="btn btn-lg mt-3 ms-3 position-absolute" @click="visible=true; overlayed=!overlayed" ><font-awesome-icon icon="fa-solid fa-bars"></font-awesome-icon></button>

</template>


<script>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import Sidebar from 'primevue/sidebar'
import { defineComponent , ref } from 'vue';

export default defineComponent({
	name:"CommunitySidebar",
	components: { Sidebar, FontAwesomeIcon },
	data(){
		return{
			visible: false,
			overlayed: false
		}
	}
	
})
</script>