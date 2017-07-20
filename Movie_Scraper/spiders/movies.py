import scrapy
import pickle
errors = {}

with open("movies_url.pkl", "rb") as picklefile:
    movies_urls = pickle.load(picklefile)

class MovieSpider(scrapy.Spider):
    name = "movies" 
    
    def start_requests(self):   
        
        urls = movies_urls
        for url in urls:
            url = "http://www.boxofficemojo.com" + url +"&adjust_yr=2017&p=.htm"
            yield scrapy.Request(url=url)



    def parse(self, response):
        try:

            title = response.xpath("//font[@face='Verdana']/b/descendant-or-self::*/text()").extract()
            if isinstance(title, list):
               title = ' '.join(title)
            elif isinstance(title, str):
               pass
            
            genre = response.xpath('//td[@valign="top"]/b/text()')[0].extract()
            runtime = response.xpath('//td[@valign="top"]/b/text()')[1].extract()
            rating = response.xpath('//td[@valign="top"]/b/text()')[2].extract()
            budget = response.xpath('//td[@valign="top"]/b/text()')[3].extract()
            distributor = response.xpath('//td[@valign="top"]/b/a/text()').extract_first()
            release_date = response.xpath('//td[@valign="top"]/b//a/text()')[1].extract()
            yield {title : [genre, runtime, rating, budget, distributor, release_date] }
       
        except:
            link = "/movies/" + str(response).split("?")[1].split("&")[0]
            yield {title: ["error", link]}
            


            

        

         
        
        

