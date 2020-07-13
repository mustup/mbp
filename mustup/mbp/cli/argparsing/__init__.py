import argparse
import logging
import sys

import mustup.mbp.cli.argparsing.types.logging_level

logger = logging.getLogger(
    __name__,
)


def set_up(
        ):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        '-d',
        '--description',
        default='',
        dest='picture_description',
        help='picture description',
        metavar='TEXT',
    )

    parser.add_argument(
        '-l',
        '--logging-level',
        default='warning',
        dest='logging_level',
        help='logging level',
        type=mustup.mbp.cli.argparsing.types.logging_level.parser,
        metavar='PYTHON_LOGGING_LEVEL',
    )

    parser.add_argument(
        '-o',
        '--output',
        default=sys.stdout,
        dest='output',
        help='path to which to write Vorbis comment',
        metavar='PATH',
        type=argparse.FileType(
            'w',
        ),
    )

    parser.add_argument(
        '-p',
        '--path',
        dest='picture_path',
        help='path to the picture',
        metavar='PATH',
        required=True,
    )

    parser.add_argument(
        '-t',
        '--type',
        choices=[
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
        ],
        dest='picture_type',
        help='ID3 APIC picture type',
        metavar='ID3_APIC_TYPE',
        required=True,
        type=int,
    )

    return parser
