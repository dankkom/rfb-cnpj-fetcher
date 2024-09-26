from pathlib import Path


def get_filename(**file_meta) -> str:
    dataset = file_meta["dataset"]
    extension = file_meta["extension"]

    if last_modified := file_meta.get("last_modified"):
        date = f"{last_modified:%Y%m%d}"
    else:
        date = "________"

    if partition := file_meta.get("partition"):
        new_name = f"{dataset}_{partition}@{date}.{extension}"
    else:
        new_name = f"{dataset}@{date}.{extension}"

    return new_name


def get_filepath(data_dir: Path, **file_meta) -> Path:
    filename = get_filename(**file_meta)
    if group := file_meta.get("group"):
        dest_dir = data_dir / group / file_meta["dataset"]
    else:
        dest_dir = data_dir / file_meta["dataset"]
    if file_meta.get("date_ref"):
        dest_dir = dest_dir / f"{file_meta['date_ref']:%Y%m}"
    filepath = dest_dir / filename
    return filepath
