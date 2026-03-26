import asyncio
from DiscordRPCT.bcolors import Bcolors as col
from win11toast import toast_async
import contextlib
from pathlib import Path

class Functs:
    @staticmethod
    def manpage1(mainexecutable: str, message: str=None):
        msg = f""
        try:
            {'None':''}[str(message)]
        except KeyError:
            msg += f"\n\n{col.WHITE}[{col.RED}!{col.WHITE}] {message}"
        helppage1 = f"""{col.TAG}{col.BOLD}╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗
║          🎫     {col.BOLD}Rich Presence Tool     🎫           ║
║ {col.WHITE}Setting A Rich PresenCe on your profile, simplified {col.TAG}║
║                                                     ║
║ {col.RED}Not affiliated with {col.BLURPLE}Discord Inc. {col.RED}in any way         {col.TAG}║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝{col.ENDC}{msg}{col.ENDC}

Usage: python3 RPC_Launcher.py [options]

OPTION          DESCRIPTION
--no-clear      Don't clear the terminal when ran with this option.
-h              Views this page.
-s              No checks, no prompts, just run. Useful for running this as a service in the background.
{col.ENDC}"""
        print(helppage1)

async def dummy(args):
    option = args.get("user_input").get("selection")
    print(option)

async def launch_notification():
    async def coroutin():
        icon = {
            'src': Path('DiscordRPCT/icon.png').absolute().as_uri(),
            'placement': 'appLogoOverride'
        }
        i = await toast_async(
            "Running in the system tray", 
            "Head over to the system tray to interact with Discord Rich Presence Tool",
            app_id='Discord Rich Presence', 
            icon=icon, 
            on_click=dummy,
            duration=None,
        )
        return i
    result = asyncio.create_task(coroutin())
    return result