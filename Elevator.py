class Elevator:
    def __init__(self, _id, _speed, _closetime, _opentime, _starttime, _stoptime, _current_call):
        self._id = _id
        self._speed = _speed
        self._closetime = _closetime
        self._opentime = _opentime
        self._starttime = _starttime
        self._stoptime = _stoptime
        self._current_call = _current_call


    def get_id(self):
        return self._id

    def get_speed(self):
        return self._speed

    def get_closetime(self):
        return self._closetime

    def get_opentime(self):
        return self._opentime

    def get_starttime(self):
        return self._starttime

    def get_stoptime(self):
        return self._stoptime

    def get_current_call(self):
        return self._current_call

    def set_current_call(self, c):
        self._current_call = c
