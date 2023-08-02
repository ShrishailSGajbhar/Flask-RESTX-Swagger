import logging
from datetime import datetime
from pathlib import Path
from typing import Optional
import os

logger_base = Path(__file__).parent

class RootLoggerManager:

    """Class for logging the machine learning application"""

    # A sample of logging.Formatter(s) that can be used by handlers
    MINIMAL_FORMATTER = logging.Formatter(
            "[%(levelname)s] %(message)s",
            datefmt = "%d-%m-%Y %H:%M:%S"
            )
    BASIC_FORMATTER = logging.Formatter(
            "[%(asctime)s] %(levelname)s -- : %(message)s",
            datefmt = "%d-%m-%Y %H:%M:%S"
            )
    VERBOSE_FORMATTER = logging.Formatter(
            "[%(asctime)s] (module = %(module)s func = %(funcName)s) %(levelname)s -- : %(message)s",
            datefmt = "%d-%m-%Y %H:%M:%S"
            )

    def __init__(self):
        # logging.getLogger() returns a reference to a logger instance with the specified name if specified else root.

        self.logger = logging.getLogger()

        self.logger.setLevel(logging.INFO)
        
        # Remove handlers because other libraries may already have their own handlers (e.g., Streamlit, requests). 
        # If we do not remove the handers then it would be a mess as our output will be a mixed one not as per the desire.
        self.logger.handlers = []

    def configure(self, output_path: Optional[Path] = None):
        """TODO: Configure the root logger's handlers and their verbosity

        :output_path (Optional): The output path used by "FileHandler". 
        :returns: TODO

        """
        # setup the console login
        self.set_console_logging(self.BASIC_FORMATTER)

        # If the output log path is provided then initiate the file logging
        if output_path:
            self.set_file_logging(path=output_path, formatter=self.VERBOSE_FORMATTER)
    
    def set_console_logging(self, formatter: logging.Formatter):
        """Add a `StreamHandler` handler to the root logger (for console logging)

        :formatter: The logging formatter that will be used.
        :returns: TODO

        """
        handler = logging.StreamHandler()

        # set logging format
        handler.setFormatter(formatter)
        handler.setLevel(logging.INFO)

        # add handler to logger
        self.logger.addHandler(handler)

    def set_file_logging(self, path: Path, formatter: logging.Formatter):
        """Add a FileHandler to the logger (for file logging)self.

        :path: TODO
        :formatter: TODO
        :returns: TODO

        """
        filename = os.path.join(path,f"{datetime.now().strftime('%d%m%Y-%H%M%S')}.log")
        filename = Path(filename)
        # If parent folders do not exist than create them
        try:
            filename.parent.mkdir(parents=True, exist_ok=True)
            handler = logging.FileHandler(filename, "w")
            # Make sure that the file now exists
            assert filename.exists()
        except Exception as e:
            logging.critical(
                    f"Unable to create the file in order to store the output logs: {e}."
                    )

        # set logging format
        handler.setFormatter(formatter)
        handler.setLevel(logging.INFO)
        
        # Add handler to the logger
        self.logger.addHandler(handler)


logger_manager = RootLoggerManager()
logger_manager.configure(output_path=Path('./logs'))
logger = logger_manager.logger