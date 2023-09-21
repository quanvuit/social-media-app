<template>
    <div class="flex flex-col rounded gap-3">
        <div class="flex flex-col w-full bg-white rounded px-4 py-4">
            <div class="flex gap-5 items-center ">
                <div class="flex justify-center items-center relative w-[200px] h-[200px]">
                    <img :src="counter.domain_Backend+counter.Profile.Avatar" class="min-w-[200px] h-[200px] rounded-full"/>
                    <!-- <div class=" absolute bottom-2 right-2 w-[45px] h-[45px] cursor-pointer ">
                        <div class="relative bg-gray-200  w-[45px] h-[45px] rounded-full "></div>
                        <font-awesome-icon icon="fa-solid fa-camera" class="absolute inset-0 mx-auto my-auto text-[25px] text-gray-800"/>
                    </div> -->
                </div>
                <div class="flex flex-col justify-center text-[30px] font-bold">
                    <h1>{{ counter.openthongtincanhan.username }}</h1>
                    <h1 class="text-[16px] font-medium shrink-0 whitespace-nowrap">{{ counter.list_followed.length }} Follow</h1>
                    <div class="flex gap-2 mt-2">
                        <img v-for=" i in counter.list_followed.slice(0,counter.SL_F)" :src="counter.domain_Backend+i.user[0].user_Member.Avatar" class="w-[40px] h-[40px] rounded-full"/>
                    </div>
                </div>
                <div class="flex flex-col gap-3 w-full grow justify-center items-center">
                    <div class="flex flex-col gap-2">
                        <div v-show="counter.Profile.Address!='null'" class="flex gap-2 items-center"><font-awesome-icon icon="fa-solid fa-house-chimney" class="text-[18px]" /><h1 class="font-medium">Live in {{counter.Profile.Address}}</h1></div>
                        <div v-show="counter.Profile.Date_of_birth!='null'" class="flex gap-2 items-center"><font-awesome-icon icon="fa-solid fa-cake-candles" class="text-[18px]" /><h1 class="font-medium">{{counter.Profile.Date_of_birth}}</h1></div>
                        <div class="flex gap-2 items-center "><font-awesome-icon icon="fa-solid fa-envelope" class="text-[20px]" /><h1 class="flex mb-1 font-medium">{{counter.openthongtincanhan.email}}</h1></div>
                    </div>
                </div>
            </div>
            <div class="flex  gap-3 mt-4 w-full grow ">
                <button v-on:click="counter.Edit_Post.so=2;" class="flex items-center justify-center gap-1 font-semibold w-[150px] py-1 rounded bg-sky-500"><font-awesome-icon icon="fa-solid fa-plus" /><h1 class="">Add posts</h1></button>
                <button v-on:click="counter.Edit_Profile.so=2; counter.Edit_Profile.Address = counter.Profile.Address; counter.Edit_Profile.Date_of_birth = counter.Profile.Date_of_birth;" class="flex items-center justify-center gap-1 font-semibold w-[150px] py-1 rounded bg-sky-500"><font-awesome-icon icon="fa-solid fa-pen" /><h1 class="">Edit profile</h1></button>
            </div>

            <!-- bang edit profile -->
            <div v-show="counter.Edit_Profile.so==2" v-on:click="counter.Edit_Profile.so=1" class="bg-gray-300 rounded fixed inset-0 z-40 opacity-50 cursor-pointer"></div>
            <div v-show="counter.Edit_Profile.so==2" class="bg-white rounded fixed inset-0 z-50 mx-auto my-auto w-[300px] h-[430px] flex flex-col justify-between items-center px-3 py-3">
                <h1 class="text-[22px] font-semibold border-b-[1px] border-gray-200 w-full text-center pb-3">Edit Profile</h1>
                <div class="flex justify-center items-center relative w-[200px] h-[200px]">
                    <img :src="counter.domain_Backend+counter.Profile.Avatar" class="min-w-[200px] h-[200px] rounded-full"/>
                    <label for="file" class=" absolute bottom-2 right-2 w-[45px] h-[45px] cursor-pointer ">
                        <div class="relative bg-gray-200  w-[45px] h-[45px] rounded-full "></div>
                        <font-awesome-icon icon="fa-solid fa-camera" class="absolute inset-0 mx-auto my-auto text-[25px] text-gray-800"/>
                        <input type="file" accept="image/*"  id="file" ref="file" class="hidden" v-on:change="Update_Member();"/>
                    </label>
                </div>
                <div class="flex flex-col gap-2">
                    <div class="flex gap-2 items-center"><font-awesome-icon icon="fa-solid fa-house-chimney" class="text-[18px]" /><input v-model="counter.Edit_Profile.Address" class="font-medium flex items-center outline-none bg-gray-100 px-2 py-1 rounded" /></div>
                    <div class="flex gap-2 items-center ml-1"><font-awesome-icon icon="fa-solid fa-cake-candles" class="text-[18px]" /><input v-model="counter.Edit_Profile.Date_of_birth" class="font-medium flex items-center outline-none bg-gray-100 px-2 py-1 rounded" /></div>
                </div>
                <button v-on:click=" Update_Member_path(); counter.Edit_Profile.so=1;" class="flex items-center justify-center gap-1 font-semibold w-[90px] py-1 rounded bg-sky-500"><h1 class="">Update</h1></button>
            </div>

            <!-- bang add post -->
            <div v-show="counter.Edit_Post.so==2" v-on:click="counter.Edit_Post.so=1;" class="bg-gray-300 rounded fixed z-40 inset-0 opacity-50 cursor-pointer"></div>
            <div v-show="counter.Edit_Post.so==2" class="bg-white rounded fixed z-50 inset-0 mx-auto my-auto w-[450px] h-[550px] flex flex-col justify-between items-center px-3 gap-3 py-3">
                <h1 class="text-[22px] font-semibold border-b-[1px] border-gray-200 w-full text-center pb-3">Edit Post</h1>
                <div class="flex gap-3 items-center text-[14px] font-semibold w-full">
                    <img :src="counter.domain_Backend+counter.Profile.Avatar" class="bg-sky-600 w-[40px] h-[40px] rounded-full" />
                    <h1>{{ counter.openthongtincanhan.username }}</h1>
                </div>
                <textarea v-model="counter.Create_Post.Content" placeholder="What are you thinking ?" id="slider3" class="w-full min-h-[100px] text-[12px] font-normal outline-none"></textarea>
                <label for="file1" class="bg-gray-100 w-full h-[250px] relative flex justify-center items-center cursor-pointer">
                    <div v-if="url_image.length>0" id="slider3" class=" flex flex-col w-full h-full overflow-y-auto border-[1px] border-gray-200">
                        <img v-for="i in url_image" :src="i" />
                    </div>
                    <font-awesome-icon   icon="fa-solid fa-plus" v-if="url_image.length==0" class="text-[35px] text-gray-500"/>
                    <font-awesome-icon icon="fa-solid fa-circle-xmark" v-if="url_image.length>0" v-on:click="url_image=[]" class="absolute top-2 right-2 text-[22px] text-gray-400" />
                </label>
                <button v-on:click="Update_Member1(); counter.Edit_Post.so=1;" class="w-full py-2 text-[18px] font-semibold bg-sky-500 rounded">Post</button>
                <input type="file" accept="image/*"  id="file1" ref="file1" multiple class="hidden" @change="onFileChange();"/>
                <h1>{{ counter.examplee }}</h1>
            </div>

        </div>
        <div v-for="i in counter.list_user_post"  class="flex flex-col gap-3 w-full h-full bg-white rounded px-4 py-4 ">
            <div class="flex justify-between relative">
                <div class="flex gap-2 items-center  ">
                    <img :src="counter.domain_Backend+counter.Profile.Avatar" class="w-[45px] h-[45px] rounded-full"/>
                    <div class="flex flex-col justify-center text-[16px] font-bold">
                        <h1>{{ counter.openthongtincanhan.username }}</h1>
                        <h1 class="text-[13px] font-medium text-gray-400">{{ i.Creation_time.split('T')[0] }}</h1>
                    </div>
                </div>
                <font-awesome-icon icon="fa-solid fa-ellipsis" v-on:click="all_cm1(i.id);" class="cursor-pointer text-[18px] hover:bg-gray-200 px-2 py-2 rounded-full"/>
                <div v-show="counter.show_delete==i.id" class="flex justify-center items-center absolute top-6 right-5 drop-shadow-md rounded w-[80px] py-1 font-medium bg-gray-200 cursor-pointer"><h1 v-on:click="counter.Delete_Post(i.id)">Delete</h1></div>
            </div>
            <p class="whitespace-pre-line text-[14px] font-normal" v-on:click="counter.show_delete=0">{{ i.Content }}</p>
            <div :class="{'grid grid-cols-1':i.post_image.length==1,
                        'grid grid-cols-2':i.post_image.length==2,
                        'grid grid-cols-3':i.post_image.length==3,
                        'grid grid-cols-4':i.post_image.length==4,
                        'grid grid-cols-5':i.post_image.length>4,
                                                                    }" v-on:click="counter.show_delete=0" class="w-full grid  gap-1">
                <img v-for="j in i.post_image" :src="counter.domain_Backend+j.Image_post" v-on:click="inset_image(i.post_image); url_image_inset_one=j.Image_post;  counter.show_image_inset=1" class="w-full h-full border-[1px] border-gray-200"/>
                <!-- bang hien anh ///////////////////////////////////////////////////// -->
                <div v-show="counter.show_image_inset==1"  class="bg-gray-300  fixed inset-0 mt-[68px] z-50 flex flex-col justify-end cursor-pointer">
                  <div v-on:click="counter.show_image_inset=0" class="w-full flex justify-end px-3 py-3"><font-awesome-icon icon="fa-solid fa-xmark" class="text-[30px]"/></div>
                  <div class="flex  grow w-full justify-center items-center ">
                    <img  :src="counter.domain_Backend+url_image_inset_one"  class=" max-w-[700px]  border-[1px] border-gray-200 "/>
                  </div>
                  <div class="flex bg-gray-400 h-[200px] w-full justify-center items-center gap-3 overflow-x-auto">
                    <img v-for="v in url_image_inset" :src="counter.domain_Backend+v.Image_post" v-on:click="inset_image_one(v.Image_post)" v-bind:class="{'border-[5px] border-lime-500':url_image_inset_one==v.Image_post}"  class=" max-h-[150px]  border-[1px] border-gray-200 "/>
                  </div>
                </div>
            </div>
            <div class="flex justify-between">
          <div class="flex gap-1 cursor-pointer">
            <img class="x16dsc37" height="18" role="presentation" src="data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 16 16'%3e%3cdefs%3e%3clinearGradient id='a' x1='50%25' x2='50%25' y1='0%25' y2='100%25'%3e%3cstop offset='0%25' stop-color='%2318AFFF'/%3e%3cstop offset='100%25' stop-color='%230062DF'/%3e%3c/linearGradient%3e%3cfilter id='c' width='118.8%25' height='118.8%25' x='-9.4%25' y='-9.4%25' filterUnits='objectBoundingBox'%3e%3cfeGaussianBlur in='SourceAlpha' result='shadowBlurInner1' stdDeviation='1'/%3e%3cfeOffset dy='-1' in='shadowBlurInner1' result='shadowOffsetInner1'/%3e%3cfeComposite in='shadowOffsetInner1' in2='SourceAlpha' k2='-1' k3='1' operator='arithmetic' result='shadowInnerInner1'/%3e%3cfeColorMatrix in='shadowInnerInner1' values='0 0 0 0 0 0 0 0 0 0.299356041 0 0 0 0 0.681187726 0 0 0 0.3495684 0'/%3e%3c/filter%3e%3cpath id='b' d='M8 0a8 8 0 00-8 8 8 8 0 1016 0 8 8 0 00-8-8z'/%3e%3c/defs%3e%3cg fill='none'%3e%3cuse fill='url(%23a)' xlink:href='%23b'/%3e%3cuse fill='black' filter='url(%23c)' xlink:href='%23b'/%3e%3cpath fill='white' d='M12.162 7.338c.176.123.338.245.338.674 0 .43-.229.604-.474.725a.73.73 0 01.089.546c-.077.344-.392.611-.672.69.121.194.159.385.015.62-.185.295-.346.407-1.058.407H7.5c-.988 0-1.5-.546-1.5-1V7.665c0-1.23 1.467-2.275 1.467-3.13L7.361 3.47c-.005-.065.008-.224.058-.27.08-.079.301-.2.635-.2.218 0 .363.041.534.123.581.277.732.978.732 1.542 0 .271-.414 1.083-.47 1.364 0 0 .867-.192 1.879-.199 1.061-.006 1.749.19 1.749.842 0 .261-.219.523-.316.666zM3.6 7h.8a.6.6 0 01.6.6v3.8a.6.6 0 01-.6.6h-.8a.6.6 0 01-.6-.6V7.6a.6.6 0 01.6-.6z'/%3e%3c/g%3e%3c/svg%3e" width="18">
            <h1>{{ i.like.length }}</h1>
          </div>
          <h1 class="cursor-pointer">{{ i.comments_post.length }} comments</h1>
        </div>
        <div class="flex justify-between w-full py-1 border-t-[1px] border-b-[1px] border-gray-300">
          <div v-on:click="add_like(i.id);" v-show="i.liked_Y_N == 'no'" class="flex gap-1 justify-center items-center  w-1/2 cursor-pointer hover:bg-gray-200 rounded py-2">
            <font-awesome-icon icon="fa-solid fa-thumbs-up"  class="text-[20px]" />
            <h1>Thích</h1>
          </div>
          <div v-on:click="remove_like(i.id);" v-show="i.liked_Y_N == 'yes'" class="flex gap-1 justify-center items-center  w-1/2 cursor-pointer hover:bg-gray-200 rounded py-2">
            <font-awesome-icon icon="fa-solid fa-thumbs-up" v-show="i.liked_Y_N == 'yes'" class="text-[20px] text-sky-600" />
            <h1 class="text-sky-600">Thích</h1>
          </div>
          <div class="flex gap-1 justify-center items-center w-1/2 cursor-pointer hover:bg-gray-200 rounded py-2">
            <i data-visualcompletion="css-img" class="x1b0d499 x1d69dk1" style="background-image: url(&quot;https://static.xx.fbcdn.net/rsrc.php/v3/y4/r/77DWt4rzuTp.png&quot;); background-position: 0px -351px; background-size: auto; width: 18px; height: 18px; background-repeat: no-repeat; display: inline-block;"></i>
            <h1>Bình luận</h1>
          </div>
        </div>
        <!-- viet cau bl -->
        <div class="flex gap-1 w-full ">
          <img :src="counter.domain_Backend+counter.Profile.Avatar" class="w-[32px] h-[32px] rounded-full"/>
          <input type="text" placeholder="Write the answer..." v-model="i.body" @keyup.enter="add_cm(i.id,i.body)"  class="bg-gray-200 px-2 py-1 rounded-full text-[13px] grow outline-none h-[32px]"/>
        </div>
        <!-- nut xem tat ca bl -->
        <h1 v-on:click="all_cm(i.id);" class="text-[14px] font-semibold cursor-pointer">See all comments</h1>
        <!-- bình luan cua moi ngươi -->
        <div v-show="counter.all_comments==i.id" class="flex flex-col gap-2">
            <div v-for="k in i.comments_post " class="flex gap-1">
              <img :src="counter.domain_Backend+k.name.user_Member.Avatar" class="w-[32px] h-[32px] rounded-full"/>
                <div class="flex  gap-1 relative">
                    <div class="flex flex-col bg-gray-200 rounded px-2 py-1 max-w-full">
                        <h1 class="text-[14px] font-semibold">{{ k.name.username }}</h1>
                        <p class="text-[13px] whitespace-pre-line">{{ k.body }}</p>
                    </div>
                    <font-awesome-icon icon="fa-solid fa-ellipsis" v-on:click="all_cm11(k.id,i.id);" class="cursor-pointer text-[15px] text-gray-400 hover:bg-gray-100 px-2 py-2 rounded-full"/>
                    <div v-show="counter.show_delete_comment==k.id&&counter.s_d_p==i.id" class="flex justify-center items-center absolute top-6 right-5 drop-shadow-md rounded w-[80px] py-1 font-medium bg-white cursor-pointer"><h1 v-on:click="delete_comment(k.id)">Delete</h1></div>
                </div>
            </div>
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
        url_image_inset:[{ "id": 4, "Image_post": "", "post": 4 }],
        url_image_inset_one:'',
    };
    },
    setup() {
        const counter = useCounterStore();
        return { counter }
    },
    mounted: function () {
        this.counter.Information_Member();
        this.counter.List_followed();
        this.counter.List_user_post();
    },
    methods:{
        async Update_Member() {
      let image = this.$refs.file.files[0];

      let formData = new FormData();
      formData.append('Date_of_birth', this.counter.Edit_Profile.Date_of_birth);
      formData.append('Address', this.counter.Edit_Profile.Address);
      formData.append('Avatar', image);
      formData.append('user', this.counter.openthongtincanhan.id);
      await axios({ method: 'put',data:formData, headers: {'Content-Type': 'multipart/form-data'}, url: this.counter.domain_Backend + '/update-information-user/' + this.counter.Profile.id + '/' });
      this.counter.Information_Member();
    },
    async Update_Member_path() {
            let formData = new FormData();
            formData.append('Date_of_birth', this.counter.Edit_Profile.Date_of_birth);
            formData.append('Address', this.counter.Edit_Profile.Address);
            formData.append('user', this.counter.openthongtincanhan.id);
            await axios({ method: 'patch',data:formData, headers: {'Content-Type': 'multipart/form-data'}, url: this.counter.domain_Backend + '/update-information-user/' + this.counter.Profile.id + '/' });
            this.counter.Information_Member();
    },
    async Update_Member1() {
      let formData = new FormData();

      for (var i = 0; i < this.$refs.file1.files.length; i++ ){
        let file = this.$refs.file1.files[i];
        formData.append('uploaded_images', file);
        }

      formData.append('Content', this.counter.Create_Post.Content);
      formData.append('user', this.counter.openthongtincanhan.id);

      await axios({ method: 'post',data:formData, headers: {'Content-Type': 'multipart/form-data'}, url: this.counter.domain_Backend + '/create-post'  });
      this.counter.List_user_post();
    },
    onFileChange(){
        for (var i = 0; i < this.$refs.file1.files.length; i++ ){
            let file = this.$refs.file1.files[i];
            this.url_image.push(URL.createObjectURL(file));
        }
    },
    all_cm11(aa,bb){
        if(this.counter.show_delete_comment!=aa){this.counter.show_delete_comment=aa}
        else{this.counter.show_delete_comment=0};
        this.counter.s_d_p=bb;
    },
    all_cm1(aa){
        if(this.counter.show_delete!=aa){this.counter.show_delete=aa}
        else{this.counter.show_delete=0};
        // this.counter.s_d_p=bb;
    },
    all_cm(aa){
        if(this.counter.all_comments!=aa){this.counter.all_comments=aa}
        else{this.counter.all_comments=0};
      },
      async add_cm(aa,bb){
        await this.counter.Add_comment(aa, bb);
        bb='';
        this.counter.List_user_post();
        this.counter.all_comments=aa;
      },
      async add_like(aa){
        await this.counter.Add_like(aa);
        this.counter.List_user_post();
      },
      async remove_like(aa){
        await this.counter.Delete_like(aa);
        this.counter.List_user_post();
      },
      async delete_comment(aa){
        await this.counter.Delete_comment(aa);
        this.counter.List_user_post();
        this.counter.show_delete_comment=0;
        this.s_d_p=0;
      },
      inset_image(aa){
        this.url_image_inset = aa;
        // this.url_image_inset_one = this.url_image_inset[0].Image_post;
      },
      inset_image_one(aa){
        this.url_image_inset_one = aa;
      }
    
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