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
        filepath = data_dir / group / file_meta["dataset"] / filename
    else:
        filepath = data_dir / file_meta["dataset"] / filename
    return filepath
