import requests
import os
from util.logger import get_logger

logger = get_logger()

class ImageDownloader:
    @staticmethod
    def download(image_url, filename, save_dir="src/output/image"):
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        try:
            response = requests.get(image_url)
            if response.status_code == 200:
                path = os.path.join(save_dir, filename)
                with open(path, 'wb') as file:
                    file.write(response.content)
                return path
            else:
                logger.warning(f"Failed to fetch image: {image_url} - Status: {response.status_code}")
        except Exception as e:
            logger.error(f"[Error] Could not download {image_url}: {e}")

        return None
