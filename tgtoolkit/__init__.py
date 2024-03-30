import os
import pyrogram

class Client(pyrogram.Client):
    def __init__(self, API_ID, API_HASH):
        super().__init("tgtools", API_ID, API_HASH, workdir=os.getcwd())
