from os import getcwd, getenv
from os.path import basename
from sys import argv, exit
import time
from configparser import ConfigParser, DuplicateSectionError
from DiscordRPCT.terminal import Terminal, Options
from DiscordRPCT.checks import Checks
from DiscordRPCT.bcolors import Bcolors as col
from DiscordRPCT.functs import Functs

ranAs_Service = False
appdata_folder = getenv('APPDATA')
RCP_Config_dot_ini = f"{appdata_folder}/Discord-Rich-Presence-Tool/RPC_Config.ini"

def prepArgs():
    if len(argv) == 1:
        return
    opts = Options()
    gaveNonExistentOpt = False
    invalid_arg = None
    Func = Functs()
    for arg in argv:
        if basename(arg).endswith("py") or basename(arg).endswith("exe"):
            continue
        elif arg not in opts.AvailableOptions:
            invalid_arg = arg
            gaveNonExistentOpt = True
            break
    if gaveNonExistentOpt:
        Func.manpage1(mainexecutable=basename(__file__), message=f"{col.RED}Option '{invalid_arg}' doesn't exist!{col.ENDC}")
        exit(2)
    if '-h' in argv:
        Func.manpage1(mainexecutable=basename(__file__), message=None)
        exit(0)
    if '-s' in argv:
        global ranAs_Service
        ranAs_Service = True

prepArgs()
OpSystem = Terminal.platCheck()
clear = Terminal.clear
dependency_checker = Checks.dependency_checker

def prompt_need_MSVC14orHigher():
    if ranAs_Service:
        return
    clear()
    print(f"""
{col.TAG}{col.BOLD}
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗
║                  🎫     {col.BOLD}Rich Presence Tool     🎫                 ║
║{col.RED} THIS PROGRAM NEEDS MICROSOFT VISUAL BUILD TOOLS 14.0 OR HIGHER!!! {col.TAG}║
║{col.WHITE}                You can get it with the below link  {col.TAG}               ║
║{col.OKGREEN}   https://www.scivision.dev/python-windows-visual-c-14-required/ {col.TAG} ║
║{col.WHITE}{col.UNBOLD}              Report broken links please! Thank you.               {col.TAG}║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝

{col.TAG}{col.BOLD}[{col.WHITE}Rich Presence{col.TAG}] {col.WHITE}{col.UNBOLD}Discord Rich Presence Tool will continue to run, assuming you have this dependency installed
        
{col.TAG}{col.BOLD}[{col.WHITE}Rich Presence{col.TAG}] {col.WHITE}{col.UNBOLD}You can disable this notice in the settings, which will be stored at:

{col.WHITE}{col.BOLD}{RCP_Config_dot_ini}""")

    confirm_understanding = input(f"\n{col.YELLOW}I understand I {col.RED}NEED {col.YELLOW}this {col.RED}dependency {col.YELLOW}installed and I know how to install this (Y/N)> ")

    if confirm_understanding.lower() == "y":
        dependency_checker()

    elif confirm_understanding.lower() == "n":
        print(f"{col.TAG}{col.BOLD}[{col.WHITE}Rich Presence{col.TAG}] {col.WHITE} Quitting application - Install {col.RED}MICROSOFT VISUAL BUILD TOOLS 14.0 OR HIGHER!!!{col.WHITE}")
        exit()

prompt_need_MSVC14orHigher()

import psutil
from pypresence import Presence
from pypresence import exceptions

config = ConfigParser()
apptag = f"{col.TAG}{col.BOLD}[{col.WHITE}Rich Presence{col.TAG}] {col.WHITE}{col.UNBOLD}"

def toomanyCharacters():
    clear()
    print(
"""
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
║ ❌ Too many characters ❌ ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
""")

def ASK_app_id():
    clear()
    RPC_application_id = input(f"{col.TAG}{col.BOLD}[{col.WHITE}Rich Presence{col.TAG}][{col.OKGREEN}setup{col.TAG}] {col.UNBOLD}{col.WHITE}Application ID (found at https://discord.com/developers, create your app on the panel)> {col.OKGREEN}{col.BOLD}")
    return RPC_application_id

def ASK_RPC_title():
    clear()
    RPC_title = input(f"{col.TAG}{col.BOLD}[{col.WHITE}Rich Presence{col.TAG}][{col.OKGREEN}setup{col.TAG}] {col.UNBOLD}{col.WHITE}Title of your rich presence?> {col.OKGREEN}{col.BOLD}")
    return RPC_title

