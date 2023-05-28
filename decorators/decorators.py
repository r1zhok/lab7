def count_of_args_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Number of arguments: {len(args) + len(kwargs)}")
        return func(*args, **kwargs)

    return wrapper


def call_limit_decorator(max_calls):
    def decorator(func):
        count = 0

        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            if count > max_calls:
                raise Exception("Too many calls")
            return func(*args, **kwargs)

        return wrapper

    return decorator
