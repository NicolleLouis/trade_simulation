from abc import ABC

from models.job.chef import Chef
from models.object.base import BaseObject


class BaseCookable(BaseObject, ABC):
    JOB_USING = [Chef]
    TRANSFORM_INTO = None

    def hook_post_sanitize(self):
        if self.TRANSFORM_INTO is None:
            raise BaseException("TRANSFORM INTO not filled")

    # 10 utility per consumable food + 5 utility per non-consumable food
    # Infinite value if the human is starving
    def utility(self, human):
        if not self.can_be_used(human):
            return None
        return 10 + self.probability() * self.TRANSFORM_INTO.FOOD_RETURN

    def usable_jobs(self, human):
        return list(
            filter(
                lambda job: job.__class__ in self.JOB_USING,
                human.jobs
            )
        )

    def can_be_used(self, human):
        return len(self.usable_jobs(human)) > 0

    def probability(self, human):
        action, probability = self.get_cook_action(human)
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
