"""Split aligned feature rows and labels reproducibly."""


def train_test_split(
    features: list[list[float]],
    labels: list[int],
    test_ratio: float,
    seed: int,
) -> tuple[
    list[list[float]],
    list[list[float]],
    list[int],
    list[int],
]:
    """Return train features, test features, train labels, and test labels."""

    raise NotImplementedError
