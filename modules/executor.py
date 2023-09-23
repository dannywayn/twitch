"""
This module helps to run commands.
"""
import subprocess
import requests


class CMD:
    """Runs cmd commands and retrieves the output."""

    @staticmethod
    def call(command: str):
        """
        Runs cmd command and retrieves the output
        :param command: the command to run.
        :return: String of the output from the command.
        """
        args = command.split(' ')
        process = subprocess.run(args=args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        process_stdout = process.stdout.decode('utf-8').strip()
        process_stderr = process.stderr.decode('utf-8').strip()
        return process.returncode, process_stdout, process_stderr
