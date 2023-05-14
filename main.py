class Projector:
    """
    My first class in Python
    """

    __instance = None

    def __init__(self, model="", resolution="", lamp_hours=0, connected_device=""):
        self.__module = model
        self.__resolution = resolution
        self.__lamp_hours = lamp_hours
        self.__connected_device = connected_device
        self.__instance = None

    @property
    def model(self):
        return self.__module

    @model.setter
    def model(self, new_model):
        self.__module = new_model

    @property
    def resolution(self):
        return self.__resolution

    @resolution.setter
    def resolution(self, new_resolution):
        self.__resolution = new_resolution

    @property
    def lamp_hours(self):
        return self.__lamp_hours

    @lamp_hours.setter
    def lamp_hours(self, new_lamp_hours):
        self.__lamp_hours = new_lamp_hours

    @property
    def connected_device(self):
        return self.__connected_device

    @connected_device.setter
    def connected_device(self, new_connected_device):
        self.__connected_device = new_connected_device

    def __repr__(self):
        return f"Projector(model={self.__module}, resolution={self.__resolution}, " \
               f"lamp_hours={self.__lamp_hours}, connected_device={self.__connected_device})"

    def add_input_device(self, device):
        self.__connected_device = device

    def disconnected_device(self):
        self.__connected_device = None

    def increase_lamp_hours(self, hours):
        self.__lamp_hours += hours

    @staticmethod
    def get_instance():
        if Projector.__instance is None:
            Projector.__instance = Projector()
        return Projector.__instance


projectors = [Projector(), Projector("Panasonic", "1920x1080", 5, "HDMI"), Projector.get_instance(),
              Projector.get_instance()]

for projector in projectors:
    print(projector)
