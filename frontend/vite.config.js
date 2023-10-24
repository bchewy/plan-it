import { fileURLToPath, URL } from 'node:url'
import fs from 'fs';  // Import the fs module
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
	},
	// Remove this for self-signed certificate
	// server: {
	// 	https: {
	// 		key: fs.readFileSync('./key.pem'),
	// 		cert: fs.readFileSync('./cert.pem'),
	// 	},
	// 	host: 'localhost',
	// 	port: 5173,  // You can specify another port if you want
	// }
	// Self signed cert above 


	// esbuild: {
	// 	// Enable esbuild's node adapter 
	// 	nodeAdapter: true
	// }
})
