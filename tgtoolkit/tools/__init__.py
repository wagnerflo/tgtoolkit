from pyrogram.handlers import MessageHandler
from pyrogram.filters import chat

class Tool:
    handler_type = MessageHandler

    def __init__(self, chatids):
        self.chatids = chatids


    async def apply(self, client):
        handler = self.handler_type(
            self.handle_message,
            chat(self.chatids) & self.filters
        )

        for chatid in self.chatids:
            async for msg in client.get_chat_history(chatid):
                if await handler.check(client, msg):
                    await self.handle_message(client, msg)

        client.add_handler(handler)

    async def handle_message(self, client, msg):
        raise NotImplementedError()
