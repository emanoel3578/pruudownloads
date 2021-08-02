<template>
  <div>
    <div class="flex justify-around bg-white">
      <div class="flex">
        <div>
          <img src="img/huelogo.png" class="max-h-32">
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

    <div class="bg-gray-700 flex justify-center font-kanit">
      <ul class="flex list-none gap-5">
        <li class="bg-white rounded-full border-2 border-black cursor-pointer hover:bg-purple-500 p-2 m-2">Home</li>
        <li class="bg-white rounded-full border-2 border-black cursor-pointer hover:bg-purple-500 p-2 m-2">PC Games</li>
        <li class="bg-white rounded-full border-2 border-black cursor-pointer hover:bg-purple-500 p-2 m-2">PC Repack</li>
        <li class="bg-white rounded-full border-2 border-black cursor-pointer hover:bg-purple-500 p-2 m-2">Games Online</li>
        <li class="bg-white rounded-full border-2 border-black cursor-pointer hover:bg-purple-500 p-2 m-2">How To Download</li>
        <li class="bg-white rounded-full border-2 border-black cursor-pointer hover:bg-purple-500 p-2 m-2">DMCA</li>
        <li class="bg-white rounded-full border-2 border-black cursor-pointer hover:bg-purple-500 p-2 m-2">About Us</li>
      </ul>
    </div>

  </div>
</template>

<script>
export default {
  name: 'Navbar',
}
</script>
