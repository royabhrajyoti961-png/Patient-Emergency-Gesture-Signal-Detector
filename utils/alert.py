from twilio.rest import Client
import pygame

# ---------------- SOUND ----------------
pygame.mixer.init()

def play_alert():
    pygame.mixer.music.load("assets/alarm.wav")
    pygame.mixer.music.play()


# ---------------- TWILIO CONFIG ----------------
ACCOUNT_SID = "YOUR_ACCOUNT_SID"
AUTH_TOKEN = "YOUR_AUTH_TOKEN"
TWILIO_NUMBER = "+1234567890"
NURSE_NUMBER = "+91XXXXXXXXXX"

client = Client(ACCOUNT_SID, AUTH_TOKEN)


# ---------------- SMS FUNCTION ----------------
def send_sms(message):
    try:
        client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=NURSE_NUMBER
        )
        print("SMS SENT:", message)
    except Exception as e:
        print("SMS ERROR:", e)


# ---------------- MAIN ALERT ----------------
def trigger_alert(message):
    play_alert()
    send_sms(f"🚨 ALERT: {message}")
