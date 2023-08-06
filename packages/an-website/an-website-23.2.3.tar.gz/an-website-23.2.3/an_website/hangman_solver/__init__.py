# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""A page that helps solving hangman puzzles."""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path
from typing import Final, cast

import orjson as json
from typed_stream import Stream

DIR: Final = os.path.dirname(__file__)


BASE_WORD_DIR: Final = Path(DIR) / "words"


def get_filenames_and_languages() -> tuple[frozenset[str], frozenset[str]]:
    """
    Find all the words and return a tuple of their file names and languages.

    The file names are each in a frozenset to guarantee immutability.
    """
    languages: set[str] = set()
    filenames = (
        Stream(os.listdir(BASE_WORD_DIR))
        .filter(lambda folder: folder.startswith("words_"))
        .peek(lambda folder: languages.add(folder.removeprefix("words_")))
        .flat_map(lambda folder: (BASE_WORD_DIR / folder).iterdir())
        .filter(lambda file: file.suffix != ".py")
        .map(lambda file: file.relative_to(BASE_WORD_DIR))
        .map(str)
        .map(lambda rel_filename: rel_filename.split(".", 1)[0])
        .collect(frozenset)
    )
    return filenames, frozenset(languages)


FILE_NAMES, LANGUAGES = get_filenames_and_languages()


@lru_cache(10)
def get_words(filename: str) -> frozenset[str]:
    """Get the words with the filename and return them."""
    with open(
        os.path.join(BASE_WORD_DIR, f"{filename}.txt"), encoding="UTF-8"
    ) as file:
        return frozenset(file.read().splitlines())


@lru_cache(10)
def get_letters(filename: str) -> dict[str, int]:
    """Get the letters dict with the filename and return it."""
    with open(
        os.path.join(BASE_WORD_DIR, f"{filename}.json"), encoding="UTF-8"
    ) as file:
        # we know the files, so we know the type
        return cast(dict[str, int], json.loads(file.read()))
