import typing

from iterpop import iterpop as ip

from ..genome_instrumentation import HereditaryStratigraphicColumn
from ._col_to_records import col_to_records


def pop_to_records(
    columns: typing.Iterable[HereditaryStratigraphicColumn],
) -> typing.Dict:
    """Serialize a sequence of `HereditaryStratigraphicColumn`s to a dict
    composed of builtin types.

    All `HereditaryStratigraphicColumn`s must share identical `policy`,
    `policy_algo`, `policy_spec`, and `differentia_bit_width`. For efficiency,
    these records are recorded once for all columns.
    """
    col_records = [col_to_records(column) for column in columns]

    res = {}
    for common_field in (
        "policy",
        "policy_algo",
        "policy_spec",
        "differentia_bit_width",
        "hstrat_version",
    ):
        res[common_field] = ip.pourhomogeneous(
            col_record.pop(common_field) for col_record in col_records
        )

    res["columns"] = col_records

    return res
