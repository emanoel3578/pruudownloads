<template lang="">
    <div>
        <div>
            <div class="flex justify-around bg-gray-400" id="top">
                <div class="flex">
                    <div>
                        <img id="pruulogo" src="/img/huelogov1.png" class="max-h-28 transform -translate-y-2 rotate-45">
                    </div>
                    <div class="flex items-center">
                        <span class="font-kanit text-xl text-white ml-2">PruuDownloads</span>
                    </div>
                </div>

                <div class="flex">
                    <div class="flex items-center">
                        <div class="flex items-center gap-2 rounded-full py-3 px-6 p-2 md:text-xl font-kanit text-white border-3 border-gray-100 bg-gradient-to-r hover:from-blue-500 hover:to-purple-400 hover:text-white cursor-pointer shadow-lg">
                            <label for="search" class="">Search for games</label>
                            <img src="/img/lupe.png">
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
                <button @click="previousPage" class="mx-3 cursor-pointer"> &#60;&#60; </button>

                <router-link @click='ChangePage' id="firstPage" class="otherPages" ref="firstpage"  :to="'/page/' + this.pageValues[0]"> {{this.pageValues[0]}} </router-link>
                <router-link @click="ChangePage" id="secondPage" class="otherPages" ref="secondpage" :to="'/page/' + this.pageValues[1]">{{this.pageValues[1]}}</router-link>
                <router-link @click="ChangePage" id="thirdPage" class="otherPages" ref="thirdpage" :to="'/page/' + this.pageValues[2]">{{this.pageValues[2]}}</router-link>
                <router-link @click="ChangePage" id="forthPage" class="otherPages" ref="forthpage" :to="'/page/' + this.pageValues[3]">{{this.pageValues[3]}}</router-link>
                <router-link @click="ChangePage" id="fifthPage" class="otherPages" ref="fifthpage" :to="'/page/' + this.pageValues[4]">{{this.pageValues[4]}}</router-link>
                <span    value="" class="mx-3" ref="">...</span>
                <button  @click="ChangePage" value="lastpage" class="otherPages" ref="lastpage">299</button>
                
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
    props:["numberPage"],
    data () {
        return {
            loadSideCards: true,
            loadMainCards: true,
            counter:0,
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
            hasTrailer: false,
            pageValues: [1,2,3,4,5]
        }
    },

    methods:{
        ChangePage (event) {
            var currentClassPage = document.getElementById(event.srcElement.id)
            currentClassPage.classList.add("currentPage")
            this.clickedPage = event.srcElement.innerText
            this.gameList = Object.entries(jsonstr)
            var endSlice = parseInt(this.clickedPage) * 20
            var startSlice = endSlice - 20
            this.currentPage = this.gameList.slice(startSlice,endSlice)
            this.currentPage.map(function (element) {
                var developersArr = element[1].split("|")[7].split("$$")
                if(developersArr[0] == "Empty") {
                    var searchString = 'search ' + `"${element[0]}"` + '; fields id;'
                    postData('https://cors-anywhere.herokuapp.com/https://api.igdb.com/v4/games?', searchString)
                    .then(responseFromApi => {
                        var idSearchedGame = 'fields *;' + 'where game = ' + `${responseFromApi[0].id}` + ';'
                        postData('https://cors-anywhere.herokuapp.com/https://api.igdb.com/v4/covers?',  idSearchedGame)
                        .then(screenshotApi => {
                            element[1] = screenshotApi[0].url.replace("t_thumb", "t_cover_big").replace("//", "https:/")
                            //console.log(screenshotApi)
                        })
                    });
                }else {
                    element[1] = developersArr[0]
                }
                //console.log((element[1].split("|")).length)
            })
        },

        nextPage () {
            this.pageValues[0] = this.pageValues[0] + 5
            this.pageValues[1] = this.pageValues[1] + 5
            this.pageValues[2] = this.pageValues[2] + 5
            this.pageValues[3] = this.pageValues[3] + 5
            this.pageValues[4] = this.pageValues[4] + 5
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
    },

    created() {

        setTimeout(() => {
            this.loadSideCards = false
        }, 2000);

        setTimeout(() => {
            this.loadMainCards = false
        }, 1500);

        console.log("Called created")
        this.gameList = Object.entries(jsonstr)
        var endSlice = parseInt(this.numberPage) * 20
        var startSlice = endSlice - 20
        this.currentPage = this.gameList.slice(startSlice,endSlice)
        this.currentPage.map(function (element) {
            var developersArr = element[1].split("|")[7].split("$$")
            if(developersArr[0] == "Empty") {
                var searchString = 'search ' + `"${element[0]}"` + '; fields id;'
                postData('https://cors-anywhere.herokuapp.com/https://api.igdb.com/v4/games?', searchString)
                .then(responseFromApi => {
                    var idSearchedGame = 'fields *;' + 'where game = ' + `${responseFromApi[0].id}` + ';'
                    postData('https://cors-anywhere.herokuapp.com/https://api.igdb.com/v4/covers?',  idSearchedGame)
                    .then(screenshotApi => {
                        element[1] = screenshotApi[0].url.replace("t_thumb", "t_cover_big").replace("//", "https:/")
                        console.log(screenshotApi)
                    })
                });
            }else {
                element[1] = developersArr[0]
            }
            //console.log((element[1].split("|")).length)
        })

        
    },


    mounted() {
        
        if (parseInt(this.numberPage) > 5) {
            var numberOfLoops = Math.floor(parseInt(this.numberPage) / 5)
            
            let i = 0
            while (i < numberOfLoops) {
                this.pageValues[0] = this.pageValues[0] + 5
                this.pageValues[1] = this.pageValues[1] + 5
                this.pageValues[2] = this.pageValues[2] + 5
                this.pageValues[3] = this.pageValues[3] + 5
                this.pageValues[4] = this.pageValues[4] + 5
                i++
            }
        }else {
            console.log("Here 2")
        }

        var firstPage = document.getElementById("firstPage").innerHTML
        var secondPage = document.getElementById("secondPage").innerHTML
        var thirdPage = document.getElementById("thirdPage").innerHTML
        var forthPage = document.getElementById("forthPage").innerHTML
        var fifthPage = document.getElementById("fifthPage").innerHTML

        if (this.numberPage == firstPage) {
            document.getElementById("firstPage").classList.toggle("currentPage")
        }
        if (this.numberPage == secondPage) {
            document.getElementById("secondPage").classList.toggle("currentPage")
        }
        if (this.numberPage == thirdPage) {
            document.getElementById("thirdPage").classList.toggle("currentPage")
        }
        if (this.numberPage == forthPage) {
            document.getElementById("forthPage").classList.toggle("currentPage")
        }
        if (this.numberPage == fifthPage) {
            document.getElementById("fifthPage").classList.toggle("currentPage")
        }
    },

    updated() {
        this.$nextTick(function() {

            var firstPage = document.getElementById("firstPage").innerHTML
            var secondPage = document.getElementById("secondPage").innerHTML
            var thirdPage = document.getElementById("thirdPage").innerHTML
            var forthPage = document.getElementById("forthPage").innerHTML
            var fifthPage = document.getElementById("fifthPage").innerHTML

            if (this.numberPage == firstPage) {
                document.getElementById("firstPage").classList.toggle("currentPage")
            }
            if (this.numberPage == secondPage) {
                document.getElementById("secondPage").classList.toggle("currentPage")
            }
            if (this.numberPage == thirdPage) {
                document.getElementById("thirdPage").classList.toggle("currentPage")
            }
            if (this.numberPage == forthPage) {
                document.getElementById("forthPage").classList.toggle("currentPage")
            }
            if (this.numberPage == fifthPage) {
                document.getElementById("fifthPage").classList.toggle("currentPage")
            }
            })
    },
}
</script>

<style>

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

