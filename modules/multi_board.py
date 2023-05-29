"""
Module of MultiBoard class
"""
from lab7.modules.abstract_projector import AbstractProjector


class MultiBoard(AbstractProjector):
    """
    Child class of AbstractProjector representing a multi-board projector.

    Attributes:
        model (str): The model of the multi-board projector.
        resolution (str): The resolution of the multi-board projector.
        connected_device (str): The currently connected device to the multi-board projector.
        color_of_surface (str): The color of the projection surface.
        is_has_magnite_surface (bool):
        Indicates if the multi-board projector has a magnetite surface.
        the_possibility_of_recording_screen (bool):
        Indicates if the multi-board projector has screen recording capability.
        guarantee (int): The guarantee period of the multi-board projector.

    Methods:
        add_input_device(device): Adds an input device to the multi-board projector.
        disconnected_device():
        Disconnects the currently connected device.
        get_remaining_working_hours(): Calculates the remaining working hours of the multi-board projector.
        __repr__(): Returns a string representation of the multi-board projector.
    """

    __WORKING_HOURS_PER_YEAR = 3650

    def __init__(self, model="", resolution="", connected_device="", color_of_surface="",
                 is_has_magnite_surface=False, the_possibility_of_recording_screen=False,
                 guarantee=0):
        """
        Initializes a MultiBoard object.

        Args:
            model (str): The model of the multi-board projector.
            resolution (str): The resolution of the multi-board projector.
            connected_device (str): The currently connected device to the multi-board projector.
            color_of_surface (str):
            The color of the projection surface.
            is_has_magnite_surface (bool): Indicates if the multi-board projector has a magnetite surface.
            the_possibility_of_recording_screen (bool):
            Indicates if the multi-board projector has screen recording capability.
            guarantee (int): The guarantee period of the multi-board projector.
        """
        super().__init__(model, resolution, connected_device)
        self.color_of_surface = color_of_surface
        self.is_has_magnite_surface = is_has_magnite_surface
        self.the_possibility_of_recording_screen = the_possibility_of_recording_screen
        self.guarantee = guarantee
        self.projector_color = {"green"}

    def add_input_device(self, device):
        """
        Adds an input device to the multi-board projector.

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
        Calculates the remaining working hours of the multi-board projector.

        Returns:
            int: The remaining working hours based on the guarantee period and working hours per year.
        """
        return self.guarantee * MultiBoard.__WORKING_HOURS_PER_YEAR

    def __repr__(self):
        """
        Returns a string representation of the multi-board projector.

        Returns:
            str: A string representation of the multi-board projector.
        """
        return f"Projector(model={self.model}, resolution={self.resolution}, " \
               f"connected_device={self.connected_device}, color_of_surface={self.color_of_surface}, " \
               f"is_has_magnite_surface={self.is_has_magnite_surface}, " \
               f"the_possibility_of_recording_screen={self.the_possibility_of_recording_screen}, " \
               f"guarantee={self.guarantee}, " \
               f"__WORKING_HOURS_PER_YEAR={MultiBoard.__WORKING_HOURS_PER_YEAR})"
