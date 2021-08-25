<template lang="">
    <div>
        <div>
            <div class="flex justify-around bg-gray-400" id="top">
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
                            <label @click="searchbar = !searchbar" for="search" class="cursor-pointer ">Search for games</label>
                            <input v-model="searchQuery" v-show="searchbar" class="text-black" size="25">
                            <img @click="sendSearch" v-show="searchbar" src="img/lupe.png">
                        </div>
                    </div>
                </div>
            </div>

            <div class="bg-gray-700 flex justify-center font-kanit">
                <ul class="flex list-none gap-5">
                    <li class="bg-white rounded-full border-2 border-black cursor-pointer hover:bg-purple-500 p-2 m-2">
                        <router-link :to="'/home'">
                            <a>Home</a>
                        </router-link>
                    </li>
                    <li class="bg-white rounded-full border-2 border-black cursor-pointer hover:bg-purple-500 p-2 m-2">
                        <router-link :to="'/pc-repack'">
                            <a>PC Repack</a>
                        </router-link>
                    </li>
                    <li class="bg-white rounded-full border-2 border-black cursor-pointer hover:bg-purple-500 p-2 m-2">
                        <router-link :to="'/gamesonline'">
                            <a>Games online</a>
                        </router-link>
                    </li>
                    <li class="bg-white rounded-full border-2 border-black cursor-pointer hover:bg-purple-500 p-2 m-2">
                        <router-link :to="'/howtodownload'">
                            <a>How to Download</a>
                        </router-link>
                    </li>
                    <li class="bg-white rounded-full border-2 border-black cursor-pointer hover:bg-purple-500 p-2 m-2">
                        <router-link :to="'/dmca'">
                            <a>DMCA</a>
                        </router-link>
                    </li>
                    <li class="bg-white rounded-full border-2 border-black cursor-pointer hover:bg-purple-500 p-2 m-2">
                        <router-link :to="'/aboutus'">
                            <a>About Us</a>
                        </router-link>
                    </li>
                </ul>
            </div>
        </div>

        <div class="mt-10 w-3/5 mx-auto my-0">
            <div class="flex gap-6">
                <div class="grid grid-cols-2">

                    <div v-for="item in currentPage" :key="item.index" class="">
                        
                        <div v-if="loadMainCards">
                            <div class="border border-purple-300 shadow rounded-md p-4 w-full mb-10 mx-auto">
                                <div class="animate-pulse flex flex-col space-y-5 justify-center h-full w-full relative">
                                    <div class="mx-auto my-0 bg-purple-400 h-4/5 w-full absolute"></div>
                                    <img :src="item[1]" class="p-5">
                                    <div class="flex-1 space-y-4 py-1">
                                        <div class="h-4 w-full bg-purple-400 rounded mx-auto my-0"></div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div v-else>
                            <div class="flex flex-col justify-center items-center my-7">
                                <div class="border-4 border-red-600 mx-2">
                                    <router-link :to="'/game/'+ item[0] + '#top' ">
                                        <img :src="item[1]" class="max-h-40 min-w-full cursor-pointer mx-auto mx-0">    
                                    </router-link>
                                </div>
                                <div class="text-center">
                                    <router-link to="/game">
                                        <a :href="'/game/'+ item[0]" class="font-kanit cursor-pointer text-white text-2xl">{{item[0]}}</a>
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
                </div>

                <div class="w-2/5">
                    <div class="my-5">
                        <span class="font-kanit text-white text-3xl">Trending</span>
                    </div>

                    <div v-if="loadSideCards">

                        <div class="border border-blue-300 shadow rounded-md p-4 max-w-sm w-4/5 mb-10 mx-auto">
                            <div class="animate-pulse flex flex-col space-y-5 justify-center">
                                <div class="mx-auto my-0 bg-blue-400 h-20 w-20"></div>
                                <div class="flex-1 space-y-4 py-1">
                                    <div class="h-4 bg-blue-400 rounded mx-auto my-0 w-4/5"></div>
                                </div>
                            </div>
                        </div>

                        <div class="border border-blue-300 shadow rounded-md p-4 max-w-sm w-4/5 mb-10 mx-auto">
                            <div class="animate-pulse flex flex-col space-y-5 justify-center">
                                <div class="mx-auto my-0 bg-blue-400 h-20 w-20"></div>
                                <div class="flex-1 space-y-4 py-1">
                                    <div class="h-4 bg-blue-400 rounded mx-auto my-0 w-4/5"></div>
                                </div>
                            </div>
                        </div>

                        <div class="border border-blue-300 shadow rounded-md p-4 max-w-sm w-4/5 mb-10 mx-auto">
                            <div class="animate-pulse flex flex-col space-y-5 justify-center">
                                <div class="mx-auto my-0 bg-blue-400 h-20 w-20"></div>
                                <div class="flex-1 space-y-4 py-1">
                                    <div class="h-4 bg-blue-400 rounded mx-auto my-0 w-4/5"></div>
                                </div>
                            </div>
                        </div>

                        <div class="border border-blue-300 shadow rounded-md p-4 max-w-sm w-4/5 mb-10 mx-auto">
                            <div class="animate-pulse flex flex-col space-y-5 justify-center">
                                <div class="mx-auto my-0 bg-blue-400 h-20 w-20"></div>
                                <div class="flex-1 space-y-4 py-1">
                                    <div class="h-4 bg-blue-400 rounded mx-auto my-0 w-4/5"></div>
                                </div>
                            </div>
                        </div>

                        <div class="border border-blue-300 shadow rounded-md p-4 max-w-sm w-4/5 mb-10 mx-auto">
                            <div class="animate-pulse flex flex-col space-y-5 justify-center">
                                <div class="mx-auto my-0 bg-blue-400 h-20 w-20"></div>
                                <div class="flex-1 space-y-4 py-1">
                                    <div class="h-4 bg-blue-400 rounded mx-auto my-0 w-4/5"></div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div v-else>
                        <div class="flex flex-col items-center mb-5">
                            <a class="w-4/5" href="http://localhost:8080/game/NM%20Hired%20Gun#top">
                                <img src="https://cdn.cloudflare.steamstatic.com/steam/apps/1222370/header.jpg?t=1624899675" class="">
                            </a>
                            <span class="mx-auto my-0 font-kanit text-white text-2xl">NM Hired Gun</span>
                        </div>

                        <div class="flex flex-col items-center mb-5">
                            <a class="w-4/5" href="http://localhost:8080/game/Aliens%20Fireteam%20Elite">
                                    <img src="https://cdn.cloudflare.steamstatic.com/steam/apps/1549970/header.jpg?t=1629799811" class="">
                                </a>
                            <span class="font-kanit text-white text-2xl">Aliens Fireteam Elite</span>
                        </div>

                        <div class="flex flex-col items-center mb-5">
                            <a class="w-4/5" href="http://localhost:8080/game/NM%20Hired%20Gun#top">
                                    <img src="https://cdn.cloudflare.steamstatic.com/steam/apps/1484900/header.jpg?t=1629812252" class="">
                                </a>
                            <span class="font-kanit text-white text-2xl">Hoa</span>
                        </div>
                        
                        <div class="flex flex-col items-center mb-5">
                            <a class="w-4/5" href="http://localhost:8080/game/Absolute%20Territory#top">
                                    <img src="https://cdn.cloudflare.steamstatic.com/steam/apps/1130880/header.jpg?t=1620641596" class="">
                                </a>
                            <span class="font-kanit text-white text-2xl">Absolute Territory</span>
                        </div>

                        <div class="flex flex-col items-center mb-5">
                            <a class="w-4/5" href="http://localhost:8080/game/Drift%20King">
                                    <img src="https://cdn.cloudflare.steamstatic.com/steam/apps/1469690/header.jpg?t=1629713717" class="">
                                </a>
                            <span class="font-kanit text-white text-2xl">Drift King</span>
                        </div>
                    </div>
                </div> 
            </div>

            <div class="flex justify-center mb-2 text-lg text-white">
                <router-link :to="'/page/' + clickedPage">
                    <button  class="mx-3 cursor-pointer"> &#60;&#60; </button>
                    <button  @click="ChangePage" value="firstpage" class="mx-3 cursor-pointer bg-blue-500 rounded-full w-6 h-6" ref="firstpage">1</button>
                    <button  @click="ChangePage" value="secondpage" class="mx-3 cursor-pointer" ref="secondpage">2</button>
                    <button  @click="ChangePage" value="thirdpage" class="mx-3 cursor-pointer" ref="thirdpage">3</button>
                    <button  @click="ChangePage" value="forthpage" class="mx-3 cursor-pointer" ref="forthpage">4</button>
                    <button  @click="ChangePage" value="fifthpage" class="mx-3 cursor-pointer" ref="fifthpage">5</button>
                </router-link>
                <span    value="fifthpage" class="mx-3" ref="fifthpage">...</span>
                <button  @click="ChangePage" value="fifthpage" class="mx-3 cursor-pointer" ref="fifthpage">299</button>
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

