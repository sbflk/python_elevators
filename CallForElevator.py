class CallForElevator:
    def __init__(self, _dt, _src, _dest):
        self._dt = _dt
        self._src = _src
        self._dest = _dest

    def get_time(self):
        return self._dt

    def get_src(self):
        return self._src

    def get_dest(self):
        return self._dest

    def get_type(self):# 1-up, 0-down
        if self._dest-self._src > 0:
            return 1
        return 0
