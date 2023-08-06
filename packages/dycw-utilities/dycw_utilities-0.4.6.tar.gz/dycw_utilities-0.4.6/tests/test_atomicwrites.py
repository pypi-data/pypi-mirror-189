from pathlib import Path
from typing import Union

from pytest import mark, param, raises

from utilities.atomicwrites import writer


class TestWriter:
    @mark.parametrize(
        ("is_binary", "contents"),
        [
            param(False, "contents", id="text"),
            param(True, b"contents", id="binary"),
        ],
    )
    def test_basic_usage(
        self,
        tmp_path: Path,
        is_binary: bool,
        contents: Union[str, bytes],
    ) -> None:
        path = tmp_path.joinpath("file.txt")
        with writer(path) as temp, temp.open(
            mode="wb" if is_binary else "w",
        ) as fh1:
            _ = fh1.write(contents)
        with path.open(mode="rb" if is_binary else "r") as fh2:
            assert fh2.read() == contents

    def test_file_exists_error(self, tmp_path: Path) -> None:
        path = tmp_path.joinpath("file.txt")
        with writer(path) as temp1, temp1.open(mode="w") as fh1:
            _ = fh1.write("contents")
        with raises(FileExistsError, match=str(path)), writer(
            path,
        ) as temp2, temp2.open(mode="w") as fh2:
            _ = fh2.write("new contents")

    def test_overwrite(self, tmp_path: Path) -> None:
        path = tmp_path.joinpath("file.txt")
        with writer(path) as temp1, temp1.open(mode="w") as fh1:
            _ = fh1.write("contents")
        with writer(path, overwrite=True) as temp2, temp2.open(mode="w") as fh2:
            _ = fh2.write("new contents")
        with path.open() as fh3:
            assert fh3.read() == "new contents"
