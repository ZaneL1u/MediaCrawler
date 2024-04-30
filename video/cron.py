import asyncio
import logging
from threading import Thread
from django_cron import CronJobBase, Schedule

from media_platform.douyin.core import DouYinCrawler

logger = logging.getLogger(__name__)


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = "video.getVideo3"

    def do(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        def start_loop():
            loop.run_until_complete(self.my_async_task())

        thread = Thread(target=start_loop)
        thread.start()
        thread.join()

    async def my_async_task(self):
        crawler = DouYinCrawler()
        crawler.init_config(
            platform="dy",
            login_type="qrcode",
            crawler_type="detail",
            start_page=1,
            keyword="python,golang",
        )
        await crawler.start()
        logger.info("This function runs every 5 minutes.")
