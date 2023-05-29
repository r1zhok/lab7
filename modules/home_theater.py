"""
Module of HomeTheater class
"""
from lab7.modules.abstract_projector import AbstractProjector


class HomeTheater(AbstractProjector):
    """
    Child class of AbstractProjector representing a home theater projector.

    Attributes:
        model (str): The model of the home theater projector.
        resolution (str): The resolution of the home theater projector.
        connected_device (str): The currently connected device to the home theater projector.
        year_of_sale (int): The year of sale of the home theater projector.
        screen_size_in_inches (int): The screen size in inches of the home theater projector.
        version_of_smart_tv (str):
         The version of the smart TV integrated with the home theater projector.
        guarantee (int): The guarantee period of the home theater projector in years.

    Methods:
        add_input_device(device): Adds an input device to the home theater projector.
        disconnected_device():
        Disconnects the currently connected device.
        get_remaining_working_hours():
        Calculates the remaining working hours of the home theater projector.
        __repr__(): Returns a string representation of the home theater projector.
    """
    __WORKING_HOURS_PER_YEAR = 3650

    def __init__(self, model="", resolution="", connected_device="", year_of_sale=0,
                 screen_size_in_inches=0, version_of_smart_tv="", guarantee=0):
        """
        Initializes a HomeTheater object.

        Args:
            model (str): The model of the home theater projector.
            resolution (str): The resolution of the home theater projector.
            connected_device (str): The currently connected device to the home theater projector.
            year_of_sale (int):
            The year of sale of the home theater projector.
            screen_size_in_inches (int):
            The screen size in inches of the home theater projector.
            version_of_smart_tv (str): The version of the smart TV integrated with the home theater projector.
            guarantee (int): The guarantee period of the home theater projector in years.
        """
        super().__init__(model, resolution, connected_device)
        self.year_of_sale = year_of_sale
        self.screen_size_in_inches = screen_size_in_inches
        self.version_of_smart_tv = version_of_smart_tv
        self.guarantee = guarantee
        self.projector_color = {"black"}

    def add_input_device(self, device):
        """
        Adds an input device to the home theater projector.

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
        Calculates the remaining working hours of the home theater projector.

        Returns:
            float: The remaining working hours based on the guarantee period and the constant
                   __WORKING_HOURS_PER_YEAR.
        """
        return self.guarantee * HomeTheater.__WORKING_HOURS_PER_YEAR

    def __repr__(self):
        """
        Returns a string representation of the home theater projector.

        Returns:
            str: A string representation of the home theater projector.
        """
        return f"Projector(model={self.model}, resolution={self.resolution}, " \
               f"connected_device={self.connected_device}, year_of_sale={self.year_of_sale}," \
               f"screen_size_in_inches={self.screen_size_in_inches}, " \
               f"version_of_smart_tv={self.version_of_smart_tv}," \
               f"guarantee={self.guarantee}, __WORKING_HOURS_PER_YEAR={HomeTheater.__WORKING_HOURS_PER_YEAR})"
