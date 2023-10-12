#!/usr/bin/env python

# Prompt the user for input
user_input = input(" (e.g., google.com): ")

# Check if the input is "google.com"
if user_input == "google.com":
    modified_input = user_input.replace(".com", "")
    print(f"You're correct and the site name is {modified_input}!")
else:
    print("You're incorrect.")
