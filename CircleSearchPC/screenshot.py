import mss
import mss.tools

def take_screenshot(region):
    """
    Takes a screenshot of a specified region.

    Args:
        region (tuple): A tuple of (left, top, right, bottom).
    """
    if region is None:
        return None

    left, top, right, bottom = region
    width = right - left
    height = bottom - top

    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": top, "left": left, "width": width, "height": height}
        output = "temp_screenshot.png"

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        return output