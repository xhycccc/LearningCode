<?php

namespace app\index\controller;

class Goods extends Base
{
    protected $is_check_login = ['*'];

    public function add()
    {
        echo '购买商品';
    }
    public function edit()
    {
        echo '退货';
    }

}