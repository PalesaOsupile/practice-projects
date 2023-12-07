import matplotlib.pyplot as plt
from datetime import datetime

# Function to record mood entry
def record_mood():
    mood = input("Enter your mood (Happy/Sad/Neutral): ").lower()
    return mood, datetime.now()

# Function to display mood statistics
def display_mood_statistics(moods):
    mood_counts = {mood: moods.count(mood) for mood in set(moods)}
    labels = mood_counts.keys()
    counts = mood_counts.values()

    plt.figure(figsize=(8, 6))
    plt.bar(labels, counts, color=['green', 'red', 'gray'])
    plt.title('Mood Tracker Statistics')
    plt.xlabel('Moods')
    plt.ylabel('Count')
    plt.show()

# Main program
mood_entries = []

while True:
    action = input("Do you want to record your mood? (yes/no): ").lower()

    if action == 'yes':
        mood, timestamp = record_mood()
        mood_entries.append((mood, timestamp))
        print("Mood recorded successfully!")

    elif action == 'no':
        display_mood_statistics([entry[0] for entry in mood_entries])
        break

    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
