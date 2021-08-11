<template lang="">
    <div>
        <div>
            <div class="flex justify-around bg-gray-400">
                <div class="flex">
                    <div>
                        <img id="pruulogo" src="img/huelogov1.png" class="max-h-28 transform -translate-y-2 rotate-45">
                    </div>
                    <div class="flex items-center">
                        <span class="font-kanit text-xl text-white ml-2">PruuDownloads</span>
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

        <div class="mt-10 w-4/5 mx-auto my-0">
            <div class="flex">
                <div class="grid grid-cols-2">
                    <div v-for="item in currentPage" :key="item.index" class="">
                        <div class="flex flex-col justify-center items-center my-7">
                            <div class="">
                                <router-link :to="'/game/'+ item[0]">
                                    <img src="img/game1.png" class="cursor-pointer w-4/5 mx-auto mx-0 border-2 border-yellow-300">    
                                </router-link>
                            </div>
                            <div class="text-center">
                                <router-link to="/game">
                                    <span class="font-kanit cursor-pointer text-white text-2xl">{{item[0]}}</span>
                                </router-link>
                            </div>
                            <div class="flex text-gray-200 font-kanit text-sm">
                                <span>About</span>
                                <span>x</span>
                                <span>Time</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="w-2/5">
                    <div class="my-5">
                        <span class="font-kanit text-white text-3xl">Trending</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="img/game1.png" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="img/game2.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="img/game3.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>
                    
                    <div class="flex flex-col items-center">
                        <img src="img/game4.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="img/game5.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="img/game6.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="img/game7.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="img/game8.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="img/game9.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="img/game10.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>
                </div>
            </div>

            <div class="flex justify-center mb-2 text-lg text-white">
                <button  class="mx-3 cursor-pointer"> &#60;&#60; </button>
                <button  value="firstpage" class="mx-3 cursor-pointer bg-blue-500 rounded-full w-6 h-6" ref="firstpage">1</button>
                <button  value="secondpage" class="mx-3 cursor-pointer" ref="secondpage">2</button>
                <button  value="thirdpage" class="mx-3 cursor-pointer" ref="thirdpage">3</button>
                <button  value="forthpage" class="mx-3 cursor-pointer" ref="forthpage">4</button>
                <button  value="fifthpage" class="mx-3 cursor-pointer" ref="fifthpage">5</button>
                <button  class="mx-3 cursor-pointer"> &#62;&#62; </button>
            </div>
        </div>
        
        <div class="w-full text-center text-white flex flex-col bg-gray-700">
            <span>Copyright © Game3rb</span>
            <span>By : Arab 4 Gamez</span>
      </div>
    </div>  
</template>

<script>
import { jsonstr } from "../../declare.js"
export default {
  name: 'Navbar',
  data () {
      return {
          gameList:[],
          currentPage:[]
      }
  },

  created() {
      this.gameList = Object.entries(jsonstr)
      this.currentPage = this.gameList.slice(0,20)
  }
}
</script>

<style>
#pruulogo {
  position: relative;
  animation-name: example;
  animation-duration: 3s;
  animation-iteration-count: infinite;
}

@keyframes example {
  0%   {left:-10px;}
  50%  {left:60px;}
  100%  {left:0px;}
}
</style>

