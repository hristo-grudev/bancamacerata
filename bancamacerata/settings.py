BOT_NAME = 'bancamacerata'

SPIDER_MODULES = ['bancamacerata.spiders']
NEWSPIDER_MODULE = 'bancamacerata.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'bancamacerata.pipelines.BancamacerataPipeline': 100,

}