
import subprocess


def diff(file1, file2):
    """
    """
    # TODO: piping to cat so it won't return error code thus exception... need a better way
    diffs = [line for line in subprocess.check_output("diff {} {} | cat".format(file1, file2), shell=True).split('\n')
             if line and not any(line.startswith(c) for c in ['>', '<', '-'])]

    return diffs



