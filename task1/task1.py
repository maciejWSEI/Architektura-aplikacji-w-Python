import inspect
from functools import wraps

def log_params(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        signature = inspect.signature(func)
        bound_args = signature.bind(*args, **kwargs)
        bound_args.apply_defaults()

        params_info = {
            name: type(value).__name__
            for name, value in bound_args.arguments.items()
        }

        print(params_info)
        return func(*args, **kwargs)

    return wrapper