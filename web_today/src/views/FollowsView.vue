<template>
    <div class="flex flex-col  gap-5 bg-white rounded min-h-screen px-5 py-4 text-[16px] font-semibold">
        <h1 class="text-[15px] border-b-[1px] border-gray-200 pb-2">People you have been following</h1>
        <div  v-for="i in counter.list_follow" class="flex items-center gap-5 w-full  justify-between ">
            <router-link :to="'/Profile-Friends/'+i.Followed_account[0].username"  v-on:click="counter.Search_friend_one(i.Followed_account[0].username);" class="flex items-center gap-3">
                <img :src="counter.domain_Backend+i.Followed_account[0].user_Member.Avatar" class="bg-sky-600 w-[60px] h-[60px] rounded-full" />
                <h1>{{ i.Followed_account[0].username  }}</h1>
            </router-link>
            <button v-on:click="counter.Delete_follow(i.id);" class="px-2 py-1 rounded bg-sky-400">Un Follow</button>
        </div>
    </div>
</template>
<script>
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';
import VueCookies from 'vue-cookies'
// import 'package:just_audio/just_audio.dart';


export default {

    setup() {
        const counter = useCounterStore();
        return { counter }
    },
    mounted: function () {
        this.counter.Information_Member();
        this.counter.List_follow();
    },
    methods:{
    },
    components: {
    }
}
</script>

<style>
#cjss::-webkit-scrollbar {
  width: 8px;
  height: 8px;               /* Chiều rộng vùng chứa scrollbar */
}
#cjss::-webkit-scrollbar-track {
  background: #393636;        /* Màu nền ngoài của thanh scrollbar */
}
#cjss::-webkit-scrollbar-thumb {
  background-color: #595857;    /* Màu của thanh cuộn (scroll thumb) */
  border-radius: 5px;       /* Bo góc scroll thumb */
  /* border: 2px solid #ccc;  Không hỗ trợ padding, margin, transition nên dùng viền cùng màu nên để padding scroll thumb */
}
#cjss::-webkit-scrollbar-thumb:hover {
    background-color: #655f58; /* Hiệu ứng di chuột đổi màu*/
}
</style>