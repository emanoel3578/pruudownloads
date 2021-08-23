<template>
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
                            <label for="search" class="">Search for games</label>
                            <img src="img/lupe.png">
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
            <div class="flex">
                <div class="flex flex-col gap-2 text-white font-kanit">
                    <div class="border-b-2 border-white pb-5 mt-8">
                        <p class="text-5xl">About us </p>
                        <p class="text-2xl">Hello !</p>
                        <p>If you opened this window, then you are probably interested to know about our site. If you did this by accident, then you can close this page 🙂 ;This site was created to share Games with Internet users. We did not make the site thematic, deciding to simply publish various material – games : online, update games, Repack games, … etc. If you want to help this project, just tell your friends about the site. If you have questions, suggestions or recommendations, then write to the administration</p>
                    </div>
                </div>

                <div>
                    <div class="flex flex-col mx-auto my-0 ">
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

            </div>
        </div>

    </div>
</template>