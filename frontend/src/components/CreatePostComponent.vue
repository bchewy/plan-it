<template>
   
   <div class="row justify-content-center">
					<div class="col-11 rounded border bg-white">
                        <p class="mt-3 text-muted">&nbsp Share something with the community!</p>
						<Editor class="mb-4" editorStyle="height: 100px"></Editor>


						<div class="row mb-3 justify-content-between">
							<span class="col-1"></span>
    <!--share badges button-->
							<button class="btn btn-secondary col-3" type="button" @click="badges = !badges" data-bs-target="#badgesOverlay" data-bs-toggle="modal"><font-awesome-icon icon="fa-solid fa-share" /> Share a badge</button>

    <!--modal for share badges-->
	<div v-if="badges" class="modal fade" id="badgesOverlay" tabindex="-1" aria-labelledby="badgesOverlayLabel" aria-hidden="true">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="BadgesModalLabel">Badges</h5>
					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<div class="modal-body">
					<ul>
						<li> Badge1 </li> <input type="radio">
					</ul>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
					<button type="button" class="btn btn-primary" @click="confirmShareBadge()">Confirm</button> <!--yet to define-->
				</div>
			</div>
		</div>
	</div>
    <!--tag friend button-->
							<button class="btn btn-secondary col-3" type="button" @click="friends=!friends" data-bs-target="#friendsOverlay" data-bs-toggle="modal"><font-awesome-icon icon="fa-solid fa-tag" /> Tag a friend</button>
    <!--tag friend model-->
    <div v-if="friends" class="modal fade" id="friendsOverlay" tabindex="-1" aria-labelledby="friendsOverlayLabel" aria-hidden="true">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="TagFriendsModalLabel">Friends</h5>
					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<div class="modal-body">
					<ul>
						<li> Friend1 </li> <input type="checkbox">
                        <li> Friend2</li> <input type="checkbox">
					</ul>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
					<button type="button" class="btn btn-primary" @click="confirmTagFriends()">Confirm</button> <!--yet to define-->
				</div>
			</div>
		</div>
	</div>
    <!--Create post button-->
    
							<button class="btn btn-success col-3" type="button"><font-awesome-icon icon="fa-solid fa-plus-square" @click="createPost()" /> Create post!</button>
							<span class="col-1"></span>
						</div>
					</div>
		</div>


</template>

<script>
import Editor from 'primevue/editor';
import { defineComponent } from 'vue';

export default defineComponent({
    name:'CreatePostComponent',
    components:{
        Editor
    },
    data(){
        return{
        badges:false,
        friends:false
        }
    }

})
</script>