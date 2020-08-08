<template>
  <div class="hello">
    <div>课程详细</div>
    <h3>{{ title }}</h3>
    <h3>{{ summary }}</h3>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      title:'',
      summary:''
    }
  },
  mounted:function () {
    //当组件一加载就执行的函数
    this.initCoursesDetail()
  },
  methods:{
    initCoursesDetail(){
      var nid = this.$route.params.id  //获取id
      console.log(nid);
      var that = this
      var url = 'http://127.0.0.1:8000/api/course_detail/'+nid
      this.$axios.request({
        url:url,
        methods:'GET',
        responseType:'json'
      }).then(function (response) {
        console.log(response)
        that.title = response.data.title;
        that.summary = response.data.summary
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>