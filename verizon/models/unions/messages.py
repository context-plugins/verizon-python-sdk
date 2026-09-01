from __future__ import annotations

from typing import TypeAlias

from ..message import Message, MessageDict
from ..message1 import Message1, Message1Dict
from ..message2 import Message2, Message2Dict
from ..message3 import Message3, Message3Dict

Messages: TypeAlias = Message | Message1 | Message2 | Message3

MessagesDict: TypeAlias = MessageDict | Message1Dict | Message2Dict | Message3Dict
