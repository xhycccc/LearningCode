<?php
namespace app\index\model;
use think\Model;
class Person extends Model
{
    protected $auto = ['ip', 'password', 'repassword'];
    protected function setIpAttr()
    {
        return request()->ip();
    }
    protected function setPasswordAttr($value)
    {
        return md5($value);
    }
    protected function setRepasswordAttr($value)
    {
        return md5($value);
    }
}