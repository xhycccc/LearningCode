<template>
  <el-menu theme="dark" :default-active="activeIndex"
  class="el-menu-demo" mode="horizontal" @select="handleSelect">
    <el-menu-item index="1"><router-link to="/index">首页</router-link></el-menu-item>
    <el-menu-item index="2"><router-link to="/micro">学位课</router-link></el-menu-item>
    <el-submenu index="3">
      <template slot="title"><router-link to="/course">课程</router-link></template>
      <el-menu-item index="3-1"><router-link to="/course-detail/1">人生苦短，我用Python</router-link></el-menu-item>
      <el-menu-item index="3-2"><router-link to="/course-detail/2">人生苦短，我用PHP</router-link></el-menu-item>
      <el-menu-item index="3-3"><router-link to="/course-detail/3">人生苦短，我用JS</router-link></el-menu-item>
    </el-submenu>
    <el-menu-item index="4"><router-link to="/news">最新消息</router-link></el-menu-item>
    <el-menu-item index="5" v-if="this.$store.state.token">
      <span><a>欢迎{{ this.$store.state.username }}登录</a></span>
      <span><a @click="logout()">注销</a></span>
    </el-menu-item>
    <el-menu-item index="5" v-else="">
      <router-link to="/login">登录</router-link>
    </el-menu-item>
  </el-menu>
</template>

<script>
  export default {
    data () {
      return {
        activeIndex: '1',
        activeIndex2: '1'
      }
    },
    methods: {
      handleSelect (key, keyPath) {
        console.log(key, keyPath)
      },
      logout(){
      this.$store.state.username=''
      this.$store.state.token=''
      }
    }
  }
</script>