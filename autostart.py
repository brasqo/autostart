#! python3
import subprocess
import webbrowser
import time

"""
This script will open up all of my startup programs as wanted
"""

#print(webbrowser._browsers)

#registering the FF browser path, needed because webrowser not seeing FF
firefox_path = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path),1)

# browser paths, use fwd slash per stackoverflow - works!
chromeBrowser = "c:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
firefoxBrowser = 'c:/Program Files (x86)/Mozilla Firefox/firefox.exe'

# using fwd slash per stackoverflow, works for browser
simplenoteProg = "c:/Program Files (x86)/Simplenote/Simplenote.exe"
outlookProg = "c:/Program Files (x86)/Microsoft Office/root/Office16/OUTLOOK.EXE"

# websites
pandoraSite = "https://www.pandora.com/station/play/3188915275042472173"
cwSite = "http://cw.fullyinvolvedsolutions.com/?company=bez"
slackSite = "https://getfullyinvolved.slack.com/messages/C1ZKR1VFD"
screenconnectSite = "https://remote.fullyinvolvedsolutions.com/Host#Access/FIS%20-%20Office//275d92c1-fd7c-4cdc-b96e-2a8e56b467aa"

#defining firefox after registering above
ff = webbrowser.get('firefox')


def main():
    '''Opens Chrome with 3 tabs: Pandora and 2 CW tabs'''
    print('.')
    print('..')
    print('...')

    webbrowser.open(pandoraSite) #opens a new browser
    print('Opening Chrome w/ a Pandora Tab...')
    time.sleep(4)
    webbrowser.open_new_tab(cwSite) #opens new tab
    print('Opening new tab: "ConnectWise"...')
    time.sleep(4)
    webbrowser.open_new_tab(cwSite)  # opens new tab
    print('Opening another new tab: "ConnectWise"...')

    print('.')
    print('..')
    print('...')

    print('Finished opening all programs.')


def openFF():
    '''Opens firefox with 3 tabs: slack and screenconnect'''
    print('.')
    print('..')
    print('...')

    ff.open_new_tab(slackSite)
    print('Opening Firefox w/ a Slack Tab...')
    time.sleep(4)
    ff.open_new_tab(screenconnectSite)
    print('Opening new Firefox tab: "ScreenConnect"...')


def openProg():
    '''Opens wanted programs via subprocess'''
    print('.')
    print('..')
    print('...')
    time.sleep(4)
    subprocess.Popen(simplenoteProg)
    print('Opening program: "SimpleNote"...')

    time.sleep(4)
    subprocess.Popen(outlookProg)
    print('Opening program: "Outlook"...')


if __name__ == '__main__':
    openFF()
    time.sleep(4)
    openProg()
    time.sleep(4)
    main()