async function postData(url = '', fields =' ') {
// Default options are marked with *
const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    headers: {
    'Content-Type': 'application/json',
    'Client-ID': 'x791m08fo4a05ewa5m869cm2ihvzw8',
    'Authorization': 'Bearer xbi3q6up891wjbshw15438e88kpb8s',
    'origin': 'x-requested-with',
    },
    body: fields // body data type must match "Content-Type" header
});
    return response.json(); // parses JSON response into native JavaScript objects
}


export default {
  name: 'Navbar',
  data () {
      return {
        loadSideCards: true,
        loadMainCards: true,
        searchbar: false,
        searchQuery: "",
        clickedPage:"",
        gameList:[],
        currentPage:[],
        currentGameLinks:[],
        sizeofgame: "",
        releaseDate: "",
        linkApi: "",
        description: "",
        screenshots: "",
        genre: "",
        systemReq: "",
        developers:"",
        devInfo:["Empty","Empty","Empty","Empty"],
        hasTrailer: false
      }
  },

  methods:{
      ChangePage (event) {
        this.clickedPage = event.srcElement.innerText
      },

      nextPage () {

      },

      previousPage () {

      },

      sendSearch () {
          if (this.searchQuery != "" && this.searchQuery != undefined) {
              window.location.href = "http://localhost:8080/search/s=" + this.searchQuery;
          }else {
              console.log("Bad Search")
              console.log(this.searchQuery)
          }
      },
  },

  created() {

        setTimeout(() => {
            this.loadSideCards = false
        }, 2000);

        setTimeout(() => {
            this.loadMainCards = false
        }, 1500);

        this.gameList = Object.entries(jsonstr)
        this.currentPage = this.gameList.slice(0,20)
        var developersArr = this.developers
        this.developers = developersArr
        this.currentPage.map(function (element) {
            var developersArr = element[1].split("|")[7].split("$$")
            if(developersArr[0] == "Empty") {
                postData('https://cors-anywhere.herokuapp.com/https://api.igdb.com/v4/screenshots?')
                .then(responseFromApi => {
                    element[1] = responseFromApi[0].url.replace("t_thumb", "t_screenshot_med_2x").replace("//", "https:/")
                });
            }else {
                element[1] = developersArr[0]
                
            }
        })
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

