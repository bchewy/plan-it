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
			path: '/how',
			component: () => import('./views/HowItWorks.vue'),
		},
		{
			path: '/route',
			component: () => import('./views/Route.vue'),
			beforeEnter: authGuard
		},
		{
			path: '/debug',
			component: () => import('./views/Debug.vue')
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

	]
})

export default router