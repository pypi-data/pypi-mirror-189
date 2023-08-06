import typing as _t

import sqlalchemy as _sa
import sqlalchemy.engine as _sa_engine
import sqlalchemy.schema as _sa_schema

import sqlalchemize.features as _features
import sqlalchemize.exceptions as _ex


def drop_table(
    table: _t.Union[_sa.Table, str],
    engine: _t.Optional[_sa_engine.Engine] = None,
    if_exists: bool = True,
    schema: _t.Optional[str] = None
) -> None:
    """
    Example
    -------
    >>> import sqlalchemy as sa
    >>> from sqlalchemize.test_setup import create_test_table
    >>> from sqlalchemize.features import get_table_names
    >>> from sqlalchemize.drop import drop_table

    >>> engine = sa.create_engine('data/sqlite:///test.db')
    >>> table = create_test_table(engine)
    >>> get_table_names(engine)
    ['xy']

    >>> drop_table(table, engine)
    >>> get_table_names(engine)
    []
    """
    if isinstance(table, str):
        if table not in _sa.inspect(engine).get_table_names(schema=schema):
            if if_exists:
                return
        if engine is None:
            raise ValueError('Must pass engine if table is str.')
        table = _features.get_table(table, engine, schema=schema)
    sql = _sa_schema.DropTable(table, if_exists=if_exists)
    engine = _ex.check_for_engine(table, engine)
    with engine.connect() as con:
        con.execute(sql)