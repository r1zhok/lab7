"""
Module of ThreeDProjector class
"""
from lab7.modules.abstract_projector import AbstractProjector


class ThreeDProjector(AbstractProjector):
    """
    Child class of AbstractProjector representing a 3D projector.

    Attributes:
        model (str): The model of the 3D projector.
        resolution (str): The resolution of the 3D projector.
        connected_device (str): The currently connected device to the 3D projector.
        guarantee (int): The guarantee period of the 3D projector.
        energy_consumption (int): The energy consumption of the 3D projector.

    Methods:
        add_input_device(device): Adds an input device to the 3D projector.
        disconnected_device(): Disconnects the currently connected device.
        get_remaining_working_hours(): Calculates the remaining working hours of the 3D projector.
        __repr__(): Returns a string representation of the 3D projector.
    """

    __WORKING_HOURS_PER_YEAR = 3650

    def __init__(self, model="", resolution="", connected_device="", guarantee=0, energy_consumption=0):
        """
        Initializes a ThreeDProjector object.

        Args:
            model (str): The model of the 3D projector.
            resolution (str): The resolution of the 3D projector.
            connected_device (str): The currently connected device to the 3D projector.
            guarantee (int): The guarantee period of the 3D projector.
            energy_consumption (int): The energy consumption of the 3D projector.
        """
        super().__init__(model, resolution, connected_device)
        self.guarantee = guarantee
        self.energy_consumption = energy_consumption
        self.projector_color = {"grey"}

    def add_input_device(self, device):
        """
        Adds an input device to the 3D projector.

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
        Calculates the remaining working hours of the 3D projector.

        Returns:
            int: The remaining working hours based on the guarantee period and working hours per year.
        """
        return self.guarantee * ThreeDProjector.__WORKING_HOURS_PER_YEAR

    def __repr__(self):
        """
        Returns a string representation of the 3D projector.

        Returns:
            str: A string representation of the 3D projector.
        """
        return f"Projector(model={self.model}, resolution={self.resolution}, " \
               f"connected_device={self.connected_device}, guarantee={self.guarantee}, " \
               f"energy_consumption={self.energy_consumption}, " \
               f"__WORKING_HOURS_PER_YEAR={ThreeDProjector.__WORKING_HOURS_PER_YEAR})"
