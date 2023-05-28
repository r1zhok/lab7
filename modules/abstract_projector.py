"""
Module of abstract projector
"""
from abc import ABC, abstractmethod


class AbstractProjector(ABC):
    """
    Abstract base class for projectors.

    Attributes:
        model (str): Model of the projector.
        resolution (str): Resolution of the projector.
        connected_device (str): Currently connected device.

    Methods:
        __iter__(): Iterator method to iterate over the projector's color options.
        get_attributes(variable=None):
        Get attributes of the projector that match the specified variable type.
        add_input_device(device): Abstract method to add an input device to the projector.
        disconnected_device():
        Abstract method to disconnect the currently connected device.
        get_remaining_working_hours():
        Abstract method to calculate the remaining working hours of the projector.
    """

    def __init__(self, model="", resolution="", connected_device=""):
        self.model = model
        self.resolution = resolution
        self.connected_device = connected_device
        self.projector_color = None

    def __iter__(self):
        """
        Iterator method to iterate over the projector's color options.

        Returns:
            iterator: Iterator object.
        """
        return iter(sorted(self.projector_color))

    def get_attributes(self, data_type):
        """
        Get attributes of the projector that match the specified variable type.

        Args:
            variable (type): Type of variable to filter attributes.

        Returns:
            dict: Dictionary containing attribute names and values
            that match the specified variable type.
        """
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

    @abstractmethod
    def add_input_device(self, device):
        """
        Abstract method to add an input device to the projector.

        Args:
            device (str): Device to add.

        Returns:
            str: Connected device.
        """

    @abstractmethod
    def disconnected_device(self):
        """
        Abstract method to disconnect the currently connected device.

        Returns:
            None
        """

    @abstractmethod
    def get_remaining_working_hours(self):
        """
        Abstract method to calculate the remaining working hours of the projector.

        Returns:
            float: Remaining working hours.
        """
