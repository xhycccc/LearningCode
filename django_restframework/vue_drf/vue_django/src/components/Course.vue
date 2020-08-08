<template>
  <div class="">
  <h1>课程</h1>
  <el-table :data="tableData" style="width: 100%">
    <el-table-column prop="pk" label="pk" width="180"></el-table-column>
    <el-table-column prop="CourseName" label="课程名称" width="180"></el-table-column>

  </el-table>
      <!-- ul>
        <li v-for="item in courseList">
          <router-link :to="{'path':'/course-detail/'+item.pk}">{{item.CourseName}}</router-link>
        </li>
      </ul !-->
  </div>
</template>

<script>
export default {
  name: 'index',
  data () {
    return {
      //msg:'课程页面',
      tableData:[],
    }
  },
   mounted:function () {
      //当组件一加载的时候就应该去数据库去获取数据
      this.initCourses()
  },
  methods:{
    initCourses:function () {
      var that = this
      this.$axios.request({
          url:'http://127.0.0.1:8000/api/course',
          method:"GET"
      }).then(function (response) {
        console.log(response.data);
        that.courseList = response.data
        that.tableData = response.data  //吧从数据库取的数据赋值到courseList列表里面
      })
    }
  }

}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

</style>