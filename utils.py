# shim to keep backward compatibility while using the utils package
from .utils import get_csv_data  # type: ignore

__all__ = ["get_csv_data"]

