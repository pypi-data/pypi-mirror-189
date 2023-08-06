import typing as _t

import sqlalchemy as _sa
import sqlalchemy.orm.session as _sa_session
import sqlalchemy.ext.automap as _sa_automap
import sqlalchemy.engine as _sa_engine

import sqlalchemize.types as _types
import sqlalchemize.exceptions as _ex
import sqlalchemize.records as _records
import sqlalchemize.select as _select


def primary_key_columns(
    sa_table: _sa.Table
) ->  _t.List[_sa.Column]:
    """
    
    """
    return list(sa_table.primary_key.columns)


def primary_key_names(
    sa_table: _sa.Table
) ->  _t.List[str]:
    return [c.name for c in primary_key_columns(sa_table)]


def get_connection(
    connection: _t.Union[_types.SqlConnection, _sa_session.Session]
) -> _types.SqlConnection:
    if isinstance(connection, _sa_session.Session):
        return connection.connection()
    return connection


def get_metadata(
    connection,
    schema: _t.Optional[str] = None
) -> _sa.MetaData:
    return _sa.MetaData(bind=connection, schema=schema)


def get_table(
    name: str,
    connection: _types.SqlConnection,
    schema: _t.Optional[str] = None
) -> _sa.Table:
    metadata = get_metadata(connection, schema)
    autoload_with = get_connection(connection)
    return _sa.Table(name,
                 metadata,
                 autoload=True,
                 autoload_with=autoload_with,
                 extend_existing=True,
                 schema=schema)


def get_class(
    name: str,
    connection: _t.Union[_types.SqlConnection, _sa_session.Session],
    schema: _t.Optional[str] = None
):
    metadata = get_metadata(connection, schema)
    connection = get_connection(connection)

    metadata.reflect(connection, only=[name], schema=schema)
    Base = _sa_automap.automap_base(metadata=metadata)
    Base.prepare()
    if name not in Base.classes:
        raise _ex.MissingPrimaryKey()
    return Base.classes[name]


def get_session(
    engine: _sa_engine.Engine
) -> _sa_session.Session:
    return _sa_session.Session(engine)


def get_column(
    sa_table: _sa.Table,
    column_name: str
) -> _sa.Column:
    return sa_table.c[column_name]


def get_table_constraints(sa_table: _sa.Table):
    return sa_table.constraints


def get_primary_key_constraints(
    sa_table: _sa.Table
) -> _t.Tuple[str,  _t.List[str]]:
    cons = get_table_constraints(sa_table)
    for con in cons:
        if isinstance(con, _sa.PrimaryKeyConstraint):
            return con.name, [col.name for col in con.columns]
    return tuple()


def missing_primary_key(
    sa_table: _sa.Table,
):
    pks = get_primary_key_constraints(sa_table)
    return pks[1] == []


def get_column_types(sa_table: _sa.Table) -> dict:
    return {c.name: c.type for c in sa_table.c}


def get_column_names(sa_table: _sa.Table) ->  _t.List[str]:
    return [c.name for c in sa_table.columns]


def get_table_names(
    engine: _sa_engine.Engine,
    schema: _t.Optional[str] = None
) ->  _t.List[str]:
    return _sa.inspect(engine).get_table_names(schema)


def get_row_count(
    sa_table: _sa.Table,
    session: _t.Optional[_types.SqlConnection] = None
) -> int:
    session = _ex.check_for_engine(sa_table, session)
    col_name = get_column_names(sa_table)[0]
    col = get_column(sa_table, col_name)
    result = session.execute(_sa.func.count(col)).scalar()
    return result if result is not None else 0


def get_schemas(engine: _sa_engine.Engine) ->  _t.List[str]:
    insp = _sa.inspect(engine)
    return insp.get_schema_names()


def _get_where_clause(
    sa_table: _sa.Table,
    record: _types.Record
) ->  _t.List[bool]:
    return [sa_table.c[key_name]==key_value for key_name, key_value in record.items()]


def tables_metadata_equal(
    sa_table1: _sa.Table,
    sa_table2: _sa.Table
) -> bool:
    if sa_table1.name != sa_table2.name: return False

    column_types1 = get_column_types(sa_table1)
    column_types2 = get_column_types(sa_table2)
    # if column_types1 != column_types2: return False

    table1_keys = primary_key_names(sa_table1)
    table2_keys = primary_key_names(sa_table2)
    if set(table1_keys) != set(table2_keys): return False

    return True
