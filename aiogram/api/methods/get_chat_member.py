from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Union

from .base import Request, TelegramMethod
from ..types import ChatMember

if TYPE_CHECKING:  # pragma: no cover
    from ..client.bot import Bot


class GetChatMember(TelegramMethod[ChatMember]):
    """
    Use this method to get information about a member of a chat. Returns a ChatMember object on
    success.

    Source: https://core.telegram.org/bots/api#getchatmember
    """

    __returning__ = ChatMember

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target supergroup or channel (in
    the format @channelusername)"""
    user_id: int
    """Unique identifier of the target user"""

    def build_request(self, bot: Bot) -> Request:
        data: Dict[str, Any] = self.dict()

        return Request(method="getChatMember", data=data)
