# rickroll

A python script for the rickroll prank. It relies on Twilio's infrastructure to request for the audio and play it to the 'target'.

## what the script does

The script simply calls the 'target number', the guy to be pranked, from a twilio allocated phone number, and plays the entire Rick Astley's 'Never Gonna Give You Up' song, if s/he doesn't hang up for some reason.

## Prerequisites

Obviously you need to have python installed on your PC.

You need a Twilio trial account or paid account. Sign Up at twilio.com.

Copy the account_SID and auth_token from your twilio account and intialize them in the code.(They are currently left blank). Intialize twilio_number to the number that given to you by Twilio. Then set the target_number to your phone number ,if you want to do some dry runs first, or set the phone number to the actual person you want to rickroll if you like to hit the ground running. Make sure you intialize the phone numbers inclusive of your area codes e.g +254713412345 or +12055515516

You need to install the Twilio package

```console
$pip install twilio
```

## Running the script

After intializing everything simply the script by running the call.py

```console
$python call.py
```

## Outro

Hopeful everything works, if doesn't feel free to report the issue.
I spend almost 13 hours perfecting this script, 90% of which was spent trying to find a reliable and FREE way to host the Never Gonna Give Up song. I doubt I will be spend this much time on another hobby script
