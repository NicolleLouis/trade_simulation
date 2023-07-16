from service.graph.logic.datalogger import DataLogger


class HumanMoney(DataLogger):
    TITLE = "Human Money"
    X_LABEL = "Days"
    Y_LABEL = "Money"
    FILE_ADDRESS = "human_money"

    # hide_dead: Remove all dead human from the graph
    # only_richest: if None, do nothing, else display only n richest human
    # only_poorest: if None, do nothing, else display only n poorest human
    def __init__(
            self,
            world,
            hide_dead=False,
            only_richest=None,
            only_poorest=None,
    ):
        self.world = world
        self.hide_dead = hide_dead
        self.only_richest = only_richest
        self.only_poorest = only_poorest
        self.sanitize()

        super().__init__()

    def sanitize(self):
        if self.only_richest is not None:
            if not isinstance(self.only_richest, int):
                raise BaseException("only_richest should be int")
        if self.only_poorest is not None:
            if not isinstance(self.only_poorest, int):
                raise BaseException("only_poorest should be int")

        if self.only_poorest == 0:
            self.only_poorest = None

        if self.only_richest == 0:
            self.only_richest = None

    def fetch_data(self):
        day = self.world.day
        for human in self.world.humans:
            self.add_point(
                human.name,
                day,
                human.money
            )

    def hook_post_computation(self):
        self.filter_dead()
        self.filter_extremum()

    def filter_dead(self):
        if self.hide_dead:
            for dead_human in self.world.dead_humans:
                self.graph_data.remove_plot_data(dead_human.name)

    def filter_extremum(self):
        if self.only_poorest is None and self.only_richest is None:
            return
        non_filtered_human = []
        self.world.humans.sort(
            key=lambda human: human.money,
        )
        if self.only_richest is not None:
            richest_humans = self.world.humans[-self.only_richest:]
            for human in richest_humans:
                non_filtered_human.append(human.name)
        if self.only_poorest is not None:
            poorest_humans = self.world.humans[:self.only_poorest]
            for human in poorest_humans:
                non_filtered_human.append(human.name)

        all_human_name = list(map(
            lambda human: human.name,
            self.world.humans
        ))
        filtered_name = set(all_human_name) - set(non_filtered_human)
        for name in filtered_name:
            self.graph_data.remove_plot_data(name)
