from pyrogram.filters import new_chat_members, left_chat_member

class delete_member_messages(Tool):
    filters = new_chat_members | left_chat_member

    async def handle_message(self, client, msg):
        await msg.delete()
