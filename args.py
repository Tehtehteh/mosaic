from dataclasses import dataclass
from argparse import ArgumentParser, Namespace
from typing import Optional


@dataclass
class Args:
    storage_dir: str
    token: str
    search_term: Optional[str]

    @classmethod
    def from_parsed_args(cls, args: Namespace) -> 'Args':
        return cls(storage_dir=args.storage_dir,
                   search_term=args.search_term,
                   token=args.token)


def parse_args() -> Args:
    parser = ArgumentParser()
    parser.add_argument('--storage_dir', dest='storage_dir', default='storage',
                        help='Directory to store images.', type=str)
    parser.add_argument('--flickr_token', dest='token', required=True,
                        help='Flickr API token.', type=str)
    parser.add_argument('--search_term', dest='search_term', required=False,
                        help='Search term to look for pictures on Flickr.', type=str)
    options = parser.parse_args()
    return Args.from_parsed_args(options)
