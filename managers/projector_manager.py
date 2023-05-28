class ProjectManager:
    """
    This class is a manager of projectors.

    It provides functionality to add projectors to a container, access projectors by index,
    iterate over projectors, find projectors based on specific criteria, and perform various operations
    on the projectors.

    Attributes:
        projectors (list): List of projectors.

    Methods:
        __len__(): Get the length of the list of projectors.
        __getitem__(item): Get the projector at the specified index in the list.
        __iter__(): Initialize the iterator for iterating over the projectors.
        __next__(): Get the next projector in the iteration.
        add_projector(projectors): Add projectors to the list.
        find_projector_by_model(model): Find projectors with a specific model.
        find_projector_by_resolution(resolution): Find projectors with a specific resolution.
        working_of_get_remaining_working_hours(): Get the remaining working hours of all projectors.
        is_all_get_remaining_working_hours_greater_than(): Check if all projectors have remaining working hours greater than 15.
        is_any_get_remaining_working_hours_greater_than(): Check if any projector has remaining working hours greater than 15.
    """

    def __init__(self):
        self.projectors = []

    def __len__(self):
        """
        Get the length of the list of projectors.

        Returns:
            int: Length of the list of projectors.
        """
        return len(self.projectors)

    def __getitem__(self, item):
        """
        Get the projector at the specified index in the list.

        Args:
            item (int): Index of the projector.

        Returns:
            object: Projector at the specified index.
        """
        return self.projectors[item]

    def __iter__(self):
        """
        Initialize the iterator for iterating over the projectors.

        Returns:
            iterator: Iterator object.
        """
        self.count = 0
        return self.projectors

    def __next__(self):
        """
        Get the next projector in the iteration.

        Returns:
            object: Next projector.

        Raises:
            StopIteration: If all projectors have been iterated.
        """
        if self.count <= len(self.projectors):
            result = self.projectors[self.count]
            self.count += 1
            return result
        else:
            raise StopIteration

    def add_projector(self, projectors):
        """
        Add projectors to the list.

        Args:
            projectors (list): List of projectors to add.

        Returns:
            list: Updated list of projectors.
        """
        self.projectors.extend(projectors)
        return self.projectors

    def find_projector_by_model(self, model):
        """
        Find projectors with a specific model.

        Args:
            model (str): Model to search for.

        Returns:
            list: List of tuples containing the index and matching projectors.
        """
        return list(enumerate(filter(lambda projector: getattr(projector, "model") == model, self.projectors)))

    def find_projector_by_resolution(self, resolution):
        """
        Find projectors with a specific resolution.

        Args:
            resolution (str): Resolution to search for.

        Returns:
            list: List of tuples containing the index and matching projectors.
        """
        return list(enumerate(filter(lambda projector: getattr(projector, "resolution") == resolution,
                                     self.projectors)))

    def working_of_get_remaining_working_hours(self):
        """
        Get the remaining working hours of all projectors.

        Returns:
            list: List of tuples containing the remaining working hours and projectors.
        """
        return list(zip([projector.get_remaining_working_hours() for projector in self.projectors], self.projectors))

    def is_all_get_remaining_working_hours_greater_than(self):
        """
        Check if all projectors have remaining working hours greater than 15.

        Returns:
            bool: True if all projectors have remaining working hours greater than 15, False otherwise.
        """
        result = []
        for i in range(0, 8):
            result.append(self.projectors[i].get_remaining_working_hours() > 15)

        return all(result)

    def is_any_get_remaining_working_hours_greater_than(self):
        """
        Check if any projector has remaining working hours greater than 15.

        Returns:
            bool: True if any projector has remaining working hours greater than 15, False otherwise.
        """
        result = []
        for i in range(0, 8):
            result.append(self.projectors[i].get_remaining_working_hours() > 15)

        return any(result)

