<template>
  <div>
    <div class="flex justify-around bg-white">
      <div class="flex">
        <div>
          <img src="img/huelogo.png" class="max-h-40">
        </div>
        <div class="flex items-center">
          <span class="font-kanit text-xl">PruuDownloads</span>
        </div>
      </div>

      <div class="flex">
        <div class="flex items-center">
          <div class="flex items-center gap-2 rounded-full py-3 px-6 p-2 md:text-xl font-kanit text-white border-3 border-gray-100 bg-gradient-to-r hover:from-blue-500 hover:to-purple-400 hover:text-white cursor-pointer shadow-lg">
            <label for="search" class="">Search for games</label>
            <img src="img/lupe.png">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
