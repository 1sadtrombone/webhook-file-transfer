import requests
import discord
import glob
import os

# where to post most recent file of
source_dir = "/home/tdyson/Screenshots"

webhook_url = os.environ['DISC_WEBHOOK']
wh = discord.SyncWebhook.from_url(webhook_url)

# find most recent filename in that directory
fnames = glob.glob(f"{source_dir}/*")
fname = max(fnames, key=os.path.getctime)

wh.send(file=discord.File(fname))
