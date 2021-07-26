<template>
<div>
    <div class="h-screen w-full bg-gradient-to-b from-black via-purple-900 to-purple-900">
      <div class="">
        <Navbar/>
      </div>

      <div>
        <Maingames/>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
import Maingames from './components/Maingames.vue'

export default {
  name: 'App',
  components: {
    Navbar,
    Maingames
  }
}
</script>

<style src="./assets/tailwind.css"></style>
