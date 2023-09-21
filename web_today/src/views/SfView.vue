<template>
    <div class="flex flex-col  gap-5 bg-white rounded min-h-screen px-5 py-4 text-[16px] font-semibold">
        <h1 class="text-[15px] border-b-[1px] border-gray-200 pb-2">Friend Search List</h1>
        <div  v-for="i in counter.list_search_friend" class="flex items-center gap-5 w-full  justify-between ">
            <router-link :to="'/Profile-Friends/'+i.username" v-on:click="counter.Search_friend_one(i.username);" class="flex items-center gap-3">
                <img :src="i.user_Member.Avatar" class="bg-sky-600 w-[60px] h-[60px] rounded-full" />
                <div class="flex flex-col ">
                    <h1>{{ i.username  }}</h1>
                    <h1 class="text-[14px] text-lime-500 font-medium">{{ i.user_Member.Address }}</h1>
                </div>
            </router-link>
            <div class="flex gap-5">
                <button v-show="i.following.status=='no'" v-on:click="Rf_S1(i.id);" class="w-[150px] py-1 rounded bg-sky-400">Follow</button>
                <button v-show="i.following.status=='yes'" v-on:click=" Rf_S2(i.following.id_following);" class="w-[150px] py-1 rounded bg-sky-400">Un Follow</button>
            </div>
        </div>
        <!-- <h1>{{ counter.list_search_friend }}</h1> -->
    </div>
</template>

<script>
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';
import VueCookies from 'vue-cookies'


export default {

    setup() {
        const counter = useCounterStore();
        return { counter }
    },
    mounted: function () {
        this.counter.Information_Member();
    },
    methods:{
        async Follow(aa){
            await this.counter.Follow_user(aa);
            this.counter.List_follow();
            this.counter.List_un_follow();
        },
        async Rf_S1(aa){
            await this.Follow(aa);
            this.counter.Search_friend();
        },
        async Rf_S2(aa){
            await this.counter.Delete_follow(aa);
            this.counter.Search_friend();
        }
    },
    components: {
    }
}
</script>