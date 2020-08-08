import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Login from '@/components/Login'
import Course from '@/components/Course'
import Micro from '@/components/Micro'
import News from '@/components/News'
import CourseDetail from '@/components/CourseDetail'
import NotFound from '@/components/NotFound'
import HelloWorld from '@/components/HelloWorld'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Helloworld',
      component: HelloWorld
    },
    {
      path: '/index/',
      name: 'index',
      component: Index
    },
    {
      path: '/course/',
      name: 'Course',
      component: Course
    },
    {
      path: '/course-detail/:id/',
      name: 'CourseDetail',
      component: CourseDetail
    },
    {
      path: '/micro/',
      name: 'Micro',
      component: Micro
    },
    {
      path: '/news/',
      name: 'News',
      component: News
    },
    {
      path: '/login/',
      name: 'Login',
      component: Login
    },
    {
      path: '*',
      component: NotFound
    }
  ],
  mode: 'history'
})
