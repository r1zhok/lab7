class ProjectManager:
    """
    This class is a manager of my classes
    In this class all my objects adds to container
    This container sort by param
    """

    def __init__(self):
        self.projectors = []

    def add_projector(self, projectors):
        """
        This method add all my objects to list and return this container
        :param projectors:
        :return:  projectors -> list
        """
        self.projectors.extend(projectors)
        return self.projectors

    def find_projector_by_model(self, model):
        """
        This method return objects witch have pole model == param model
        :param model:
        :return: filtered_projector -> list
        """
        filtered_projector = list(filter(lambda projector: (projector.model == model), self.projectors))
        return filtered_projector

    def find_projector_by_resolution(self, resolution):
        """
        This method sort my objects by param resolution
        if object have pole resolution == param resolution
        this objects adds to list
        returns list with objects
        :param resolution:
        :return: filtered_projector -> list
        """
        filtered_projector = list(filter(lambda projector: projector.resolution == resolution, self.projectors))
        return filtered_projector
