from lab7.managers.projector_manager import ProjectManager


class SetManager:
    """
    This class works with a set of resolutions.

    Args:
        project_manager (ProjectManager): The ProjectManager instance to work with.

    Attributes:
        manager (ProjectManager): The ProjectManager instance.

    """

    def __init__(self, project_manager: ProjectManager):
        self.manager = project_manager

    def __iter__(self):
        """
        Iterate over the set of colors from the projectors.

        Yields:
            str: A set of color.

        """
        self.count = 0
        for projector in self.manager:
            for set_of_color in projector.projector_color():
                yield set_of_color

    def __len__(self):
        """
        Get the total length of colors from all projectors.

        Returns:
            int: The total length of colors.

        """
        length = 0
        for projector in self.manager:
            length += len(projector.projector_color())
        return length

    def __getitem__(self, item):
        """
        Get the colors from the specified index.

        Args:
            item (int): The index.

        Returns:
            list: The colors from the specified index.

        """
        return self.manager[item].projector_color()

    def __next__(self):
        """
        Get the next projector in the manager.

        Returns:
            Projector: The next projector.

        Raises:
            StopIteration: If there are no more projectors.

        """
        if self.count <= len(self.manager):
            result = self.manager
            self.count += 1
            return result
        else:
            raise StopIteration
