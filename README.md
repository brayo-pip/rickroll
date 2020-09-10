# rickroll

A python script for the rickroll prank. It relies on Twilio's infrastructure to request for the audio and play it to the 'target'.

## what the script does

The script simply calls the 'target number', the guy to be pranked, from a twilio allocated number, and plays the entire Rick Astley's 'Never Gonna Give You Up' song, if s/he doesn't hang up for some reason.

## Prerequisites

Obviously you need to have python installed on your PC.

You need a Twilio trial account or pay for it whatever. Sign Up at twilio.com.

Copy the account_SID and auth_token from your twilio account and intialize them in the code.(They are currently left blank). Intialize twilio_number to the number that given to you by Twilio. Then set the target_number to your number ,if you want to do some dry runs first, or set the number to the actual person you want to rickroll if you like to hit the ground running.

You need to install the Twilio package

```console
$pip install twilio
```

## Running the script

After intializing everything simply the script by running the call.py

```console
$python call.py
```
