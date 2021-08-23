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
                <div class="flex flex-col text-white font-kanit">
                    <div class="flex flex-col gap-5 pb-5 mt-8">
                        <div class="">
                            <p class="text-5xl">DMCA </p>
                        </div>
                        <div class="">
                            <a href="localhost:8080/home" class="text-red-400">www.pruudownloads.net</a>
                            <p>is in compliance with 17 U.S.C.512 and the Digital Millennium Copyright Act (DMCA). It is our policy to respond to any infringement notices and take appropriate actions under the Digital Millennium Copyright Act (DMCA) and other applicable intellectual property laws. If your copyrighted material has been posted on</p> 
                            <a href="localhost:8080/home" class="text-red-400">www.pruudownloads.net</a>
                            <p>or if hyperlinks to your copyrighted material are returned through our search engine and you want this material removed, you must provide a written communication that details the information listed in the following section. Please be aware that you will be liable for damages (including costs and attorneys fees) if you misrepresent information listed on our site that is infringing on your copyrights.
                            The following elements must be included in your copyright infringement claim:</p>
                        </div>
                        <div class="text-white text-xl border-b-2 pb-2 border-white">
                            <ul>
                                <li>=> Complete name(s) of the content in question</li>
                                <li>=> Post a link to the details Post.</li>
                                <li>=> Your company name</li>
                                <li>=> Personal info</li>
                                <li>=> Phone number</li>
                            </ul>
                        </div>

                        <div class="flex flex-col gap-2">
                            <p>Send the infringement notice via email with the Subject (We Do Not Ignore Emails). Infringement to:</p>
                            <p class="text-4xl text-blue-600"> GAME3RB.COM@GMAIL.COM</p>
                            <p class="">Removal requests are usually handled within 1h-24 hours (Max). If We Didn’t Answer in the time mentioned, Just refresh Post/Page Link you will find it already REMOVED! Usually, We Remove all reported LINKS as soon as we receive your email notification (Less than an hour)</p>
                        </div>

                        <div class="border-b-2 border-white-200 pb-2">
                            <p class="text-yellow-500">Disclaimer 1</p>
                            <p>Game3rb is absolutly legal and contain only links to other sites such as (Uptobox, Zippyshare, Go4Up, Sendspace, Up07, 1fichier…), We do not host anything (rar,iso,torrent…) on our server.</p>
                            <p class="text-yellow-500">Disclaimer 2</p>
                            <p>This site, All Links , other resources are reproduced from others Public forums & blogs & others websites.</p>
                        </div>
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