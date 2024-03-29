import IndicatorTypes

from utils import *
from api import *


def scrape_file(hash, type):
    details = scrape_details(type, hash, "general")
    return [hash, details["base_indicator"]["id"], details["pulse_info"]["count"]], None


if __name__ == '__main__':
    load_scrape_save("datasets/group/FileHash-MD5.csv", "datasets/parsed/FileHash-MD5_parsed.csv",
                     lambda h: scrape_file(h, IndicatorTypes.FILE_HASH_MD5),
                     start=0,
                     count=300,
                     batch_size=50)

    load_scrape_save("datasets/group/FileHash-SHA1.csv", "datasets/parsed/FileHash-SHA1_parsed.csv",
                     lambda h: scrape_file(h, IndicatorTypes.FILE_HASH_SHA1),
                     start=0,
                     count=300,
                     batch_size=50)

    load_scrape_save("datasets/group/FileHash-SHA256.csv", "datasets/parsed/FileHash-SHA256_parsed.csv",
                     lambda h: scrape_file(h, IndicatorTypes.FILE_HASH_SHA256),
                     start=0,
                     count=300,
                     batch_size=50)
