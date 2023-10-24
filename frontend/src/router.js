// router.js

import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
	history: createWebHistory(),
	routes: [
		{
			path: '/',
			component: () => import('./views/Home.vue')
		},
		{
			path: '/route',
			component: () => import('./views/Route.vue')
		},
		// {
		// 	path: '/debug',
		// 	component: () => import('./views/Debug.vue')
		// },
		{
			path: '/profile',
			component: () => import('./views/Profile.vue')
		},
		{
			path: '/profile/public/:userEmail',
			component: () => import('./views/ProfilePublic.vue')
		},
		{
			path: '/community',
			component: () => import('./views/Community.vue')
		},
		{
			path: '/settings',
			component: () => import('./views/Settings.vue')
		},
		{
			path: '/admin',
			component: () => import('./views/Admin.vue')
		},
		{
			path: '/badges',
			component: () => import('./views/Badges.vue')
		},
		{
			path:'/community/createGroup',
			component: () =>('./views/CreateGroup.vue')
		},
		,
		{
			path:'/community/friendCommnunity',
			component: () =>('./views/FriendCommunity.vue')
		}
		,
		{
			path:'/community/yourGroups',
			component: () =>('./views/YourGroups.vue')
		},

	]
})

export default router