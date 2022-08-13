import platform
import subprocess


def clear_screen():
    """
    Clear the screen.
    """
    if platform.system().lower() == 'windows':
        subprocess.check_call('cls', shell=True)
    else:
        print(subprocess.check_output('clear').decode())
