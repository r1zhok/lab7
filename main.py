from lab7.modules.lamp_projector import LampProjector
from lab7.modules.home_theater import HomeTheater
from lab7.modules.multi_board import MultiBoard
from lab7.modules.tree_d_projector import ThreeDProjector
from lab7.managers.projector_manager import ProjectManager

if __name__ == "__main__":
    projectors = [LampProjector("Panasonic", "480p", "HDMI", 5, "presentation", 15),
                  LampProjector("Epson", "4k", "HDMI", 5, "sport", 15),
                  HomeTheater("Samsung", "8k", "HDMI, USB", 2023, 57, "last", 5),
                  HomeTheater("Samsung", "4k", "HDMI", 2021, 45, "last", 3),
                  MultiBoard("Prestigio", "1920x1080", "HDMI", "multicolor", True, True, 5),
                  MultiBoard("Prestigio", "1920x1080", "HDMI", "black", True, False, 4),
                  ThreeDProjector("Panasonic", "4k", "HDMI", 4, 30),
                  ThreeDProjector("Epson", "4k", "HDMI", 2, 45)]

    projector_manager = ProjectManager()

    print("All my objects: ")
    print(projector_manager.add_projector(projectors))

    print("Sorted massive by param: ")
    print("-----------------------------------------------------------")
    print(projector_manager.find_projector_by_model("Panasonic"))
    print("-----------------------------------------------------------")
    print(projector_manager.find_projector_by_resolution("1920x1080"))






