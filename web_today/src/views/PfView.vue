<template>
    <div class="flex flex-col rounded gap-3">
        <div class="flex flex-col w-full bg-white rounded px-4 py-4">
            <div class="flex gap-5 items-center ">
                <div class="flex justify-center items-center relative w-[200px] h-[200px]">
                    <img :src="counter.list_search_friend_one[0].user_Member.Avatar" class="min-w-[200px] h-[200px] rounded-full"/>
                    <!-- <div class=" absolute bottom-2 right-2 w-[45px] h-[45px] cursor-pointer ">
                        <div class="relative bg-gray-200  w-[45px] h-[45px] rounded-full "></div>
                        <font-awesome-icon icon="fa-solid fa-camera" class="absolute inset-0 mx-auto my-auto text-[25px] text-gray-800"/>
                    </div> -->
                </div>
                <div class="flex flex-col justify-center text-[30px] font-bold">
                    <h1>{{ counter.list_search_friend_one[0].username }}</h1>
                    <h1 class="text-[16px] font-medium shrink-0 whitespace-nowrap">{{ counter.list_followed.length }} Follow</h1>
                    <div class="flex gap-2 mt-2">
                        <img v-for=" i in counter.list_followed.slice(0,counter.SL_F)" :src="counter.domain_Backend+i.user[0].user_Member.Avatar" class="w-[40px] h-[40px] rounded-full"/>
                    </div>
                </div>
                <div class="flex flex-col gap-3 w-full grow justify-center items-center">
                    <div class="flex flex-col gap-2">
                        <div v-show="counter.list_search_friend_one[0].user_Member.Address!='null'" class="flex gap-2 items-center"><font-awesome-icon icon="fa-solid fa-house-chimney" class="text-[18px]" /><h1 class="font-medium">Live in {{counter.list_search_friend_one[0].user_Member.Address}}</h1></div>
                        <div v-show="counter.list_search_friend_one[0].user_Member.Date_of_birth!='null'" class="flex gap-2 items-center"><font-awesome-icon icon="fa-solid fa-cake-candles" class="text-[18px]" /><h1 class="font-medium">{{counter.list_search_friend_one[0].user_Member.Date_of_birth}}</h1></div>
                        <div class="flex gap-2 items-center "><font-awesome-icon icon="fa-solid fa-envelope" class="text-[20px]" /><h1 class="flex mb-1 font-medium">{{counter.openthongtincanhan.email}}</h1></div>
                    </div>
                </div>
            </div>
        </div>
        <div v-for="i in counter.list_user_post"  class="flex flex-col gap-3 w-full h-full bg-white rounded px-4 py-4 ">
            <div class="flex justify-between relative">
                <div class="flex gap-2 items-center  ">
                    <img :src="counter.list_search_friend_one[0].user_Member.Avatar" class="w-[45px] h-[45px] rounded-full"/>
                    <div class="flex flex-col justify-center text-[16px] font-bold">
                        <h1>{{ counter.list_search_friend_one[0].username }}</h1>
                        <h1 class="text-[13px] font-medium text-gray-400">{{ i.Creation_time.split('T')[0] }}</h1>
                    </div>
                </div>
            </div>
            <p class="whitespace-pre-line text-[14px] font-normal" v-on:click="counter.show_delete=0">{{ i.Content }}</p>
            <div :class="{'grid grid-cols-1':i.post_image.length==1,
                        'grid grid-cols-2':i.post_image.length==2,
                        'grid grid-cols-3':i.post_image.length==3,
                        'grid grid-cols-4':i.post_image.length==4,
                        'grid grid-cols-5':i.post_image.length>4,
                                                                    }" v-on:click="counter.show_delete=0" class="w-full grid  gap-1">
                <img v-for="j in i.post_image" :src="counter.domain_Backend+j.Image_post"  class="w-full h-full border-[1px] border-gray-200"/>
            </div>
        </div>
    </div>
</template>

<script>
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';
import VueCookies from 'vue-cookies'


export default {
    data() {
    return {
        url_image: [],
    };
    },
    setup() {
        const counter = useCounterStore();
        return { counter }
    },
    mounted: function () {
        let aa = this.$route.params.user;
        this.counter.Search_friend_one(aa);
        this.counter.Information_Member();
    },
    methods:{
    },
    components: {
    }
}
</script>

<style>
#slider3::-webkit-scrollbar {
  width: 6px;               /* Chiều rộng vùng chứa scrollbar */
}
#slider3::-webkit-scrollbar-track {
  background: #F3F4F6;        /* Màu nền ngoài của thanh scrollbar */
}
#slider3::-webkit-scrollbar-thumb {
  background-color: #dbdcdf;    /* Màu của thanh cuộn (scroll thumb) */
  border-radius: 5px;       /* Bo góc scroll thumb */
  /* border: 2px solid #ccc;  Không hỗ trợ padding, margin, transition nên dùng viền cùng màu nên để padding scroll thumb */
}


</style>