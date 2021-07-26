<template>
<div>
    <div class="h-screen w-full bg-gradient-to-b from-black via-purple-900 to-purple-900">
      <div class="">
        <Navbar/>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'

export default {
  name: 'App',
  components: {
    Navbar
  }
}
</script>

<style src="./assets/tailwind.css"></style>
