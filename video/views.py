import json
from django.http import JsonResponse

from media_platform.douyin.core import DouYinCrawler
from video.models import VideoInfo
from django.core.serializers import serialize


async def getVideos(request):
    videos = VideoInfo.objects.all()
    return JsonResponse({"data": json.loads(serialize("json", videos))})


async def syncVideos(request):
    try:
        crawler = DouYinCrawler()
        crawler.init_config(
            platform="dy",
            login_type="qrcode",
            crawler_type="detail",
        )
        await crawler.start()
        return JsonResponse({"status": True})
    except Exception as e:
        print(e)
        return JsonResponse({"status": False})
