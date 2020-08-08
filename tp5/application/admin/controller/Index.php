<?php
namespace app\admin\controller;
use think\Controller;
use app\admin\model\User;
use think\db;
class Index extends Controller
{
    public function login()
    {
        return $this->fetch();
    }
    public function logout()
    {
        session(null);
        $this->success('退出成功', 'Index/login');
    }
    public function check()
    {
        $data = input('post.');
        $user = new User();
        $result = Db::table('think_user')->where('name', $data['name'])->find();
        if ($result) {
            if($result['password'] === md5($data['password'])){
                session('name', $data['name']);
                $this->success('登录成功', 'User/index');
            }else{
                $this->error('密码不正确');
                exit;
            }
        }else{
            $this->error('用户名不存在');
        }
    }
}