<template>
  <div class="">
    <h2>登录页面</h2>
    <p>用户名：<input type="text" placeholder="username" v-model="username"></p>
    <p>密码：<input type="text" placeholder="password" v-model="password"></p>
    <button><a @click="DoLogin()">提交</a></button>
  </div>
</template>

<script>
export default {
  name: 'index',
  data () {
    return {
      username: "",
      password: ""
    }
  },
    methods:{
      DoLogin (){
          var that = this
//          console.log(this.$axios);
          this.$axios.request({  //发送axios请求
            //url:'http://127.0.0.1:8000/login/',
            url:'http://127.0.0.1:8000/auth/',
            method:"POST",
            data:{
              username:this.username,
              password:this.password
            },
            responseType:'json'  //期望返回的类型是json的格式
          }).then(function (response) {  //吧返回的结果交给回调函数处理
            //登录成功之后，找到全局变量，吧用户名和token赋值到其中
            console.log(response.data);
            var data = {'token': response.data.token, 'username': that.username}
            that.$store.commit('saveToken',data);
            //重定向(登录成功之后让跳转到index页面)
              that.$router.push('/index')
              //为什么不直接用this呢？这里的this代表的是$axios,用that他代指的是整个Vue对象
          })
      }
    }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

</style>