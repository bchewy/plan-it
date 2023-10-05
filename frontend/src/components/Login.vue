<template>
	<div>
		<button @click="login">Log in</button>
		Login here!
	</div>
</template>
<script>
import { useAuth0 } from '@auth0/auth0-vue';

export default {
	setup() {
		const { loginWithRedirect } = useAuth0();


		console.log('Setup method is called');  // Log when setup is initialized

		// Log the loginWithRedirect method to see what it actually is
		console.log('loginWithRedirect method:', loginWithRedirect);

		return {
			login: async () => {
				console.log('Login button clicked');
				try {
					await loginWithPopup();
					console.log('User:', user);
					console.log('Authenticated:', isAuthenticated);
				} catch (e) {
					console.error('Failed to login:', e);
				}
			},
			user,
			isAuthenticated,
		};

	}
};
</script>