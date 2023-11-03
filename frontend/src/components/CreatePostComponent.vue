<template>
	<div class="row justify-content-center mt-4">
		<div class="col-10 rounded border bg-white">
			<p class="mt-3 text-muted">&nbsp Share something with the community!</p>
			<Editor class="mb-4" editorStyle="height: 100px" v-model="content"></Editor>
		
						<div class="row mb-3 justify-content-between">
							<span class="col-1"></span>
    <!--share badges button-->
							<button class="btn btn-secondary col-3" type="button" data-bs-target="#badgesOverlay" data-bs-toggle="modal"><font-awesome-icon icon="fa-solid fa-share" /> Share a badge</button>

    <!--modal for share badges-->
	<div class="modal fade" id="badgesOverlay" tabindex="-1" aria-labelledby="badgesOverlayLabel" aria-hidden="true">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="BadgesModalLabel">Badges</h5>
					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<div class="modal-body">
					<ul class="list-unstyled">
						<li v-for="i in userBadges" class="row"><div class="card col-10 mb-2 ms-4" :style="[badge==i.id?'background-color:rgb(175, 209, 191)':'']"><img class="card-img-top w-50 mt-3 mx-auto rounded-circle" :src="i.image"><div class="card-body"><div class="card-title fw-bold text-center">{{ i.name }}</div></div></div><div class="col align-items-center d-flex">  <input type="radio" name="badges" :value="i.id" v-model="badge" > </div></li> 
						

					</ul>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-secondary" data-bs-dismiss="modal" @click="badge=''">Cancel</button>
					<button type="button" class="btn btn-primary" data-bs-dismiss="modal"  >Confirm</button>
				</div>
			</div>
		</div>
	</div>
    <!--tag friend button-->
							<button class="btn btn-secondary col-3" type="button" data-bs-target="#friendsOverlay" data-bs-toggle="modal"><font-awesome-icon icon="fa-solid fa-tag" /> Tag a friend</button>
    <!--tag friend model-->
    <div class="modal fade" id="friendsOverlay" tabindex="-1" aria-labelledby="friendsOverlayLabel" aria-hidden="true">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="TagFriendsModalLabel">Friends</h5>
					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<div class="modal-body">
					<ul class="list-group">
						<li v-for="friend in userFriends" class="list-group-item">  <input type="checkbox" :value="friend"  v-model="taggedfriends" class="me-2">{{friend.handle}} </li>
                        
					</ul>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-secondary" data-bs-dismiss="modal" @click="taggedfriends=[]" >Cancel</button>
					<button type="button" class="btn btn-primary" data-bs-dismiss="modal">Confirm</button> <!--yet to define-->
				</div>
			</div>
		</div>
	</div>
    <!--Create post button-->
    
							<button class="btn btn-success col-3" type="button"  @click="createPost(thisuser.email,thisuser.handle,thisuser.pictureurl)" data-bs-target="#createPostOverlay" data-bs-toggle="modal"><font-awesome-icon icon="fa-solid fa-plus-square" /> Create post!</button>
							<span class="col-1"></span>
	<div class="modal fade" id="createPostOverlay" tabindex="-1" aria-labelledby="createPostOverlayLabel" aria-hidden="true">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="ModalLabel">Post status</h5>
					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<div class="modal-body">
					<p v-if="postStatus">Post created successfully!</p>
					<p v-else>Post creation failed! </p>
				</div>
				<div class="modal-footer">
			
					<button type="button" class="btn btn-primary" data-bs-dismiss="modal">Confirm</button>
				</div>
			</div>
		</div>
	</div>
						</div>
					</div>
				</div>

		
</template>

<script>

import Editor from 'primevue/editor';
import { defineComponent } from 'vue';
import { useAuth0 } from '@auth0/auth0-vue';
import axios from 'axios';


export default defineComponent({
	setup() {
		const { loginWithRedirect, user, isAuthenticated } = useAuth0();


		console.log('Setup method is called');

		return {
			login: async () => {
				console.log('Login button clicked');
				try {
					await loginWithRedirect();
				} catch (e) {
					alert('Failed to login');
					console.error('Failed to login:', e);
				}
			},
			user,
			isAuthenticated,

		};
	},
	name: 'CreatePostComponent',
	components: {
		Editor
	},
	data() {
		return {
			badges: false,
			friends: false,
			content: '',
			badge: '',
			taggedfriends: [],
			likes: [],
			postStatus:false,
			thisuser:'',
			userFriends:[],
			userBadges:[],
			


		}
	},
	
	async created(){
		
			const url = `https://api.bchwy.com/users/iz/${encodeURIComponent(this.user.email)}`;
			const headers = {
				"x-api-key": "PlanItIsTheBestProjectEverXYZ",
			};

			try {
				const response = await axios.get(url, { headers });
				this.thisuser=response.data
				
				
				for(let badgeID of response.data.badges){
					console.log(badgeID)
					const badgeDetailsUrl = `https://api.bchwy.com/badges/${badgeID}`
					try{
						const badgeDetailsResponse = await axios.get(badgeDetailsUrl, { headers });
						this.userBadges.push({
							id:badgeID,
							image: badgeDetailsResponse.data.image,
							name: badgeDetailsResponse.data.name
						})
					}

					catch(error){console.error("error",error)}
				}
				 for (let friend of response.data.friends){
					console.log(friend)
					const friendDetailsURL = `https://api.bchwy.com/users/iz/${encodeURIComponent(friend)}`
				
					try{
						const friendDetailsResponse = await axios.get(friendDetailsURL,{headers});
						this.userFriends.push({handle: "@"+friendDetailsResponse.data.handle})
					}
					catch(error){
						console.error("error",error)
					}
				 }

			

			} catch (error) {
				console.error("Error fetching user", error);
			}
			






		
	},

	

		
		
		parseParams(params) {
			const keys = Object.keys(params)
			let options = ''

			keys.forEach((key) => {
				const isParamTypeObject = typeof params[key] === 'object'
				const isParamTypeArray = isParamTypeObject && params[key].length >= 0

				if (!isParamTypeObject) {
					options += `${key}=${params[key]}&`
				}

				if (isParamTypeObject && isParamTypeArray) {
					params[key].forEach((element) => {
						options += `${key}=${element}&`
					})
				}
			})

			return options ? options.slice(0, -1) : options
		},
		async createPost(useremail,username,userprofile) {
			console.log('content')
			console.log(this.content)
			const url = `https://api.bchwy.com/users/${encodeURIComponent(useremail)}/posts`;
			const headers = {
				"Content-Type": "application/json",
				"x-api-key": "PlanItIsTheBestProjectEverXYZ",
			};
			const contentData = this.content;

			const params = {
				userprofile: userprofile,
				username: username,
				useremail: useremail,
				content: contentData,
				badge: this.badge,
				taggedfriends: this.taggedfriends,
				likes: this.likes
			};

			axios.post(url, { params }, { headers })
				.then(response => {
					console.log('response data here')
					
					console.log(response.data);
					if(response.data.message=='Post created successfully.'){
						this.postStatus=true
					}


				})
				.catch(error => {
					console.error("Error:", error);
				});


			//
			// const response = await axios.post(url, {
			// 	params: {
			// 		content: this.content,
			// 		badge: this.badge,
			// 		taggedfriends: this.taggedfriends
			// 	},
			// 	paramsSerializer: (params) => this.parseParams(params)
			// })


			// 	.catch(error => { console.log(error.message) })
			// console.log(response)
		}


	}
)
</script>