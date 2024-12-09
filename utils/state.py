class State:
    _state = {}
    _initial = {}
    _previous = {}
    _is_modified = False

    def __init__(self, defaults={}):
        self.define(defaults)

    def define(self, definition):
        self._state.update(definition)
        self._initial.update(definition)
        self._previous.update(definition)
        self._is_modified = True
        return self.get_all()

    def get(self, prop):
        return self.get_all()[prop]
    
    def get_all(self):
        return dict(self._state)
    
    def set(self, prop, value):
        return self.set_multiple({prop: value})
    
    def set_multiple(self, updates):
        self._state.update(updates)
        self._is_modified = self._state != self._previous
        self._previous.update(self._state)
        return self.get_all()
    
    def reset(self):
        self._state = self._initial.copy()
        return self.get_all()
    
    def has_changed(self):
        return self._is_modified
    
    def acknowledge(self):
        self._is_modified = False
        return self.get_all()
    