class InvalidRatingError(Exception):
    """Exception raised for invalid rating values."""
    pass

class InvalidDistanceError(Exception):
    """Exception raised for invalid distance values."""
    pass

class RideHistoryFileError(Exception):
    """Exception raised for issues with the ride history file."""
    pass

class InvalidVehicleError(Exception):
    """Exception raised for invalid vehicle type."""
    pass
