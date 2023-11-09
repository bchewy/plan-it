// router.js

import { createRouter, createWebHistory } from 'vue-router'
import { authGuard } from "@auth0/auth0-vue";


const router = createRouter({
	history: createWebHistory(),
	routes: [
		{
			path: '/',
			component: () => import('./views/Home.vue')
		},
		{
			path: '/about',
			component: () => import('./views/About.vue'),
		},
		{
			path: '/route',
			component: () => import('./views/Route.vue'),
			beforeEnter: authGuard
		},
		{
			path: '/verify',
			component: () => import('./views/Verify.vue'),
			beforeEnter: authGuard

		},
		{
			path: '/profile',
			component: () => import('./views/Profile.vue'),
			beforeEnter: authGuard

		},
		{
			path: '/leaderboard',
			component: () => import('./views/Leaderboards.vue'),
			beforeEnter: authGuard

		},
		{
			path: '/profile/public/:userEmail',
			component: () => import('./views/ProfilePublic.vue')
		},
		{
			path: '/community',
			component: () => import('./views/Community.vue'),
			beforeEnter: authGuard

		},
		{
			path: '/settings',
			component: () => import('./views/Settings.vue'),
			beforeEnter: authGuard

		},
		{
			path: '/admin',
			component: () => import('./views/Admin.vue'),
			beforeEnter: authGuard

		},
		// {
		// 	path: '/badges',
		// 	component: () => import('./views/Badges.vue'),
		// 	// beforeEnter: authGuard

		// },
		{
			path: '/community/createGroup',
			component: () => import('./views/CreateGroup.vue')
		},
		{
			path: '/community/friendCommunity',
			component: () => import('./views/FriendCommunity.vue')
		}
		,
		{
			path: '/community/yourGroups',
			component: () => import('./views/YourGroups.vue')
		},
		{
			path: '/community/yourActivity',
			component: () => import('./views/YourActivity.vue')
		},

		{
			path: '/compare',
			component: () => import('./components/Compare.vue')
		},

	]
})

export default router