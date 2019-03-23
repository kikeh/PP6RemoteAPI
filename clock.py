class Clock:
    DEFAULT_TIME = '00:00:00'

    IS_AM = 0
    IS_PM = 1
    IS_24H = 2

    COUNTDOWN_TIMER = 0
    COUNTDOWN_TO_TIME = 1
    ELAPSED_TIME = 2

    def __init__(self, index, clock_info):
        self.index = index
        self._initialize_with_clock_info(
            name=clock_info.get('clockName'),
            time=clock_info.get('clockTime'),
            clock_type=clock_info.get('clockType'),
            display_type=clock_info.get('clockIsPM'),
            is_overrun=clock_info.get('clockOverrun'),
            duration=clock_info.get('clockDuration'),
            end_time=clock_info.get('clockEndTime'),
            state=clock_info.get('clockState'),
        )

    def _initialize_with_clock_info(
            self,
            name=None,
            time=None,
            clock_type=None,
            display_type=None,
            is_overrun=False,
            duration=None,
            end_time=None,
            state=False
    ):
        self.name = name
        self.time = time or self.DEFAULT_TIME
        self.clock_type = clock_type or self.COUNTDOWN_TIMER
        self.display_type = display_type or self.IS_24H
