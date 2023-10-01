"""
This module helps to run commands.
"""
import subprocess
import re
import traceback
from modules.base_module import BaseClass


class CMD:
    """Runs cmd commands and retrieves the output."""

    @staticmethod
    def split_arguments(input_string):
        pattern = r'(\'[^\']*\'|"[^"]*"|\S+)'
        arguments = re.findall(pattern, input_string)
        arguments = [arg.strip('\'"') for arg in arguments]
        return arguments

    @staticmethod
    def call(command: str):
        """
        Runs cmd command and retrieves the output
        :param command: the command to run.
        :return: String of the output from the command.
        """
        try:
            args = CMD.split_arguments(command)
            process = subprocess.run(args=args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, timeout=80)
            process_stdout = process.stdout.decode().strip()
            process_stderr = process.stderr.decode().strip()
            return process.returncode, process_stdout, process_stderr
        except:
            BaseClass.write_log(traceback.format_exc())
