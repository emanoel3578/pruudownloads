<template>
    <div class="font-kanit">
        <div class="">
            <div class="flex justify-around bg-white">
                <div class="flex">
                    <div>
                        <img src="../../public/img/huelogo.png" class="max-h-32">
                    </div>
                    <div class="flex items-center">
                        <span class="font-kanit text-xl">PruuDownloads</span>
                    </div>
                </div>

                <div class="flex">
                    <div class="flex items-center">
                        <div class="flex items-center gap-2 rounded-full py-3 px-6 p-2 md:text-xl font-kanit text-white border-3 border-gray-100 bg-gradient-to-r hover:from-blue-500 hover:to-purple-400 hover:text-white cursor-pointer shadow-lg">
                            <label for="search" class="">Search for games</label>
                            <img src="../../public/img/lupe.png">
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
                <div class="flex flex-col w-full">
                    <div class="flex text-white mb-5">
                        <div class="border-2 border-black bg-gray-800 px-3">
                            <a>category/</a>
                            <a>category/</a>
                            <a>category/</a>
                            <a>category/</a>
                        </div>
                    </div>

                    <div class="flex flex-col text-white">
                        <div class="flex">
                            <p class="text-3xl">Download&nbsp;</p>
                            <p class="text-3xl">Name of the game</p>
                        </div>
                        <div class="flex mt-5">
                            <p>about&nbsp;</p>
                            <p>:time:</p>
                        </div>
                    </div>

                    <div class="flex justify-center">
                        <img src="../../public/img/mainimg.png" class="w-3/5">
                    </div>

                    <div class="flex flex-col ">
                        <div class="my-5">
                            <p class="text-2xl text-white">Game details</p>
                        </div>

                        <div class="text-gray-300 ">
                            <div class="flex">
                                <p class="font-bold">Release name:&nbsp;</p>
                                <p>INFORMATION FROM API</p>
                            </div>
                            <div class="flex mb-5">
                                <p class="font-bold">Size:&nbsp;</p>
                                <p>INFORMATION FROM API</p>
                            </div>
                            <div class="flex">
                                <p class="font-bold">Title:&nbsp;</p>
                                <p>INFORMATION FROM API</p>
                            </div>
                            <div class="flex">
                                <p class="font-bold">Genre:&nbsp;</p>
                                <p>INFORMATION FROM API</p>
                            </div>
                            <div class="flex">
                                <p class="font-bold">Developer:&nbsp;</p>
                                <p>INFORMATION FROM API</p>
                            </div>
                            <div class="flex">
                                <p class="font-bold">Publisher:&nbsp;</p>
                                <p>INFORMATION FROM API</p>
                            </div>
                            <div class="flex">
                                <p class="font-bold">Release Date:&nbsp;</p>
                                <p>INFORMATION FROM API</p>
                            </div>

                            <div class="flex text-xl text-green-500 my-5">
                                <p>ALL Reviews:</p>
                                <p>INFO FROM API</p>
                            </div>

                            <div class="flex flex-col text-xl">
                                <p class="text-yellow-500">🙋‍♂ After reviewing the game, BUY the game to support the developer 👇</p>
                                <p class="text-red-500">Steam LINK FROM API </p>
                            </div>
                        </div>

                        <div class="flex flex-col justify-center my-5">
                            <div class="flex justify-center mb-3">
                                <p class="text-white text-3xl">Screenshots</p>
                            </div>

                            <div class="flex justify-center">
                                <img src="../../public/img/mainimg.png" class="w-3/5">
                            </div>
                        </div>

                        <div class="flex flex-col my-5">
                            <div class="flex justify-center mb-2">
                                <p class="text-white text-3xl">
                                    Trailer
                                </p>
                            </div>

                            <div class="flex justify-center">
                                <video controls autoplay muted loop>
                                    <source src="../../public/img/testvideo.webm" type="video/webm">
                                </video>
                            </div>
                        </div>

                        <!-- Main information about the games div -->
                        <div class="flex flex-col" id="aboutgame">
                            <div class="my-2">
                                <p class="text-white text-3xl mb-2">
                                    About this game
                                </p>
                                <p class="text-white text-gray-300">
                                    DESCRIPTION ABOUT THE GAME COMING FROM API
                                </p>
                            </div>

                            <div class="flex flex-col my-2">
                                <p class="text-white text-3xl">System requirements</p>
                                <div class="flex-col">
                                    <div class="flex">
                                        <p class="text-gray-200 font-bold">OS:&nbsp;</p>
                                        <p class="text-gray-300">INFO FROM API</p>
                                    </div>
                                    <div class="flex">
                                        <p class="text-gray-200 font-bold">Processor:&nbsp;</p>
                                        <p class="text-gray-300">INFO FROM API</p>
                                    </div>
                                    <div class="flex">
                                        <p class="text-gray-200 font-bold">Memory:&nbsp;</p>
                                        <p class="text-gray-300">INFO FROM API</p>
                                    </div>
                                    <div class="flex">
                                        <p class="text-gray-200 font-bold">Graphics:&nbsp;</p>
                                        <p class="text-gray-300">INFO FROM API</p>
                                    </div>
                                    <div class="flex">
                                        <p class="text-gray-200 font-bold">Storage:&nbsp;</p>
                                        <p class="text-gray-300">INFO FROM API</p>
                                    </div>
                                </div>
                            </div>

                            <!-- Section for HOW TO INSTALL THE GAME -->
                            <div class="flex flex-col my-3">
                                <div class="mb-2">
                                    <p class="text-white text-3xl">How to install the game</p>
                                </div>

                                <div class="flex flex-col text-gray-300">
                                    <p>1) Download the game using a Torrent program or Direct program</p>
                                    <p>2) Extract the game to your preferred location with WinRar or 7-Zip</p>
                                    <p>3) Wait for the extraction to end</p>
                                    <p>4) No need to install the game, just start with the LAUNCHER of the game as administrator</p>
                                    <p>5) Play!</p>
                                </div>
                            </div>

                            <!-- Section for GENERAL NOTES: -->
                            <div class="flex flex-col my-5">
                                <div class="flex flex-col mb-2">
                                    <p class="text-white text-3xl">General Notes:</p>
                                </div>

                                <div class="flex flex-col text-gray-300">
                                    <p>– Make sure you have Spacewar installed. Windows Key + R and type (steam://install/480).</p>
                                    <p>– It is recommended to turn off your antivirus as some files get detected as false positive.</p>
                                    <p>– – Do not block the game with firewall if you are playing an online game with your friends.</p>
                                    <p>– In the case of an offline game, you may need to block it with firewall to prevent it from going online.</p>
                                    <p>– Turn Off your AntiVirus and Block the game’s exe in your firewall to prevent the game from trying to go online ..</p>
                                    <p>– If you install games to your system drive, it may be necessary to run this game with admin privileges instead</p>
                                </div>
                            </div>

                            <!-- Section for DOWNLOAD LINKS -->
                            <div class="flex flex-col my-5">
                                <div class="mb-3">
                                    <p class="text-white text-3xl">Download Game</p>
                                </div>

                                <div class="flex flex-col text-center justify-center">
                                    <div class="border-b-2 border-gray-300 pb-4 mb-4">
                                        <p class="text-blue-300 text-3xl mb-2">
                                            Mediafire:
                                        </p>
                                        <div class="flex justify-center">
                                            <div class="flex justify-center border-2 bg-blue-500 w-2/5 cursor-pointer py-1">
                                                <img src="../../public/img/downloadbutton.png" class="border-r-2 border-gray-300 pr-4 mr-4">
                                                <p class="text-xl text-gray-200">
                                                    Download
                                                </p>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="border-b-2 border-gray-300 pb-4 mb-4">
                                        <p class="text-red-300 text-3xl mb-2">
                                            MEGA:
                                        </p>
                                        <div class="flex justify-center">
                                            <div class="flex justify-center border-2 bg-blue-500 w-2/5 cursor-pointer py-1">
                                                <img src="../../public/img/downloadbutton.png" class="border-r-2 border-gray-300 pr-4 mr-4">
                                                <p class="text-xl text-gray-200">
                                                    Download
                                                </p>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="border-b-2 border-gray-300 pb-4 mb-4">
                                        <p class="text-purple-400 font-bold text-3xl mb-2">
                                            Bowfile:
                                        </p>
                                        <div class="flex justify-center">
                                            <div class="flex justify-center border-2 bg-blue-500 w-2/5 cursor-pointer py-1">
                                                <img src="../../public/img/downloadbutton.png" class="border-r-2 border-gray-300 pr-4 mr-4">
                                                <p class="text-xl text-gray-200">
                                                    Download
                                                </p>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="border-b-2 border-gray-300 pb-4 mb-4">
                                        <p class="text-green-300 text-3xl mb-2">
                                            TORRENT:
                                        </p>
                                        <div class="flex justify-center">
                                            <div class="flex justify-center border-2 bg-blue-500 w-2/5 cursor-pointer py-1">
                                                <img src="../../public/img/downloadbutton.png" class="border-r-2 border-gray-300 pr-4 mr-4">
                                                <p class="text-xl text-gray-200">
                                                    Download
                                                </p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!--SECTION for Recommendations -->
                            <div>
                                <div>
                                    <p class="text-white text-3xl">Recommendations</p>
                                </div>
                                <div>
                                    <p class="text-gray-300 text-xl">In construction</p>
                                </div>

                            </div>

                            <!--SECTION for comments -->
                            <div>
                                <div>
                                    <p class="text-white text-3xl">Comments</p>
                                </div>
                                <div>
                                    <p class="text-gray-300 text-xl">In construction</p>
                                </div>
                            </div>


                            
                        </div>

                    </div>
                </div>

                <div class="w-2/5">
                    <div class="my-5">
                        <span class="font-kanit text-white text-3xl">Trending</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="../../public/img/game1.png" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="../../public/img/game2.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="../../public/img/game3.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>
                    
                    <div class="flex flex-col items-center">
                        <img src="../../public/img/game4.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="../../public/img/game5.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="../../public/img/game6.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="../../public/img/game7.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="../../public/img/game8.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="../../public/img/game9.jpg" class="w-4/5">
                        <span class="font-kanit text-white text-2xl">Title title title</span>
                    </div>

                    <div class="flex flex-col items-center">
                        <img src="../../public/img/game10.jpg" class="w-4/5">
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
    props:["name"],
    data () {
        return {
            gameList:[],
            currentPage:[],
            currentGameLinks:"",
        }
    },

    created() {
        this.gameList = Object.entries(jsonstr)
        this.currentPage = this.gameList.slice(0,20)
        var currentgame = this.name
        var downloadLink = this.currentGameLinks
        this.gameList.map(function (element) {
            element.map(function (el) {
                if (el == currentgame) {
                    downloadLink = element[1]
                }
            })
        })
        console.log(currentgame)
        console.log(downloadLink)
    }
}
</script>