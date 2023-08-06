import io

from kikiutils.decorators import try_and_get_data
from kikiutils.check import isbytes
from kikiutils.file import get_file_mime, save_file_as_bytesio
from kikiutils.requests import get_response
from PIL import Image
from typing import Optional

from .typehint import ImageData


__all__ = [
    'convert_image',
    'get_image'
]


@try_and_get_data
def convert_image(
    image_data: ImageData,
    format: str = 'webp',
    quality: int = 100,
    get_bytes: bool = False
):
    """Convert image to other format, return bytes or BytesIO object."""

    if isbytes(image_data):
        image_data = io.BytesIO(image_data)
    image = Image.open(image_data)

    return save_file_as_bytesio(
        image.save,
        get_bytes,
        format=format,
        quality=quality,
        lossless=False
    )


@try_and_get_data
def get_image(
    url: str,
    check: bool = True,
    get_bytes: bool = False,
    request_method: str = 'GET',
    convert_format: Optional[str] = None
):
    """Get image by url, return bytes or BytesIO object."""

    if (response := get_response(url, request_method)) is None:
        return

    image_bytes = response.content

    if check and get_file_mime(image_bytes)[0] != 'image':
        return

    if convert_format:
        image_bytes = convert_image(image_bytes, convert_format, get_bytes=True)

    if get_bytes:
        return image_bytes

    return io.BytesIO(image_bytes)
