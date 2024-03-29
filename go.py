import random
import string
import time
import asyncio
import pyautogui
import discord

# Function to generate a random email
def generate_random_email():
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    email = f"malikolop{random_suffix}@example.com"
    return email

# Function to automate Gmail signup using mouse movements
def signup_to_gmail(email, password, first_name, last_name, birth_month, birth_day, birth_year):
    # Open Chrome (Assuming it's already installed and pinned to the taskbar)
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('chrome')
    pyautogui.press('enter')
    time.sleep(5)

    # Click on the address bar to enter URL
    pyautogui.click(x=108, y=62)  # Adjust these coordinates based on your screen resolution
    time.sleep(1)

    # Enter the URL
    pyautogui.write("https://accounts.google.com/SignUp?service=mail")
    pyautogui.press('enter')
    time.sleep(10)

    # Enter first name
    pyautogui.click(x=400, y=350)  # Adjust these coordinates based on your screen resolution
    pyautogui.write(first_name)

    # Enter last name
    pyautogui.click(x=400, y=410)  # Adjust these coordinates based on your screen resolution
    pyautogui.write(last_name)

    # Enter birth date
    pyautogui.click(x=400, y=490)  # Adjust these coordinates based on your screen resolution
    pyautogui.write(birth_month)
    pyautogui.press('tab')
    pyautogui.write(birth_day)
    pyautogui.press('tab')
    pyautogui.write(birth_year)

    # Click gender dropdown
    pyautogui.click(x=400, y=540)  # Adjust these coordinates based on your screen resolution
    time.sleep(1)

    # Choose male
    pyautogui.move(0, 30)  # Move down to male option
    pyautogui.click()
    time.sleep(1)

    # Click on "Use my current email address instead" option
    pyautogui.click(x=400, y=600)  # Adjust these coordinates based on your screen resolution
    time.sleep(1)

    # Enter custom email address
    pyautogui.click(x=400, y=650)  # Adjust these coordinates based on your screen resolution
    pyautogui.write(email)
    pyautogui.press('enter')
    time.sleep(5)

    # Enter password
    pyautogui.click(x=400, y=700)  # Adjust these coordinates based on your screen resolution
    pyautogui.write(password)
    pyautogui.press('tab')
    pyautogui.write(password)
    pyautogui.press('enter')
    time.sleep(5)

    # Click Next
    pyautogui.click(x=400, y=750)  # Adjust these coordinates based on your screen resolution
    time.sleep(10)

# Function to send message to Discord channel
async def send_discord_message(channel_id, message):
    client = discord.Client()
    await client.login("YOUR_DISCORD_BOT_TOKEN")
    channel = client.get_channel(channel_id)
    await channel.send(message)
    await client.logout()

# Main function
def main():
    discord_channel_id = "YOUR_DISCORD_CHANNEL_ID"
    password = "1998loveme"
    first_name = "John"
    last_name = "Doe"
    birth_month = "01"
    birth_day = "01"
    birth_year = "1980"

    # Generate random email
    email = generate_random_email()

    # Automate Gmail signup using mouse movements
    signup_to_gmail(email, password, first_name, last_name, birth_month, birth_day, birth_year)

    # Send message to Discord channel
    discord_message = f"Randomly generated email: {email}, Password: {password}"
    asyncio.run(send_discord_message(discord_channel_id, discord_message))

if __name__ == "__main__":
    main()
