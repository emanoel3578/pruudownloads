<template lang="">
    <div>
        <div class="mt-10 w-4/5 mx-auto my-0">
            <div class="flex">
                <div class="grid grid-cols-2">
                    <div v-for="item in currentPage" :key="item.index" class="">
                        <div class="flex flex-col justify-center items-center my-7">
                            <div class="">
                                <img src="img/game1.png" class="cursor-pointer w-4/5 mx-auto mx-0 border-2 border-yellow-300">    
                            </div>
                            <div class="text-center">
                                <span class="font-kanit cursor-pointer text-white text-2xl">{{item[0]}}</span>
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

