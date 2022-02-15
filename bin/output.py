import subprocess
from time import sleep


class Output:
    _completed_steps: int
    _close: bool
    _total_steps: int

    def __init__(self, total_steps=50):
        self._close = False
        self._completed_steps = 0
        self._total_steps = total_steps

    def progress_output(self):
        _length: int = 50

        complete: int = int((self._completed_steps / self._total_steps) * _length)
        progress_anim: str = '['
        for i in range(1, _length):
            if i <= complete:
                progress_anim += '█'
            else:
                progress_anim += '-'

        progress_anim += '] {}% completed'.format(round((self._completed_steps / self._total_steps) * 100, 2))
        print(progress_anim)

    def set_progress(self, steps_completed):
        self._completed_steps = steps_completed
        self.progress_output()

    def end(self):
        self._close = True


if __name__ == '__main__':
    out = Output(75)

    out.progress_output()
    sleep(2)
    out.set_progress(5)
    sleep(1)
    out.set_progress(30)
    sleep(1)
    out.set_progress(62)
    sleep(1)
    out.set_progress(75)
    sleep(1)
