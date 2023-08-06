import io

from typing import Optional

from .typehint import ImageData

async def aconvert_image(image_data: ImageData, format: str = 'webp', quality: int = 100, get_bytes: bool = False) -> Optional[bytes | io.BytesIO]: ...
async def aget_image(url: str, check: bool = True, get_bytes: bool = False, request_method: str = 'GET') -> Optional[bytes | io.BytesIO]: ...
