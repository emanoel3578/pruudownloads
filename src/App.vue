<template>
<div>
    <div class="bg-gradient-to-b from-black via-purple-900 to-purple-900">
      <div class="">
        <Navbar/>
      </div>

      <div>
        <Maingames/>
      </div>

      <div>
        <Footer/>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
import Maingames from './components/Maingames.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    Navbar,
    Maingames,
    Footer,
  }
}
</script>

<style src="./assets/tailwind.css"></style>
