from __future__ import annotations

from datetime import timedelta
from typing import TYPE_CHECKING, Any, Generic, List, Literal, Mapping, Optional, Set, Type, TypeVar, Union

from chalk._validation.feature_validation import FeatureValidation
from chalk.features._encoding.primitive import TPrimitive
from chalk.utils.collections import ensure_tuple
from chalk.utils.duration import Duration, parse_chalk_duration, timedelta_to_duration

T = TypeVar("T")
TPrim = TypeVar("TPrim", bound=TPrimitive)
TRich = TypeVar("TRich")

if TYPE_CHECKING:
    import polars as pl

    from chalk.features._encoding.converter import TDecoder, TEncoder


class WindowedInstance(Generic[T]):
    def __init__(self, values: Mapping[str, T]):
        self.values = values

    def __call__(self, period: str):
        return self.values[period]


class WindowedMeta(type, Generic[T]):
    def __getitem__(cls, underlying: Type[T]) -> "Windowed[Type[T]]":
        return Windowed(
            kind=underlying,
            buckets=[],
            mode="tumbling",
            description=None,
            owner=None,
            tags=None,
            name=None,
            default=None,
            max_staleness=None,
            version=None,
            etl_offline_to_online=None,
            encoder=None,
            decoder=None,
            min=None,
            max=None,
            min_length=None,
            max_length=None,
            contains=None,
            dtype=None,
        )  # noqa


JsonValue = Any


def get_duration_secs(duration: Union[str, int, timedelta]) -> int:
    if isinstance(duration, str):
        duration = parse_chalk_duration(duration)
    if isinstance(duration, timedelta):
        duration_secs_float = duration.total_seconds()
        duration_secs_int = int(duration_secs_float)
        if duration_secs_float != duration_secs_int:
            raise ValueError("Windows that are fractions of seconds are not yet supported")
        duration = duration_secs_int
    return duration


def get_name_with_duration(name_or_fqn: str, duration: Union[str, int, timedelta]) -> str:
    duration_secs = get_duration_secs(duration)
    return f"{name_or_fqn}__{duration_secs}__"


class Windowed(Generic[TPrim, TRich], metaclass=WindowedMeta):
    _buckets: List[str]
    _mode: Optional[Literal["tumbling", "continuous"]]
    _description: Optional[str]
    _owner: Optional[str]
    _tags: Optional[Any]
    _name: Optional[str]
    _default: Optional[TRich]
    _version: Optional[int]
    _etl_offline_to_online: Optional[bool]
    _encoder: Optional[TEncoder[TPrim, TRich]]
    _decoder: Optional[TDecoder[TPrim, TRich]]
    _min: Optional[TRich]
    _max: Optional[TRich]
    _min_length: Optional[int]
    _max_length: Optional[int]
    _contains: Optional[TRich]
    _dtype: Optional[Union[Type[pl.DataType], pl.DataType]]

    @property
    def buckets_seconds(self) -> Set[int]:
        return set(int(parse_chalk_duration(bucket).total_seconds()) for bucket in self._buckets)

    @property
    def kind(self) -> Type[TRich]:
        if self._kind is None:
            raise RuntimeError("Window type has not yet been parsed")
        return self._kind

    @kind.setter
    def kind(self, kind: Type[TRich]) -> None:
        assert self._kind is None, "Window type cannot be set twice"
        self._kind = kind

    def to_feature(self, bucket: Optional[Union[int, str]]):
        from chalk.features import Feature

        assert self._name is not None

        if bucket is None:
            name = self._name
        else:
            if get_duration_secs(bucket) not in self.buckets_seconds:
                raise ValueError(f"Bucket {bucket} is not in the list of specified buckets")
            name = get_name_with_duration(self._name, bucket)

        return Feature(
            name=name,
            version=self._version,
            owner=self._owner,
            tags=None if self._tags is None else list(ensure_tuple(self._tags)),
            description=self._description,
            primary=False,
            default=self._default,
            max_staleness=(
                timedelta_to_duration(self._max_staleness)
                if isinstance(self._max_staleness, timedelta)
                else self._max_staleness
            ),
            etl_offline_to_online=self._etl_offline_to_online,
            encoder=self._encoder,
            decoder=self._decoder,
            pyarrow_dtype=self._dtype,
            validations=FeatureValidation(
                min=self._min,
                max=self._max,
                min_length=self._min_length,
                max_length=self._max_length,
                contains=self._contains,
            ),
            # Only the root feature should have all the durations
            # The pseudofeatures, which are bound to a duration, should not have the durations
            # of the other buckets
            window_durations=tuple(self.buckets_seconds) if bucket is None else tuple(),
            window_duration=None if bucket is None else get_duration_secs(bucket),
            window_mode=self._mode,
        )

    def __init__(
        self,
        buckets: List[str],
        mode: Literal["tumbling", "continuous"],
        description: Optional[str],
        owner: Optional[str],
        tags: Optional[Any],
        name: Optional[str],
        default: Optional[TRich],
        max_staleness: Optional[Duration],
        version: Optional[int],
        etl_offline_to_online: Optional[bool],
        encoder: Optional[TEncoder[TPrim, TRich]],
        decoder: Optional[TDecoder[TPrim, TRich]],
        min: Optional[TRich],
        max: Optional[TRich],
        min_length: Optional[int],
        max_length: Optional[int],
        contains: Optional[TRich],
        dtype: Optional[Union[Type[pl.DataType], pl.DataType]],
        kind: Optional[Type[TRich]],
    ):
        self._kind = kind
        self._name: Optional[str] = None
        self._buckets = buckets
        self._mode = mode
        self._description = description
        self._owner = owner
        self._tags = tags
        self._name = name
        self._default = default
        self._max_staleness = max_staleness
        self._description = description
        self._version = version
        self._etl_offline_to_online = etl_offline_to_online
        self._encoder = encoder
        self._decoder = decoder
        self._min = min
        self._max = max
        self._min_length = min_length
        self._max_length = max_length
        self._contains = contains
        self._dtype = dtype


class SelectedWindow:
    def __init__(self, kind: Windowed, selected: str):
        self.windowed = kind
        self.selected = selected


def windowed(
    *buckets: str,
    mode: Literal["tumbling", "continuous"] = "tumbling",
    description: Optional[str] = None,
    owner: Optional[str] = None,
    tags: Optional[Any] = None,
    name: Optional[str] = None,
    default: Optional[T] = None,
    max_staleness: Optional[Duration] = ...,
    version: Optional[int] = None,
    etl_offline_to_online: Optional[bool] = None,
    encoder: Optional[TEncoder[TPrim, TRich]] = None,
    decoder: Optional[TDecoder[TPrim, TRich]] = None,
    min: Optional[T] = None,
    max: Optional[T] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    contains: Optional[T] = None,
    dtype: Optional[Union[Type[pl.DataType], pl.DataType]] = None,
) -> Windowed[T]:
    return Windowed(
        list(buckets),
        mode=mode,
        description=description,
        owner=owner,
        tags=tags,
        name=name,
        default=default,
        max_staleness=max_staleness,
        version=version,
        etl_offline_to_online=etl_offline_to_online,
        encoder=encoder,
        decoder=decoder,
        min=min,
        max=max,
        min_length=min_length,
        max_length=max_length,
        contains=contains,
        dtype=dtype,
        kind=None,
    )