def ASK_RPC_desc():
    clear()
    RPC_desc = input(f"{col.TAG}{col.BOLD}[{col.WHITE}Rich Presence{col.TAG}][{col.OKGREEN}setup{col.TAG}] {col.UNBOLD}{col.WHITE}Description of your rich presence?> {col.OKGREEN}{col.BOLD}")
    return RPC_desc

def ASK_RPC_WantButtons():
    RPC_Buttons = input(f"{col.TAG}{col.BOLD}[{col.WHITE}Rich Presence{col.TAG}][{col.OKGREEN}setup{col.TAG}] {col.UNBOLD}{col.WHITE}Do you want buttons on your rich presence? (Y/N)> {col.OKGREEN}{col.BOLD}")
    if RPC_Buttons.lower() == "y":
        return "y"
    elif RPC_Buttons.lower() == "n":
        return "n"
    else:
        clear()
        print(
f"""{col.RED}
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
║ ❌    {col.WHITE}Invalid reply{col.RED}    ❌ ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
{col.WHITE}Your choices are:
- {col.WHITE}({col.OKGREEN}y{col.WHITE})es - Set up buttons for my rich presence.
- {col.WHITE}({col.RED}n{col.WHITE})o - Do not set up buttons on my rich presence.""")
        ASK_RPC_WantButtons()
def ASK_RPC_NumbOfButtons():
    RPC_Buttons_HowMany = input(f"{col.TAG}{col.BOLD}[{col.WHITE}Rich Presence{col.TAG}][{col.OKGREEN}setup{col.TAG}] {col.UNBOLD}{col.WHITE}How many buttons do you want on your rich presence? (1-2, choose one)>  {col.OKGREEN}{col.BOLD}")
    if str(RPC_Buttons_HowMany) == '1':
        return "1"
    elif str(RPC_Buttons_HowMany) == '2':
        return "2"
    else:
        clear()
        print(
f"""{col.RED}
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
║ ❌    {col.WHITE}Invalid reply{col.RED}    ❌ ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
{col.WHITE}Your choices are:
- 1 - Set up 1 button.
- 2 - Set up 2 buttons.
            """)
        time.sleep(3)
        clear()
        ASK_RPC_NumbOfButtons()

def ask_rpc_1stbutton_label(rpc__how_many_buttons: str):
    rpc__how_many_buttons = rpc__how_many_buttons
    RPC_Single_Button_LabelText = str()
    if str(rpc__how_many_buttons) == "1":
        RPC_Single_Button_LabelText = input(f"{col.TAG}{col.BOLD}[{col.WHITE}Rich Presence{col.TAG}][{col.OKGREEN}setup{col.TAG}]{col.TAG}[{col.WHITE}1/1 button{col.TAG}] {col.UNBOLD}{col.WHITE}Which text shall be displayed on your button? (type some text)>  {col.OKGREEN}{col.BOLD}")
    elif str(rpc__how_many_buttons) == "2":
        RPC_Single_Button_LabelText = input(f"{col.TAG}{col.BOLD}[{col.WHITE}Rich Presence{col.TAG}][{col.OKGREEN}setup{col.TAG}]{col.TAG}[{col.WHITE}1/2 button{col.TAG}] {col.UNBOLD}{col.WHITE}Which text shall be displayed on your button? (type some text)>  {col.OKGREEN}{col.BOLD}")
    if len(RPC_Single_Button_LabelText) <= 32:
        return RPC_Single_Button_LabelText
    elif len(RPC_Single_Button_LabelText) > 32:
        clear()
        print(
    f"""{col.RED}
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
║ ❌ {col.WHITE}Too many characters ❌ {col.RED}║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
    """)
        time.sleep(3)
        clear()
        ask_rpc_1stbutton_label(rpc__how_many_buttons)

