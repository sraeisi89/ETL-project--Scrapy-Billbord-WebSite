from datetime import timedelta, datetime
import scrapy

class Billboard_spider(scrapy.Spider):
    name = 'Billboard'
    allowed_domains = ['billboard.com']
    start_urls = ['https://www.billboard.com/charts/artist-100/']
    week = 1

    def roll_back_date(self, chart_date):
        roll_back = timedelta(weeks=1)
        previous_date = chart_date - roll_back
        previous_date = previous_date.strftime('%Y-%m-%d')
        return previous_date

    def parse(self, response):
        chart_date_string = (response.css('#chart-date-picker::attr(data-date)').get()).strip()
        chart_date = datetime.strptime(chart_date_string, '%Y-%m-%d').date()

        artists = response.css('div.o-chart-results-list-row-container')
        artist_rank = 1
        for items in artists:
            if artist_rank <= 5:
                rank = items.css('span.c-label.a-font-primary-bold-l::text').get()
                name = items.css('#title-of-a-story::text').get()
                yield {
                    'ranking': rank.strip(),
                    'name': name.strip()
                }
            artist_rank += 1

        previous_date_string = self.roll_back_date(chart_date)
        previous_week_url = f'https://www.billboard.com/charts/artist-100/{previous_date_string}'
        if self.week < 4:
            self.week += 1
            yield scrapy.Request(previous_week_url, callback=self.parse)



