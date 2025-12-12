import cv2
import numpy as np
from PIL import Image

def clean_image(pil_image, white_point=226):
    """
    Applies a linear levels adjustment to the image, setting the white point.
    This effectively removes light gray bleed-through by mapping the 
    white_point (default 226) and everything above it to pure white (255).
    
    Args:
        pil_image (PIL.Image): The input image.
        white_point (int): The pixel value (0-255) to map to pure white (255).
                           
    Returns:
        PIL.Image: The cleaned image.
    """
    # Convert PIL to OpenCV (numpy array)
    # Handle RGB vs L
    if pil_image.mode == 'RGB':
        img_np = np.array(pil_image)
        # We can apply the LUT to all channels independently
    elif pil_image.mode == 'L':
        img_np = np.array(pil_image)
    else:
        img_np = np.array(pil_image.convert('RGB'))

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
    # If RGB, cv2.LUT works on 3 channels if the array is right, or we can just use numpy indexing for speed if 1D LUT
    # cv2.LUT expects 8-bit input.
    
    cleaned_np = cv2.LUT(img_np, lut)
    
    # Convert back to PIL
    cleaned_pil = Image.fromarray(cleaned_np)
    
    if pil_image.mode != cleaned_pil.mode:
        cleaned_pil = cleaned_pil.convert(pil_image.mode)

    return cleaned_pil
