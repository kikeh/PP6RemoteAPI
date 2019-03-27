class Clock:
    DEFAULT_TIME = '00:00:00'

    IS_AM = 0
    IS_PM = 1
    IS_24H = 2

    COUNTDOWN_TIMER = 0
    COUNTDOWN_TO_TIME = 1
    ELAPSED_TIME = 2

    def __init__(self, index, clock_info, client=None):
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
        self.client = client

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
        self.is_overrun = is_overrun
        self.duration = duration or self.DEFAULT_TIME
        self.end_time = end_time or self.DEFAULT_TIME
        self.state = state

    @property
    def settings(self):
        return {
            'clockIndex': self.index,
            'clockTime': self.time,
            'clockName': self.name,
            'clockType': self.clock_type,
            'clockIsPM': self.display_type,
            'clockOverrun': self.is_overrun,
        }

    def update(self, new_settings):
        if self.client:
            command = {'action': 'clockUpdate'}
            settings = self.settings
            settings.update(new_settings)
            command.update(settings)
            return self.client.async_send(command, expect_response=False)

    def set_time(self, time):
        if self.client:
            return self.update({'clockTime': time})

    def start(self):
        if self.client:
            command = {
                'action': 'clockStart',
                'clockIndex': self.index,
            }
            return self.client.async_send(command, expect_response=False)

    def stop(self):
        if self.client:
            command = {
                'action': 'clockStop',
                'clockIndex': self.index,
            }
            return self.client.async_send(command, expect_response=False)

    def reset(self):
        if self.client:
            command = {
                'action': 'clockReset',
                'clockIndex': self.index,
            }
            return self.client.async_send(command, expect_response=False)

    def __repr__(self):
        return f'<Clock: {self.name} | {self.index}>'
