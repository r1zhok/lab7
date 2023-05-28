from lab7.modules.abstract_projector import AbstractProjector


class MultiBoard(AbstractProjector):
    """
    This class is a child class of AbstractProjector class
    This class implements father poles and has own:
    color_of_surface, is_has_magnite_surface, the_possibility_of_recording_screen,
    guarantee, WORKING_HOURS_PER_YEAR (this class has static final pole)
    This class implements father methods
    Also this class has __repr__
    """
    __WORKING_HOURS_PER_YEAR = 3650

    def __init__(self, model="", resolution="", connected_device="", color_of_surface="",
                 is_has_magnite_surface=False, the_possibility_of_recording_screen=False,
                 guarantee=0):
        super().__init__(model, resolution, connected_device)
        self.color_of_surface = color_of_surface
        self.is_has_magnite_surface = is_has_magnite_surface
        self.the_possibility_of_recording_screen = the_possibility_of_recording_screen
        self.guarantee = guarantee
        self.projector_color = {"green"}

    def add_input_device(self, device):
        self.connected_device = device

    def disconnected_device(self):
        self.connected_device = None

    def get_remaining_working_hours(self):
        return self.guarantee * MultiBoard.__WORKING_HOURS_PER_YEAR

    def __repr__(self):
        return f"Projector(model={self.model}, resolution={self.resolution}, " \
               f"connected_device={self.connected_device}, color_of_surface={self.color_of_surface}, " \
               f"is_has_magnite_surface={self.is_has_magnite_surface}, " \
               f"the_possibility_of_recording_screen={self.the_possibility_of_recording_screen}, " \
               f"guarantee={self.guarantee}, " \
               f"__WORKING_HOURS_PER_YEAR={MultiBoard.__WORKING_HOURS_PER_YEAR}) "
