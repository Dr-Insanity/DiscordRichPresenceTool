from DiscordRPCT.bcolors import Bcolors as col
from DiscordRPCT.terminal import Terminal
from os import system as command
class Checks:
    def check_pypresence():
        try:
            Terminal.announce("Checking if further dependencies are installed...")
            Terminal.announce("attempting to use pypresence")
            from pypresence import Presence
            from pypresence import exceptions
            Terminal.announce(f"""pypresence was already {col.OKGREEN}{col.BOLD}INSTALLED!
{col.WHITE}{col.UNBOLD}dependency checks {col.OKGREEN}{col.BOLD}Done!""")
            input("Hit enter to continue... ")

        except ImportError:
            Terminal.announce(f"pypresence {col.RED}{col.BOLD}NOT INSTALLED!\n{col.WHITE}{col.UNBOLD}Attempting to install it for you...")
            print("                                                  ")
            print("=================BEGIN OF INSTALL=================")
            command("pip install pypresence")
            print("==================END OF INSTALL==================")
            print("                                                  ")
            Terminal.announce(f"pypresence {col.OKGREEN}{col.BOLD}INSTALLED!\n{col.WHITE}{col.UNBOLD}dependency checks {col.OKGREEN}{col.BOLD}Done!")
            input("Hit enter to continue... ")

    def check_psutil():
        Terminal.announce("attempting to use psutil")
        try: # try to import psutil, for checking if Discord is running, or not.
            import psutil
            Terminal.announce(f"psutil was already {col.OKGREEN}{col.BOLD}INSTALLED!\n{col.WHITE}{col.UNBOLD}commencing other dependency checks...")
            input("Hit enter to continue... ")

        except ImportError:
            Terminal.announce(f"psutil {col.RED}{col.BOLD}NOT INSTALLED!\n{col.WHITE}{col.UNBOLD}Attempting to install it for you...")
            print("=================BEGIN OF INSTALL=================")
            command("pip install psutil")
            print("==================END OF INSTALL==================")
            Terminal.announce(f"psutil {col.OKGREEN}{col.BOLD}INSTALLED!\n{col.WHITE}{col.UNBOLD}commencing other dependency checks...")
            input("Hit enter to continue... ")
    
    def dependency_checker():
        Terminal.clear()
        Terminal.announce("Checking if further dependencies are installed...")
        Checks.check_psutil()
        Checks.check_pypresence()