def ask_rpc_1stbutton_URL(rpc__how_many_buttons):
    if str(rpc__how_many_buttons) == "1":
        RPC_Single_Button_LabelText = input(f"{col.TAG}{col.BOLD}[{col.WHITE}Rich Presence{col.TAG}][{col.OKGREEN}setup{col.TAG}]{col.TAG}[{col.WHITE}1/1 button{col.TAG}] {col.UNBOLD}{col.WHITE}Which URL shall be shared> {col.OKGREEN}{col.BOLD}")
        return RPC_Single_Button_LabelText
    elif str(rpc__how_many_buttons) == "2":
        RPC_Single_Button_LabelText = input(f"{col.TAG}{col.BOLD}[{col.WHITE}Rich Presence{col.TAG}][{col.OKGREEN}setup{col.TAG}]{col.TAG}[{col.WHITE}1/2 button{col.TAG}] {col.UNBOLD}{col.WHITE}Which URL shall be shared> {col.OKGREEN}{col.BOLD}")
        return RPC_Single_Button_LabelText

def ask_rpc_2ndbutton_label():
    RPC_Single_Button_LabelText = input(f"{col.TAG}{col.BOLD}[{col.WHITE}Rich Presence{col.TAG}][{col.OKGREEN}setup{col.TAG}]{col.TAG}[{col.WHITE}2/2 button{col.TAG}] {col.UNBOLD}{col.WHITE}Which text shall be displayed on your button? (type some text)> {col.OKGREEN}{col.BOLD}")
    if len(RPC_Single_Button_LabelText) <= 32:
        return RPC_Single_Button_LabelText
    elif len(RPC_Single_Button_LabelText) > 32:
        clear()
        print(
    F"""{col.RED}
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
║ ❌ {col.WHITE}Too many characters{col.RED} ❌ ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
    """)
        time.sleep(3)
        clear()
        ask_rpc_2ndbutton_label()


def ask_rpc_2ndbutton_URL():
    RPC_Single_Button_LabelText = input(f"{col.TAG}{col.BOLD}[{col.WHITE}Rich Presence{col.TAG}][{col.OKGREEN}setup{col.TAG}]{col.TAG}[{col.WHITE}2/2 button{col.TAG}] {col.UNBOLD}{col.WHITE}Which URL shall be shared> {col.OKGREEN}{col.BOLD}")
    return RPC_Single_Button_LabelText
def ASK_RPC_Buttons():

    """
    ╔═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
    ║ ❌    Invalid reply    ❌ ║
    ╚═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
    Your choices are:
    - 1 (1 button on your RPC)
    - 2 (2 buttons on your RPC, which is the max as well)"""
    RPC_Buttons = input(f"{col.YELLOW}[Rich Presence][setup] Do you want buttons on your rich presence? (Y/N)>")

    if RPC_Buttons.lower() == "n":
        return

    config.read(RCP_Config_dot_ini)

    with open(RCP_Config_dot_ini, 'w') as f:
        config.write(f)

