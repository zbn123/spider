# spider
scrapy&amp;urlib使用

1. lagouspider中成功使用了xpath,定义了items,spider逻辑
2. lianjiaspider中使用了多层次爬取，在pipelines中实现了二次爬取，可以在lianjiaspider中实现递归&翻页爬取；在midlleware中设置了动态代理和user-agent；在setting中配置了代理和user-agent；可以在setting中配置数据库，然后再pipelines中写入数据库；
3. lagou-urllib中使用了BS和urllib，加入睡眠时间，可以不断爬取，没出现封IP；
