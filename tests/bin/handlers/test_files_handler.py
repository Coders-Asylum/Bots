from unittest import TestCase, main
from os import path
from bin.handlers.files_handler import FileHandler


class TestFileHandler(TestCase):
    fileHandler = FileHandler()

    test_content: str = ('Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget \n'
                         'dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, '
                         'nascetur ridiculus mus. Donec \n '
                         'quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis '
                         'enim. Donec pede justo, \n '
                         '    fringilla vel, aliquet nec, vulputate eget, arcu. \n'
                         '\n'
                         'In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede '
                         'mollis pretium. Integer \n '
                         'tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. '
                         'Aenean leo ligula, \n '
                         'porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, '
                         'viverra quis, feugiat a, tellus.')

    test_append_content: str = (
        '\nPhasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. \n'
        'Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas '
        '\n '
        'tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. '
        'Nam \n '
        'quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. '
        'Donec \n '
        'vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus '
        'tincidunt. \n '
        'Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum '
        '\n '
        '    sodales, augue velit cursus nunc,')

    test_file_path: str = '/res/test_text.txt'

    def test_create_file(self):
        print('Testing file creation...')
        self.fileHandler.create_file(self.test_file_path, self.test_content)
        self.assertEqual(path.exists(self.test_file_path), True)

    def test_create_file_integrity(self):
        self.fileHandler.create_file(self.test_file_path, self.test_content)
        self.assertEqual(path.exists(self.test_file_path), True)

        actual_file = open(self.test_file_path, 'r')
        actual_content = actual_file.read()
        actual_file.close()

        self.assertEqual(self.test_content, actual_content)

    def test_update_file(self):
        self.fileHandler.create_file(self.test_file_path, self.test_content)
        self.assertEqual(path.exists(self.test_file_path), True)

        self.fileHandler.update_file(self.test_file_path, self.test_append_content)
        actual_file = open(self.test_file_path, 'r')
        actual_content = actual_file.read()

        self.assertEqual(self.test_content + self.test_append_content, actual_content)

    def test_delete_file(self):
        self.fileHandler.delete_file(self.test_file_path)
        self.assertEqual(path.exists(self.test_file_path), False)


if __name__ == '__main__':
    main()
