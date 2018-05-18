# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem


class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    domain_url ="https://www.qiushibaike.com"
    def parse(self, response):
        duanzidivs = response.xpath("//div[@id='content-left']/div")
        for duanzidiv in duanzidivs:
            #.get()获取xpath()返回值里面第一个内容
            author = duanzidiv.xpath(".//h2/text()").get().strip()
            # getall()返回里面所有的内容
            content = duanzidiv.xpath(".//div[@class='content']/span/text()").getall()
            content = "".join(content).strip()
            print("="*30)
            print(content)
            print("="*30)
            yield QsbkItem(author=author,content=content)
        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        if not next_url:
            return
        yield scrapy.Request(self.domain_url+next_url,callback=self.parse)

        pass
