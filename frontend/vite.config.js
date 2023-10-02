import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
	define: {
		// API_KEY: JSON.stringify(process.env.GOOGLE_WOOGLE)
	},
	plugins: [
		vue(),
	],
	resolve: {
		alias: {
			'@': fileURLToPath(new URL('./src', import.meta.url))
		}
	}
	// esbuild: {
	// 	// Enable esbuild's node adapter 
	// 	nodeAdapter: true
	// }
})
