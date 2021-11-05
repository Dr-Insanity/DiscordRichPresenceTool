try:
    # version
    Version = "0.0.2"
    Presence_of_remaining_junk_code = True # It's a joke, but yes really, there's some junk code I still need to cleanup

    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        YELLOW = '\033[38;5;220m'
        RED = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNBOLD = '\033[22m'
        UNDERLINE = '\033[4m'
        TAG = '\033[38;5;208m'
        WHITE = '\033[38;5;15m'
        BLURPLE = '\033[38;5;117m'
    import re
    import os
    import platform
    import time
    import json
    from configparser import ConfigParser, DuplicateSectionError

    def clear():
        # cross-platform clear console
        if platform.system() == 'Linux':
            os.system("clear")
        elif platform.system() == 'Darwin':
            os.system("clear")
        else:
            if platform.system() == 'Windows':
                os.system("cls")

    def dependency_checker():
        clear()
        print(f"{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}] {bcolors.UNBOLD}Checking if further dependencies are installed...")

        def check_psutil():
            print(f"{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}] {bcolors.UNBOLD}attempting to use psutil")
            try: # try to import psutil, for checking if Discord is running, or not.
                import psutil

            except ImportError:
                print(f"{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}] {bcolors.UNBOLD}psutil {bcolors.RED}{bcolors.BOLD}NOT INSTALLED!\n{bcolors.WHITE}{bcolors.UNBOLD}Attempting to install it for you...")
                print("                                                  ")
                print("=================BEGIN OF INSTALL=================")
                os.system("pip install psutil")
                print("==================END OF INSTALL==================")
                print("                                                  ")
                print(f"{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}] {bcolors.UNBOLD}psutil {bcolors.OKGREEN}{bcolors.BOLD}INSTALLED!\n{bcolors.WHITE}{bcolors.UNBOLD}commencing other dependency checks...")
                input("Hit enter to continue... ")

        check_psutil()

        def check_pypresence():
            try:
                from pypresence import Presence
                from pypresence import exceptions

            except ImportError:
                print(f"{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}] {bcolors.UNBOLD}pypresence {bcolors.RED}{bcolors.BOLD}NOT INSTALLED!\n{bcolors.WHITE}{bcolors.UNBOLD}Attempting to install it for you...")
                print("                                                  ")
                print("=================BEGIN OF INSTALL=================")
                os.system("pip install pypresence")
                print("==================END OF INSTALL==================")
                print("                                                  ")
                print(f"{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}] {bcolors.UNBOLD}pypresence {bcolors.OKGREEN}{bcolors.BOLD}INSTALLED!\n{bcolors.WHITE}{bcolors.UNBOLD}dependency checks {bcolors.OKGREEN}{bcolors.BOLD}Done!")
                input("Hit enter to continue... ")

        check_pypresence()

    config = ConfigParser(allow_no_value=True)

    def ensureconfig():
        """
        reads in the config file and returns a bolean (true OR false)
        """
        # check 'n read, watch 'n learn
        # The force is with those who read the source
        try:
            does_conf_exist = open('RPC_Config.ini', 'r')
            if bool(does_conf_exist) == True:
                return True
                
        except FileNotFoundError:
            # Config doesn't exist, create now since it's safe.

            config.read('RPC_Config.ini')
            config.add_section('settings')
            
            # code snippet
           # config.set('settings', 'disable-vc-notice')
           # config.set('settings', 'disable-requirements-notice')
           # config.set('settings', 'disable-button-notice')
           # config.set('settings', 'disable-splashscreen') # aka Loader / loading screen / etc

            with open('RPC_Config.ini', 'w') as f:
                config.write(f)
            return True
    def prompt_need_MSVC14orHigher():
        clear()
        print(f"""{bcolors.TAG}{bcolors.BOLD}╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗
║                  🎫     {bcolors.BOLD}Rich Presence Tool     🎫                 ║
║{bcolors.RED} THIS PROGRAM NEEDS MICROSOFT VISUAL BUILD TOOLS 14.0 OR HIGHER!!! {bcolors.TAG}║
║{bcolors.WHITE}                You can get it with the below link  {bcolors.TAG}               ║
║{bcolors.OKGREEN}   https://www.scivision.dev/python-windows-visual-c-14-required/ {bcolors.TAG} ║
║{bcolors.WHITE}{bcolors.UNBOLD}              Report broken links please! Thank you.               {bcolors.TAG}║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
VERSION: {Version}

{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}] {bcolors.WHITE}{bcolors.UNBOLD}It's possible that you may already have this installed. Try to proceed.

{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}] {bcolors.WHITE}{bcolors.UNBOLD}Discord Rich Presence Tool will continue to run, assuming you have this dependency installed
{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}] {bcolors.WHITE}{bcolors.UNBOLD}Settings will be stored at:

{bcolors.OKCYAN}{bcolors.BOLD}{os.getcwd()}

""")

        # creating config now + all possible settings, overwritten by user, if preferenced, in the future
        # firstly, try and read if it exists, we don't want to overwrite the current config file now, don't we?

        confirm_understanding = input(f"{bcolors.YELLOW}I got this dependency {bcolors.OKGREEN}{bcolors.BOLD}installed {bcolors.UNBOLD}{bcolors.YELLOW}({bcolors.OKGREEN}{bcolors.BOLD}Y{bcolors.WHITE}{bcolors.UNBOLD}/{bcolors.RED}{bcolors.BOLD}N{bcolors.YELLOW}{bcolors.UNBOLD}){bcolors.WHITE}> ")

        if confirm_understanding.lower() == "y":
            ensureconfig()
            pass

        elif confirm_understanding.lower() == "n":
            print(f"{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}] {bcolors.WHITE} Quitting application - Install {bcolors.RED}MICROSOFT VISUAL BUILD TOOLS 14.0 OR HIGHER!!!{bcolors.WHITE}")
            quit()

        if ensureconfig() == True:
            pass

            dependency_checker()

    import psutil
    from pypresence import Presence
    from pypresence import exceptions

    apptag = f"{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}] {bcolors.UNBOLD}"

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
        RPC_application_id = input(f"{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}][{bcolors.OKGREEN}setup{bcolors.TAG}] {bcolors.UNBOLD}{bcolors.WHITE}Application ID (found at https://discord.com/developers, create your app on the panel)> {bcolors.OKGREEN}{bcolors.BOLD}")
        return RPC_application_id

    def ASK_RPC_title():
        clear()
        RPC_title = input(f"{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}][{bcolors.OKGREEN}setup{bcolors.TAG}] {bcolors.UNBOLD}{bcolors.WHITE}Title of your rich presence?> {bcolors.OKGREEN}{bcolors.BOLD}")
        return RPC_title

    def ASK_RPC_desc():
        clear()
        RPC_desc = input(f"{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}][{bcolors.OKGREEN}setup{bcolors.TAG}] {bcolors.UNBOLD}{bcolors.WHITE}Description of your rich presence?> {bcolors.OKGREEN}{bcolors.BOLD}")
        return RPC_desc

    def ASK_RPC_WantButtons():
        RPC_Buttons = input(f"{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}][{bcolors.OKGREEN}setup{bcolors.TAG}] {bcolors.UNBOLD}{bcolors.WHITE}Do you want buttons on your rich presence? (Y/N)> {bcolors.OKGREEN}{bcolors.BOLD}")
        if RPC_Buttons.lower() == "y":
            return "y"
        elif RPC_Buttons.lower() == "n":
            return "n"
        else:
            clear()
            print(
"""
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
║ ❌    Invalid reply    ❌ ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
Your choices are:
- (y)es - Set up buttons for my rich presence.
- (n)o - Do not set up buttons on my rich presence.
""")

            ASK_RPC_WantButtons()
    def ASK_RPC_NumbOfButtons():
        RPC_Buttons_HowMany = input(f"{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}][{bcolors.OKGREEN}setup{bcolors.TAG}] {bcolors.UNBOLD}{bcolors.WHITE}How many buttons do you want on your rich presence? (1-2, choose one)>  {bcolors.OKGREEN}{bcolors.BOLD}")
        if str(RPC_Buttons_HowMany) == '1':
            return "1"
        elif str(RPC_Buttons_HowMany) == '2':
            return "2"
        else:
            clear()
            print(
    """
    ╔═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
    ║ ❌    Invalid reply    ❌ ║
    ╚═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
    Your choices are:
    - 1 - Set up 1 button.
    - 2 - Set up 2 buttons.
                """)
            time.sleep(3)
            clear()
            ASK_RPC_NumbOfButtons()

    def ask_rpc_1stbutton_label(rpc__how_many_buttons):
        if str(rpc__how_many_buttons) == "1":
            RPC_Single_Button_LabelText = input(f"{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}][{bcolors.OKGREEN}setup{bcolors.TAG}]{bcolors.TAG}[{bcolors.WHITE}1/1 button{bcolors.TAG}] {bcolors.UNBOLD}{bcolors.WHITE}Which text shall be displayed on your button? (type some text)>  {bcolors.OKGREEN}{bcolors.BOLD}")
        elif str(rpc__how_many_buttons) == "2":
            RPC_Single_Button_LabelText = input(f"{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}][{bcolors.OKGREEN}setup{bcolors.TAG}]{bcolors.TAG}[{bcolors.WHITE}1/2 button{bcolors.TAG}] {bcolors.UNBOLD}{bcolors.WHITE}Which text shall be displayed on your button? (type some text)>  {bcolors.OKGREEN}{bcolors.BOLD}")
        if len(RPC_Single_Button_LabelText) <= 32:
            return RPC_Single_Button_LabelText
        elif len(RPC_Single_Button_LabelText) > 32:
            clear()
            print(
        """
        ╔═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
        ║ ❌ Too many characters ❌ ║
        ╚═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
        """)
            time.sleep(3)
            clear()
            ask_rpc_1stbutton_label()

    def ask_rpc_1stbutton_URL(rpc__how_many_buttons):
        if str(rpc__how_many_buttons) == "1":
            RPC_Single_Button_LabelText = input(f"{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}][{bcolors.OKGREEN}setup{bcolors.TAG}]{bcolors.TAG}[{bcolors.WHITE}1/1 button{bcolors.TAG}] {bcolors.UNBOLD}{bcolors.WHITE}Which URL shall be shared> {bcolors.OKGREEN}{bcolors.BOLD}")
            return RPC_Single_Button_LabelText
        elif str(rpc__how_many_buttons) == "2":
            RPC_Single_Button_LabelText = input(f"{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}][{bcolors.OKGREEN}setup{bcolors.TAG}]{bcolors.TAG}[{bcolors.WHITE}1/2 button{bcolors.TAG}] {bcolors.UNBOLD}{bcolors.WHITE}Which URL shall be shared> {bcolors.OKGREEN}{bcolors.BOLD}")
            return RPC_Single_Button_LabelText

    def ask_rpc_2ndbutton_label():
        RPC_Single_Button_LabelText = input(f"{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}][{bcolors.OKGREEN}setup{bcolors.TAG}]{bcolors.TAG}[{bcolors.WHITE}2/2 button{bcolors.TAG}] {bcolors.UNBOLD}{bcolors.WHITE}Which text shall be displayed on your button? (type some text)> {bcolors.OKGREEN}{bcolors.BOLD}")
        if len(RPC_Single_Button_LabelText) <= 32:
            return RPC_Single_Button_LabelText
        elif len(RPC_Single_Button_LabelText) > 32:
            clear()
            print(
        """
        ╔═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
        ║ ❌ Too many characters ❌ ║
        ╚═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
        """)
            time.sleep(3)
            clear()
            ask_rpc_2ndbutton_label()


    def ask_rpc_2ndbutton_URL():
        RPC_Single_Button_LabelText = input(f"{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}][{bcolors.OKGREEN}setup{bcolors.TAG}]{bcolors.TAG}[{bcolors.WHITE}2/2 button{bcolors.TAG}] {bcolors.UNBOLD}{bcolors.WHITE}Which URL shall be shared> {bcolors.OKGREEN}{bcolors.BOLD}")
        return RPC_Single_Button_LabelText


    def ASK_RPC_Buttons(): ### THIS IS THE JUNK CODE I keep as code snippet, for now. 
        #Yes I am aware of other solutions. Thank you for your efforts to remind me, in case you wanted to do that. But no need :) I'm more comfortable with this way.
        # I delete it once I have these parts in a similar use somewhere else in the code. :)
        
        """ # apparently a doc string / multiline string now? lol. It used to be a print, yes.

        # I wrote all these explanations now, and took some time for it.
        # so why not delete it now and work it off and be done with it?
        # good point. I actually want to do something else, and at the same time willing to finish the feats off this day.

        # help me, bored. or idk. Warning, focus significantly reduced by 90%. Help. What am I doing. Why am I doing this. WTF. I got ADHD. Someone slap me out of this nonsense. I snapped out of it myself.
        ╔═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
        ║ ❌    Invalid reply    ❌ ║
        ╚═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
        Your choices are:
        - 1 (1 button on your RPC)
        - 2 (2 buttons on your RPC, which is the max as well)"""
        RPC_Buttons = input(f"{bcolors.YELLOW}[Rich Presence][setup] Do you want buttons on your rich presence? (Y/N)>")

        if 1 == 1:
            fak = "fack"
        elif RPC_Buttons.lower() == "n":
            return

        config.read('RPC_Config.ini')
        # config.add_section('RPC_details')
        # config.set('RPC_details', 'rpc_application_id', RPC_application_id)
        # config.set('RPC_details', 'rpc_title', RPC_title)
        # config.set('RPC_details', 'rpc_desc', RPC_desc)

        with open('RPC_Config.ini', 'w') as f:
            config.write(f)

    def CompileConfig():
        config.read('RPC_Config.ini')

        print(f"""{bcolors.TAG}{bcolors.BOLD}
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗
║          🎫     {bcolors.BOLD}Rich Presence Tool     🎫       ║
║ {bcolors.WHITE}You are going to set up a rich presence on your {bcolors.TAG}║
║ {bcolors.WHITE}Discord profile. Be sure you have the following {bcolors.TAG}║
║ {bcolors.WHITE}info ready to configure your rich presence with {bcolors.TAG}║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
{bcolors.WHITE}- Application ID, found at your 
application at discord.com/developers/applications
If you have no application, create one.

- An idea about what you want your friends / server 
buddies to see on your Discord profile.

-[OPTIONAL] Buttons with labels
+ URLs to share is Required!!!

{bcolors.TAG}{bcolors.BOLD}╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─╗
║ {bcolors.WHITE}! ! Scroll UP to read from beginning ! ! {bcolors.TAG}║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─╝
""")
        optional_option = input(f"Hit enter to continue...")

        rpc_title               = ASK_RPC_title()
        rpc_desc                = ASK_RPC_desc()

        config.read('RPC_Config.ini')
        clear()
        print(
            f"""{bcolors.TAG}{bcolors.BOLD}
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗
║          🎫     {bcolors.BOLD}Rich Presence Tool     🎫         ║
║                                                   ║
║{bcolors.WHITE} Setting buttons requires a URL you wish to share. {bcolors.TAG}║
║{bcolors.WHITE}      If you have no URLs to share, you can now  {bcolors.TAG}  ║
║{bcolors.WHITE}                  answer with "N"                {bcolors.TAG}  ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝

""")
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
        print(f"""{bcolors.TAG}{bcolors.BOLD}
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗
║          🎫     {bcolors.BOLD}Rich Presence Tool     🎫       ║
║ {bcolors.WHITE}           The configuration is {bcolors.OKGREEN}done {bcolors.TAG}           ║
║ {bcolors.WHITE}           Config will be saved at:{bcolors.TAG}             ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝\n             {bcolors.WHITE}{os.getcwd()}""")
        input(f'{bcolors.WHITE}{bcolors.UNBOLD}Hit enter save and\nto launch your custom-made Rich Presence\non your Discord profile... ')
        config.set('RPC_details', 'rpc_application_id', RPC_application_id)
        config.set('RPC_details', 'rpc_title', rpc_title)
        config.set('RPC_details', 'rpc_desc', rpc_desc)
        with open('RPC_Config.ini', 'w') as f:
            config.write(f)
        time.sleep(1) # wait because further functions read too early, saying the config doesn't exist while it was just created.

    def SetupNewRPC():
        # start with clean terminal
        clear()

        CompileConfig()

    def ConfigCheck():
        clear()
        try:
            open('RPC_Config.ini', 'r')
            
            config.read("RPC_Config.ini")
            if config.has_section("RPC_details"):
                pass
            elif not config.has_section("RPC_details"):
                SetupNewRPC()
                return
            print(
    f"""{bcolors.TAG}{bcolors.BOLD}
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗
║ 🎫  Rich Presence Tool  🎫  ║
║ {bcolors.OKGREEN}A rich presence was set up !{bcolors.TAG}║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
    """)
            YesOrNo = input(f"{bcolors.BOLD}{bcolors.TAG}[{bcolors.WHITE}Rich Presence{bcolors.TAG}] {bcolors.WHITE}Do you wish to Use this or Change or View?\n{bcolors.YELLOW}1. {bcolors.OKGREEN}(Use)\n{bcolors.YELLOW}2. {bcolors.RED}(Change)\n{bcolors.YELLOW}3. {bcolors.OKCYAN}(View)\n\n{bcolors.TAG}Make a choice {bcolors.WHITE}({bcolors.OKGREEN}1 {bcolors.WHITE}/ {bcolors.RED}2 {bcolors.WHITE}/ {bcolors.OKCYAN}3{bcolors.WHITE})> {bcolors.OKGREEN}{bcolors.BOLD}")

            proper_replies = ['1', '2', '3']

            if YesOrNo.lower() in proper_replies:
                if YesOrNo.lower() == '1':
                    pass
                elif YesOrNo.lower() == '2':
                    clear()
                    SetupNewRPC()
                else:
                    if YesOrNo.lower() == '3':
                        try:
                            clear()
                            open('RPC_Config.ini', 'r')
                            config.read('RPC_Config.ini')

                            rpc_application_id  = config['RPC_details']['rpc_application_id']
                            rpc_desc            = config['RPC_details']['rpc_desc']
                            rpc_title           = config['RPC_details']['rpc_title']
                            amount_of_buttons   = config['RPC_details']['rpc_buttons_amount']

                            if amount_of_buttons == "1":
                                btnlbl1             = config['RPC_details']['btnlbl1']
                                btnurl1             = config['RPC_details']['btnurl1']

                                print(f"{bcolors.BOLD}{bcolors.YELLOW}Current Rich Presence:")
                                print(f"{bcolors.YELLOW}{bcolors.BOLD}Title: {bcolors.WHITE}--------> {bcolors.OKCYAN}{rpc_title}")
                                print(f"{bcolors.YELLOW}{bcolors.BOLD}Description: {bcolors.WHITE}--> {bcolors.OKCYAN}{rpc_desc}")
                                print(f"{bcolors.YELLOW}{bcolors.BOLD}App ID: {bcolors.WHITE}-------> {bcolors.OKCYAN}{rpc_application_id}")
                                print(f"{bcolors.YELLOW}{bcolors.BOLD}Buttons:")
                                print(f"{bcolors.YELLOW}{bcolors.BOLD}First Button Label: {bcolors.WHITE}--> {bcolors.OKCYAN}{btnlbl1}")
                                print(f"{bcolors.YELLOW}{bcolors.BOLD}First Button Shared URL: {bcolors.WHITE}--> {bcolors.OKCYAN}{btnurl1}")

                                input(f"{bcolors.UNBOLD}{bcolors.WHITE}\nHit enter to go back and decide what to do... ")
                                ConfigCheck()
                            elif amount_of_buttons == "2":
                                btnlbl1             = config['RPC_details']['btnlbl1'] # button label #1
                                btnurl1             = config['RPC_details']['btnurl1'] # button URL #1
                                btnlbl2             = config['RPC_details']['btnlbl2'] # button label #2
                                btnurl2             = config['RPC_details']['btnurl2'] # button URL #2

                                print(f"{bcolors.BOLD}{bcolors.YELLOW}Current Rich Presence:")
                                print(f"{bcolors.YELLOW}{bcolors.BOLD}Title: {bcolors.WHITE}--------> {bcolors.OKCYAN}{rpc_title}")
                                print(f"{bcolors.YELLOW}{bcolors.BOLD}Description: {bcolors.WHITE}--> {bcolors.OKCYAN}{rpc_desc}")
                                print(f"{bcolors.YELLOW}{bcolors.BOLD}App ID: {bcolors.WHITE}-------> {bcolors.OKCYAN}{rpc_application_id}")
                                print(f"{bcolors.YELLOW}{bcolors.BOLD}Buttons:")
                                print(f"{bcolors.YELLOW}{bcolors.BOLD}First Button Label: {bcolors.WHITE}--> {bcolors.OKCYAN}{btnlbl1}")
                                print(f"{bcolors.YELLOW}{bcolors.BOLD}First Button Shared URL: {bcolors.WHITE}--> {bcolors.OKCYAN}{btnurl1}")
                                print(f"{bcolors.YELLOW}{bcolors.BOLD}Second Button Label: {bcolors.WHITE}----> {bcolors.OKCYAN}{btnlbl2}")
                                print(f"{bcolors.YELLOW}{bcolors.BOLD}Second Button Shared URL: {bcolors.WHITE}--> {bcolors.OKCYAN}{btnurl2}")

                                input(f"{bcolors.UNBOLD}{bcolors.WHITE}\nHit enter to go back and decide what to do... ")
                                ConfigCheck()
                            else:
                                if amount_of_buttons == "0":
                                    print(f"{bcolors.BOLD}{bcolors.YELLOW}Current Rich Presence:")
                                    print(f"{bcolors.YELLOW}{bcolors.BOLD}Title: {bcolors.WHITE}--------> {bcolors.OKCYAN}{rpc_title}")
                                    print(f"{bcolors.YELLOW}{bcolors.BOLD}Description: {bcolors.WHITE}--> {bcolors.OKCYAN}{rpc_desc}")
                                    print(f"{bcolors.YELLOW}{bcolors.BOLD}App ID: {bcolors.WHITE}-------> {bcolors.OKCYAN}{rpc_application_id}")

                                    input(f"{bcolors.UNBOLD}{bcolors.WHITE}\nHit enter to go back and decide what to do... ")
                                    ConfigCheck()
                        except FileNotFoundError:
                            clear()
                            print(
                        """
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
║ ❌ Config file missing! please relaunch the application! ❌ ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
                        """)
                            time.sleep(5)
                            quit()
            else:
                Q_ChangeRPC_InvalidReply()

        except FileNotFoundError: # We assume URL was never been given to use.

            SetupNewRPC()

    def Q_ChangeRPC_InvalidReply():
        clear()
        print(
"""
╔═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
║ ❌    Invalid reply    ❌ ║
╚═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
Your choices are:
- 1 (use)
- 2 (change)
- 3 (View the current Rich Presence)""")
        time.sleep(3)
        ConfigCheck()

    def SplashScreen():
        clear()
        print(
    f"""{bcolors.TAG}{bcolors.BOLD}
    ╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗
    ║          🎫     {bcolors.BOLD}Rich Presence Tool     🎫           ║
    ║ {bcolors.WHITE}Setting A Rich PresenCe on your profile, simplified {bcolors.TAG}║
    ║                                                     ║
    ║ {bcolors.RED}Not affiliated with {bcolors.BLURPLE}Discord Inc. {bcolors.RED}in any way         {bcolors.TAG}║
    ╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
    {bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}Rich Presence{bcolors.TAG}] {bcolors.OKGREEN}Initialising . . .
            """)

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
            # Let’s use this function to check if any process with ‘chrome’ substring in name is running or not i.e.
            # Check if any chrome process was running or not.
            if checkIfProcessRunning('Discord'):
                clear()
                print(f'{bcolors.TAG}{bcolors.BOLD}[{bcolors.WHITE}RichPresence{bcolors.TAG}] {bcolors.RED}Tango {bcolors.OKGREEN}spotted{bcolors.WHITE}! Discord is {bcolors.OKGREEN}running{bcolors.WHITE}!')

                try:
                    LaunchRichPresence()
                
                except exceptions.InvalidPipe:
                    # need to wait a bit before Discord is reading rich presence from any game / app
                    # let's wait max 20 seconds so we give Discord client the time before we shoot our rich presence.
                    print('[RichPresence] Waiting for Discord to listen for rich presence . . .')
                    time.sleep(20)

                    # Let's give it a shot now, launching Rich Presence
                    try:
                        LaunchRichPresence()
                    except exceptions.PyPresenceException:
                        main()

            else:
                print('[RichPresence] Waiting for Discord to launch . . .')

                time.sleep(5) # don't spam the console, print the above line only per 5 seconds.

                # re-check every 5 seconds by calling the function over until Discord is spotted and running.
                main()

    def RPCWithoutButtons(rpc_application_id, rpc_title, rpc_desc):
            client_id = rpc_application_id
            RPC = Presence(client_id)  # Initialize the client class
            RPC.connect() # Start the handshake loop

            RichPresenceData = (RPC.update(state=rpc_title, details=rpc_desc))  # Set the presence
            
            print(
        f"""{bcolors.OKGREEN}
        ╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
        ║ ✅{bcolors.BOLD}{bcolors.WHITE} Looking good! {bcolors.TAG}RichPresence {bcolors.WHITE}is {bcolors.OKGREEN}UP {bcolors.WHITE}and {bcolors.YELLOW}shining {bcolors.WHITE}on your profile! ✅ {bcolors.OKGREEN}  ║
        ╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
        {bcolors.YELLOW}If not, check if you have the following option enabled in Discord:
        {bcolors.BOLD}{bcolors.WHITE}User Settings > Activity Status > Display current activity as a status message.
        """)
            print(f"{bcolors.BOLD}{bcolors.YELLOW}These settings were applied on your Rich Presence:")
            print(f"{bcolors.YELLOW}{bcolors.BOLD}Title: {bcolors.WHITE}--------> {bcolors.OKCYAN}{rpc_title}")
            print(f"{bcolors.YELLOW}{bcolors.BOLD}Description: {bcolors.WHITE}--> {bcolors.OKCYAN}{rpc_desc}")
            print(f"{bcolors.YELLOW}{bcolors.BOLD}App ID: {bcolors.WHITE}-------> {bcolors.OKCYAN}*censored*")
            
            while True:  # The presence will stay on as long as the program is running
                time.sleep(15) # Can only update rich presence every 15 seconds

    def RPC1button(rpc_application_id, rpc_title, rpc_desc, btnlbl1, btnurl1):
            client_id = rpc_application_id
            RPC = Presence(client_id)  # Initialize the client class
            RPC.connect() # Start the handshake loop

            click_me = [{"label": f"{btnlbl1}", "url": f"{btnurl1}"}]

            RichPresenceData = (RPC.update(state=f"{rpc_title}", details=f"{rpc_desc}", buttons=click_me))  # Set the presence
            
            print(
        f"""{bcolors.OKGREEN}
        ╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
        ║ ✅{bcolors.BOLD}{bcolors.WHITE} Looking good! {bcolors.TAG}RichPresence {bcolors.WHITE}is {bcolors.OKGREEN}UP {bcolors.WHITE}and {bcolors.YELLOW}shining {bcolors.WHITE}on your profile! ✅ {bcolors.OKGREEN}  ║
        ╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
        {bcolors.YELLOW}If not, check if you have the following option enabled in Discord:
        {bcolors.BOLD}{bcolors.WHITE}User Settings > Activity Status > Display current activity as a status message.
        """)
            print(f"{bcolors.BOLD}{bcolors.YELLOW}These settings were applied on your Rich Presence:")
            print(f"{bcolors.YELLOW}{bcolors.BOLD}Title: {bcolors.WHITE}--------> {bcolors.OKCYAN}{rpc_title}")
            print(f"{bcolors.YELLOW}{bcolors.BOLD}Description: {bcolors.WHITE}--> {bcolors.OKCYAN}{rpc_desc}")
            print(f"{bcolors.YELLOW}{bcolors.BOLD}App ID: {bcolors.WHITE}-------> {bcolors.OKCYAN}*****************")
            print(f"{bcolors.YELLOW}{bcolors.BOLD}Buttons:")
            print(f"{bcolors.YELLOW}{bcolors.BOLD}First Button Label: {bcolors.WHITE}--> {bcolors.OKCYAN}{btnlbl1}")
            print(f"{bcolors.YELLOW}{bcolors.BOLD}First Button Shared URL: {bcolors.WHITE}--> {bcolors.OKCYAN}{btnurl1}")

            while True:  # The presence will stay on as long as the program is running
                time.sleep(15) # Can only update rich presence every 15 seconds

    def RPC2buttons(rpc_application_id, rpc_title, rpc_desc, btnlbl1, btnurl1, btnlbl2, btnurl2):
            client_id = rpc_application_id
            RPC = Presence(client_id)  # Initialize the client class
            RPC.connect() # Start the handshake loop

            click_me = [{"label": f"{btnlbl1}", "url": f"{btnurl1}"}, {"label": f"{btnlbl2}", "url": f"{btnurl2}"}]

            RichPresenceData = (RPC.update(state=f"{rpc_title}", details=f"{rpc_desc}", buttons=click_me))  # Set the presence
            
            print(
        f"""{bcolors.OKGREEN}
        ╔═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╗                        
        ║ ✅{bcolors.BOLD}{bcolors.WHITE} Looking good! {bcolors.TAG}RichPresence {bcolors.WHITE}is {bcolors.OKGREEN}UP {bcolors.WHITE}and {bcolors.YELLOW}shining {bcolors.WHITE}on your profile! ✅ {bcolors.OKGREEN}  ║
        ╚═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═─═╝
        {bcolors.YELLOW}If not, check if you have the following option enabled in Discord:
        {bcolors.BOLD}{bcolors.WHITE}User Settings > Activity Status > Display current activity as a status message.
        """)
            print(f"{bcolors.BOLD}{bcolors.YELLOW}These settings were applied on your Rich Presence:")
            print(f"{bcolors.YELLOW}{bcolors.BOLD}Title: {bcolors.WHITE}--------> {bcolors.OKCYAN}{rpc_title}")
            print(f"{bcolors.YELLOW}{bcolors.BOLD}Description: {bcolors.WHITE}--> {bcolors.OKCYAN}{rpc_desc}")
            print(f"{bcolors.YELLOW}{bcolors.BOLD}App ID: {bcolors.WHITE}-------> {bcolors.OKCYAN}*****************")
            print(f"{bcolors.YELLOW}{bcolors.BOLD}Buttons:")
            print(f"{bcolors.YELLOW}{bcolors.BOLD}First Button Label: {bcolors.WHITE}--> {bcolors.OKCYAN}{btnlbl1}")
            print(f"{bcolors.YELLOW}{bcolors.BOLD}First Button Shared URL: {bcolors.WHITE}--> {bcolors.OKCYAN}{btnurl1}")
            print(f"{bcolors.YELLOW}{bcolors.BOLD}Second Button Label: {bcolors.WHITE}--> {bcolors.OKCYAN}{btnlbl2}")
            print(f"{bcolors.YELLOW}{bcolors.BOLD}Second Button Shared URL: {bcolors.WHITE}--> {bcolors.OKCYAN}{btnurl2}")

            while True:  # The presence will stay on as long as the program is running
                time.sleep(15) # Can only update rich presence every 15 seconds

    def LaunchRichPresence():
        try:
            open('RPC_Config.ini', 'r')
            config.read('RPC_Config.ini')

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
            quit()

    main()
except KeyboardInterrupt:
    quit()