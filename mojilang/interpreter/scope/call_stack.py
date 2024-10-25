

class CallStack:
    def __init__(self):
        self._stack = []

    def push(self, function_name, arguments):
        new_entry = CallStackEntry(function_name, arguments)
        self._stack.append(new_entry)

    def pop(self):
        return self._stack.pop()


class CallStackEntry:
    def __init__(self, function_name, arguments):
        self._function_name = function_name
        self._arguments = arguments

    def get_function_name(self):
        return self._function_name

    def get_arguments(self):
        return self._arguments
