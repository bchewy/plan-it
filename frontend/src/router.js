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
		{
			path: '/debug',
			component: () => import('./views/Debug.vue')
		},
		{
			path: '/profile',
			component: () => import('./views/Profile.vue')
		},
		{
			path: '/community',
			component: () => import('./views/Community.vue')
		}
	]
})

export default router