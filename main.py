class Projector:
    """
    This class have information about projector
    He has information about class:model, resolution, lamp_hours, connected_device
    And also has methods __repr__, add_input_device(@param device->str)
    disconnected_device, increase_lamp_hours(@param hours),
    this method increase lamp hours work,
    and method get-instance, this method creates obj of this class
    """

    __instance = None

    def __init__(self, model="", resolution="", lamp_hours=0, connected_device=""):
        self.module = model
        self.resolution = resolution
        self.lamp_hours = lamp_hours
        self.connected_device = connected_device
        self.instance = None

    def __repr__(self):
        return f"Projector(model={self.module}, resolution={self.resolution}, " \
               f"lamp_hours={self.lamp_hours}, connected_device={self.connected_device})"

    def add_input_device(self, device):
        self.connected_device = device

    def disconnected_device(self):
        self.connected_device = None

    def increase_lamp_hours(self, hours):
        self.lamp_hours += hours

    @staticmethod
    def get_instance():
        if not Projector.__instance:
            Projector.__instance = Projector()
        return Projector.__instance


projectors = [Projector(), Projector("Panasonic", "1920x1080", 5, "HDMI"), Projector.get_instance(),
              Projector.get_instance()]

list = []
for x in range(1,11):
    list.append(x)

print(list)
print(list[1::2])

for projector in projectors:
    print(projector)
