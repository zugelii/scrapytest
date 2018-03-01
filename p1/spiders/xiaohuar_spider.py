
#!/usr/bin/env python
#_*_ coding := utf-8 _*_
import scrapy


class XiaoHuarrSpider(scrapy.Spider):
	name = "xiaohuar"
	allowed_domains = ["xiaohuar.com"]
	start_urls = [
		"http://www.xiaohuar.com/hua/",
	]
	def parse(slef, response):
		#分析页面
		#找到页面中符合页面规则的内容（校花图片），保存
		#找到所有的a标签，在访问其他a标签，一层一层的搞下去

		hxs = HtmlXpathSelector(response)#创建查询对象

		#如果url是http://www.xiaohuar.com/list-1-\d+.html
		if re.match("http://www.xiaohuar.com/list-1-\d+.html", response.url):#如果url能够匹配到所需要爬取的url, 即本站url
		    items = hxs.select('//div[@class="item_list infinite_scroll"]/div')#select中填写查询目标，按scrapy查询语法书写
		    for i in range(len(itemss)):
		    	src = hxs.select('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/a/img/@src' % i).extract()#查询所有img标签的src属性，即获取校花图片地址
		    	name = hxs.select('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/span/text()' % i).extract()#获取span的文本内容，即校花姓名
		    	school = hxs.select('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/div[@class="btns"]/a/text()' % i).extract()#校花学校
		    	if src:
		    		ab_src = "http://www.xiaohuar.com" + src[0]#相对路径拼接
		    		file_name = "%s_%s.jpg" % (school[0].encode("utf-8"), name[0].encode('utf-8'))#文件名 因为python27默认编码格式是unicode编码
		    		file_path = os.path.join("D:/pythonwork/scrapy/test", file_name)
		    		urllib.urlretrieve(ab_src, file_path)
