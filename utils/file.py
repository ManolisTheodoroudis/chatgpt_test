import os
from config.config import CONF


class File_Utils():

    def get_filepath(expected, filename):
        root_dir = os.path.abspath(os.curdir)
        file_path = os.path.join(root_dir, "data", "files", filename)

        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        CONF.logger.info(f"File path to upload: '{file_path}'")

        return file_path