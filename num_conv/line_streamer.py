"""Module containing the classes defining the interface for and implementation of a line streamer."""

from abc import ABC, abstractmethod

import logging

logger = logging.getLogger(__name__)


class LineStreamer(ABC):
    """
    Interface for a line streamer class.

    Subclasses should may be a text file parser, or a standard input parser,
    etc.

    Each subclass should be responsible for the creation and teardown of any resources
    it uses - hence should implement the __del__() method and close any resources in there.
    """

    @abstractmethod
    def get_line(self):
        raise NotImplementedError(
            "Should implement get_line()"
        )

    @abstractmethod
    def __del__(self):
        raise NotImplementedError(
            "Should implement __del__()"
        )


class TxtFileLineStreamer(LineStreamer):
    """
    Class implementing the LineStreamer interface for the case of .txt files.

    Attributes
    ----------
    txt_file : file
        File containing the lines to stream from.


    Methods
    -------
    get_line()
        Returns the next line from the open text file. If the file contains no more lines,
        returns an empty string.
    """

    def __init__(self, file_location):
        """
        Parameters
        ----------
        file_location : string
            String containing the location of the text file to open.
        """
        self.txt_file = open(file_location, 'r')
        logging.info("Txt line streamer opened file at location: {}.".format(file_location))

    def __del__(self):
        self.txt_file.close()
        logging.info("Txt line streamer closed file.")

    def get_line(self):
        """
        Returns the next line from the open text file. If the file contains no more lines,
        returns an empty string.

        Returns
        ------
        string
            Contains the next line from the open file.
        """
        return self.txt_file.readline()
