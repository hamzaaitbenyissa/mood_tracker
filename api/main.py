# let's build a fast rest api to track the mood of a user
import dataclasses
import enum
from enum import Enum
from fastapi import FastAPI


class Mood(Enum):
    HAPPY = enum.auto()
    SAD = enum.auto()
    ANGRY = enum.auto()
    CONFUSED = enum.auto()
    SICK = enum.auto()


@dataclasses.dataclass
class MoodEntry:
    mood: Mood
    timestamp: str

    def __dict__(self):
        return {"mood": self.mood.name, "timestamp": self.timestamp}

    def __str__(self):
        return f"{self.mood.name} on {self.timestamp}"

    def __repr__(self):
        return self.__str__()


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to the mood tracker"}


# for the moment we will use a runtime memory to store the mood entries
mood_entries: list[MoodEntry] = [MoodEntry(mood=Mood.HAPPY, timestamp="2021-01-01")]


@app.post("/mood")
def mood_entry(entry: MoodEntry):
    mood_entries.append(entry)
    return {"message": "Mood entry added"}


@app.get("/moods/")
def moods():
    return mood_entries
