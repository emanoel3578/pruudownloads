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
                            <label @click="searchbar = !searchbar" for="search" class="cursor-pointer ">Search for games</label>
                            <input v-model="searchQuery" v-show="searchbar" class="text-black" size="25">
                            <img @click="sendSearch" src="/img/lupe.png">
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

        <div class="mt-5 w-3/5 mx-auto my-0">
            <p class="text-white font-kanit text-4xl">Search Results:</p>
        </div>

        <div class="mt-5 w-3/5 mx-auto my-0">
            <div class="flex">

                <div class="grid grid-cols-2">
                    <div v-for="item in queryArray" :key="item.index" class="">
                        <div class="flex flex-col justify-center items-center my-7">
                            <div class="border-4 border-red-600">
                                <router-link :to="'/game/'+ item[0] + '#top' ">
                                    <img :src="item[1]" class="cursor-pointer max-h-44 mx-auto mx-0">    
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

                <div class="w-2/5">
                    <div class="my-5">
                        <span class="font-kanit text-white text-3xl">Trending</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="/img/game1.png" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="/img/game2.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="/img/game3.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>
                    
                    <div class="flex flex-col items-center">
                        <img src="/img/game4.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="/img/game5.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="/img/game6.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="/img/game7.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="/img/game8.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="/img/game9.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="/img/game10.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>
                </div>
            </div>

            
            <div class="flex justify-center mb-2 text-lg text-white">
                <button  @click="previousPage" class="mx-3 cursor-pointer"> &#60;&#60; </button>
                <button  @click="ChangePage"  id="firstPage" value="firstpage" class="otherPages" ref="firstpage">{{this.pageValues[0]}}</button>
                <button  @click="ChangePage"  id="secondPage" value="secondpage" class="otherPages" ref="secondpage">{{this.pageValues[1]}}</button>
                <button  @click="ChangePage"  id="thirdPage" value="thirdpage" class="otherPages" ref="thirdpage">{{this.pageValues[2]}}</button>
                <button  @click="ChangePage"  id="forthPage" value="forthpage" class="otherPages" ref="forthpage">{{this.pageValues[3]}}</button>
                <button  @click="ChangePage"  id="fifthPage" value="fifthpage" class="otherPages" ref="fifthpage">{{this.pageValues[4]}}</button>
                <button @click="nextPage"  class="mx-3 cursor-pointer"> &#62;&#62; </button>
            </div>



            <!-- <div class="flex justify-center mb-2 text-lg text-white">
                <button @click="previousPage" class="mx-3 cursor-pointer"> &#60;&#60; </button>

                <router-link @click='ChangePage' id="firstPage" class="otherPages" ref="firstpage"  :to="'/page/' + this.pageValues[0]"> {{this.pageValues[0]}} </router-link>
                <router-link @click="ChangePage" id="secondPage" class="otherPages" ref="secondpage" :to="'/page/' + this.pageValues[1]">{{this.pageValues[1]}}</router-link>
                <router-link @click="ChangePage" id="thirdPage" class="otherPages" ref="thirdpage" :to="'/page/' + this.pageValues[2]">{{this.pageValues[2]}}</router-link>
                <router-link @click="ChangePage" id="forthPage" class="otherPages" ref="forthpage" :to="'/page/' + this.pageValues[3]">{{this.pageValues[3]}}</router-link>
                <router-link @click="ChangePage" id="fifthPage" class="otherPages" ref="fifthpage" :to="'/page/' + this.pageValues[4]">{{this.pageValues[4]}}</router-link>
                <span    value="" class="mx-3" ref="">...</span>
                <button  @click="ChangePage" value="lastpage" class="otherPages" ref="lastpage">299</button>
                
                <button @click="nextPage" class="mx-3 cursor-pointer"> &#62;&#62; </button>
            </div> -->
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
    name: 'Search',
    props:["query"],
    data () {
        return {
            pageSelected:"",
            searchbar: true,
            searchQuery: this.query.substring(1),
            queryArray: [],
            queryArrayTotal: [],
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
            pageValues: []
        }
    },

    methods:{
        ChangePage (event) {
            this.clickedPage = event.srcElement.innerText
            var endSlice = parseInt(this.clickedPage) * 20
            var startSlice = endSlice - 20
            this.queryArray = this.queryArrayTotal.slice(startSlice,endSlice)

            if (this.clickedPage == "1") {
                document.getElementById("firstPage").classList.add("currentPage")
                document.getElementById("secondPage").classList.remove("currentPage")
                document.getElementById("thirdPage").classList.remove("currentPage")
                document.getElementById("forthPage").classList.remove("currentPage")
                document.getElementById("fifthPage").classList.remove("currentPage")
            }
            if (this.clickedPage == "2") {
                document.getElementById("firstPage").classList.remove("currentPage")
                document.getElementById("secondPage").classList.add("currentPage")
                document.getElementById("thirdPage").classList.remove("currentPage")
                document.getElementById("forthPage").classList.remove("currentPage")
                document.getElementById("fifthPage").classList.remove("currentPage")
            }
            if (this.clickedPage == "3") {
                document.getElementById("firstPage").classList.remove("currentPage")
                document.getElementById("secondPage").classList.remove("currentPage")
                document.getElementById("thirdPage").classList.add("currentPage")
                document.getElementById("forthPage").classList.remove("currentPage")
                document.getElementById("fifthPage").classList.remove("currentPage")
            }
            if (this.clickedPage == "4") {
                document.getElementById("firstPage").classList.remove("currentPage")
                document.getElementById("secondPage").classList.remove("currentPage")
                document.getElementById("thirdPage").classList.remove("currentPage")
                document.getElementById("forthPage").classList.add("currentPage")
                document.getElementById("fifthPage").classList.remove("currentPage")
            }
            if (this.clickedPage == "5") {
                document.getElementById("firstPage").classList.remove("currentPage")
                document.getElementById("secondPage").classList.remove("currentPage")
                document.getElementById("thirdPage").classList.remove("currentPage")
                document.getElementById("forthPage").classList.remove("currentPage")
                document.getElementById("fifthPage").classList.add("currentPage")
            }
        },


        // Possivel bug no futuro pq não estou com paciencia para adicionar paginas em uma search acima de 100 items 
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
        console.log("Called created")
        var query = this.query.substring(1)
        var queryArrayTotal = this.queryArrayTotal
        
        this.gameList = Object.entries(jsonstr)
        this.gameList.map(function (element) {
            if ((element[0]).toLocaleLowerCase().includes(("query").toLocaleLowerCase()) || (element[1]).toLocaleLowerCase().includes((query).toLocaleLowerCase())) {
                queryArrayTotal.push(element)
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
            }
        })

        var numberofPages =  Math.ceil(queryArrayTotal.length / 20)

        for (var i = 0; i < numberofPages; i++) {
            this.pageValues.push(i+1)
        }

        console.log(this.pageValues)
        this.queryArray = queryArrayTotal.slice(0,20)
    },


    mounted() {
        document.getElementById("firstPage").classList.add("currentPage")
    },

    updated() {
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

