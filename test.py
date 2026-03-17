from win11toast import toast
from pathlib import Path

def dummy(args):
    option = args.get("user_input").get("selection")
    print(option)

def launch_notification():
    icon = {
        'src': Path('DiscordRPCT/icon.png').absolute().as_uri(),
        'placement': 'appLogoOverride'
    }
    i = toast(
        "Running in the system tray", 
        "Choose an option. Alternatively, ignore this notification",
        app_id='Discord Rich Presence', 
        icon=icon, 
        selection=['Open RPC', 'Pause status', 'Edit RPC'], 
        button='Submit',
        on_click=dummy
    )
    print(i.get("user_input"))
launch_notification()
while True:
    ""