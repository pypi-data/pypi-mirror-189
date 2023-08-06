from __future__ import annotations
import typing as _t

import sqlalchemy.engine as _sa_engine
import sqlalchemy as _sa
from fullmetalalchemy.basetable import BaseTable

import fullmetalalchemy.delete as _delete
import fullmetalalchemy.features as _features
import fullmetalalchemy.insert as _insert
import fullmetalalchemy.update as _update
import fullmetalalchemy.types as _types


class SessionTable(BaseTable):
    def __init__(
        self,
        name: str,
        engine: _sa_engine.Engine,
        schema: _t.Optional[str] = None
    ) -> None:
        super().__init__(name, engine, schema)
        self.session = _features.get_session(engine)

    def __enter__(self) -> SessionTable:
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.rollback()
            raise exc_value
        else:
            self.commit()

    def __repr__(self) -> str:
        return f'SessionTable(name={self.name}, columns={self.column_names}, pks={self.primary_key_names}, types={self.column_types})'

    def commit(self) -> SessionTable:
        """Commit session, return new SessionTable"""
        self.session.commit()
        return SessionTable(self.name, self.engine, self.schema)
    
    def rollback(self) -> SessionTable:
        """Rollback session, return new SessionTable"""
        self.session.rollback()
        return SessionTable(self.name, self.engine, self.schema)

    def delete_records(
        self,
        column_name: str,
        values: _t.Sequence
    ) -> None:
        _delete.delete_records_session(self.sa_table, column_name, values, self.session)

    def delete_records_by_values(
        self,
        records: _t.List[dict]
    ) -> None:
        _delete.delete_records_by_values_session(self.sa_table, records, self.session)

    def delete_all_records(self) -> None:
        _delete.delete_all_records_session(self.sa_table, self.session)

    def insert_from_table(
        self,
        sa_table: _sa.Table
    ) -> None:
        _insert.insert_from_table_session(self.sa_table, sa_table, self.session)

    def insert_records(
        self,
        records: _t.Sequence[_types.Record]
    ) -> None:
        _insert.insert_records_session(self.sa_table, records, self.session)

    def update_matching_records(
        self,
        records: _t.Sequence[_types.Record],
        match_column_names: _t.Sequence[str]
    ) -> None:
        _update.update_matching_records_session(
            self.sa_table, records, match_column_names, self.session)

    def update_records(
        self,
        records: _t.Sequence[_types.Record],
        match_column_names: _t.Optional[_t.Sequence[str]] = None,
    ) -> None:
        _update.update_records_session(
            self.sa_table, records, self.session, match_column_names)

    def set_column_values(
        self,
        column_name: str,
        value: _t.Any
    ) -> None:
        _update.set_column_values_session(
            self.sa_table, column_name, value, self.session)