def CompileConfig():
    print(f"""{col.TAG}{col.BOLD}
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗
║          🎫     {col.BOLD}Rich Presence Tool     🎫       ║
║                                                 {col.TAG}║
║      {col.YELLOW}{col.BOLD}It appears this is your first launch       {col.TAG}║
║      {col.YELLOW}{col.BOLD}Or you've deleted your config file         {col.TAG}║
║                                                 ║
║ {col.WHITE}You are going to set up a rich presence on your {col.TAG}║
║ {col.WHITE}Discord profile. Be sure you have the following {col.TAG}║
║ {col.WHITE}info ready to configure your rich presence with {col.TAG}║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
{col.WHITE}- Application ID, found at your 
application at discord.com/developers/applications
If you have no application, create one.

- An idea about what you want your friends / server 
buddies to see on your Discord profile.

-[OPTIONAL] Buttons with labels
+ URLs to share is Required!!!

{col.TAG}{col.BOLD}╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─╗
║ {col.WHITE}! ! Scroll UP to read from beginning ! ! {col.TAG}║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─╝
{col.WHITE}
        """)
    input(f"{col.UNBOLD}Hit enter to continue... ")
    rpc_title               = ASK_RPC_title()
    rpc_desc                = ASK_RPC_desc()
    clear()
    print(
        f"""{col.TAG}{col.BOLD}
        ╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗
        ║          🎫     {col.BOLD}Rich Presence Tool     🎫         ║
        ║                                                   ║
        ║{col.WHITE} Setting buttons requires a URL you wish to share. {col.TAG}║
        ║{col.WHITE}      If you have no URLs to share, you can now  {col.TAG}  ║
        ║{col.WHITE}                  answer with "N"                {col.TAG}  ║
        ╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
-       """)
    rpc_want_buttons   = ASK_RPC_WantButtons()
    try:
        config.add_section('RPC_details')
    except DuplicateSectionError:
        pass
    if rpc_want_buttons.lower() == "y":
        rpc__how_many_buttons   = ASK_RPC_NumbOfButtons()
        config.set('RPC_details', 'rpc_buttons_amount', str(rpc__how_many_buttons))

        if str(rpc__how_many_buttons) == "1":
            rpc__1st_button_label   = ask_rpc_1stbutton_label(rpc__how_many_buttons)
            rpc__1st_button_URL     = ask_rpc_1stbutton_URL(rpc__how_many_buttons)
            config.set('RPC_details', 'btnlbl1', rpc__1st_button_label)
            config.set('RPC_details', 'btnurl1', rpc__1st_button_URL)
            pass

        elif str(rpc__how_many_buttons) == "2":
            rpc__1st_button_label   = ask_rpc_1stbutton_label(rpc__how_many_buttons)
            rpc__1st_button_URL     = ask_rpc_1stbutton_URL(rpc__how_many_buttons)
            rpc__2nd_button_label   = ask_rpc_2ndbutton_label()
            rpc__2nd_button_URL     = ask_rpc_2ndbutton_URL()
            config.set('RPC_details', 'btnlbl1', rpc__1st_button_label)
            config.set('RPC_details', 'btnurl1', str(rpc__1st_button_URL))
            config.set('RPC_details', 'btnlbl2', str(rpc__2nd_button_label))
            config.set('RPC_details', 'btnurl2', str(rpc__2nd_button_URL))
            pass

    elif rpc_want_buttons.lower() == "n":
        config.set('RPC_details', 'rpc_buttons_amount', "0")
        pass
    
    RPC_application_id = ASK_app_id()
    clear()
    print(f"""{col.TAG}{col.BOLD}
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗
║          🎫     {col.BOLD}Rich Presence Tool     🎫       ║
║ {col.WHITE}           The configuration is {col.OKGREEN}done {col.TAG}           ║
║ {col.WHITE}           Config will be saved at:{col.TAG}             ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝\n             {col.WHITE}{getcwd()}""")
    input(f'{col.WHITE}{col.UNBOLD}Hit enter save and\nto launch your custom-made Rich Presence\non your Discord profile... ')
    config.set('RPC_details', 'rpc_application_id', RPC_application_id)
    config.set('RPC_details', 'rpc_title', rpc_title)
    config.set('RPC_details', 'rpc_desc', rpc_desc)
    with open(RCP_Config_dot_ini, 'w') as f:
        config.write(f)
    time.sleep(1) # wait because following functions read too early, saying the config doesn't exist while it was just created.

def SetupNewRPC():
    # start with clean terminal
    clear()
    CompileConfig()

