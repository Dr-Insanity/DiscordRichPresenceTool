from DiscordRPCT.bcolors import Bcolors as col

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