# find_a_cpu
I'd like to find this here CPU; a Ryzen 5 5600X.

# Installation
If you want to run this locally, clone this repository.

Navigate to the `find_a_cpu` directory and run:
```
pip install -r requirements.txt
```

## Twilio Account
We're using the [Twilio Python library]() to send updates, so you'll need to sign up for a free account. Once verified, you'll need to verify your own number (the one we'll be sending notifications _to_) and create a Twilio-generated number (the one we'll be sending notifications _from_). Also, gather your `Twilio Account SID` and your `Auth Token` from the account dashboard.

Replace these lines with your `Twilio Account SID` and `Auth Token` data:
```
find_a_cpu.py:5,6:
account = TWILIO_ACCOUNT_SID
token = TWILIO_AUTH_TOKEN
```

Replace these lines with your verified number and the Twilio-generated number:
```
find_a_cpu.py:26,27,39,40:
to = YOUR_VERIFIED_NUMBER,
from_ = TWILIO_NUMBER,
```

## Scheduling
Use your scheduler of choice! Because I'm on a Mac, I ended up using `launchd` again:
```
~/Library/LaunchAgents/<job.plist>:
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>find_a_cpu</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Users/michaelkopsho/.pyenv/shims/python3</string>
        <string>/Users/michaelkopsho/learning/find_a_cpu.py</string>
    </array>
    <key>StartInterval</key>
    <integer>60</integer>
    <key>StandardOutPath</key>
    <string>/Users/michaelkopsho/logs/find_a_cpu_out.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/michaelkopsho/logs/find_a_cpu_error.log</string>
</dict>
</plist>
```

Save that, then load the job into the scheduler (your UID can be found by typing `id` into the command line):
```
launchctl bootstrap gui/UID ~/Library/LaunchAgents/<job.plist>
```

This runs the program every 60 seconds; season to taste.
