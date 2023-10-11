import { defineStore } from 'pinia';

import axios from 'axios';
import VueCookies from 'vue-cookies'
import { fa0 } from '@fortawesome/free-solid-svg-icons';

import { useRoute } from 'vue-router';
const Route = useRoute();


export const useCounterStore = defineStore('counter', {
  state: () => {
    return {
      domain_Backend: 'http://127.0.0.1:8000', domain_Frontend: '', Path_Route: useRoute(),

      // Social///////////////////////
      Table_Lg_Rg: 0, Form_Lg_R: true, Lg: { username: '', password: '' }, Rg: { username: '', email: '', password: '', confirm_password: '' },
      openthongtincanhan: { id: '', username: '', email: '', password: '', token: '' }, Error_Lg: { so: 1, thong_bao: '' }, Error_Rg: { so: 1, thong_bao: '' }, Rg_TC: 1, Show_DD_image: false,
      Profile: { id: '', Date_of_birth: '', Address: '', Avatar: '' }, Edit_Profile: { so: 1, Date_of_birth: '', Address: '' }, Edit_Post: { so: 1, Date_of_birth: '', Address: '' }, Data_Image: '', list_un_follow: '', SL_F: 0, list_followed: '',
      list_follow: [{
        Followed_account: [{
          "id": '',
          "username": '',
          "email": '',
          "user_Member": {
            "id": '',
            "Date_of_birth": null,
            "Address": null,
            "Avatar": null,
            "user": ''
          }
        }]
      }],
      Create_Post: { Content: '' }, examplee: '', list_user_post: '', show_delete: '', list_post_home: '', search_friend: '', list_search_friend: '', list_search_friend_one: [
        {
          "id": '',
          "username": "",
          "email": "",
          "user_Member": {
            "id": '',
            "user": {
              "id": '',
              "username": "",
              "email": "",
              "user_Member": ''
            },
            "Date_of_birth": "null",
            "Address": "null",
            "Avatar": ""
          }
        }
      ],
      all_comments: 0, body_comment: '', show_delete_comment: 0, s_d_p: 0, show_image_inset: 0,

    }
  },

  getters: {
    // cookievalue: (state) => state.openthongtincanhan.token + "(Theta)" + state.openthongtincanhan.id,
  },

  actions: {
    async dangnhaptaikhoanvataocookie() {
      try {
        this.openthongtincanhan = await axios({ method: 'post', url: this.domain_Backend + '/login', data: { "username": this.Lg.username, "password": this.Lg.password } });
        this.openthongtincanhan = this.openthongtincanhan.data;
        VueCookies.set("Lg_T", this.openthongtincanhan.token + "eab42d241cad8d" + this.openthongtincanhan.id, "7d");
        this.Table_Lg_Rg = 2;
        VueCookies.set("Tab_Lg_T", 2, "365d");
        this.Information_Member();
        this.List_un_follow();
      }
      catch (error) {
        this.Error_Lg.so = 2;
        this.Error_Lg.thong_bao = error.response.data['Error'];
      }

    },
    async keep_login() {
      try {
        this.openthongtincanhan.id = await VueCookies.get("Lg_T").split('eab42d241cad8d')[1];
        this.openthongtincanhan.token = await VueCookies.get("Lg_T").split('eab42d241cad8d')[0];
      }
      catch {
        this.openthongtincanhan = { id: '', username: '', email: '', password: '', token: '' };
        this.Table_Lg_Rg = 1;
      }
      if (this.openthongtincanhan.token != '') {
        try {
          // this.Table_Lg_Rg = 2;
          this.openthongtincanhan = await axios({ method: 'post', url: this.domain_Backend + '/keeplogin', data: { "id": this.openthongtincanhan.id, "token": this.openthongtincanhan.token }, headers: { Authorization: 'Token ' + this.openthongtincanhan.token } });
          this.Table_Lg_Rg = 2;
          this.openthongtincanhan = this.openthongtincanhan.data;
          this.List_un_follow();
        }
        catch {
          this.openthongtincanhan = { id: '', username: '', email: '', password: '', token: '' };
          this.Table_Lg_Rg = 1;
        }
      }
    },
    async dangxuattaikhoan() {
      await axios({ method: 'post', url: this.domain_Backend + '/user/auth/logout/', headers: { Authorization: 'Token ' + this.openthongtincanhan.token } });
      this.Table_Lg_Rg = 1;
      VueCookies.set("Tab_Lg_T", 1, "365d");
      VueCookies.remove("Lg_T");
    },
    async dangkitaikhoan() {
      try {
        await axios({ method: 'post', url: this.domain_Backend + '/register', data: { "email": this.Rg.email, "username": this.Rg.username, "password": this.Rg.password, "confirm_password": this.Rg.confirm_password } });
        this.Rg_TC = 2;
        this.Error_Rg.so = 1;
        this.Error_Rg.thong_bao = 'Successful account registration';
        this.Rg = { username: '', email: '', password: '', confirm_password: '' };
      }
      catch (error) {
        this.Error_Rg.so = 2;
        this.Rg_TC = 1;
        this.Error_Rg.thong_bao = error.response.data['Error'];
      }
    },
    async Information_Member() {
      this.Profile = await axios({ method: 'get', params: { username_id: this.openthongtincanhan.id }, url: this.domain_Backend + '/information-user' });
      this.Profile = this.Profile.data.Data;
      this.Edit_Profile.Address = this.Profile.Address;
      this.Edit_Profile.Date_of_birth = this.Profile.Date_of_birth;
    },
    async List_follow() {
      this.list_follow = await axios({ method: 'get', params: { username_id: this.openthongtincanhan.id }, url: this.domain_Backend + '/list-user-follow' });
      this.list_follow = this.list_follow.data.Data;
    },
    async List_followed() {
      this.list_followed = await axios({ method: 'get', params: { username_id: this.openthongtincanhan.id }, url: this.domain_Backend + '/list-user-followed' });
      this.list_followed = this.list_followed.data.Data;
      if (this.list_followed.length > 3) {
        this.SL_F = 3
      }
      else {
        this.SL_F = this.list_followed.length;
      }
    },
    async Follow_user(fl_id) {
      await axios({ method: 'post', data: { username_id: this.openthongtincanhan.id, username_followed_id: fl_id }, url: this.domain_Backend + '/follow-user' });
    },
    async Delete_follow(fl_id) {
      await axios({ method: 'get', params: { follow_id: fl_id }, url: this.domain_Backend + '/delete-follow' });
      this.List_follow();
      this.List_un_follow();
    },
    async List_un_follow() {
      this.list_un_follow = await axios({ method: 'get', params: { username_id: this.openthongtincanhan.id }, url: this.domain_Backend + '/list-user-un-follow' });
      this.list_un_follow = this.list_un_follow.data.Data;
    },
    async List_user_post() {
      this.list_user_post = await axios({ method: 'get', params: { username_id: this.openthongtincanhan.id }, url: this.domain_Backend + '/list-post-user' });
      this.list_user_post = this.list_user_post.data.Data;

      for (let i = 0; i < this.list_user_post.length; i++) {
        this.list_user_post[i].liked_Y_N = 'no';
        for (let j = 0; j < this.list_user_post[i].like.length; j++) {
          if (this.openthongtincanhan.username == this.list_user_post[i].like[j].username) {
            this.list_user_post[i].liked_Y_N = 'yes';
          }
        }
      }
    },
    async Delete_Post(post_id) {
      await axios({ method: 'get', params: { post_id: post_id }, url: this.domain_Backend + '/delete-post' });
      this.List_user_post();
    },
    async List_post_home() {
      this.list_post_home = await axios({ method: 'get', params: { username_id: this.openthongtincanhan.id }, url: this.domain_Backend + '/list-post' });
      this.list_post_home = this.list_post_home.data.Data;

      for (let i = 0; i < this.list_post_home.length; i++) {
        this.list_post_home[i].liked_Y_N = 'no';
        for (let j = 0; j < this.list_post_home[i].like.length; j++) {
          if (this.openthongtincanhan.username == this.list_post_home[i].like[j].username) {
            this.list_post_home[i].liked_Y_N = 'yes';
          }
        }
      }
    },
    async Search_friend() {
      this.list_search_friend = await axios({ method: 'get', url: this.domain_Backend + '/search-friend?search=' + this.search_friend });
      this.list_search_friend = this.list_search_friend.data;

      for (let i = 0; i < this.list_search_friend.length; i++) {
        this.list_search_friend[i].following = { status: 'no', id_following: '' };
        for (let j = 0; j < this.list_search_friend[i].user_followed.length; j++) {
          if (this.openthongtincanhan.username == this.list_search_friend[i].user_followed[j].user[0].username) {
            this.list_search_friend[i].following = { status: 'yes', id_following: this.list_search_friend[i].user_followed[j].id };
          }
        }
      }
    },
    async Search_friend_one(aa) {
      this.list_search_friend_one = await axios({ method: 'get', url: this.domain_Backend + '/search-friend?search=' + aa });
      this.list_search_friend_one = await this.list_search_friend_one.data;

      this.list_followed = await axios({ method: 'get', params: { username_id: this.list_search_friend_one[0].id }, url: this.domain_Backend + '/list-user-followed' });
      this.list_followed = this.list_followed.data.Data;
      if (this.list_followed.length > 3) {
        this.SL_F = 3
      }
      else {
        this.SL_F = this.list_followed.length;
      }

      // this.list_user_post = await axios({ method: 'get', params: { username_id: this.list_search_friend_one[0].id }, url: this.domain_Backend + '/list-post-user' });
      // this.list_user_post = this.list_user_post.data.Data;

      this.list_user_post = await axios({ method: 'get', params: { username_id: this.list_search_friend_one[0].id }, url: this.domain_Backend + '/list-post-user' });
      this.list_user_post = this.list_user_post.data.Data;
    },
    async Add_comment(aa, bb) {
      await axios({ method: 'post', data: { username_id: this.openthongtincanhan.id, post_id: aa, body: bb }, url: this.domain_Backend + '/add-comment' });
    },
    async Add_like(aa) {
      await axios({ method: 'get', params: { username_id: this.openthongtincanhan.id, post_id: aa }, url: this.domain_Backend + '/like-post' });
    },
    async Delete_like(aa) {
      await axios({ method: 'get', params: { username_id: this.openthongtincanhan.id, post_id: aa }, url: this.domain_Backend + '/delete-like-post' });
    },
    async Delete_comment(aa) {
      await axios({ method: 'get', params: { comment_id: aa }, url: this.domain_Backend + '/delete-comment' });
    },
  }
})


