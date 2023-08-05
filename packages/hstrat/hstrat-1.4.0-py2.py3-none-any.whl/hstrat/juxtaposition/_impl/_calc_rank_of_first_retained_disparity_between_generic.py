from collections import deque
import typing

from ...genome_instrumentation import HereditaryStratigraphicColumn


def calc_rank_of_first_retained_disparity_between_generic(
    first: HereditaryStratigraphicColumn,
    second: HereditaryStratigraphicColumn,
    *,
    first_start_idx: int = 0,
    second_start_idx: int = 0,
    confidence_level: float,
) -> typing.Optional[int]:
    """Find first mismatching strata between columns.

    Implementation detail. Provides general-case implementation.
    """
    # helper setup
    first_iter = first._stratum_ordered_store.IterRankDifferentia(
        get_rank_at_column_index=first.GetRankAtColumnIndex,
        start_column_index=first_start_idx,
    )
    second_iter = second._stratum_ordered_store.IterRankDifferentia(
        get_rank_at_column_index=second.GetRankAtColumnIndex,
        start_column_index=second_start_idx,
    )
    first_cur_rank, first_cur_differentia = next(first_iter)
    second_cur_rank, second_cur_differentia = next(second_iter)
    first_prev_rank: int
    second_prev_rank: int

    def advance_first():
        nonlocal first_prev_rank, first_cur_rank, first_cur_differentia, first_iter
        try:
            first_prev_rank = first_cur_rank
            first_cur_rank, first_cur_differentia = next(first_iter)
        except StopIteration:
            first_iter = None

    def advance_second():
        nonlocal second_prev_rank, second_cur_rank, second_cur_differentia, second_iter
        try:
            second_prev_rank = second_cur_rank
            second_cur_rank, second_cur_differentia = next(second_iter)
        except StopIteration:
            second_iter = None

    # we need to keep track of enough last-seen common ranks so that we
    # can discount this many (minus 1) as potentially occuring due to
    # spurious differentia collisions
    assert (
        first.GetStratumDifferentiaBitWidth()
        == second.GetStratumDifferentiaBitWidth()
    )
    collision_implausibility_threshold = (
        first.CalcMinImplausibleSpuriousConsecutiveDifferentiaCollisions(
            significance_level=1.0 - confidence_level,
        )
    )
    assert collision_implausibility_threshold > 0
    # holds up to n last-seen common ranks,
    # with the newest last-seen rank at the front (index 0)
    # and the up to nth last-seen rank at the back (index -1)
    preceding_common_ranks = deque([], collision_implausibility_threshold)
    # a.k.a.
    # while (
    #     first_column_idx < first.GetNumStrataRetained()
    #     and second_column_idx < second.GetNumStrataRetained()
    # ):
    while first_iter is not None and second_iter is not None:
        if first_cur_rank == second_cur_rank:
            # strata at same rank can be compared
            if first_cur_differentia == second_cur_differentia:
                preceding_common_ranks.appendleft(first_cur_rank)
                # matching differentiae at the same rank,
                # keep searching for mismatch
                # advance first and second
                # must ensure both advance, even if one stops iteration
                advance_first()
                advance_second()
            else:
                # mismatching differentiae at the same rank
                preceding_common_ranks.appendleft(first_cur_rank)
                assert 0 <= first_cur_rank < first.GetNumStrataDeposited()

                # discount collision_implausibility_threshold - 1 common
                # ranks due to potential spurious differentia collisions;
                # if not enough common ranks are available we still know
                # *definitively* that a disparity occured (because we
                # observed disparite strata at the same rank); so, make the
                # conservative assumption that the disparity occured as far
                # back as possible (the oldest up to nth last-seen common
                # rank, at the back of the deque)
                return preceding_common_ranks[-1]
        elif first_cur_rank < second_cur_rank:
            # current stratum on first column older than on second column
            # advance to next-newer stratum on first column
            advance_first()
        elif first_cur_rank > second_cur_rank:
            # current stratum on second column older than on first column
            # advance to next-newer stratum on second column
            advance_second()

    if first_iter is not None:
        # although no mismatching strata found between first and second
        # first has strata ranks beyond the newest found in second
        # conservatively assume mismatch will be with next rank of second
        assert second_iter is None
        preceding_common_ranks.appendleft(second_prev_rank + 1)
        res = preceding_common_ranks[-1]
        assert 0 <= res <= first.GetNumStrataDeposited()
        assert 0 <= res <= second.GetNumStrataDeposited()
        return res
    elif second_iter is not None:
        # although no mismatching strata found between second and first
        # second has strata ranks beyond the newest found in first
        # conservatively assume mismatch will be with next rank
        assert first_iter is None
        preceding_common_ranks.appendleft(first_prev_rank + 1)
        res = preceding_common_ranks[-1]
        assert 0 <= res <= first.GetNumStrataDeposited()
        assert 0 <= res <= second.GetNumStrataDeposited()
        return res
    else:
        # no disparate strata found
        # and first and second have the same newest rank
        assert first_iter is None and second_iter is None
        preceding_common_ranks.appendleft(None)
        return preceding_common_ranks[-1]
