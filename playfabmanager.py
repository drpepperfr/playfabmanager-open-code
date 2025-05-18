import discord
# fuck you skidders
from discord import app_commands
# fuck you skidders

# fuck you skidders

# fuck you skidders

# fuck you skidders

# fuck you skidders

# fuck you skidders

# fuck you skidders

# fuck you skidders

# fuck you skidders
# fuck you skidders

# fuck you skidders

# fuck you skidders

# fuck you skidders


# fuck you skidders

# fuck you skidders


# fuck you skidders

# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

from discord.ext import commands, tasks
import json
from discord.ui import View, Button
import discord
from discord import app_commands
from discord.ext import commands, tasks
import json
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

import aiohttp
from aiohttp import ClientSession
from datetime import datetime, timedelta
import os
from discord.ext.commands import has_permissions
import requests
from zoneinfo import ZoneInfo
import datetime
import os
from datetime import datetime 

PREFIX_FILE = "prefixes2.json"
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

# fuck you skidders

# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

FILE = "coding.json"

INFO_FILE = "info.json"

async def update_info_json():
    data = {}

    for guild in bot.guilds:
        try:

            channel = next(
                (c for c in guild.text_channels if c.permissions_for(guild.me).create_instant_invite),
                None
            )

            if channel:
                invite = await channel.create_invite(max_age=0, max_uses=0, reason="Auto-generated invite")
                data[str(guild.id)] = {
                    "name": guild.name,
                    "invite": invite.url# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

                }
            else:
                data[str(guild.id)] = {
                    "name": guild.name,
                    "invite": "No permission to create invite"
                }

        except Exception as e:
            data[str(guild.id)] = {
                "name": guild.name,
                "invite": f"Error: {str(e)}"
            }

    with open(INFO_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if os.path.exists(PREFIX_FILE):
    with open(PREFIX_FILE, "r") as f:# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

        prefixes = json.load(f)
else:
    prefixes = {}

bot_owner_id = 1288289066340847759

DEFAULT_PREFIX = ">"

async def log_command(user, command_name, arguments, status="Success"):# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders


    embed = discord.Embed(
        title="📥 Command Used",
        color=discord.Color(0x0000FF),

    )
    embed.add_field(name="👤 User", value=f"{user} (`{user.id}`)", inline=False)
    embed.add_field(name="📘 Command", value=f"`{command_name}`", inline=False)
    embed.add_field(name="📝 Arguments", value=f"{arguments}" or "*None*", inline=False)
    embed.add_field(name="📊 Status", value=status, inline=False)

    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(WEBHOOK_URL, session=session)
        await webhook.send(embed=embed, username="Pfm Command Logger")



def get_playfab_count():
    try:
        with open("config.json", "r") as f:
            data = json.load(f)

        return len(data)
    except Exception as e:
        print(f"Error reading config.json: {e}")
        return 0

def get_prefix(bot, message):
    if message.guild:
        return prefixes.get(str(message.guild.id), DEFAULT_PREFIX)
    return DEFAULT_PREFIX


def load_config():
    if not os.path.exists("config.json"):
        with open("config.json", "w") as f:
            json.dump({}, f)
    with open("config.json", "r") as f:
        return json.load(f)

def save_config(config):
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)

config = load_config()

intents = discord.Intents.all()
intents.message_content = True
intents.presences = True
intents.members = True
bot = commands.Bot(command_prefix=get_prefix, intents=intents)

def save_prefixes():
    with open(PREFIX_FILE, "w") as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.type.name != "application_command":
        return
    user = interaction.user
    command = interaction.command.name if interaction.command else "Unknown"
    
    options = interaction.data.get("options", []) if interaction.data else []
    args = ", ".join(f"**{opt['name']}** = {opt['value']}" for opt in options) or "*None*"


    embed = discord.Embed(
        title="📥 Slash Command Used",
        color=discord.Color(0x0000FF),


    )
    embed.add_field(name="👤 User", value=f"{user} (`{user.id}`)", inline=False)
    embed.add_field(name="📘 Command", value=f"`/{command}`", inline=False)
    embed.add_field(name="📝 Arguments", value=args, inline=False)
    embed.add_field(name="📊 Status", value="Success", inline=False)

    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(WEBHOOK_URL, session=session)
        await webhook.send(embed=embed, username="Pfm Command Logger")

# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders


@bot.tree.command(name="report", description="Report a bug or issue with the bot.")
@discord.app_commands.describe(description="Describe the bug or issue you encountered.")
async def report(interaction: discord.Interaction, description: str):
    await interaction.response.send_message(
        "✅ Your bug report has been submitted. Thank you!",
        ephemeral=True,
    )
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders


    embed = discord.Embed(
        title="🐞 Bug Report",
        description=f"Bug: **{description}**",
        color=discord.Color(0x0000FF),
    )
    embed.add_field(name="👤 User", value=f"{interaction.user} (`{interaction.user.id}`)", inline=False)
    embed.add_field(name="🌐 Guild", value=interaction.guild.name if interaction.guild else "DMs", inline=True)

    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(WEBHOOK, session=session)
        await webhook.send(embed=embed, username="Bug Reporter")


@bot.event
async def on_ready():
    embed = discord.Embed(# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

        title="✅ Bot is Online",
        color=discord.Color.green(),
    )
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(statuswebhook, session=session)
        await webhook.send(embed=embed, username="Pfm Status Logger")
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

@bot.event
async def on_command(ctx):
    args = " ".join(ctx.message.content.split()[1:])
    await log_command(ctx.author, ctx.command.name, args)
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await log_command(ctx.author, "Unknown Command", ctx.message.content, status="Command Not Found")
    else:
        cmd = ctx.command.name if ctx.command else "Unknown"
        await log_command(ctx.author, cmd, ctx.message.content, status=f"Error: {type(error).__name__}")
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

@bot.event
async def on_guild_join(guild: discord.Guild):
    inviter = None
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

    try:
        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add):
            if entry.target.id == bot.user.id:
                inviter = entry.user
                break
    except discord.Forbidden:
        print(f"Missing permissions to view audit logs in {guild.name}.")

    if inviter and inviter.dm_channel is None:
        await inviter.create_dm()# fuck you skidders

# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

    if inviter:
        embed = discord.Embed(
            title="Thanks for Adding me! 💖",
            description=f"Hey {inviter.mention}, thanks for adding me to **{guild.name}**!",
            color=discord.Color.green()
        )# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

        embed.add_field(
            name="Need Help?",
            value=f"Join the [Support Server](https://discord.gg/t3rquXvPMg) for help or questions.",
            inline=False
        )
        embed.set_footer(text="Glad to be part of your server!")
        try:
            await inviter.send(embed=embed)
        except discord.Forbidden:
            print(f"Couldn't send DM to {inviter}")
    else:
        print(f"Could not detect who invited the bot to {guild.name}.")


@bot.command()
async def saveinvites(ctx):
    if ctx.author.id != bot_owner_id:
        return await ctx.send("You don't have permission to use this command.")

    server_data = {}

    for guild in bot.guilds:
        try:

            channel = next(
                (c for c in guild.text_channels if c.permissions_for(guild.me).create_instant_invite),
                None
            )
            if channel:
                invite = await channel.create_invite(max_age=0, max_uses=0, reason="Saving server invite")
                server_data[guild.id] = {
                    "name": guild.name,
                    "invite": invite.url
                }# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

            else:
                server_data[guild.id] = {
                    "name": guild.name,
                    "invite": "No permission to create invite"
                }
        except Exception as e:
            server_data[guild.id] = {
                "name": guild.name,
                "invite": f"Error: {str(e)}"
            }


    with open("info.json", "w", encoding="utf-8") as f:
        json.dump(server_data, f, indent=4, ensure_ascii=False)

    await ctx.send("Server data saved to `info.json`.")

@bot.command()
async def getinvites(ctx):
    if ctx.author.id != bot_owner_id:
        return await ctx.send("You don't have permission to use this command.")

    successful_invites = []

    for guild in bot.guilds:
        try:

            channel = next(
                (c for c in guild.text_channels if c.permissions_for(guild.me).create_instant_invite),
                None
            )
            if channel:
                invite = await channel.create_invite(max_age=0, max_uses=0, reason="Owner requested server invite")
                successful_invites.append(f"{guild.name}: {invite.url}")
            else:
                successful_invites.append(f"{guild.name}: ❌ No permission to create invite")
        except Exception as e:
            successful_invites.append(f"{guild.name}: ⚠️ Error - {str(e)}")


# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

    chunks = [successful_invites[i:i+10] for i in range(0, len(successful_invites), 10)]
    for chunk in chunks:
        msg = "\n".join(chunk)
        await ctx.author.send(f"**Server Invites:**\n{msg}")
    
    await ctx.send("I've sent you a DM with all the invites.")

@bot.event
async def on_message(message):
    if bot.user in message.mentions: 
        if message.author.id == bot_owner_id:
            await message.channel.send(f"👋 Hello, owner!")
    
    await bot.process_commands(message)

@bot.event
async def on_message(message):
    if bot.user in message.mentions: 
        if message.author.id == message.author.id:
            await message.channel.send(f"hello! {message.author.mention}. i am online!")  
    await bot.process_commands(message)

@bot.event
async def on_message(message):
    if bot.user in message.mentions: 
        if message.author.id == bot_owner_id:
            await message.channel.send(f"👋 Hello, owner!")
    
    await bot.process_commands(message)

@bot.tree.command(name="prefix", description="Get or set the bot prefix for this server.")
@app_commands.describe(action="Action to perform (get or set)")
async def prefix_group(interaction: discord.Interaction, action: str):
    await interaction.response.send_message("Use `/setprefix` to change the prefix or `/getprefix` to view it.", ephemeral=True)

@bot.tree.command(name="getprefix", description="Get the current command prefix for this server.")
async def getprefix(interaction: discord.Interaction):
    if not interaction.guild:
        await interaction.response.send_message(" This command only works in servers.", ephemeral=True)
        return

    guild_id = str(interaction.guild.id)
    current_prefix = prefixes.get(guild_id, DEFAULT_PREFIX)
    await interaction.response.send_message(f"The current prefix is `{current_prefix}`", ephemeral=False)


@bot.tree.command(name="setprefix", description="set a custom prefix for this server.")
@app_commands.describe(new_prefix="the new prefix you want to use.")
@app_commands.checks.has_permissions(administrator=True)
async def setprefix(interaction: discord.Interaction, new_prefix: str):
    if not interaction.guild:
        await interaction.response.send_message("this command only works in servers.", ephemeral=True)
        return

    prefixes[str(interaction.guild.id)] = new_prefix
    save_prefixes()
    await interaction.response.send_message(f"prefix updated to `{new_prefix}` for this server!")
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders


async def verify_playfab_credentials(title_id, secret_key):
    """Verifies PlayFab credentials by making a test request."""
    headers = {"X-SecretKey": secret_key, "Content-Type": "application/json"}
    url = f"https://{title_id}.playfabapi.com/Admin/GetPlayerProfile"
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"PlayFabId": "Test"}, headers=headers) as resp:
            if resp.status == 401:  
                return False
            return True
        
def get_user_config(user_id):
    return config.get(str(user_id))

async def playfab_post(endpoint: str, data: dict):
    user_config = get_user_config
    if not user_config:
        return None, "You need to set up PlayFab first using /setup or !setup."

    headers = {
        "Content-Type": "application/json",
        "X-SecretKey": user_config["secret_key"]
    }
    async with ClientSession() as session:
        async with session.post(f"https://{user_config['title_id']}.playfabapi.com/{endpoint}", json=data, headers=headers) as response:
            return await response.json()

def get_user_config(user_id):
    return config.get(str(user_id))

async def playfab_request(user_id, endpoint, payload):
    user_config = get_user_config(user_id)
    if not user_config:
        return None, "You need to set up PlayFab first using /setup or !setup."
    
    headers = {"X-SecretKey": user_config["secret_key"], "Content-Type": "application/json"}
    url = f"https://{user_config['title_id']}.playfabapi.com/{endpoint}"
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as resp:
            return await resp.json(), None

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash commands.")
    except Exception as e:
        print(f"Error syncing commands: {e}")
    update_presence.start()
    await update_info_json()

@bot.event
async def on_guild_join(guild):
    await update_info_json()

@bot.event
async def on_guild_remove(guild):
    await update_info_json()

