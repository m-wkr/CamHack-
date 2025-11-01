import tempfile
import subprocess
import logging
import os
import math
from ds_store import DSStore

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class FinderFile:
    def __init__(
        self,
        title: str,
        position: tuple[int, int],
        is_link: bool = False,
        href: str | None = None,
        tag: str | None = None,
    ):
        self.title: str = title
        self.position: tuple[int, int] = position
        self.is_link: bool = is_link
        self.href: str | None = href
        self.tag: str | None = tag


def finder_render(site_name="Test Site"):
    with tempfile.TemporaryDirectory() as tmpdirname:
        logger.info("Created temporary directory %s", tmpdirname)
        os.mkdir(os.path.join(tmpdirname, site_name))

        # Create 100 sample files
        for i in range(100):
            file_path = os.path.join(tmpdirname, site_name, f"file_{i}.txt")
            with open(file_path, "w") as f:
                f.write("\n")
        logger.info("Created 100 sample files in %s", tmpdirname)

        with DSStore.open(os.path.join(tmpdirname, site_name, ".DS_Store"), "w+") as d:
            for i in range(100):
                filename = f"file_{i}.txt"
                angle = (i / 100) * 2 * math.pi
                radius = 200
                x = int(300 + radius * math.cos(angle))
                y = int(300 + radius * math.sin(angle))
                d[filename]["Iloc"] = (x, y)
            logger.info("Set icon positions in .DS_Store")

        with DSStore.open(os.path.join(tmpdirname, ".DS_Store"), "w+") as d:
            d[site_name]["icvp"] = {
                "backgroundColorBlue": 1.0,
                "gridSpacing": 54.0,
                "textSize": 12.0,
                "backgroundColorRed": 1.0,
                "backgroundType": 0,
                "backgroundColorGreen": 1.0,
                "gridOffsetX": 0.0,
                "gridOffsetY": 0.0,
                "scrollPositionY": 0.0,
                "showItemInfo": False,
                "viewOptionsVersion": 1,
                "scrollPositionX": 0,
                "arrangeBy": "none",
                "labelOnBottom": True,
                "iconSize": 16.0,
                "showIconPreview": False,
            }

        # Open the temporary directory in Finder
        subprocess.run(["open", os.path.join(tmpdirname, site_name)])
        logger.info("Opened Finder at %s", os.path.join(tmpdirname, site_name))

        # Blocking call to keep the temp directory alive for inspection
        input("Press Enter to continue...")
