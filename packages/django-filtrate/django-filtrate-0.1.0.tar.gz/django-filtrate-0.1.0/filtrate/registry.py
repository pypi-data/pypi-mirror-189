from django.db.models import Model


class AlreadyRegistered(Exception):
    """Raised when a Model is already registered with the FilterRegistry"""

    pass


class NotRegistered(Exception):
    """Raised when a Model is not already registered with the FilterRegistry, but is
    attempting to be unregistered"""

    pass


class ModelNotFound(Exception):
    """Raised when a Model is looked up in the FilterRegistry, but has not been registered."""

    pass


class FilterRegistry:
    """
    The primary purpose of the FilterRegistry is to ensure that only registered models are available
    in the FiltrateAdmin.
    """

    def __init__(self):
        self._registry = {}

    def register(self, cls: Model) -> None:
        """Register a Model with Filtrate.  This allows users with access to create filters to select
        this model to create custom filters for.

        Args:
            cls (Model): The model being registered.

        Raises:
            `AlreadyRegistered` if the model has already been registered
        """
        if cls in self._registry:
            raise AlreadyRegistered(f"The model {cls.__name__} is already registered")

        self._registry[cls.__name__] = cls

    def unregister(self, cls: Model) -> None:
        """Unregister a Model with Filtrate.  This will cause the model to no longer be available for
        creating filters.

        Args:
            cls (Model): The model being unregistered.

        Raises:
            `NotRegistered` if the model is not currently registered
        """
        if cls.__name__ not in self._registry:
            raise NotRegistered(f"The model {cls.__name__} is not registered")

        del self._registry[cls.__name__]

    def get(self, model_name: str, raise_exception: bool = True) -> Model | None:
        if model_name not in self._registry:
            if raise_exception:
                raise ModelNotFound(f"Model {model_name} is not a valid model")

            return

        return self._registry[model_name]

    def all(self):
        return self._registry.items()


filter_registry = FilterRegistry()
