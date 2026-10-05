import argparse
from dataclasses import dataclass, field


@dataclass
class URL:
    protocol: str
    hostname: str
    path: str
    port: int | None = None


allowed_protocols = ["http"]


def parse_url(url: str) -> URL:
    protocol, _url = url.split("://", maxsplit=1)
    if "://" not in url:
        raise ValueError("Invalid URL: missing protocol")
    if protocol not in allowed_protocols:
        raise ValueError("Protocol Not allowed")
    url_parts = _url.split("/")
    hostname = url_parts[0]
    path = "/".join(url_parts[1:]) if len(url_parts) > 1 else ""
    port = hostname.split(":")[1] if len(hostname.split(":")) > 1 else None
    return URL(protocol, hostname, path, port)


def main():
    parser = argparse.ArgumentParser(description="Mini curl")
    parser.add_argument("--url", required=True)
    arguments = parser.parse_args()

    url: URL = parse_url(arguments.url)
    print(url)


if __name__ == "__main__":
    main()
