# -*- coding: utf-8 -*-
# @Author  : relakkes@gmail.com
# @Time    : 2024/1/14 18:46
# @Desc    : 抖音存储实现类
import asyncio
import csv
import json
import os
import pathlib
from typing import Dict

import aiofiles

from base.base_crawler import AbstractStore
from tools import utils
from var import crawler_type_var
from video.models import VideoInfo


class DouyinCsvStoreImplement(AbstractStore):
    csv_store_path: str = "data/douyin"

    def make_save_file_name(self, store_type: str) -> str:
        """
        make save file name by store type
        Args:
            store_type: contents or comments

        Returns: eg: data/douyin/search_comments_20240114.csv ...

        """
        return f"{self.csv_store_path}/{crawler_type_var.get()}_{store_type}_{utils.get_current_date()}.csv"

    async def save_data_to_csv(self, save_item: Dict, store_type: str):
        """
        Below is a simple way to save it in CSV format.
        Args:
            save_item:  save content dict info
            store_type: Save type contains content and comments（contents | comments）

        Returns: no returns

        """
        pathlib.Path(self.csv_store_path).mkdir(parents=True, exist_ok=True)
        save_file_name = self.make_save_file_name(store_type=store_type)
        async with aiofiles.open(
            save_file_name, mode="a+", encoding="utf-8-sig", newline=""
        ) as f:
            writer = csv.writer(f)
            if await f.tell() == 0:
                await writer.writerow(save_item.keys())
            await writer.writerow(save_item.values())

    async def store_content(self, content_item: Dict):
        """
        Xiaohongshu content CSV storage implementation
        Args:
            content_item: note item dict

        Returns:

        """
        await self.save_data_to_csv(save_item=content_item, store_type="contents")


class DouyinDbStoreImplement(AbstractStore):
    async def store_content(self, content_item: Dict):
        """
        Douyin content DB storage implementation
        Args:
            content_item: content item dict

        Returns:

        """

        # print(VideoInfo.objects.get(pk=content_item.get("aweme_id")))

        # 更新或新建 VideoInfo
        newVideo = VideoInfo.objects.update_or_create(
            aweme_id=content_item.get("aweme_id"),
            defaults={
                "aweme_id": content_item.get("aweme_id"),
                "aweme_type": content_item.get("aweme_type"),
                "title": content_item.get("title"),
                "desc": content_item.get("desc"),
                "create_time": content_item.get("create_time"),
                "user_id": content_item.get("user_id"),
                "sec_uid": content_item.get("sec_uid"),
                "short_user_id": content_item.get("short_user_id"),
                "user_unique_id": content_item.get("user_unique_id"),
                "user_signature": content_item.get("user_signature"),
                "nickname": content_item.get("nickname"),
                "avatar": content_item.get("avatar"),
                "liked_count": content_item.get("liked_count"),
                "collected_count": content_item.get("collected_count"),
                "comment_count": content_item.get("comment_count"),
                "share_count": content_item.get("share_count"),
                "ip_location": content_item.get("ip_location"),
                "last_modify_ts": content_item.get("last_modify_ts"),
                "cover": content_item.get("cover"),
                "aweme_url": content_item.get("aweme_url"),
            },
        )

        print("newVideo", newVideo)

        # from .douyin_store_sql import (
        #     add_new_content,
        #     query_content_by_content_id,
        #     update_content_by_content_id,
        # )

        # aweme_id = content_item.get("aweme_id")
        # aweme_detail: Dict = await query_content_by_content_id(content_id=aweme_id)
        # if not aweme_detail:
        #     content_item["add_ts"] = utils.get_current_timestamp()
        #     if content_item.get("title"):
        #         await add_new_content(content_item)
        # else:
        #     await update_content_by_content_id(aweme_id, content_item=content_item)


class DouyinJsonStoreImplement(AbstractStore):
    json_store_path: str = "data/douyin"
    lock = asyncio.Lock()

    def make_save_file_name(self, store_type: str) -> str:
        """
        make save file name by store type
        Args:
            store_type: Save type contains content and comments（contents | comments）

        Returns:

        """
        return f"{self.json_store_path}/{crawler_type_var.get()}_{store_type}_{utils.get_current_date()}.json"

    async def save_data_to_json(self, save_item: Dict, store_type: str):
        """
        Below is a simple way to save it in json format.
        Args:
            save_item: save content dict info
            store_type: Save type contains content and comments（contents | comments）

        Returns:

        """
        pathlib.Path(self.json_store_path).mkdir(parents=True, exist_ok=True)
        save_file_name = self.make_save_file_name(store_type=store_type)
        save_data = []

        async with self.lock:
            if os.path.exists(save_file_name):
                async with aiofiles.open(save_file_name, "r", encoding="utf-8") as file:
                    save_data = json.loads(await file.read())

            save_data.append(save_item)
            async with aiofiles.open(save_file_name, "w", encoding="utf-8") as file:
                await file.write(json.dumps(save_data, ensure_ascii=False))

    async def store_content(self, content_item: Dict):
        """
        content JSON storage implementation
        Args:
            content_item:

        Returns:

        """
        await self.save_data_to_json(content_item, "contents")
