"""Module for image cleanup operations."""

try:
    import cv2
except ImportError:
    cv2 = None
import numpy as np
from PIL import Image


def clean_image(pil_image: Image.Image, white_point: int = 226) -> Image.Image:
    """Applies a linear levels adjustment to the image, setting the white point.

    This effectively removes light gray bleed-through by mapping the
    white_point (default 226) and everything above it to pure white (255).

    Args:
        pil_image (PIL.Image): The input image.
        white_point (int): The pixel value (0-255) to map to pure white (255).

    Returns:
        PIL.Image: The cleaned image.
    """
    # Convert PIL to numpy array
    if pil_image.mode == "RGB":
        img_np = np.array(pil_image)
    elif pil_image.mode == "L":
        img_np = np.array(pil_image)
    else:
        img_np = np.array(pil_image.convert("RGB"))

    # Create LookUp Table (LUT) for linear levels adjustment
    lut = np.zeros((256,), dtype=np.uint8)
    for i in range(256):
        if i >= white_point:
            val = 255
        else:
            # Linear interpolation: 0 -> 0, white_point -> 255
            val = i * 255.0 / white_point
        lut[i] = np.clip(val, 0, 255)

    # Apply LUT
    if cv2 is not None:
        cleaned_np = cv2.LUT(img_np, lut)
    else:
        cleaned_np = lut[img_np]

    # Convert back to PIL
    cleaned_pil = Image.fromarray(cleaned_np)

    if pil_image.mode != cleaned_pil.mode:
        cleaned_pil = cleaned_pil.convert(pil_image.mode)

    return cleaned_pil
