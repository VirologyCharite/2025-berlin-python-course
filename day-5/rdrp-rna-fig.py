import argparse
import tomllib

from rdrplib import RdrpFig


def main():
    parser = argparse.ArgumentParser(
        description="Make a figure of an RNA molecule in a polymerase"
    )
    parser.add_argument("--rna", help="The RNA sequence.", required=True)
    parser.add_argument(
        "--structure", help="The 'structure' information.", required=True
    )
    parser.add_argument(
        "--figure-filename",
        help="The file to write the figure to.",
        required=True,
    )
    parser.add_argument(
        "--config",
        default="config.toml",
        help="The configuration file.",
    )

    args = parser.parse_args()

    with open(args.config, 'rb') as f:
        config = tomllib.load(f)

    r = RdrpFig(args.rna, args.structure, config)
    r.save_figure(args.figure_filename)


if __name__ == "__main__":
    main()
