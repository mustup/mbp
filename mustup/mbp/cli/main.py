import logging

import mustup.mbp.cli.argparsing
import mustup.mbp.cli.logging
import mustup.mbp.main

logger = logging.getLogger(
    __name__,
)


def entry_point(
        ):
    parser = mustup.mbp.cli.argparsing.set_up(
    )

    args = parser.parse_args(
    )

    logging_level = args.logging_level

    mustup.mbp.cli.logging.set_up(
        level=logging_level,
    )

    mustup.mbp.main.generate(
        picture_description=args.picture_description,
        picture_path=args.picture_path,
        picture_type=args.picture_type,
        output=args.output,
    )