def ConfigCheck():
    clear()
    try:
        open(RCP_Config_dot_ini, 'r').close()
        YesOrNo = Terminal.prompt(f"\n{col.TAG}{col.BOLD}╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗\n║ 🎫  {col.WHITE}Rich Presence Tool  {col.TAG}🎫  ║\n║ {col.OKGREEN}A rich presence was set up !{col.TAG}║\n╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝\nDo you wish to Use, Change or View this?\n{col.YELLOW}1. {col.OKGREEN}(Use)\n{col.YELLOW}2. {col.RED}(Change)\n{col.YELLOW}3. {col.OKCYAN}(View)\n{col.YELLOW}4. {col.DRED}(Exit)\n\n{col.TAG}Make a choice {col.WHITE}({col.OKGREEN}1 {col.WHITE}/ {col.RED}2 {col.WHITE}/ {col.OKCYAN}3 {col.WHITE}/ {col.DRED}4{col.WHITE})> {col.OKGREEN}{col.BOLD}", allowed_replies=('1', '2', '3', '4'))
        if YesOrNo.lower() == '1':
            pass
        elif YesOrNo.lower() == '2':
            clear()
            SetupNewRPC()
        elif YesOrNo.lower() == '4':
            print(col.ENDC)
            exit(0)
        elif YesOrNo.lower() == '3':
                try:
                    clear()
                    open(RCP_Config_dot_ini, 'r')
                    config.read(RCP_Config_dot_ini)

                    rpc_application_id  = config['RPC_details']['rpc_application_id']
                    rpc_desc            = config['RPC_details']['rpc_desc']
                    rpc_title           = config['RPC_details']['rpc_title']
                    amount_of_buttons   = config['RPC_details']['rpc_buttons_amount']

                    if amount_of_buttons == "1":
                        btnlbl1             = config['RPC_details']['btnlbl1']
                        btnurl1             = config['RPC_details']['btnurl1']

                        print(f"""{col.BOLD}{col.YELLOW}Current Rich Presence:
{col.YELLOW}{col.BOLD}Title: {col.WHITE}--------> {col.OKCYAN}{rpc_title}
{col.YELLOW}{col.BOLD}Description: {col.WHITE}--> {col.OKCYAN}{rpc_desc}
{col.YELLOW}{col.BOLD}App ID: {col.WHITE}-------> {col.OKCYAN}{rpc_application_id}
{col.YELLOW}{col.BOLD}Buttons
{col.YELLOW}{col.BOLD}First Button Label: {col.WHITE}--> {col.OKCYAN}{btnlbl1}
{col.YELLOW}{col.BOLD}First Button Shared URL: {col.WHITE}--> {col.OKCYAN}{btnurl1}""")

                        input(f"{col.UNBOLD}{col.WHITE}\nHit enter to go back and decide what to do... ")
                        ConfigCheck()
                    elif amount_of_buttons == "2":
                        btnlbl1             = config['RPC_details']['btnlbl1'] # button label #1
                        btnurl1             = config['RPC_details']['btnurl1'] # button URL #1
                        btnlbl2             = config['RPC_details']['btnlbl2'] # button label #2
                        btnurl2             = config['RPC_details']['btnurl2'] # button URL #2

                        print(f"""{col.BOLD}{col.YELLOW}Current Rich Presence:
{col.YELLOW}{col.BOLD}Title: {col.WHITE}--------> {col.OKCYAN}{rpc_title}
{col.YELLOW}{col.BOLD}Description: {col.WHITE}--> {col.OKCYAN}{rpc_desc}
{col.YELLOW}{col.BOLD}App ID: {col.WHITE}-------> {col.OKCYAN}{rpc_application_id}
{col.YELLOW}{col.BOLD}Buttons
{col.YELLOW}{col.BOLD}First Button Label: {col.WHITE}--> {col.OKCYAN}{btnlbl1}
{col.YELLOW}{col.BOLD}First Button Shared URL: {col.WHITE}--> {col.OKCYAN}{btnurl1}
{col.YELLOW}{col.BOLD}Second Button Label: {col.WHITE}----> {col.OKCYAN}{btnlbl2}
{col.YELLOW}{col.BOLD}Second Button Shared URL: {col.WHITE}--> {col.OKCYAN}{btnurl2}""")

                        input(f"{col.UNBOLD}{col.WHITE}\nHit enter to go back and decide what to do... ")
                        ConfigCheck()
                    else:
                        if amount_of_buttons == "0":
                            print(f"""{col.BOLD}{col.YELLOW}Current Rich Presence:
{col.YELLOW}{col.BOLD}Title: {col.WHITE}--------> {col.OKCYAN}{rpc_title}
{col.YELLOW}{col.BOLD}Description: {col.WHITE}--> {col.OKCYAN}{rpc_desc}
{col.YELLOW}{col.BOLD}App ID: {col.WHITE}-------> {col.OKCYAN}{rpc_application_id}""")

                            input(f"{col.UNBOLD}{col.WHITE}\nHit enter to go back and decide what to do... ")
                            ConfigCheck()
                except KeyboardInterrupt:
                    ConfigCheck()
                except FileNotFoundError:
                    clear()
                    print(
                f"""{col.RED}
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
║ ❌ {col.WHITE}Config file missing! please relaunch the application! {col.RED}❌ ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝{col.ENDC}""")
                    time.sleep(5)
                    exit(1)

    except FileNotFoundError: # We assume URL was never given to use.
        SetupNewRPC()

