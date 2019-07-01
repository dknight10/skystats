class UploadException(Exception):
    """
    Base upload exception.
    """


class ConfigurationException(UploadException):
    """
    The configuration was incorrect.
    """


class InvalidFileException(UploadException):
    """
    The uploaded file was incorrect.
    """


class ParsingException(UploadException):
    """
    The contents of the file were incorrect.
    """
