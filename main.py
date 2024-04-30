import asyncio
import os
import sys

from base.base_crawler import AbstractCrawler
from media_platform.douyin import DouYinCrawler


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawler.settings")


class CrawlerFactory:
    CRAWLERS = {
        "dy": DouYinCrawler,
    }

    @staticmethod
    def create_crawler(platform: str) -> AbstractCrawler:
        crawler_class = CrawlerFactory.CRAWLERS.get(platform)
        if not crawler_class:
            raise ValueError(
                "Invalid Media Platform Currently only supported xhs or dy or ks or bili ..."
            )
        return crawler_class()


async def main():
    crawler = DouYinCrawler()
    crawler.init_config(
        platform="dy",
        login_type="qrcode",
        crawler_type="detail",
        start_page=1,
        keyword="python,golang",
    )
    await crawler.start()


if __name__ == "__main__":
    try:
        # asyncio.run(main())

        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        sys.exit()
