<template>

<div class="row justify-content-center my-4 ">
					<!--header-->
					<div class="col-10 rounded border bg-white position-relative">
                        
<div class="row">
    <div class="col-1 d-flex align-items-center">
                        <img :src="profileImage" class="rounded-circle mt-2" style="width:40px;">  
                        
                        
                        <span class="fw-bold ms-2"> {{ username }} </span>
                      </div>  
</div>      
                <br>
                       <span class="fs-5"><slot></slot></span> <br><br>
                       <span class="fs-5" v-for="friend in taggedFriends"> @{{ friend }}  </span>
                       <div class="border-rounded border mt-3 " style="background-color: rgb(218, 239, 216);">
                        
                      <div class="row">
                        <div class="col-3 justify-content-end d-flex my-3 ms-3">
                        <br> <img :src="badges[badge].icon" style="width:100%" class="rounded-circle">
                        </div>
                        <div class="col ms-2 mt-2 align-items-center d-flex">
                        <p class="fs-5"><span class="fw-bold fs-3">{{ badges[badge].name }} </span><br><br> {{ badges[badge].description }} <br><br> <strong>Milestone:</strong> {{ badges[badge].milestone }}</p></div>
                    </div>
                    </div>
                        
                        
                        <br>
                    <span class="text-muted">{{ timePosted }}</span>  
                    <hr>
                        
                        <div class="text-muted fw-bold mb-2">{{ likeCounter }} likes</div>
    


						<heart_btn></heart_btn>
						<br><br>
</div>
					</div>
				
</template>


<script>
import { defineComponent } from 'vue';
import heart_btn from './like_button.vue'

export default defineComponent({
    name: 'PostComponent',
    components: {
        heart_btn
    },
    data(){
        return{
        }},
    props:{
        username: String,
        badge: String, 
        taggedFriends: Array, 
        profileImage: String,
    timePosted: String,
liked: Array,
comments:Array},

computed:{
    likeCounter(){
        return this.liked.length
    }
}
    

})




</script>