from pydantic import BaseModel


class FramingSpecs(BaseModel):
    frame_width: float
    frame_height: float
    top_bottom_margin: float
    left_right_margin: float
    image_width: float
    image_height: float


def calculate_margins(
    *,
    frame_width: float,
    frame_height: float,
    image_aspect_ratio: float,
    min_margin: float
):
    assert image_aspect_ratio >= 1
    if frame_width >= frame_height:
        # First try the long side (width) having min_margin
        left_right_margin = min_margin
        printed_image_width = frame_width - 2 * left_right_margin
        printed_image_height = printed_image_width / image_aspect_ratio
        top_bottom_margin = (frame_height - printed_image_height) / 2
        if top_bottom_margin >= min_margin:
            return FramingSpecs(
                frame_width=frame_width,
                frame_height=frame_height,
                top_bottom_margin=top_bottom_margin,
                left_right_margin=left_right_margin,
                image_width=printed_image_width,
                image_height=printed_image_height,
            )
        else:
            # Next try min_margin for height
            top_bottom_margin = min_margin
            printed_image_height = frame_height - 2 * top_bottom_margin
            printed_image_width = printed_image_height * image_aspect_ratio
            left_right_margin = (frame_width - printed_image_width) / 2
            return FramingSpecs(
                frame_width=frame_width,
                frame_height=frame_height,
                top_bottom_margin=top_bottom_margin,
                left_right_margin=left_right_margin,
                image_width=printed_image_width,
                image_height=printed_image_height,
            )
    else:
        # So frame height > width
        # First try the long side (height) having min_margin
        top_bottom_margin = min_margin
        printed_image_height = frame_height - 2 * top_bottom_margin
        printed_image_width = printed_image_height / image_aspect_ratio
        left_right_margin = (frame_width - printed_image_width) / 2
        if left_right_margin >= min_margin:
            return FramingSpecs(
                frame_width=frame_width,
                frame_height=frame_height,
                top_bottom_margin=top_bottom_margin,
                left_right_margin=left_right_margin,
                image_width=printed_image_width,
                image_height=printed_image_height,
            )
        else:
            left_right_margin = min_margin
            printed_image_width = frame_width - 2 * left_right_margin
            printed_image_height = printed_image_width * image_aspect_ratio
            top_bottom_margin = (frame_height - printed_image_height) / 2
            return FramingSpecs(
                frame_width=frame_width,
                frame_height=frame_height,
                top_bottom_margin=top_bottom_margin,
                left_right_margin=left_right_margin,
                image_width=printed_image_width,
                image_height=printed_image_height,
            )
