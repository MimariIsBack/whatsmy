## whatsmy

This Python script retrieves and displays your system's IP address, MAC address, and DNS servers.

## Description

This script uses Python to fetch:
- Your public IP address
- Your local machine's MAC address
- DNS server details

It can be helpful for networking or troubleshooting issues on your machine.

## Installation

Ensure you have these installed. : 
Python3,
,Psutil
,Requests

## Usage

1. Clone this repository.
2. Open a terminal/command prompt in the directory where the script is located.
3. Run the script with:
   ```bash
   python script.py

## Important

Overview

This software may be incorrectly flagged by Windows Defender, VirusTotal, or other antivirus programs due to its behavior. It requests certain network-related information, including:

IP Address,

MAC Address,

DNS Server Information,

These requests are often used for legitimate purposes, such as improving network functionality or troubleshooting. However, because these actions can resemble those typically associated with malware or unauthorized software, they may trigger a false positive in antivirus scans.

## Why It Happens
Antivirus software uses patterns and heuristics to identify potential threats. Since some malicious software also requests similar information to perform harmful actions, any software that does the same may be mistakenly categorized as a virus or malware. This is a known issue that can occur with many legitimate programs that interact with network configurations or systems.

## What’s a False Positive?
Explanation

A false positive happens when your antivirus software thinks something is dangerous when it actually isn’t. It’s like your antivirus being overly cautious and mistakenly thinking a safe file or program is a virus or malware.

## Why Do False Positives Happen?

Antivirus software looks for patterns or behaviors that resemble things viruses do. But sometimes, regular, harmless programs might accidentally trigger these alarms. Here’s why that might happen:

Unusual behavior: If a program does something a little out of the ordinary—like checking your network settings or asking for your IP address—it might get flagged, even though it’s perfectly fine.

Code overlap: Sometimes, safe programs share similar code with known viruses, which can confuse the antivirus software.

Aggressive detection: Some antivirus programs are set to be extra sensitive, and when they see something they’re not familiar with, they’ll flag it just to be safe.

## Assurances
Please be assured that this software is completely safe to use and does not have any malicious intent. I respect user privacy and only request this information for necessary, harmless purposes related to the functionality of the executable which is networking or troubleshooting issues on your machine.
