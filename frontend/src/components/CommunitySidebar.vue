
<template>
	<Sidebar v-model:visible="visible" style="background-color: #739072">
		
		<div class="p-sidebar-content px-3 pt-3">
			<span class="h5 beige-colour">Plan-it Community <font-awesome-icon icon="fa-solid fa-house"></font-awesome-icon></span>
			
			<ul class="navbar-nav flex-column mt-5">
				<li class="active nav-item"><router-link class="h3 nav-link beige-colour" to="/community"><font-awesome-icon icon="fa-solid fa-user"></font-awesome-icon> For You</router-link></li>
				<hr>
				<li class="nav-item dropdown"><a class="h3 nav-link dropdown-toggle beige-colour" href="#" data-bs-toggle="dropdown"><font-awesome-icon icon="fa-solid fa-people-group"></font-awesome-icon>  Groups</a>
					<ul class="dropdown-menu beige-colour" style="background-color: #739072">
						<li><router-link class="dropdown-item beige-colour" to="/community/createGroup" style="background-color: #739072"><font-awesome-icon icon="fa-solid fa-plus" /> Create group</router-link></li>
						<li><router-link class="dropdown-item beige-colour" to="/community/yourGroups" style="background-color: #739072"><font-awesome-icon icon="fa-solid fa-users" /> Your groups</router-link></li>
					</ul>
				</li>
				<hr>
				<li class="nav-item"><router-link class="h3 nav-link beige-colour" to="/community/friendCommunity"><font-awesome-icon icon="fa-solid fa-user-group"></font-awesome-icon>  Your Friends</router-link></li>
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

<style scoped>

.beige-colour {
  color: rgba(236, 227, 206, 1);
}

.p-sidebar-content {
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
  width: 250px;
  background-color: #739072;
  overflow-y: auto;
  z-index: 1;
}

.p-sidebar-content li {
  cursor: pointer;
  padding: 10px;

  /* Display the text in the sidebar items */
  display: flex;
  align-items: center;
}

.p-sidebar-content i {
  font-size: 24px;
  color: #ffffff;
}

.p-sidebar-content li span {
  /* Hide the text in the sidebar items by default */
  display: none;
}

.p-sidebar-content li:hover {
  background-color: #537052;
}

.p-sidebar-content li:hover span {
  /* Show the text in the sidebar items when they are hovered over */
  display: block;
}

.p-sidebar-content .dropdown-menu {
  position: absolute;
  left: 50px;
  top: 0;
  width: 200px;
  background-color: #739072;
  border: 1px solid #ffffff;
  z-index: 2;
}

.p-sidebar-content .dropdown-menu li {
  cursor: pointer;
  padding: 10px;
}

.p-sidebar-content .dropdown-menu li:hover {
  background-color: #537052;
}

.p-sidebar-content .dropdown-menu i {
  font-size: 16px;
  color: #ffffff;
}


</style>

