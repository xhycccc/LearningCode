<?php
class autoload
{
    public static function load1($className)
    {
        if (is_file($className.'.php'))
        {
            require $className.'.php';
        }
    }
    public static function load2($className)
    {
        if (is_file('./app/'.$className.'.php'))
        {
            require './app/'.$className.'.php';
        }
    }
    public static function load3($className)
    {
        if (is_file('./lib/'.$className.'.php'))
        {
            require './lib/'.$className.'.php';
        }
    }
}
spl_autoload_register('autoload::load1()');
spl_autoload_register('autoload::load2()');
spl_autoload_register('autoload::load3()');
$test1 = new test1();
$test2 = new test2();
$test3 = new test3();