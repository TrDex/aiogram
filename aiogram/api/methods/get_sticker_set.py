from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict

from .base import Request, TelegramMethod
from ..types import StickerSet

if TYPE_CHECKING:  # pragma: no cover
    from ..client.bot import Bot


class GetStickerSet(TelegramMethod[StickerSet]):
    """
    Use this method to get a sticker set. On success, a StickerSet object is returned.

    Source: https://core.telegram.org/bots/api#getstickerset
    """

    __returning__ = StickerSet

    name: str
    """Name of the sticker set"""

    def build_request(self, bot: Bot) -> Request:
        data: Dict[str, Any] = self.dict()

        return Request(method="getStickerSet", data=data)
