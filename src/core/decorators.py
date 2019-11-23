from core.pytensions.patch import patch


def extends(type):
    def decorator(func):
        patch(type)[func.__name__] = func
    return decorator
