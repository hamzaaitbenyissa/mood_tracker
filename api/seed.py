# let's create a seed.py file that will seed the mood_entries with some data

from main import Mood, MoodEntry, mood_entries

mood_entries.append(MoodEntry(mood=Mood.HAPPY, timestamp="2021-01-01"))
