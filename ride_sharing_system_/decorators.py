def ride_logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("\nRide successfully booked.")
        return result
    return wrapper

