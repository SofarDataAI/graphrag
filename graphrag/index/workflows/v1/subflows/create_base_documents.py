# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""All the steps to transform base documents."""

from typing import cast

import modin.pandas as pd
from datashaper import (
    Table,
    VerbInput,
    verb,
)
from datashaper.table_store.types import VerbResult, create_verb_result

from graphrag.index.flows.create_base_documents import (
    create_base_documents as create_base_documents_flow,
)
from graphrag.index.utils.ds_util import get_required_input_table


@verb(name="create_base_documents", treats_input_tables_as_immutable=True)
def create_base_documents(
    input: VerbInput,
    document_attribute_columns: list[str] | None = None,
    **_kwargs: dict,
) -> VerbResult:
    """All the steps to transform base documents."""
    source = cast(pd.DataFrame, input.get_input())
    text_units = cast(pd.DataFrame, get_required_input_table(input, "text_units").table)

    output = create_base_documents_flow(
        source, text_units, document_attribute_columns=document_attribute_columns
    )

    return create_verb_result(
        cast(
            Table,
            output,
        )
    )
