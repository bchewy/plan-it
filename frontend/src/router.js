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
	]
})

export default router