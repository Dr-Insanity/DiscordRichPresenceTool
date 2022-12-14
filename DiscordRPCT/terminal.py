from DiscordRPCT.bcolors import Bcolors as col
from time import sleep
from os import system
from platform import system as system_
from typing import Union
from sys import argv

win = 'Windows'
lin = 'Linux'
mac = 'Darwin'

class Options:

    @property
    def AvailableOptions(self):
        return [
            "-h",
            "--no-clear",
            "-s"
        ]
def parseSubFeatures(subfeatures: Union[str, tuple[str]]):
    prefixed_features = f""
    if isinstance(subfeatures, tuple):
        for subfeature in subfeatures:
            prefixed_features += subfeature
    elif isinstance(subfeatures, str):
        prefixed_features += subfeatures
    elif subfeatures is None:
        return ""
    return prefixed_features

class Subfeatures():
    @property
    def DEBUG(self):
        return f"{col.TAG}{col.BOLD}[{col.GRAY}DEBUG{col.TAG}]"
    @property
    def TEST(self):
        return f"{col.TAG}{col.BOLD}[{col.YELLOW}TEST{col.TAG}]"
    @property
    def AAAA(self):
        return f"{col.TAG}{col.BOLD}[{col.GREEN}AAAA{col.TAG}]"
    @property
    def BBBB(self):
        return f"{col.TAG}{col.BOLD}[{col.BLUE}BBBB{col.TAG}]"
    @property
    def SETUP(self):
        return f"{col.TAG}{col.BOLD}[{col.RED}CCCC{col.TAG}]"

class Terminal:

    def platCheck():
        if system_() == lin:
            return lin

        elif system_() == mac:
            return mac

        elif system_() == win:
                return win

    def clear():
        if "--no-clear" in argv: return
        def winClear():
            system("cls")
        def linClear():
            system("clear")
        def macClear():
            system("clear")

        doClear = {
            win:winClear,
            lin:linClear,
            mac:macClear
        }

        try:
            doClear[system_()]()
        except KeyError:
            print(f"""{col.RED}╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
║ ❌ {col.WHITE}Cannot detect your platform{col.RED} ❌ ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
{col.WHITE}We need to know what your OS is to know how to clear the terminal.\n{col.BOLD}{col.RED}Sorry! {col.DRED}Exiting!{col.ENDC}""")

    def announce(text: str, subfeatures: Union[str, tuple]=None):
        print(f"{col.TAG}{col.BOLD}[{col.WHITE}Rich Presence{col.TAG}]{parseSubFeatures(subfeatures)} {col.WHITE}{col.UNBOLD}{text}")

    def prompt(question: str, answer_required=True, subfeatures: Union[str, tuple[str]]=None, allowed_replies: tuple[str]=None) -> Union[str, None]:
        try:
            reply = input(f"{col.TAG}{col.BOLD}[{col.WHITE}Rich Presence{col.TAG}]{parseSubFeatures(subfeatures)} {col.WHITE}{col.UNBOLD}{question}")
            if reply.lower() in allowed_replies:
                return reply
            else:
                Terminal.clear()
                print(f"""{col.RED}╔═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
║ ❌    {col.WHITE}Invalid reply{col.RED}    ❌ ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
{col.WHITE}Your choices are:""")
                for option in allowed_replies:
                    print(f"- {col.WHITE}{option}")
                sleep(2)
                Terminal.clear()
                reply = Terminal.prompt(question, answer_required, subfeatures, allowed_replies)
                return reply

        except KeyboardInterrupt:
            if answer_required:
                Terminal.clear()
                print(f"{col.TAG}{col.BOLD}[{col.WHITE}Rich Presence{col.TAG}]{parseSubFeatures(subfeatures)} {col.WHITE}{col.UNBOLD}"+question+f"❌    {col.WHITE}Answer {col.RED}required    ❌")
                sleep(2)
                Terminal.clear()
                reply = Terminal.prompt(question, answer_required, subfeatures, allowed_replies)
                return reply
            print(f"{col.GRAY}\nCancelled\n")
            return None