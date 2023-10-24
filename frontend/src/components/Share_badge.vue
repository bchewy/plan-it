<template>

<div v-if="badges" class="d-flex justify-content-center align-items-center">
					<div class="modal fade" id="badgesOverlay" tabindex="-1" aria-labelledby="badgesOverlayLabel" aria-hidden="true">
						<div class="modal-dialog">
							<div class="modal-content">
								<div class="modal-header">
									<h5 class="modal-title" id="makePostModalLabel">Badges</h5>
									<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
								</div>
								<div class="modal-body">
									<ul>
                                        <li> Badge1 </li> <input type="radio">
                                    </ul>
								</div>
								<div class="modal-footer">
									<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
									<button type="button" class="btn btn-primary" @click="confirmShareBadge">Confirm</button> <!--yet to define-->
								</div>
							</div>
						</div>
					</div>
					<button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#badgesOverlay">Make a Post</button>
				</div>
</template>

<script>
import { ref, defineComponent, computed, reactive } from "vue";
import axios from "axios";
import { useAuth0 } from '@auth0/auth0-vue';

export default defineComponent({
props:['userme'],
setup(props){
    const { user, isAuthenticated } = useAuth0();
    const badges=false;
    return{
        badges,
        isAuthenticated,
        user

    }
}

})


</script>