<template>
	<button class="btn btn-secondary col-3" type="button" @click="badges = !badges" data-bs-target="#badgesOverlay" data-bs-toggle="modal"><font-awesome-icon icon="fa-solid fa-share" /> Share a badge</button>

	<div v-if="badges" class="modal fade" id="badgesOverlay" tabindex="-1" aria-labelledby="badgesOverlayLabel" aria-hidden="true">
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
					<button type="button" class="btn btn-secondary" data-bs-dismiss="modal" @click="badges = !badges">Close</button>
					<button type="button" class="btn btn-primary" @click="confirmShareBadge">Confirm</button> <!--yet to define-->
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import { ref, defineComponent, computed, reactive } from "vue";
import axios from "axios";
import { useAuth0 } from '@auth0/auth0-vue';

export default defineComponent({

	data() {
		return {
			badges: false
		}
	}
}

)


</script>