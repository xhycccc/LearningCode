## Demo

- test.html和jsonp.php

* 访问test.html, 对jsonp.php发起请求，然后将获取到的数据传入callback函数处理。

## POC

poc.html用于验证jsonp接口是否存在敏感信息泄露。将代码中`s.src`直接替换为目标地址，并且浏览器保持目标站点的登录状态。访问poc.html看能否获取到敏感信息。