def SplashScreen():
    if ranAs_Service:
        return
    clear()
    print(f"""{col.TAG}{col.BOLD}╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗
║          🎫     {col.BOLD}Rich Presence Tool     🎫           ║
║ {col.WHITE}Setting A Rich PresenCe on your profile, simplified {col.TAG}║
║                                                     ║
║ {col.RED}Not affiliated with {col.BLURPLE}Discord Inc. {col.RED}in any way         {col.TAG}║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝""")
    Terminal.announce(f"{col.OKGREEN}Initialising . . .")

    time.sleep(5) # give people the time to read front page of this CLI-based utility
    clear() # Clear the current terminal / CMD / Powershell Window
    
    ConfigCheck()

SplashScreen()

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def main():
    while True:
        if checkIfProcessRunning('Discord'):
            clear()
            Terminal.announce(f'{col.RED}Tango {col.OKGREEN}spotted{col.WHITE}! Discord is {col.OKGREEN}running{col.WHITE}!')

            try:
                LaunchRichPresence()
            
            except exceptions.InvalidPipe:
                # need to wait a bit before Discord is reading rich presence from any game / app
                # let's wait max 20 seconds so we give Discord client the time before we shoot our rich presence.
                Terminal.announce('Waiting for Discord to listen for rich presence . . .')
                time.sleep(20)

                # Let's give it a shot now, launching Rich Presence
                try:
                    LaunchRichPresence()
                except exceptions.PyPresenceException:
                    main()

        else:
            print(f'{col.BOLD}{col.TAG}[{col.WHITE}Rich Presence{col.TAG}] {col.WHITE}Waiting for Discord to launch . . .')

            time.sleep(5) # don't spam the console, print the above line only per 5 seconds.

            # re-check every 5 seconds by calling the function over until Discord is spotted and running.
            main()

def RPCWithoutButtons(rpc_application_id, rpc_title, rpc_desc):
        client_id = rpc_application_id
        RPC = Presence(client_id)  # Initialize the client class
        RPC.connect() # Start the handshake loop

        RichPresenceData = (RPC.update(state=rpc_title, details=rpc_desc))  # Set the presence
        
        print(f"""{col.OKGREEN}╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
║ ✅{col.BOLD}{col.WHITE} Looking good! {col.TAG}RichPresence {col.WHITE}is {col.OKGREEN}UP {col.WHITE}and {col.YELLOW}shining {col.WHITE}on your profile! ✅{col.OKGREEN} ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
{col.YELLOW}If not, check if you have the following option enabled in Discord:
{col.BOLD}{col.WHITE}User Settings > Activity Status > Display current activity as a status message.

{col.BOLD}{col.YELLOW}These settings were applied on your Rich Presence:
{col.YELLOW}{col.BOLD}Title: {col.WHITE}--------> {col.OKCYAN}{rpc_title}
{col.YELLOW}{col.BOLD}Description: {col.WHITE}--> {col.OKCYAN}{rpc_desc}
{col.YELLOW}{col.BOLD}App ID: {col.WHITE}-------> {col.OKCYAN}*censored*""")
        
        while True:  # The presence will stay on as long as the program is running
            time.sleep(15) # Can only update rich presence every 15 seconds

def RPC1button(rpc_application_id, rpc_title, rpc_desc, btnlbl1, btnurl1):
        client_id = rpc_application_id
        RPC = Presence(client_id)  # Initialize the client class
        RPC.connect() # Start the handshake loop

        RichPresenceData = (RPC.update(state=f"{rpc_title}", details=f"{rpc_desc}", buttons=[{"label": f"{btnlbl1}", "url": f"{btnurl1}"}]))  # Set the presence
        
        print(f"""{col.OKGREEN}╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
║ ✅{col.BOLD}{col.WHITE} Looking good! {col.TAG}RichPresence {col.WHITE}is {col.OKGREEN}UP {col.WHITE}and {col.YELLOW}shining {col.WHITE}on your profile! ✅{col.OKGREEN} ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
{col.YELLOW}If not, check if you have the following option enabled in Discord:
{col.BOLD}{col.WHITE}User Settings > Activity Status > Display current activity as a status message.

{col.BOLD}{col.YELLOW}These settings were applied on your Rich Presence:
{col.YELLOW}{col.BOLD}Title: {col.WHITE}--------> {col.OKCYAN}{rpc_title}
{col.YELLOW}{col.BOLD}Description: {col.WHITE}--> {col.OKCYAN}{rpc_desc}
{col.YELLOW}{col.BOLD}App ID: {col.WHITE}-------> {col.OKCYAN}*****************
{col.YELLOW}{col.BOLD}Buttons
{col.YELLOW}{col.BOLD}First Button Label: {col.WHITE}--> {col.OKCYAN}{btnlbl1}
{col.YELLOW}{col.BOLD}First Button Shared URL: {col.WHITE}--> {col.OKCYAN}{btnurl1}""")

        while True:  # The presence will stay on as long as the program is running
            time.sleep(15) # Can only update rich presence every 15 seconds

