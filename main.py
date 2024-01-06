import os
import colorama
import sys
import pytube
import subprocess
import webbrowser
import aiohttp
import asyncio
import time
import requests
import threading
from colorama import Fore

colorama.init()

async def visit_site(url, num_visits):
    async with aiohttp.ClientSession() as session:
        for i in range(1, num_visits + 1):
            async with session.get(url) as response:
                if response.status == 200:
                    print(f"Visited {url}.")
                    print("Now Running Script Press Ctrl+C to Stop The Process..")
                else:
                    print(f"Failed to visit {url} (status code: {response.status}).")
            await asyncio.sleep(1)  # Optional delay to control the rate of visits

async def curlbot(url, num_tasks):
    tasks = [visit_site(url, num_tasks) for _ in range(num_tasks)]
    await asyncio.gather(*tasks)

def selfbot():
    url = input("Enter the URL to visit: ")

    if not url.startswith(("http://", "https://")):
        print("That's not a valid URL.")
        return

    num_tasks = 5  # Number of concurrent tasks

    while True:
        try:
            asyncio.run(curlbot(url, num_tasks))
        except KeyboardInterrupt:
            print("\nVisits stopped.")
            break
def new_update(false_url):
    print("There's a new update.")
    try:
        response = requests.get(false_url)
        if response.status_code == 200:
            new_url = response.text.strip()
            webbrowser.open(new_url)
        else:
            print("Failed to fetch data from the false URL.")
    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching data:", e)

def main():
    url = "https://rentry.co/w455i/raw"
    false_url = "https://rentry.co/yeu42/raw"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text.strip().lower()
            if data == "true":
                onstart()
            elif data == "false":
                new_update(false_url)
            else:
                print("Invalid response in the raw text.")
        else:
            print("Failed to fetch data from the URL.")
    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching data:", e)
