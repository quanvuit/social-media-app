<template>
    <div @mouseover="cvb='#bcbcbc'" @mouseleave="cvb='#F3F4F6'" class="flex flex-col   max-h-screen max-w-[300px] min-w-[300px] mt-4  px-3 py-3 bg-gray-100 rounded   grow text-[14px] font-semibold  gap-3">
        <h1 class="text-[15px] border-b-[1px] border-gray-200 pb-2">People you may know</h1>
        <div id="slider" class="flex flex-col gap-3 overflow-auto ">
            <div v-for="i in counter.list_un_follow"  class="flex items-center gap-3 justify-between">
                <router-link :to="'/Profile-Friends/'+i.username" v-on:click="counter.Search_friend_one(i.username);" class="flex gap-2 items-center">
                    <img :src="counter.domain_Backend+i.user_Member.Avatar" class="bg-sky-600 w-[40px] h-[40px] rounded-full" />
                    <h1>{{ i.username  }}</h1>
                </router-link>
                <button v-on:click="Follow(i.id);" class="px-2 py-1 rounded bg-sky-400">Follow</button>
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
            cvb:'#E5E7EB' ,
        }
    },
    setup() {
        const counter = useCounterStore();
        return {counter}
    },
    mounted: function () {
    },
    methods:{
        async Follow(aa){
            await this.counter.Follow_user(aa);
            this.counter.List_follow();
            this.counter.List_un_follow();
        },
    }
    }
</script>

<style>
#slider::-webkit-scrollbar {
  width: 6px;               /* Chiều rộng vùng chứa scrollbar */
}
#slider::-webkit-scrollbar-track {
  background: #F3F4F6;        /* Màu nền ngoài của thanh scrollbar */
}
#slider::-webkit-scrollbar-thumb {
  background-color: v-bind(cvb);    /* Màu của thanh cuộn (scroll thumb) */
  border-radius: 5px;       /* Bo góc scroll thumb */
  /* border: 2px solid #ccc;  Không hỗ trợ padding, margin, transition nên dùng viền cùng màu nên để padding scroll thumb */
}


</style>