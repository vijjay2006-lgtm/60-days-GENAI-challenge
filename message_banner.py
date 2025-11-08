import pyautogui
import time

print("🟢 Script started... waiting 3 seconds before showing banner.")
time.sleep(3)

message = "🎉 pyautogui — one week completed — pyautogui completed in VS Code 🎉"
print("🟢 Showing alert message now...")

pyautogui.alert(
    text=message,
    title="WhatsApp Broadcast Simulation 💚",
    button="OK"
)

print("✅ Message displayed successfully.")
import pywhatkit
pywhatkit.sendwhatmsg("+917231832211",
                      "🎉 pyautogui — one week completed — pyautogui completed in VS Code 🎉",
                      19, 45)
                      