import scrapy
import pickle

with open("movies_url.pkl", "rb") as picklefile:
    movies_urls = pickle.load(picklefile)

class MovieSpider(scrapy.Spider):
    name = "movies_gross_fix" 
    
    def start_requests(self):   
        
        urls = movies_urls
        for url in urls:
            url_fixed = "http://www.boxofficemojo.com/movies/?page=weekly&adjust_mo=&adjust_yr=2017&"+url.split("?")[1]
            yield scrapy.Request(url=url_fixed) 

    def parse(self, response):
        try:
            title = response.xpath("//font[@face='Verdana']/b/descendant-or-self::*/text()").extract()
            if isinstance(title, list):
                title = ' '.join(title)
            elif isinstance(title, str):
               pass
            
            week1rank = response.xpath("//table//tr[count(td)=9]/td//text()").extract()[1]
            week1gross = response.xpath("//table//tr[count(td)=9]/td//text()").extract()[2]
            week1theatercount= response.xpath("//table//tr[count(td)=9]/td//text()").extract()[4]
            week2rank= response.xpath("//table//tr[count(td)=9]/td//text()").extract()[10]
            week2gross= response.xpath("//table//tr[count(td)=9]/td//text()").extract()[11]
            week1and2perchange= response.xpath("//table//tr[count(td)=9]/td//text()").extract()[12]
            week2theatercount= response.xpath("//table//tr[count(td)=9]/td//text()").extract()[13]
            
            yield {title: [week1rank, week1gross, week1theatercount, week2rank, week2gross, week1and2perchange, week2theatercount]}

       
        except:
            yield {title: response}
