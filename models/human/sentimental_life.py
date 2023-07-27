from constants.sentimental_status import SentimentalStatus
from models.event.childbirth import Childbirth


class SentimentalLife:
    WEDDING_LEGAL_AGE = 100

    def __init__(self, human):
        self.human = human
        self.status = SentimentalStatus.SINGLE
        self.soulmate = None
        self.parent_a = None
        self.parent_b = None
        self.children = []
        self.events = []

    def can_wed(self):
        if self.status != SentimentalStatus.SINGLE:
            return False
        if self.human.age < self.WEDDING_LEGAL_AGE:
            return False
        return True

    def wed(self, soulmate):
        if not self.can_wed():
            raise BaseException("Should not wed")
        if self.human.is_male == soulmate.is_male:
            raise BaseException("Only hetero couple allowed")

        self.status = SentimentalStatus.COUPLE

        self.soulmate = soulmate
        soulmate_life = soulmate.sentimental_life
        soulmate_life.status = SentimentalStatus.COUPLE
        soulmate_life.soulmate = self.human

        self.add_event(Childbirth(self))

    def soulmate_death(self):
        self.status = SentimentalStatus.WIDOW
        self.remove_event(Childbirth)

    def death(self):
        if self.status == SentimentalStatus.COUPLE:
            self.soulmate.sentimental_life.soulmate_death()

    def add_child(self, child):
        self.children.append(child)

    def add_event(self, event):
        self.events.append(event)

    def remove_event(self, event_class):
        self.events = [
            event for event in self.events if not isinstance(event, event_class)
        ]
