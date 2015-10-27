WDWNTNowTasks is a Python project for querying the WDWNT Now API as scheduled tasks.

# Usage

Before executing, be sure to run the following:
1. `sudo apt-get update && sudo apt-get upgrade`<br>
2. `sudo apt-get install python-setuptools python-dev libffi-dev`<br>
3. `sudo easy_install pip`<br>
4. `sudo pip install tweepy`<br>
5. `sudo pip install requests`<br>
6. `sudo pip install requests[security]`<br>

## Wait Times

python main.py 'waittime' 'Current wait before the next expedition:' 26068

returns
> "Current wait before next expedition: 40 minutes"
