#!/usr/bin/env python3
"""
NetGuard Key Generator
"""
import argparse
import hashlib
from typing import List


def generate_keys(challenge_code: str) -> List[str]:
    """
    Generates possible keys for the given challenge code.
    
    Args:
        challenge_code: The input challenge code string.
        
    Returns:
        A list of possible MD5 hash keys.
    """
    keys = []
    for suffix in ("NetGuard3", "NetGuard2"):
        payload = f"{challenge_code}{suffix}".encode("utf-8")
        keys.append(hashlib.md5(payload).hexdigest())
    return keys


def main() -> None:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Generate possible keys from a NetGuard challenge code."
    )
    parser.add_argument(
        "challenge_code",
        help="The challenge code (e.g., 784019874562340ghjsfdk)"
    )
    
    args = parser.parse_args()
    
    print("Possible keys:")
    for key in generate_keys(args.challenge_code):
        print(key)


if __name__ == "__main__":
    main()
