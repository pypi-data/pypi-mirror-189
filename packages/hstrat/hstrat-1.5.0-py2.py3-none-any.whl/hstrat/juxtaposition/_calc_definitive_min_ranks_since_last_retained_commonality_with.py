import typing

from ..genome_instrumentation import HereditaryStratigraphicColumn
from ._calc_ranks_since_last_retained_commonality_with import (
    calc_ranks_since_last_retained_commonality_with,
)


def calc_definitive_min_ranks_since_last_retained_commonality_with(
    focal: HereditaryStratigraphicColumn,
    other: HereditaryStratigraphicColumn,
) -> typing.Optional[int]:
    """Determine hard, inclusive lower bound on generations since MRCA.

    At least, how many depositions have elapsed along the focal column's line
    of descent since the last matching strata at the same rank between focal
    and other?

    Returns None if no common ancestor between focal and other can be
    resolved with absolute confidence.
    """
    confidence_level = 0.49
    assert (
        focal.GetStratumDifferentiaBitWidth()
        == other.GetStratumDifferentiaBitWidth()
    )
    assert (
        focal.CalcMinImplausibleSpuriousConsecutiveDifferentiaCollisions(
            significance_level=1.0 - confidence_level,
        )
        == 1
    )
    return calc_ranks_since_last_retained_commonality_with(
        focal,
        other,
        confidence_level=confidence_level,
    )
