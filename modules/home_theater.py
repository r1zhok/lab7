from lab7.modules.abstract_projector import AbstractProjector


class HomeTheater(AbstractProjector):
    """
    This class is child of parent class AbstractProjector
    This class implements father poles and have own poles:
    year_of_sale, screen_size_in_inches, version_of_smart_tv, guarantee, WORKING_HOURS_PER_YEAR
    (this class has static final pole)
    This class implements father poles
    This class has __repr__
    """
    __WORKING_HOURS_PER_YEAR = 3650

    def __init__(self, model="", resolution="", connected_device="", year_of_sale=0,
                 screen_size_in_inches=0, version_of_smart_tv="", guarantee=0):
        super().__init__(model, resolution, connected_device)
        self.year_of_sale = year_of_sale
        self.screen_size_in_inches = screen_size_in_inches
        self.version_of_smart_tv = version_of_smart_tv
        self.guarantee = guarantee

    def add_input_device(self, device):
        self.connected_device = device

    def disconnected_device(self):
        self.connected_device = None

    def get_remaining_working_hours(self):
        return self.guarantee * HomeTheater.__WORKING_HOURS_PER_YEAR

    def __repr__(self):
        return f"Projector(model={self.model}, resolution={self.resolution}, " \
               f"connected_device={self.connected_device}, year_of_sale={self.year_of_sale}," \
               f"screen_size_in_inches={self.screen_size_in_inches}, version_of_smart_tv={self.version_of_smart_tv}," \
               f"guarantee={self.guarantee}, __WORKING_HOURS_PER_YEAR={HomeTheater.__WORKING_HOURS_PER_YEAR}) "
