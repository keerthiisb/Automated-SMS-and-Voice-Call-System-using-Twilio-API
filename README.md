# Automated-SMS-and-Voice-Call-System-using-Twilio-API
Built an automated communication system using Twilio API for sending SMS and making voice calls with status monitoring and retries.

1.Overview

This project demonstrates how to use the Twilio API to send automated SMS and make voice calls with status monitoring and retry mechanisms. The system sends SMS messages and makes voice calls with pre-recorded messages, ensuring reliable delivery and real-time communication.

2.Features

Send SMS: Sends an SMS message with a specified body to a target phone number.

Automated Voice Calls: Makes a phone call to a target number with a pre-recorded voice message using Twilio's Text-to-Speech (TTS) feature.

Status Monitoring: Monitors the call status and retries if necessary until the call is successfully completed.

3.Prerequisites

A Twilio account (sign up at Twilio).

Twilio SID and Auth Token from your Twilio console.

Twilio Python Library installed.

4.Setup

Obtain your Twilio SID and Auth Token from the Twilio console.

Replace the placeholder SID, Auth Token, and phone numbers in the script with your actual details.

SID - Your Twilio account SID.

token - Your Twilio authentication token.

from_ - The Twilio phone number you're sending the SMS and making the call from.

to - The recipient's phone number.

5.Code Explanation

Twilio Client Setup: The Client object is used to interact with the Twilio API by providing your SID and Auth Token.

SMS Sending: The client.messages.create() method is used to send an SMS with the specified content.

Voice Call: The client.calls.create() method is used to initiate a voice call. The message is sent as a twiml (Twilio Markup Language) that plays the pre-recorded message during the call.

Call Monitoring: The call status is checked every 25 seconds using client.calls(call_sid).fetch() to determine whether the call was answered or not. If not, the script retries.

Screenshots:

![1](https://github.com/user-attachments/assets/b67cc4a9-802e-43e4-8034-51002551cc87)

![2](https://github.com/user-attachments/assets/15536b73-feea-4807-88a4-c7c18ba95e17)

![3](https://github.com/user-attachments/assets/cb181c4c-b486-421d-8168-8a50785fed30)

![4](https://github.com/user-attachments/assets/16bdb4fe-636b-418f-bda4-723634d23faf)


