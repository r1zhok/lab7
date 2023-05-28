from lab7.modules.abstract_projector import AbstractProjector


class LampProjector(AbstractProjector):
    """
    This class is child class of parent AbstractProjector class
    This class has 3 poles from father class and 3 own poles
    Also this class implements father class methods and have own method
    This class has __repr__
    """

    def __init__(self, model="", resolution="", connected_device="", lamp_hours=0,
                 description_of_the_information_output_mode="", the_maximum_permissible_lamp_operating_time=0):
        super().__init__(model, resolution, connected_device)
        self.lamp_hours = lamp_hours
        self.descriptionOfTheInformationOutputMode = description_of_the_information_output_mode
        self.theMaximumPermissibleLampOperatingTime = the_maximum_permissible_lamp_operating_time

    def add_input_device(self, device):
        self.connected_device = device

    def disconnected_device(self):
        self.connected_device = None

    def get_remaining_working_hours(self):
        return self.theMaximumPermissibleLampOperatingTime

    def lamp_hours(self, hours):
        """
        This method increases work of lamp
        :param hours:
        :return: None
        """
        self.lamp_hours += hours

    def __repr__(self):
        return f"Projector(model={self.model}, resolution={self.resolution}, " \
               f"connected_device={self.connected_device}, lamp_hours={self.lamp_hours}," \
               f"descriptionOfTheInformationOutputMode={self.descriptionOfTheInformationOutputMode}," \
               f"theMaximumPermissibleLampOperatingTime={self.theMaximumPermissibleLampOperatingTime}) "
