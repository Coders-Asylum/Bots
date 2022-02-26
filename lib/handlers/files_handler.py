from os import path, remove, makedirs


class FileHandler:
    @staticmethod
    def create_file(file_path: str, contents: str):
        """
        Creates a file and writes to it
        Use this if you want to update the file if it has changes in between
        :param file_path: File path where the file needs to be created or exits with file name and extension
        :param contents: content that is to populated/written in the file
        :return: None
        """
        makedirs(path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as _file:
            _file.write(contents)

    @staticmethod
    def update_file(file_path: str, contents: str):
        """
        Updates the file by adding from last line of the file
        :param file_path: File path where the file needs to be created or exits with file name and extension
        :param contents: content that is to populated/appended from the end of the file file
        :return: None
        """
        makedirs(path.dirname(file_path), exist_ok=True)
        with open(file_path, 'a') as _file:
            _file.write(contents)

    @staticmethod
    def delete_file(file_path: str):
        """
        Deletes the file in the specified path
        :param file_path: File path where the file needs to be created or exits with file name and extension
        :return: None
        """

        if path.exists(file_path):
            remove(file_path)
