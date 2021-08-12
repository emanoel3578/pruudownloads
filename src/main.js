import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Vue3VideoPlayer from '@cloudgeek/vue3-video-player'
import '@cloudgeek/vue3-video-player/dist/vue3-video-player.css'

createApp(App).use(router).use(Vue3VideoPlayer).mount('#app')
