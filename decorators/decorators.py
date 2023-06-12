"""
Module of decorations
"""
import logging
from functools import wraps


def count_of_args_decorator(func):
    """
    Decorator that counts the number of arguments passed to a function.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.
    """

    def wrapper(*args, **kwargs):
        """
        Wrapper function that counts the number of arguments and calls the original function.

        Args:
            *args: Positional arguments passed to the function.
            **kwargs: Keyword arguments passed to the function.

        Returns:
            The result of the original function call.
        """
        print(f"Number of arguments: {len(args) + len(kwargs)}")
        return func(*args, **kwargs)

    return wrapper


def call_limit_decorator(max_calls):
    """
    Decorator that limits the number of times a function can be called.

    Args:
        max_calls (int): The maximum number of allowed function calls.

    Returns:
        function: The decorator function.
    """

    def decorator(func):
        count = 0

        def wrapper(*args, **kwargs):
            """
            Wrapper function that limits the number of function calls.

            Args:
                *args: Positional arguments passed to the function.
                **kwargs: Keyword arguments passed to the function.

            Returns:
                The result of the original function call.
            Raises:
                Exception: If the maximum number of calls is exceeded.
            """
            nonlocal count
            count += 1
            if count > max_calls:
                raise Exception("Too many calls")
            return func(*args, **kwargs)

        return wrapper

    return decorator


def logged(exception, mode):
    def decorator(func):
        count = 0
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            nonlocal count
            for argument in args:
                count+=1
                try:
                    if type(argument) is not str:
                        raise exception
                except exception:
                    if mode == "console":
                        logging.getLogger().setLevel(logging.DEBUG)
                        logging.debug('The argument type must be str')
                    elif mode == "file":
                        logging.basicConfig(level=logging.DEBUG, filename='my_log.log')
                        logging.debug('The argument type must be str')
                    else:
                        raise TypeError("Log can be only console or file")
                else:
                    if len(args)==count:
                        return func(self, *args, **kwargs)
        return wrapper

    return decorator
