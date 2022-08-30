import datetime
from pathlib import Path


def get_filename(file_info: dict) -> Path:
    file = Path(file_info["filename"])
    if last_modified := file_info.get("last-modified"):
        date = datetime.datetime.strptime(
            file_info.get("last-modified", "9999-12-31 23:59:59"),
            "%Y-%m-%d %H:%M:%S",
        )
        date = f"{date:%Y%m%d}"
    else:
        date = "_______"
    original_stem = file.stem
    suffix = file.suffix
    new_name = f"{original_stem}@{date}{suffix}"
    return Path(new_name)
