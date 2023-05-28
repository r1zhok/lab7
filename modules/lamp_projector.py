"""
Module of LampProjector class
"""
from lab7.modules.abstract_projector import AbstractProjector


class LampProjector(AbstractProjector):
    """
    Child class of AbstractProjector representing a lamp projector.

    Attributes:
        model (str): The model of the lamp projector.
        resolution (str): The resolution of the lamp projector.
        connected_device (str): The currently connected device to the lamp projector.
        lamp_hours (int): The total lamp hours of the lamp projector.
        description_of_the_information_output_mode (str):
        Description of the information output mode.
        the_maximum_permissible_lamp_operating_time (int): The maximum permissible lamp operating time.

    Methods:
        add_input_device(device): Adds an input device to the lamp projector.
        disconnected_device(): Disconnects the currently connected device.
        get_remaining_working_hours(): Calculates the remaining working hours of the lamp projector.
        lamp_hours(hours): Increases the lamp working hours of the lamp projector.
        __repr__(): Returns a string representation of the lamp projector.
    """

    def __init__(self, model="", resolution="", connected_device="", lamp_hours=0,
                 description_of_the_information_output_mode="",
                 the_maximum_permissible_lamp_operating_time=0):
        """
        Initializes a LampProjector object.

        Args:
            model (str): The model of the lamp projector.
            resolution (str): The resolution of the lamp projector.
            connected_device (str): The currently connected device to the lamp projector.
            lamp_hours (int): The total lamp hours of the lamp projector.
            description_of_the_information_output_mode (str): Description of the information output mode.
            the_maximum_permissible_lamp_operating_time (int): The maximum permissible lamp operating time.
        """
        super().__init__(model, resolution, connected_device)
        self.lamp_hours = lamp_hours
        self.description_of_the_information_output_mode = description_of_the_information_output_mode
        self.the_maximum_permissible_lamp_operating_time = the_maximum_permissible_lamp_operating_time
        self.projector_color = {"yellow"}

    def add_input_device(self, device):
        """
        Adds an input device to the lamp projector.

        Args:
            device (str): The input device to add.
        """
        self.connected_device = device

    def disconnected_device(self):
        """
        Disconnects the currently connected device.
        """
        self.connected_device = None

    def get_remaining_working_hours(self):
        """
        Calculates the remaining working hours of the lamp projector.

        Returns:
            int: The remaining working hours based on the maximum permissible lamp operating time.
        """
        return self.the_maximum_permissible_lamp_operating_time

    def lamp_hours(self, hours):
        """
        Increases the lamp working hours of the lamp projector.

        Args:
            hours (int): The number of hours to increase the lamp working hours.
        """
        self.lamp_hours += hours

    def __repr__(self):
        """
        Returns a string representation of the lamp projector.

        Returns:
            str: A string representation of the lamp projector.
        """
        return f"Projector(model={self.model}, resolution={self.resolution}, " \
               f"connected_device={self.connected_device}, lamp_hours={self.lamp_hours}," \
               f"description_of_the_information_output_mode={self.description_of_the_information_output_mode}," \
               f"the_maximum_permissible_lamp_operating_time={self.the_maximum_permissible_lamp_operating_time})"
