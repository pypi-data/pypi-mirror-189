from ._AnyTreeAscendingIter import AnyTreeAscendingIter
from ._RecursionLimit import RecursionLimit
from ._ScalarFormatterFixedPrecision import ScalarFormatterFixedPrecision
from ._alifestd_aggregate_phylogenies import alifestd_aggregate_phylogenies
from ._alifestd_assign_contiguous_ids import alifestd_assign_contiguous_ids
from ._alifestd_collapse_unifurcations import alifestd_collapse_unifurcations
from ._alifestd_find_leaf_ids import alifestd_find_leaf_ids
from ._alifestd_has_compact_ids import alifestd_has_compact_ids
from ._alifestd_has_contiguous_ids import alifestd_has_contiguous_ids
from ._alifestd_has_multiple_roots import alifestd_has_multiple_roots
from ._alifestd_is_asexual import alifestd_is_asexual
from ._alifestd_is_sexual import alifestd_is_sexual
from ._alifestd_is_topologically_sorted import alifestd_is_topologically_sorted
from ._alifestd_make_ancestor_id_col import alifestd_make_ancestor_id_col
from ._alifestd_make_ancestor_list_col import alifestd_make_ancestor_list_col
from ._alifestd_parse_ancestor_id import alifestd_parse_ancestor_id
from ._alifestd_parse_ancestor_ids import alifestd_parse_ancestor_ids
from ._alifestd_to_working_format import alifestd_to_working_format
from ._alifestd_topological_sort import alifestd_topological_sort
from ._alifestd_try_add_ancestor_id_col import alifestd_try_add_ancestor_id_col
from ._alifestd_validate import alifestd_validate
from ._all_same import all_same
from ._all_unique import all_unique
from ._apply_swaps import apply_swaps
from ._bit_ceil import bit_ceil
from ._bit_floor import bit_floor
from ._caretdown_marker import caretdown_marker
from ._caretup_marker import caretup_marker
from ._check_testing_requirements import check_testing_requirements
from ._consume import consume
from ._count_unique import count_unique
from ._demark import demark
from ._div_range import div_range
from ._find_bounds import find_bounds
from ._get_hstrat_version import get_hstrat_version
from ._give_len import give_len
from ._indices_of_unique import indices_of_unique
from ._is_base64 import is_base64
from ._is_in_coverage_run import is_in_coverage_run
from ._is_in_unit_test import is_in_unit_test
from ._is_nondecreasing import is_nondecreasing
from ._is_nonincreasing import is_nonincreasing
from ._is_strictly_decreasing import is_strictly_decreasing
from ._is_strictly_increasing import is_strictly_increasing
from ._is_subset import is_subset
from ._iter_chunks import iter_chunks
from ._jit import jit
from ._jit_numba_dict_t import jit_numba_dict_t
from ._jit_numpy_bool_t import jit_numpy_bool_t
from ._jit_numpy_int64_t import jit_numpy_int64_t
from ._launder_impl_modules import launder_impl_modules
from ._log_once_in_a_row import log_once_in_a_row
from ._memoize_generator import memoize_generator
from ._omit_last import omit_last
from ._pairwise import pairwise
from ._popcount import popcount
from ._release_cur_mpl_fig import release_cur_mpl_fig
from ._scale_luminosity import scale_luminosity
from ._seed_random import seed_random
from ._splicewhile import splicewhile
from ._swap_rows_and_indices import swap_rows_and_indices
from ._zip_strict import zip_strict

# adapted from https://stackoverflow.com/a/31079085
__all__ = [
    "alifestd_aggregate_phylogenies",
    "alifestd_assign_contiguous_ids",
    "alifestd_collapse_unifurcations",
    "alifestd_find_leaf_ids",
    "alifestd_has_compact_ids",
    "alifestd_has_contiguous_ids",
    "alifestd_has_multiple_roots",
    "alifestd_is_asexual",
    "alifestd_is_sexual",
    "alifestd_is_topologically_sorted",
    "alifestd_make_ancestor_id_col",
    "alifestd_make_ancestor_list_col",
    "alifestd_parse_ancestor_id",
    "alifestd_parse_ancestor_ids",
    "alifestd_to_working_format",
    "alifestd_topological_sort",
    "alifestd_try_add_ancestor_id_col",
    "alifestd_validate",
    "all_same",
    "all_unique",
    "apply_swaps",
    "AnyTreeAscendingIter",
    "bit_ceil",
    "bit_floor",
    "caretdown_marker",
    "caretup_marker",
    "check_testing_requirements",
    "consume",
    "count_unique",
    "demark",
    "div_range",
    "find_bounds",
    "get_hstrat_version",
    "give_len",
    "indices_of_unique",
    "is_base64",
    "is_in_coverage_run",
    "is_in_unit_test",
    "is_nondecreasing",
    "is_nonincreasing",
    "is_strictly_decreasing",
    "is_strictly_increasing",
    "is_subset",
    "iter_chunks",
    "jit",
    "jit_numba_dict_t",
    "jit_numpy_bool_t",
    "jit_numpy_int64_t",
    "launder_impl_modules",
    "log_once_in_a_row",
    "memoize_generator",
    "omit_last",
    "pairwise",
    "popcount",
    "RecursionLimit",
    "release_cur_mpl_fig",
    "scale_luminosity",
    "ScalarFormatterFixedPrecision",
    "seed_random",
    "splicewhile",
    "swap_rows_and_indices",
    "zip_strict",
]

for o in __all__:
    try:
        eval(o).__module__ = __name__
    except (AttributeError, TypeError):
        pass
