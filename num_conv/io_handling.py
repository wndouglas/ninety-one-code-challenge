"""Module containing the IO handling functionality."""

from abc import ABC, abstractmethod

import logging

logger = logging.getLogger(__name__)


class InputStreamer(ABC):
    """
    Interface for an input streamer class.

    Subclasses may be a text file streamer, or a standard input streamer,
    etc.

    Each subclass should be responsible for the creation and teardown of any resources
    it uses - hence should implement the __del__() method and close any resources in there.
    """

    def __init__(self, file_location):
        """
        Parameters
        ----------
        file_location : string
            String containing the location of the text file to open.
        """
        self.file_location = file_location

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


class TxtFileInputStreamer(InputStreamer):
    """
    Class implementing the InputStreamer interface for the case of .txt files.

    Attributes
    ----------
    file_location : string
        File containing the lines to stream from.

    Methods
    -------
    get_line()
        Returns the next line from the open text file. If the file contains no more lines,
        returns an empty string.
    """

    def __init__(self, file_location):
        super().__init__(file_location)

        try:
            self._txt_file = open(file_location, 'r', encoding='utf-8-sig')
        except FileNotFoundError:
            logging.error("incorrect file path", exc_info=True)
            raise

        logging.info("Txt input streamer opened file at location: {}.".format(file_location))

    def __del__(self):
        self._txt_file.close()
        logging.info("Txt input streamer closed file at location: {}.".format(self.file_location))

    def get_line(self):
        """
        Returns the next line from the open text file. If the file contains no more lines,
        returns an empty string.

        Returns
        ------
        string
            Contains the next line from the open file.
        """
        return self._txt_file.readline()


class OutputStreamer(ABC):
    """
    Interface for an output streamer class.

    Subclasses may be a text file streamer, or a standard input streamer, etc.

    Each subclass should be responsible for the creation and teardown of any resources
    it uses - hence should implement the __del__() method and close any resources in there.
    """

    def __init__(self, file_location=None):
        """
        Parameters
        ----------
        file_location : string
            String containing the location of the text file to open.
        """
        self.file_location = file_location

    @abstractmethod
    def set_line(self, line):
        raise NotImplementedError(
            "Should implement get_line()"
        )

    @abstractmethod
    def __del__(self):
        raise NotImplementedError(
            "Should implement __del__()"
        )


class TxtFileOutputStreamer(OutputStreamer):
    """
    Class implementing the OutputStreamer interface for the case of .txt files.

    Attributes
    ----------
    file_location : string
        File containing the lines to stream into.

    Methods
    -------
    set_line(line)
        Streams the line given into the opened text file.
    """

    def __init__(self, file_location):
        super().__init__(file_location)
        self._txt_file = open(file_location, 'w')
        logging.info("Txt output streamer opened file at location: {}.".format(file_location))

    def __del__(self):
        self._txt_file.close()
        logging.info("Txt output streamer closed file at location: {}.".format(self.file_location))

    def set_line(self, line):
        """
        Outputs the given line to the text file and adds a newline character.

        Parameters
        ------
        line : string
            Contains the next line to be streamed into the open file.
        """
        self._txt_file.write(line + "\n")


class StdOutputStreamer(OutputStreamer):
    """
    Class implementing the OutputStreamer interface for the case of outputting to STDOUT files.

    Methods
    -------
    set_line(line)
        Streams the line given into the opened text file.
    """

    def __init__(self):
        super().__init__()
        logging.info("STDOUT streamer initialised.")

    def __del__(self):
        logging.info("STDOUT streamer closed.")

    def set_line(self, line):
        """
        Outputs the given line to STDOUT and adds a newline character.

        Parameters
        ------
        line : string
            Contains the next line to be streamed into the open file.
        """
        print(line)


def output_streamer_factory(file_location):
    """Responsible for creating the correct type output streamer.

    Parameter
    ---------
    file_location : string
        Location of the specified output file.

    Returns
    -------
    OutputStreamer
        Returns an output streamer object.
    """
    if file_location is None:
        return StdOutputStreamer()
    else:
        return TxtFileOutputStreamer(file_location)
