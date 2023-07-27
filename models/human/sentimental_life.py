from constants.sentimental_status import SentimentalStatus


class SentimentalLife:
    WEDDING_LEGAL_AGE = 100

    def __init__(self, human):
        self.human = human
        self.status = SentimentalStatus.SINGLE
        self.soulmate = None

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

    def soulmate_death(self):
        self.status = SentimentalStatus.WIDOW

    def death(self):
        if self.status == SentimentalStatus.COUPLE:
            self.soulmate.sentimental_life.soulmate_death()
