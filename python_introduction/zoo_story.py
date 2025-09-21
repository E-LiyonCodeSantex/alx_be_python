# Prompt the user for words
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter one more adjective: ")
adjective4 = input("Enter a final adjective: ")
adjective5 = input("enter one more adjective: ")
animal = input("Name an animal: ")
activity = input("Enter a verb ending in -ing: ")
weather = input("What's the weather like today (sunny, rainy, cloudy)? ")

# Conditional variation based on weather
if weather.lower() == "sunny":
    setting = "The sun was shining brightly"
elif weather.lower() == "rainy":
    setting = "Raindrops danced on the leaves"
elif weather.lower() == "cloudy":
    setting = "The sky was a soft shade of gray"
else:
    setting = "The weather was quite mysterious"

# Build the story
story = f"""
in the {adjective1} house, I went to the kitchen. {setting}, and I saw {adjective2} and wodered.
I experience a crazy {adjective3} {animal} watching me while {activity} from the pot.
Then, I spotted a dengerious {adjective4} ewi liping in the sun.
What a misterious, cogitive and {adjective5} experience!
"""

# Display the final story
print("\nHere’s your Mad Libs story:")
print(story)
