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
		// 	path: '/activity',
		// 	component: () => import('./views/Activity.vue')
		// },
		{
			path: '/profile',
			component: () => import('./views/Profile.vue')
		},
		{
			path: '/community',
			component: () => import('./views/Community.vue')
		},
		{
			path: '/settings',
			component: () => import('./views/Settings.vue')
		}
	]
})

export default router