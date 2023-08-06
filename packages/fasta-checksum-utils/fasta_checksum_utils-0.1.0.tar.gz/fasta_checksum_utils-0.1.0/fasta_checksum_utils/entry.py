import argparse
import asyncio

from pathlib import Path

from .algorithms import AlgorithmMD5, AlgorithmTRUNC512
from .fasta import fasta_report


async def main():
    parser = argparse.ArgumentParser(
        prog="fasta-checksum-utils",
        description="A library and command-line utility for checksumming FASTA files and individual contigs.",
    )

    parser.add_argument("fasta", type=Path, help="A FASTA file to checksum.")
    parser.add_argument(
        "--out-format", type=str, default="text", choices=("text", "bento-json"),
        help="Output format for checksum report; either 'text' or 'bento-json' (default: 'text').")

    args = parser.parse_args()

    report = await fasta_report(args.fasta, (AlgorithmMD5, AlgorithmTRUNC512))
    if args.out_format == "bento-json":
        print(report.as_bento_json())
    else:
        print(report.as_text_report(), end="")


def entry():
    asyncio.run(main())


if __name__ == "__main__":  # pragma: no cover
    entry()
