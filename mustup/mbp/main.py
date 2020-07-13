import base64
import logging
import mimetypes
import os

number_endianness = 'big'

logger = logging.getLogger(
    __name__,
)


def generate(
            picture_description,
            picture_path,
            picture_type,
            output,
        ):
    output.write(
        'METADATA_BLOCK_PICTURE=',
    )

    metadata_block_picture_data = [
    ]

    picture_type_bytes = picture_type.to_bytes(
        length=4,
        signed=False,
        byteorder=number_endianness,
    )

    metadata_block_picture_data.extend(
        picture_type_bytes,
    )

    mime_type, _ = mimetypes.guess_type(
        url=picture_path,
    )

    logger.info(
        'inferred MIME type: %s',
        mime_type,
    )

    mime_type_length = len(
        mime_type,
    )

    logger.debug(
        'length of MIME type string: %i bytes',
        mime_type_length,
    )

    mime_type_length_bytes = mime_type_length.to_bytes(
        length=4,
        signed=False,
        byteorder=number_endianness,
    )

    metadata_block_picture_data.extend(
        mime_type_length_bytes,
    )

    mime_type_bytes = mime_type.encode(
        'ascii',
    )

    metadata_block_picture_data.extend(
        mime_type_bytes,
    )

    picture_description_length = len(
        picture_description,
    )

    logger.debug(
        'length of description: %i bytes',
        picture_description_length,
    )

    picture_description_length_bytes = picture_description_length.to_bytes(
        length=4,
        signed=False,
        byteorder=number_endianness,
    )

    metadata_block_picture_data.extend(
        picture_description_length_bytes,
    )

    picture_description_bytes = picture_description.encode(
        'utf-8',
    )

    metadata_block_picture_data.extend(
        picture_description_bytes,
    )

    picture_width = 0
    picture_height = 0
    picture_color_depth = 0
    picture_color_amount = 0

    picture_width_bytes = picture_width.to_bytes(
        length=4,
        signed=False,
        byteorder=number_endianness,
    )

    metadata_block_picture_data.extend(
        picture_width_bytes,
    )

    picture_height_bytes = picture_height.to_bytes(
        length=4,
        signed=False,
        byteorder=number_endianness,
    )

    metadata_block_picture_data.extend(
        picture_height_bytes,
    )

    picture_color_depth_bytes = picture_color_depth.to_bytes(
        length=4,
        signed=False,
        byteorder=number_endianness,
    )

    metadata_block_picture_data.extend(
        picture_color_depth_bytes,
    )

    picture_color_amount_bytes = picture_color_amount.to_bytes(
        length=4,
        signed=False,
        byteorder=number_endianness,
    )

    metadata_block_picture_data.extend(
        picture_color_amount_bytes,
    )

    picture_file = open(
        picture_path,
        'rb',
    )

    picture_file_descriptor = picture_file.fileno(
    )

    picture_stat_results = os.stat(
        picture_file_descriptor,
    )

    picture_size = picture_stat_results.st_size

    logger.debug(
        'size of image file: %i bytes',
        picture_size,
    )

    picture_size_bytes = picture_size.to_bytes(
        length=4,
        signed=False,
        byteorder=number_endianness,
    )

    metadata_block_picture_data.extend(
        picture_size_bytes,
    )

    picture_data = picture_file.read(
    )

    picture_data_length = len(
        picture_data,
    )

    logger.debug(
        'size of read image data: %i bytes',
        picture_data_length,
    )

    assert picture_size == picture_data_length

    metadata_block_picture_data.extend(
        picture_data,
    )

    metadata_block_picture_data_base64 = base64.b64encode(
        s=bytes(
            metadata_block_picture_data,
        ),
    )

    metadata_block_picture_data_base64_ascii = metadata_block_picture_data_base64.decode(
        'ascii',
    )

    output.write(
        metadata_block_picture_data_base64_ascii,
    )

    output.write(
        '\n',
    )
