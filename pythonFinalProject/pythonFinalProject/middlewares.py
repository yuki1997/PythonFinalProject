# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time
from scrapy.http import HtmlResponse
from scrapy import signals
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


# class SeleiumMiddleware(object):
#     def __init__(self, timeout=None, service_args=[]):
#         self.timeout = timeout
#         self.browser = webdriver.Chrome(service_args=service_args)
#         self.browser.set_window_size(1920, 1080)
#         self.browser.set_page_load_timeout(self.timeout)
#         self.wait = WebDriverWait(self.browser, self.timeout)
#
#     def __del__(self):
#         self.browser.close()
#
#     def process_request(self, request, spider):
#         pass
#
#     def from_crawler(cls, crawler):
#         return cls(timeout = crawler.setting.get('SELENIUM_TIMEOUT'),
#                    service_args = crawler.setting.get('CHROME_SERVICE_ARGS'))

class PythonfinalprojectSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class PythonfinalprojectDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        driver = spider.driver
        if request.url in spider.start_urls:
            try:
                driver.get(request.url)
                for key, value in spider.DemoSpider.getLevelList():
                    for key1, value1 in spider.DemoSpider.getYearList():
                        for key2, value2 in spider.DemoSpider.getProvinceList():
                            Select(driver.find_element_by_name('cengci')).select_by_value(value)
                            Select(driver.find_element_by_name('year')).select_by_value(value1)
                            Select(driver.find_element_by_xpath(
                                '/html/body/div[5]/div/div/div/form/ul/li[3]/select')).select_by_value(value2)
                            spider.DemoSpider.Click()
                            time.sleep(1)
                return HtmlResponse(url=request.url, body=self.driver.page.source, request=request, encoding='utf-8', status=200)

            except TimeoutError:
                return HtmlResponse(url=request.url, status=500, request=request)
        # return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