def nitrogen():
    nitrogen_path = os.path.join(os.path.dirname(__file__), "Tools", "nitrogen.py")
    try:
        if os.name == "nt":  # Windows
            subprocess.Popen(["python", nitrogen_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            subprocess.Popen(["python", nitrogen_path], start_new_session=True)
    except Exception as e:
        print(f"Error running nitrogen.py: {e}")
    else:
        print("running nitrogen")



def stop_spam():
    # Function to stop webhook spamming when Enter is pressed
    input("\nPress Enter to stop the webhook spamming.")
    print('\nWebhook spamming stopped.')
    global stop_spamming
    stop_spamming = True

def spam_webhook(webhook_url, content):
    print('\nSpamming webhook. Press Enter to stop.')
    global stop_spamming
    stop_spamming = False
    try:
        # Start the spamming in a separate thread
        thread = threading.Thread(target=do_spam, args=(webhook_url, content))
        thread.start()

        # Start the input handling in the main thread
        stop_spam()

        # Wait for the spamming thread to finish before continuing
        thread.join()
    except KeyboardInterrupt:
        # Handle the case when Enter is pressed to stop spamming
        print('\nWebhook spamming stopped.')

def do_spam(webhook_url, content):
    global stop_spamming
    while not stop_spamming:
        try:
            response = requests.post(webhook_url, json={'content': content})

            if response.status_code == 204:
                print("Sent Message")
            else:
                print(f"Failed to send webhook request. Status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred while sending the webhook request: {e}")
            break

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break


def delete_webhook(webhook_url):
    try:
        response = requests.delete(webhook_url)

        if response.status_code == 204:
            print("Webhook deleted successfully.")
        else:
            print(f"Failed to delete webhook. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while deleting the webhook: {e}")

def expand_url(url):
    try:
        redirect_history = []
        response = requests.head(url, allow_redirects=True)
        while response.history:
            redirect_history.append(response.url)
            response = requests.head(response.url, allow_redirects=True)
        redirect_history.append(response.url)

        print("Redirection history:")
        for i, redirect in enumerate(redirect_history):
            print(f"{i + 1}. {redirect}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while expanding the URL: {e}")

def loading(duration):
    start_time = time.time()
    while True:
        for i in range(4):
            sys.stdout.write('\rLoading' + '.' * i)
            sys.stdout.flush()
            time.sleep(0.5)
        if time.time() - start_time >= duration:
            break

    sys.stdout.write('\n')  # Add a newline character to return to normal output

def premium(buy):
    webbrowser.open(buy)

buy = "https://evanyx.pro/premium"

def discord(invite):
    webbrowser.open(invite)

invite = "https://discord.gg/USEgrTUJVN"


def menu2():
    global onstart2
    white = Fore.WHITE
    magenta = Fore.MAGENTA

    print(f"""
    {white}███████╗██╗   ██╗ █████╗ ███╗   ██╗██╗   ██╗██╗  ██╗
    {white}██╔════╝██║   ██║██╔══██╗████╗  ██║╚██╗ ██╔╝╚██╗██╔╝
    {white}█████╗  ██║   ██║███████║██╔██╗ ██║ ╚████╔╝  ╚███╔╝ 
    {white}██╔══╝  ╚██╗ ██╔╝██╔══██║██║╚██╗██║  ╚██╔╝   ██╔██╗ 
    {white}███████╗ ╚████╔╝ ██║  ██║██║ ╚████║   ██║   ██╔╝ ██╗
    {white}╚══════╝  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝
    Owner: Thisco
    Co Owner: Apethym
    {magenta}
    [help] [ytdwn] [discord] [exit]

    [16] Back                            [20] coming later        [24] coming later        [28] coming later
    [17] Protect Your Discord Account    [21] coming later        [25] coming later        [29] coming later
    [18] Site Visit Bot                  [22] coming later        [26] coming later        [30] coming later
    [19] coming later                    [23] coming later        [27] coming later        [31] coming later

    {white}
    """)

    command = input(">")

    if command == "18":
        selfbot()
        onstart2()

    # Youtube Video Downloader
    if command.lower() == "ytdwn":
        url = input("Enter the YouTube video URL: ")
        option = input("Enter 'mp3' for audio or 'mp4' for video: ")

        if option == "mp3":
            video = pytube.YouTube(url)
            audio_stream = video.streams.get_audio_only()
            filename = audio_stream.default_filename
            audio_stream.download()
            print("Saved in path:", os.path.abspath(filename))
        elif option == "mp4":
            video = pytube.YouTube(url)
            video_stream = video.streams.get_highest_resolution()
            filename = video_stream.default_filename
            video_stream.download()
            print("Saved in path:", os.path.abspath(filename))
        else:
            print("Invalid option. Please choose 'mp3' or 'mp4'.")

        time.sleep(2)
        onstart2()

    #Discord
    if command.lower() == "discord":
        open_discord()
        time.sleep(1)
        onstart()

    if command == "16":
        print("Going Back To Main Menu..")
        time.sleep(1)
        onstart()

    # Token Guard
    if command == "17":
        os.system("start https://github.com/ZaikoARG/TokenGuard")
        print("Credits to ZaikoARG")
        time.sleep(2)
        onstart2()

    if command == "19":
        print("coming later")
        time.sleep(1)
        onstart2()
def menu():
    global onstart
    white = Fore.WHITE
    magenta = Fore.MAGENTA

    print(f"""

    {white}███████╗██╗   ██╗ █████╗ ███╗   ██╗██╗   ██╗██╗  ██╗
    {white}██╔════╝██║   ██║██╔══██╗████╗  ██║╚██╗ ██╔╝╚██╗██╔╝
    {white}█████╗  ██║   ██║███████║██╔██╗ ██║ ╚████╔╝  ╚███╔╝ 
    {white}██╔══╝  ╚██╗ ██╔╝██╔══██║██║╚██╗██║  ╚██╔╝   ██╔██╗ 
    {white}███████╗ ╚████╔╝ ██║  ██║██║ ╚████║   ██║   ██╔╝ ██╗
    {white}╚══════╝  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝
    Owner: Thisco
    Co Owner: Apethym
    {magenta}
    [help] [ytdwn] [discord] [exit]

    [0] Rat Stealer        [4] DDos                         [8] Token BruteForce     [12] House Changer
    [1] Ip Lookup          [5] Token Checker                [9] Ip Pinger            [13] Nitro Generator
    [2] Webhook Deleter    [6] Token Generator              [10] URL Expander        [14] Account Nuker
    [3] Webhook Spammer    [7] ID To Token (First Part)     [11] Stresser            [15] More...

    {white}
    """)

    command = input(">")
  
    # Youtube Video Downloader
    if command.lower() == "ytdwn":
        url = input("Enter the YouTube video URL: ")
        option = input("Enter 'mp3' for audio or 'mp4' for video: ")

        if option == "mp3":
            video = pytube.YouTube(url)
            audio_stream = video.streams.get_audio_only()
            filename = audio_stream.default_filename
            audio_stream.download()
            print("Saved in path:", os.path.abspath(filename))
        elif option == "mp4":
            video = pytube.YouTube(url)
            video_stream = video.streams.get_highest_resolution()
            filename = video_stream.default_filename
            video_stream.download()
            print("Saved in path:", os.path.abspath(filename))
        else:
            print("Invalid option. Please choose 'mp3' or 'mp4'.")

        time.sleep(2)
        onstart()



    #discord
    if command.lower() == "discord":
        open_discord()
        time.sleep(1)
        onstart()

    #15 more
    if command == "15":
        time.sleep(1)
        onstart2()

    if command == "14":
        nuke = os.path.join(os.path.dirname(__file__), "Tools", "accountnuker.py")
        os.startfile(nuke)
        time.sleep(1)
        onstart()
    #Nitro Generator + Checker
    if command == "13":
        nitrogen()
        time.sleep(1)
        onstart()
    #Hypesquad Changer
    if command == "12":
        Hype = os.path.join(os.path.dirname(__file__), "Tools", "Hypesquad.py")
        os.startfile(Hype)
        time.sleep(1)
        onstart()

    #Stresser
    if command == "11":
        Stress = os.path.join(os.path.dirname(__file__), "Tools", "Stresser.py")
        os.startfile(Stress)
        time.sleep(1)
        onstart()

    #ID To Token
    if command == "7":
        TokenID = os.path.join(os.path.dirname(__file__), "Tools", "IDToken.py")
        os.startfile(TokenID)
        time.sleep(1)
        onstart()

    # Expand URL
    if command == "10":
        url_to_expand = input("Enter the URL you want to expand: ")
        expand_url(url_to_expand)
        input("Press Enter to continue to the main menu..")
        onstart()

    #Ip Pinger
    if command == "9":
        IpPinger = os.path.join(os.path.dirname(__file__), "Tools", "Pinger.bat")
        os.startfile(IpPinger)
        time.sleep(1)
        onstart()

    #Token Brute Force
    if command == "8":
        TokenBF = os.path.join(os.path.dirname(__file__), "Tools", "TokenBF.py")
        os.startfile(TokenBF)
        time.sleep(1)
        onstart()
    #Spam Webhook
    if command == "3":
        webhook_url = input("Enter the URL of the webhook you want to spam: ")
        content = input("Enter the text you want it to be spammed with: ")
        spam_webhook(webhook_url, content)
        onstart()

    #Token Generator
    if command == "5":
        print("Coming Later")
        time.sleep(1)
        onstart()
    #Token Checker
    if command == "5":
        print("Coming Later")
        time.sleep(1)
        onstart()
    #Rat Builder
    if command == "0":
        python_path = sys.executable
        builder_path = os.path.join(os.path.dirname(__file__), "builder.py")
        os.system(f"{python_path} {builder_path}")
        time.sleep(1)
        onstart()
    #Webhook Deleter
    elif command == "2":
        print("Delete a webhook")
        webhook_url = input("Enter the URL of the webhook you want to delete: ")
        # Use threading to avoid blocking the main menu while the request is made
        thread = threading.Thread(target=delete_webhook, args=(webhook_url,))
        thread.start()
        time.sleep(1)
        input("Press Enter to continue to the main menu..")
        onstart()
   #DDos - UDP Flood Attack
    if command == "4":
        ddos = os.path.join(os.path.dirname(__file__), "Tools", "DDOS.py")
        os.startfile(ddos)
        time.sleep(1)
        onstart()


    #discord
    if command.lower() == "discord":
        open_discord()
        time.sleep(1)

    #exit
    if command.lower() == "exit":
        print("> Exiting Evanyx..")
        time.sleep(1)
        sys.exit(0)
    #help
    if command.lower() == "help":
        time.sleep(0.2)
        print("""> Contact :

            Discord: Thisco
            Discord: Apethym

        """)
        input("Press Enter To Exit Help")
        onstart()

    #Ip Lookup
    if command == "1":
        iplookup_path = os.path.join(os.path.dirname(__file__), "Tools", "iplookup.exe")
        os.startfile(iplookup_path)
        time.sleep(1)
        onstart()

def open_discord():
    discord_invite_link = "https://discord.gg/USEgrTUJVN"
    webbrowser.open(discord_invite_link)
def onstart():
    cmd = 'mode 120,28'
    os.system(cmd)
    os.system("cls && title Evanyx - Multitool")
    menu()

def onstart2():
    cmd = 'mode 120,28'
    os.system(cmd)
    os.system("cls && title Evanyx - Multitool")
    menu2()

main()