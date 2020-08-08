<?php
namespace app\index\controller;
use app\index\controller\Base;
class Comment extends Base
{
    protected $is_check_login = ['add'];
    public function add()
    {
        echo '发表评论';
    }

}