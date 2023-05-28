from abc import ABC, abstractmethod


class AbstractProjector(ABC):
    """
    This is abstract class
    This class has 3 public poles:
    model, resolution, connected_device.
    This class has 3 abstract methods:
    add_input_device, disconnected_device, get_remaining_working_hours.
    They are all implements in child's classes
    """

    def __init__(self, model="", resolution="", connected_device=""):
        self.model = model
        self.resolution = resolution
        self.connected_device = connected_device
        self.projector_color = None

    def __iter__(self):
        return iter(sorted(self.projector_color))

    def get_attributes(self, variable=None):
        return {key: value for key, value in self.__dict__.items() if isinstance(value, variable)}

    @abstractmethod
    def add_input_device(self, device):
        """
        This method change self.connected_device on device
        :param device:
        :return: connected_device -> str
        """

    @abstractmethod
    def disconnected_device(self):
        """
        This method delete self.connected_device
        :return: None
        """

    @abstractmethod
    def get_remaining_working_hours(self):
        """
        This method calculates how much projector will be working
        :return: float
        """

