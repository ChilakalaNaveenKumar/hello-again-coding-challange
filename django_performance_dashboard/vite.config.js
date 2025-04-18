// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    vue(),
    tailwindcss()
  ],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false,
      }
    },
    allowedHosts: ['.ngrok-free.app'], // ✅ allows all hosts including ngrok
    host: '0.0.0.0',     // ✅ required for access outside the container
    port: 5173,
    strictPort: true     // ✅ ensures ngrok port stays fixed
  }
})