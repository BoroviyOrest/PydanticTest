from typing import Callable


def is_editable(editable_in_statuses: list[int]) -> Callable:
    def is_editable_inner(cls, v, values):
        # if we don't have any value then no need to check if the field was editable
        if not v:
            return

        status = values['status']
        assert status in editable_in_statuses, f'this field is not editable in status {status}'
        return v

    return is_editable_inner


def is_obligatory(obligatory_from_status: int) -> Callable:
    def is_obligatory_inner(cls, v, values):
        # if we have a value then no need to check if the field was obligatory
        if v is not None:
            return v

        status = values['status']
        assert status < obligatory_from_status, f'this field is obligatory in status {status}'
        return v

    return is_obligatory_inner
