from abc import ABC

from models.object.base import BaseObject


class BaseCookable(BaseObject, ABC):
    TRANSFORM_INTO = None

    def hook_post_sanitize(self):
        if self.TRANSFORM_INTO is None:
            raise BaseException("TRANSFORM INTO not filled")

    def utility(self, human):
        if self.can_be_used(human):
            return 10 * self.cook_probability(human) * self.TRANSFORM_INTO.FOOD_RETURN
        if self.can_be_produced(human):
            return 10/self.produce_probability(human)

    def usable_jobs(self, human):
        from models.job.chef import Chef

        return list(
            filter(
                lambda job: job.__class__ in [Chef],
                human.jobs
            )
        )

    def produce_jobs(self, human):
        return list(
            filter(
                lambda job: job.is_item_produced(self.__class__),
                human.jobs
            )
        )

    def can_be_used(self, human):
        return len(self.usable_jobs(human)) > 0

    def can_be_produced(self, human):
        return len(self.produce_jobs(human)) > 0

    def cook_probability(self, human):
        action, probability = self.get_cook_action(human)
        return probability

    def produce_probability(self, human):
        action, probability = self.get_produce_action(human)
        return probability

    def get_cook_action(self, human):
        best_action = None
        best_probability = None
        for job in self.usable_jobs(human):
            for action in job.actions:
                if action.OBJECT.NAME == self.NAME:
                    probability = action.probability()
                    if best_probability is None or probability > best_probability:
                        best_action = action
                        best_probability = probability

        return best_action, best_probability

    def get_produce_action(self, human):
        best_action = None
        best_probability = None
        for job in self.produce_jobs(human):
            for action in job.actions:
                if action.OBJECT.NAME == self.NAME:
                    probability = action.probability()
                    if best_probability is None or probability > best_probability:
                        best_action = action
                        best_probability = probability

        return best_action, best_probability
