<template lang="">
    <div>
        <div>
            <div class="flex justify-around bg-gray-400" id="top">
                <div class="flex">
                    <div>
                        <img id="pruulogo" src="img/huelogov1.png" class="max-h-28 transform -translate-y-2 rotate-45">
                    </div>
                    <div class="flex items-center">
                        <span class="font-kanit text-xl text-black ml-2 text-white">PruuDownloads</span>
                    </div>
                </div>

                <div class="flex">
                    <div class="flex items-center">
                        <div class="flex items-center gap-2 rounded-full py-3 px-6 p-2 md:text-xl font-kanit text-white border-3 border-gray-100 bg-gradient-to-r hover:from-blue-500 hover:to-purple-400 hover:text-white cursor-pointer shadow-lg">
                            <label @click="searchbar = !searchbar" for="search" class="cursor-pointer ">Search for games</label>
                            <input v-on:keyup.enter="sendSearch" v-model="searchQuery" v-show="searchbar" class="text-black" size="25">
                            <img @click="sendSearch" v-show="searchbar" src="img/lupe.png">
                        </div>
                    </div>
                </div>
            </div>

            <div class="bg-gray-700 flex justify-center font-kanit">
                <ul class="flex list-none gap-5 items-center">
                    <li class="text-white cursor-pointer hover:text-purple-500 p-2">
                        <router-link :to="'/home'" class="flex items-center">
                            <img id="homePru" src="img/huelogov1.png" class="max-h-10 invisible">
                            <a @mouseover="showPru" @mouseleave="hidePru">Home</a>
                        </router-link>
                    </li>
                    <li class="text-white cursor-pointer hover:text-purple-500 p-2">
                        <router-link :to="'/pc-repack'" class="flex items-center">
                            <img id="RepackPru" src="img/huelogov1.png" class="max-h-10 invisible">
                            <a @mouseover="showPru" @mouseleave="hidePru">PC Repack</a>
                        </router-link>
                    </li>
                    <li class="text-white cursor-pointer hover:text-purple-500 p-2 ">
                        <router-link :to="'/gamesonline'" class="flex items-center">
                            <img id="OnlinePru" src="img/huelogov1.png" class="max-h-10 invisible">
                            <a @mouseover="showPru" @mouseleave="hidePru">Games online</a>
                        </router-link>
                    </li>
                    <li @mouseover ="categoriesHover = true" @mouseleave ="categoriesHover = false" class="text-white cursor-pointer hover:text-purple-500 p-2 relative">
                        <div class="flex items-center">
                            <img id="CategoriesPru" src="img/huelogov1.png" class="max-h-10 invisible">
                            <a @mouseover="showPru" @mouseleave="hidePru">Categories</a>
                        </div>
                        <div v-show="categoriesHover" class="z-10 border-2 border-black font-kanit cursor-default flex absolute text-white bg-purple-500 gap-5 rounded-lg">
                            <ul class="m-3 ">
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Singleplayer">Singleplayer</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Multiplayer">Multiplayer</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Indie">Indie</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Action">Action</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Adventure">Adventure</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Casual">Casual</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Simulation">Simulation</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=RPG">RPG</a></li>
                            </ul>

                            <ul class="m-3">
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=2D">2D</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Atmospheric">Atmospheric</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Puzzle">Puzzle</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Strategy">Strategy</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Pixel">Pixel</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Fantasy">Fantasy</a></li>
                                <li class="cursor-pointer mb-1 mx-2 hover:text-black"><a href="http://localhost:8080/search/s=Colorful">Colorful</a></li>
                            </ul>
                        </div>
                    </li>
                    <li class="text-white cursor-pointer hover:text-purple-500 p-2 ">
                        <router-link :to="'/dmca'" class="flex items-center">
                            <img id="DMCAPru" src="img/huelogov1.png" class="max-h-10 invisible">
                            <a @mouseover="showPru" @mouseleave="hidePru">DMCA</a>
                        </router-link>
                    </li>
                    <li class="text-white cursor-pointer hover:text-purple-500 p-2 ">
                        <router-link :to="'/aboutus'" class="flex items-center">
                            <img id="AboutPru" src="img/huelogov1.png" class="max-h-10 invisible">
                            <a @mouseover="showPru" @mouseleave="hidePru">About Us</a>
                        </router-link>
                    </li>
                </ul>
            </div>
        </div>

        <div class="mt-10 w-3/5 mx-auto my-0">
            <div class="flex gap-6">
                <div class="grid grid-cols-2">

                    <div v-for="item in apidata" :key="item.index" class="">
                        
                        <div v-if="LoadMainCards">
                            <div class="border border-purple-300 shadow rounded-md p-4 w-full mb-10 mx-auto">
                                <div class="animate-pulse flex flex-col space-y-5 justify-center h-full w-full relative">
                                    <div class="mx-auto my-0 bg-purple-400 h-4/5 w-full absolute"></div>
                                    <img :src="item.imgheader" alt="">
                                    <div class="flex-1 space-y-4 py-1">
                                        <div class="h-4 w-full bg-purple-400 rounded mx-auto my-0"></div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div v-else>
                            <div class="flex flex-col justify-center items-center my-7 relative transition duration-500 ease-in-out transform hover:-translate-y-1 hover:scale-110">
                                <img :id="item.name.replace(/ /g,'')" src="/img/coop.png" class="absolute left-0 -top-5 transform -rotate-45 hidden">
                                <div class="border-4 border-red-600 mx-2 hover:border-blue-500">
                                    <router-link :to="'/game/'+ item.id">
                                        <img :src="item.imgheader" class="max-h-40 min-w-full cursor-pointer mx-auto mx-0 ">    
                                    </router-link>
                                </div>
                                <div class="text-center mt-2">
                                    <router-link :to="'/game/' +  item.id">
                                        <a :href="'/game/'+ item.id" class="font-kanit cursor-pointer text-white text-2xl">{{item.nameref}}</a>
                                    </router-link>
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
                <button @click="previousPage" class="mx-3 cursor-pointer"> &#60;&#60; </button>
                <a id="firstPage"  @click="ChangePage" value="firstpage" class="otherPages currentPage" ref="firstpage">{{this.pageValues[0]}}</a>
                <a id="secondPage" @click="ChangePage" value="secondpage" class="otherPages" ref="secondpage">{{this.pageValues[1]}}</a>
                <a id="thirdPage" @click="ChangePage" value="thirdpage" class="otherPages" ref="thirdpage">{{this.pageValues[2]}}</a>
                <a id="forthPage" @click="ChangePage" value="forthpage" class="otherPages" ref="forthpage">{{this.pageValues[3]}}</a>
                <a id="fifthPage" @click="ChangePage" value="fifthpage" class="otherPages" ref="fifthpage">{{this.pageValues[4]}}</a>
                
                <span value="fifthpage" class="mx-3" ref="fifthpage">...</span>
                <button  @click="ChangePage" id="lastPage" class="mx-3 cursor-pointer">{{this.lastPage}}</button>
                <button @click="nextPage" class="mx-3 cursor-pointer"> &#62;&#62; </button>
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
        categoriesHover: false,
        loadSideCards: true,
        LoadMainCards: true,
        lastPage: "",
        searchbar: false,
        searchQuery: "",
        clickedPage:"",
        gameList:[],
        currentPage:[],
        apidata:[],
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
        hasTrailer: false,
        pageValues: []
      }
  },

  methods:{

      showPru (event) {
          var selectedCategorie = event.srcElement.parentElement.childNodes[0].id
          document.getElementById(selectedCategorie).classList.add("showPru")
      },

      hidePru (event) {
          var selectedCategorie = event.srcElement.parentElement.childNodes[0].id
          document.getElementById(selectedCategorie).classList.remove("showPru")
      },

      ChangePage (event) {
        this.clickedPage = event.srcElement.innerText
        window.location.href = "http://localhost:8080/page/" + this.clickedPage
      },

      nextPage () {
          var gameList = Object.entries(jsonstr)
            if (gameList.length / 20 > 5 && Math.floor(gameList.length/20) + 1 > parseInt(document.getElementById("fifthPage").innerHTML)) {
                this.pageValues[0] = this.pageValues[0] + 5
                this.pageValues[1] = this.pageValues[1] + 5
                this.pageValues[2] = this.pageValues[2] + 5
                this.pageValues[3] = this.pageValues[3] + 5
                this.pageValues[4] = this.pageValues[4] + 5
            }
      },

      previousPage () {
          if(this.pageValues[0] > 1) {
                this.pageValues[0] = this.pageValues[0] - 5
                this.pageValues[1] = this.pageValues[1] - 5
                this.pageValues[2] = this.pageValues[2] - 5
                this.pageValues[3] = this.pageValues[3] - 5
                this.pageValues[4] = this.pageValues[4] - 5
            }
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

  updated() {
        var gameChecker = this.apidata
        
        gameChecker.map(function (element) {
            var onlineChecker = element.gamemode
            
            if(onlineChecker == "Online") {
                document.getElementById(element.name.replace(/ /g, "")).classList.add("showMP")
            }   
        })

        if(document.getElementById("firstPage").innerHTML == "1") {
            document.getElementById("firstPage").classList.toggle("currentPage")
        }else {
            document.getElementById("firstPage").classList.remove("currentPage")
        }
  },

  created() {

        this.axios.get('http://127.0.0.1:8000/api/paginate').then((response)=>{
            this.apidata = response.data.Results.data;
            this.LoadMainCards = false
        })

        setTimeout(() => {
            this.loadSideCards = false
        }, 2000);

        this.gameList = Object.entries(jsonstr)
        this.lastPage = Math.floor(this.gameList.length / 20) + 1
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

        var numberofPages =  Math.ceil(this.gameList.length / 20)

        for (var i = 0; i < numberofPages; i++) {
            this.pageValues.push(i+1)
        }
    }
}
</script>

<style>

.showPru {
    visibility: visible;
}

.showMP {
    display: block;
}

.currentPage{
    margin-right: 0.75em;
    margin-left: 0.75em;
    text-align: center;
    cursor: pointer;
    background-color: #3B82F6;
    border-radius: 25px;
    width: 1.5em;
    height: 1.5em;
}

.otherPages {
    margin-right: 0.75em;
    margin-left: 0.75em;
    cursor: pointer;
}

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

