from lab7.modules.abstract_projector import AbstractProjector


class ThreeDProjector(AbstractProjector):
    """
    This class is a child class of AbstractProjector class
    This class implements father poles and has own:
    guarantee, energy_consumption, WORKING_HOURS_PER_YEAR
    (this class also has static final pole)
    This class implements father methods
    This class has __repr__
    """
    __WORKING_HOURS_PER_YEAR = 3650

    def __init__(self, model="", resolution="", connected_device="",
                 guarantee=0, energy_consumption=0):
        super().__init__(model, resolution, connected_device)
        self.guarantee = guarantee
        self.energy_consumption = energy_consumption

    def add_input_device(self, device):
        self.connected_device = device

    def disconnected_device(self):
        self.connected_device = None

    def get_remaining_working_hours(self):
        return self.guarantee * ThreeDProjector.__WORKING_HOURS_PER_YEAR

    def __repr__(self):
        return f"Projector(model={self.model}, resolution={self.resolution}, " \
               f"connected_device={self.connected_device}, guarantee={self.guarantee}, " \
               f"energy_consumption={self.energy_consumption}, " \
               f"__WORKING_HOURS_PER_YEAR={ThreeDProjector.__WORKING_HOURS_PER_YEAR}) "