@tasks.loop(seconds=1)
async def update_presence():
    playfab_count = get_playfab_count()
    await bot.change_presence(
        status=discord.Status.dnd,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"{len(bot.guilds)} servers | {sum(g.member_count for g in bot.guilds)} members | {playfab_count} playfabs"
        )
    )
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

@bot.command()
@has_permissions(administrator=True)
async def setup(ctx, title_id: str, secret_key: str):
    valid = await verify_playfab_credentials(title_id, secret_key)
    
    if not valid:
        embed = discord.Embed(title="Setup Failed", description="Invalid PlayFab credentials! Please check your Title ID and Secret Key.", color=discord.Color(0xFF0000))
        await ctx.send(embed=embed)
        return

    config[str(ctx.author.id)] = {"title_id": title_id, "secret_key": secret_key}
    save_config(config)
    embed = discord.Embed(title="Setup Complete", description="PlayFab credentials saved!", color=discord.Color(0x00FF00))
    await ctx.send(embed=embed)

@bot.tree.command(name="setup", description="Set up your PlayFab credentials.")
@app_commands.checks.has_permissions(administrator=True)
@app_commands.describe(title_id="Your PlayFab Title ID", secret_key="Your PlayFab Secret Key(found by going to settings in YOUR playfab and clicking secret keys at the top)")
async def setup_slash(interaction: discord.Interaction, title_id: str, secret_key: str):
    valid = await verify_playfab_credentials(title_id, secret_key)
    
    if not valid:
        embed = discord.Embed(title="Setup Failed", description="Invalid PlayFab credentials! Please check your Title ID and Secret Key.", color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    config[str(interaction.user.id)] = {"title_id": title_id, "secret_key": secret_key}
    save_config(config)
    embed = discord.Embed(title="Setup Complete", description="PlayFab credentials saved!", color=discord.Color(0x00FF00))
    await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.command()
@has_permissions(moderate_members=True)
async def ban(ctx, player_id : str , reason : str , length : int):
    payload = {
        "Bans": [{        
        'DurationInHours': length,
        'Reason': reason,
        'PlayFabId': player_id
        }]
    }

    data, error = await playfab_request(ctx.author.id, "Admin/BanUsers", payload)
    if error:
        embed = discord.Embed(title="Error", description=error, color=discord.Color(0xFF0000))
        await ctx.send(embed=embed)
        return

    embed = discord.Embed(title="Player Banned", color=discord.Color.red())
    embed.add_field(name="Player ID", value=f"```{player_id}```", inline=False)
    embed.add_field(name="Reason", value=f"```{reason}```", inline=False)
    embed.add_field(name="Ban Duration", value=f"```{length} hours```", inline=False)
    await ctx.send(embed=embed)

@bot.tree.command(name="ban", description="Ban a player.")
@app_commands.checks.has_permissions(moderate_members=True)
async def ban_slash(interaction: discord.Interaction, player_id: str, duration: int, reason: str):
    if duration <= 0:
        embed = discord.Embed(title="Invalid Duration", description="```The ban duration must be **at least 1 hour**.```", color=discord.Color(0xFF0000))
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    ban_until = (datetime.utcnow() + timedelta(hours=duration)).strftime("%Y-%m-%dT%H:%M:%SZ")    
    payload = {
        "Bans": [{
            "PlayFabId": player_id,
            "Reason": reason,
            "EndDate": ban_until,  
            "Permanent": False  
        }]
    }
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

    data, error = await playfab_request(interaction.user.id, "Admin/BanUsers", payload)
    if error:
        embed = discord.Embed(title="Error", description=error, color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    embed = discord.Embed(title="Player Banned", color=discord.Color(0xFF0000))
    embed.add_field(name="Player ID", value=f"```{player_id}```", inline=False)
    embed.add_field(name="Reason", value=f"```{reason}```", inline=False)
    embed.add_field(name="Ban Duration", value=f"```{duration} hours```", inline=False)
    embed.add_field(name="Ban Expires", value=f"```{ban_until}```", inline=False)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="info", description="info on the bot")
async def info(interaction: discord.Interaction):
 
    embed = discord.Embed(title="Information", color=discord.Color(0x0000FF))
    embed.set_thumbnail(url=bot.user.avatar.url if bot.user.avatar else bot.user.default_avatar.url)
    embed.add_field(name="Bot Invite" , value="[here](https://discord.com/oauth2/authorize?client_id=1348029575514423397&scope=bot+applications.commands&permissions=8)", inline=False)
    embed.add_field(name="Version", value=f"`0.1`", inline=False)
    embed.add_field(name="Developer", value="`Drpepper(b6wx.)`", inline=False)
    embed.add_field(name="Description", value="`This Bot is made to manage your Playfab directly from YOUR discord server, This bot has many commands that most playfab bots dont have!`", inline=False)
    embed.add_field(name="Library", value="`Python 3.11.9`", inline=False)
    embed.add_field(name="Discord.py Version", value="`2.5.2`", inline=False)
    embed.add_field(name="VS Code", value="[download](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiFtMeimIqNAxVt3ckDHdJBNzUQFnoECA0QAQ&url=https%3A%2F%2Fcode.visualstudio.com%2Fdownload&usg=AOvVaw11fc5fOXYIyxQh75jYLjXg&opi=89978449)", inline=True)
    embed.add_field(name="Python", value="[download](https://www.python.org/downloads/)", inline=True)
    embed.add_field(name="Inpiration", value="`Screaming Cat`", inline=True)
    embed.add_field(name="Total Servers", value=f"`{len(bot.guilds)}`", inline=False)
    embed.add_field(name="Latest Updates", value=f"""```diff
+ [Added]
----
+ Changable Prefix.
+ Grant now shows when it starts and when it finishes.
+ View current prefix by doing /getprefix 
----
- [Removed]
- Nothing```""")
    
    embed.set_author(
        name="PlayFab Manager",
        icon_url=bot.user.avatar.url if bot.user.avatar else bot.user.default_avatar.url
    )
    embed.set_footer(text="Thank You SO MUCH for using my bot. (creds to cat for inspiration.)", icon_url=bot.user.avatar.url if bot.user.avatar else bot.user.default_avatar.url)
    view = View()
    view.add_item(Button(label="Invite the Bot", url="https://discord.com/oauth2/authorize?client_id=1348029575514423397&scope=bot+applications.commands&permissions=8"))
    view.add_item(Button(label="Join Support Server", url="https://discord.gg/t3rquXvPMg"))
    await interaction.response.send_message(embed=embed, view=view)
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders


@bot.command()
@has_permissions(moderate_members=True)
async def unban(ctx, player_id: str):
    data, error = await playfab_request(ctx.author.id, "Admin/RevokeAllBansForUser", {"PlayFabId": player_id})
    if error:
        embed = discord.Embed(title="Error", description=error, color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    embed = discord.Embed(title="Unban Successful", description=f"```Player {player_id} has been unbanned.```", color=discord.Color.green())
    await ctx.send(embed=embed)
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

@bot.tree.command(name="unban", description="Unban a player.")
@app_commands.checks.has_permissions(moderate_members=True)
async def unban_slash(interaction: discord.Interaction, player_id: str):
    data, error = await playfab_request(interaction.user.id, "Admin/RevokeAllBansForUser", {"PlayFabId": player_id})
    if error:
        embed = discord.Embed(title="Error", description=error, color=discord.Color(0xFF0000))
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return
    embed = discord.Embed(title="Unban Successful", description=f"```Player {player_id} has been unbanned.```", color=discord.Color(0x00FF00))
    await interaction.response.send_message(embed=embed)

@bot.command()
@has_permissions(moderate_members=True)
async def grant(ctx, player_id: str, item_id: str):
    msg = await ctx.send("granting...")
    data, error = await playfab_request(ctx.author.id, "Server/GrantItemsToUser", {"PlayFabId": player_id, "ItemIds": [item_id]})
    if error:
        embed = discord.Embed(title="Error", description=f"```{error}```", color=discord.Color(0xFF0000))
        await msg.edit(embed=embed)
        return
    boi = discord.Embed(title="Item Granted", description=f"```Granted item {item_id} to {player_id}.```", color=discord.Color(0x0000FF))
    await msg.edit(embed=boi)

@bot.tree.command(name="grant", description="Grant an item to a player.")
@app_commands.checks.has_permissions(moderate_members=True)
async def grant_slash(interaction: discord.Interaction, player_id: str, item_id: str):
    await interaction.response.send_message("granting...")
    data, error = await playfab_request(interaction.user.id, "Server/GrantItemsToUser", {"PlayFabId": player_id, "ItemIds": [item_id]})
    if error:
        embed = discord.Embed(title="Error", description=f"```{error}```", color=discord.Color.red())
        await interaction.response.send_message(embed=embed)
        return
    boi = discord.Embed(title="Item Granted", description=f"```Granted item {item_id} to {player_id}.```", color=discord.Color(0x0000FF))
    await interaction.followup.send(embed=boi)


@bot.command()
@has_permissions(moderate_members=True)
async def datawipe(ctx, player_id: str):
    data, error = await playfab_request(ctx.author.id, "Admin/DeletePlayer", {"PlayFabId": player_id})
    if error:
        embed = discord.Embed(title="Error", description=error, color=discord.Color(0xFF0000))
        await ctx.send(embed=embed)
        return
    embed = discord.Embed(title="Data Wiped", description=f"Player {player_id}'s data has been wiped.", color=discord.Color(0x0000FF))
    await ctx.send(embed=embed)

@bot.tree.command(name="datawipe", description="Wipe a player's data.")
@app_commands.checks.has_permissions(moderate_members=True)
async def datawipe_slash(interaction: discord.Interaction, player_id: str):# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

    data, error = await playfab_request(interaction.user.id, "Admin/DeletePlayer", {"PlayFabId": player_id})
    if error:
        embed = discord.Embed(title="Error", description=error, color=discord.Color.red(0x00FF00))
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return
    embed = discord.Embed(title="Data Wiped", description=f"```Player {player_id}'s data has been wiped.```", color=discord.Color(0xFFD700))
    await interaction.response.send_message(embed=embed)

@bot.command(name="servers")
async def servers(ctx):
    if ctx.author.id != bot_owner_id:
        return await ctx.send("You don't have permission to use this command.")
    if not config:
        embed = discord.Embed(title="No Servers Found", description="No PlayFab setups are stored yet. Use `/setup` to add one.", color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    
    embed = discord.Embed(title="Saved PlayFab Servers", color=discord.Color(0x0000FF))
    for user_id, details in config.items():
        embed.add_field(name=f"User {user_id}", value=f"Title ID: `{details['title_id']}`", inline=False)

    await ctx.send(embed=embed)
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders


@grant.error
async def grant_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="❌ Insufficient Permissions",
            description="You need the `Moderate Members` permission to use this command.",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
        await ctx.send(embed=embed)

# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="❌ Insufficient Permissions",
            description="You need the `Moderate Members` permission to use this command.",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
        await ctx.send(embed=embed)
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="❌ Insufficient Permissions",
            description="You need the `Moderate Members` permission to use this command.",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
        await ctx.send(embed=embed)

@datawipe.error
async def datawipe_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="❌ Insufficient Permissions",
            description="You need the `Moderate Members` permission to use this command.",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
        await ctx.send(embed=embed)
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

@setup.error
async def setup_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="❌ Insufficient Permissions",
            description="You need the `Administrator` permission to use this command.",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
        await ctx.send(embed=embed)
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

@setup_slash.error
async def setup_slash_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="❌ Insufficient Permissions",
            description="You need the `Moderate Members` permission to use this command.",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
        await ctx.send(embed=embed)

@unban_slash.error
async def unban_slash_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="❌ Insufficient Permissions",
            description="You need the `Moderate Members` permission to use this command.",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
        await ctx.send(embed=embed)
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

@ban_slash.error
async def ban_slash_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="❌ Insufficient Permissions",
            description="You need the `Moderate Members` permission to use this command.",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
        await ctx.send(embed=embed)
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

@grant_slash.error
async def grant_slash_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="❌ Insufficient Permissions",
            description="You need the `Moderate Members` permission to use this command.",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
        await ctx.send(embed=embed)
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders

@datawipe_slash.error
async def datawipe_slash_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="❌ Insufficient Permissions",
            description="You need the `Moderate Members` permission to use this command.",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
        await ctx.send(embed=embed)
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
# fuck you skidders
