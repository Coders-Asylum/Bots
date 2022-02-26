from unittest import TestCase, main
from io import StringIO
from unittest.mock import patch

from lib import Output


class unittests(TestCase):
    out = Output(75)

    __step_1: str = '[-------------------------------------------------] 0.0% completed\n'
    __step_2: str = '[███----------------------------------------------] 6.67% completed\n'
    __step_3: str = '[████████████████████-----------------------------] 40.0% completed\n'
    __step_4: str = '[█████████████████████████████████████████--------] 82.67% completed\n'
    __step_5: str = '[█████████████████████████████████████████████████] 100.0% completed\n'

    def test_output(self):
        with patch('sys.stdout', new=StringIO()) as actual_output:
            self.out.progress_output()
            self.assertEqual(self.__step_1, actual_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as actual_output:
            self.out.set_progress(5)
            self.assertEqual(self.__step_2, actual_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as actual_output:
            self.out.set_progress(30)
            self.assertEqual(self.__step_3, actual_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as actual_output:
            self.out.set_progress(62)
            self.assertEqual(self.__step_4, actual_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as actual_output:
            self.out.set_progress(75)
            self.assertEqual(self.__step_5, actual_output.getvalue())


if __name__ == '__main__':
    main()
