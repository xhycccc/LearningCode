<?php
namespace app\index\controller;
use think\Controller;
use think\Request;
//实现登录状态识别
class Base extends Controller
{
    protected $is_check_login = [''];
    public function _initialize()
    {
        if(!$this->isLogin() && in_array(Request::instance()->action(), $this->is_check_login)||$this->is_check_login[0]=='*'){
            return $this->error('请先登录', 'index/Index/login');
        }
    }
    public function isLogin()
    {
        return session('?name'); //判断当前作用域是否赋值
    }
}