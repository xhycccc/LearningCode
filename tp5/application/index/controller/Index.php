<?php
namespace app\index\controller;
use app\index\model\Person as PersonModel;
use app\index\validate\Person as PersonValidate;

class Index extends Base
{
    protected $is_check_login = ['index'];
    public function index()
    {
        return $this->fetch();
    }
    public function login()
    {
        return $this->fetch();
    }
    public function logout()
    {
        session(null);
        $this->success('退出成功', 'Index/login');
    }
    public function register()
    {
        return $this->fetch();
    }
    public function add()
    {
        $data =  input('post.');
        dump($data);
        $val = new PersonValidate();
        if (!$val->check($data)){
            $this->error($val->getError());
            exit;
        }
        $user = new PersonModel($data);
        $ret = $user->allowField(true)->save();
        if ($ret){
            $this->success('注册成功', 'Index/index');
        }else {
            $this->error('注册失败');
        }
    }
    public function check()
    {
        $data = input('post.');
        $person = new PersonModel();
        $result = $person->where('name', $data['name'])->find();
        if ($result) {
            if($result['password'] === md5($data['password'])){
                session('name', $data['name']);
                $this->success('登录成功', 'Index/index');
            }else{
                $this->error('密码不正确');
                exit;
            }
        }else{
            $this->error('用户名不存在');
        }
    }
}