def RPC2buttons(rpc_application_id, rpc_title, rpc_desc, btnlbl1, btnurl1, btnlbl2, btnurl2):
        client_id = rpc_application_id
        RPC = Presence(client_id)  # Initialize the client class
        RPC.connect() # Start the handshake loop

        click_me = [{"label": f"{btnlbl1}", "url": f"{btnurl1}"}, {"label": f"{btnlbl2}", "url": f"{btnurl2}"}]

        RichPresenceData = (RPC.update(state=f"{rpc_title}", details=f"{rpc_desc}", buttons=click_me))  # Set the presence
        
        print(
    f"""{col.OKGREEN}
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
║ ✅{col.BOLD}{col.WHITE} Looking good! {col.TAG}RichPresence {col.WHITE}is {col.OKGREEN}UP {col.WHITE}and {col.YELLOW}shining {col.WHITE}on your profile! ✅{col.OKGREEN} ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
{col.YELLOW}If not, check if you have the following option enabled in Discord:
{col.BOLD}{col.WHITE}User Settings > Activity Status > Display current activity as a status message.

{col.BOLD}{col.YELLOW}These settings were applied on your Rich Presence:
{col.YELLOW}{col.BOLD}Title: {col.WHITE}--------> {col.OKCYAN}{rpc_title}
{col.YELLOW}{col.BOLD}Description: {col.WHITE}--> {col.OKCYAN}{rpc_desc}
{col.YELLOW}{col.BOLD}App ID: {col.WHITE}-------> {col.OKCYAN}*****************
{col.YELLOW}{col.BOLD}Buttons
{col.YELLOW}{col.BOLD}First Button Label: {col.WHITE}--> {col.OKCYAN}{btnlbl1}
{col.YELLOW}{col.BOLD}First Button Shared URL: {col.WHITE}--> {col.OKCYAN}{btnurl1}
{col.YELLOW}{col.BOLD}Second Button Label: {col.WHITE}--> {col.OKCYAN}{btnlbl2}
{col.YELLOW}{col.BOLD}Second Button Shared URL: {col.WHITE}--> {col.OKCYAN}{btnurl2}""")
        while True:  # The presence will stay on as long as the program is running
            time.sleep(15) # Can only update rich presence every 15 seconds

def LaunchRichPresence():
    try:
        open(RCP_Config_dot_ini, 'r')
        config.read(RCP_Config_dot_ini)

        rpc_application_id  = config['RPC_details']['rpc_application_id']
        rpc_desc            = config['RPC_details']['rpc_desc']
        rpc_title           = config['RPC_details']['rpc_title']
        amount_of_buttons   = config['RPC_details']['rpc_buttons_amount']

        if amount_of_buttons == "1":
            btnlbl1             = config['RPC_details']['btnlbl1']
            btnurl1             = config['RPC_details']['btnurl1']
            RPC1button(rpc_application_id, rpc_title, rpc_desc, btnlbl1, btnurl1)

        elif amount_of_buttons == "2":
            btnlbl1             = config['RPC_details']['btnlbl1'] # button label #1
            btnurl1             = config['RPC_details']['btnurl1'] # button URL #1
            btnlbl2             = config['RPC_details']['btnlbl2'] # button label #2
            btnurl2             = config['RPC_details']['btnurl2'] # button URL #2

            RPC2buttons(rpc_application_id, rpc_title, rpc_desc, btnlbl1, btnurl1, btnlbl2, btnurl2)
        else:
            if amount_of_buttons == "0":
                RPCWithoutButtons(rpc_application_id, rpc_title, rpc_desc)
    except FileNotFoundError:
        clear()
        print(
    """
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
║ ❌ Config file missing! please relaunch the application! ❌ ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
    """)
        time.sleep(5)
        exit()
main()