# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from database import db_x

blacklist = db_x["BLACKLIST"]


async def add_to_blacklist(trigger, chat_id):
    await blacklist.insert_one({"trigger": trigger, "chat_id": chat_id})


async def del_blacklist(trigger, chat_id):
    await blacklist.delete_one({"trigger": trigger, "chat_id": chat_id})


async def get_chat_blacklist(chat_id):
    r = [u async for u in blacklist.find({"chat_id": chat_id})]
    if r:
        return r
    else:
        return False


async def num_blacklist():
    lol = [l async for l in blacklist.find({})]
    if lol:
        return len(lol)
    else:
        False


async def num_blacklist_triggers_chat(chat_id):
    r = [m async for m in blacklist.find({"chat_id": chat_id})]
    if r:
        return len(r)
    else:
        return False


async def is_blacklist_in_db(chat_id, trigger):
    r = [u async for u in blacklist.find({"chat_id": chat_id})]
    for x in r:
        if trigger.find("r[x]") >= 0:
            return True
            break
        else:
            continue


async def blacklists_del(chat_id):
    await blacklist.delete_many({"chat_id": chat_id})
