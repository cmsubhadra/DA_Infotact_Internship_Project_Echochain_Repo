import csv
import scrapy
from pathlib import Path


class MarketplaceSpider(scrapy.Spider):
    name = "marketplace"

    async def start(self):
        # Project structure:
        #
        # Echochain_Repo/
        # ├── data/
        # │   └── marketplace_listings.csv
        # └── scrapy_project/
        #     └── echochain_scraper/
        #         └── spiders/
        #             └── marketplace_spider.py

        project_root = Path(__file__).resolve().parents[3]

        csv_file = project_root / "data" / "marketplace_listings.csv"

        self.logger.info("=" * 60)
        self.logger.info(f"PROJECT ROOT: {project_root}")
        self.logger.info(f"CSV FILE: {csv_file}")
        self.logger.info(f"CSV EXISTS: {csv_file.exists()}")
        self.logger.info("=" * 60)

        if not csv_file.exists():
            self.logger.error(f"CSV FILE NOT FOUND: {csv_file}")
            return

        with open(
            csv_file,
            mode="r",
            encoding="utf-8-sig",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            count = 0

            for row in reader:
                count += 1

                self.logger.info(
                    f"Reading listing {count}: {row.get('listing_id')}"
                )

                yield row

            self.logger.info(f"TOTAL RECORDS READ: {count}")