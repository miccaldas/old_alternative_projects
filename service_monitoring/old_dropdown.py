"""
Here we'll define the dropdown with
all the information options.
"""
from __future__ import unicode_literals

import re
import subprocess
import sys

import click
import isort  # noqa: F401
import questionary
# import snoop
from questionary import Separator, Style

subprocess.run(["isort", __file__])


# @snoop
def dropdown():
    """
    We'll use Questionary's multiple choice
    option, to ask what information he wants.
    It was used variables to identify the
    questions strings, because this allows for
    a value, dependent on a series of 'if'
    statements, to be chosen from them. When
    I did the same without the loop, the
    value was always the last if clause value.
    It was also added the 'path' and 'units'
    values to their respective 'app' and
    'resposta' variables, so that, when running
    'main', all the necessary information is
    already processed.
    """

    custom_style_monitor = Style(
        [
            ("qmark", "fg:#ff5c8d bold"),
            ("question", "fg:#E0DDAA bold"),
            ("answer", "fg:#eeedde"),
            ("pointer", "fg:#BB6464 bold"),
            ("highlighted", "fg:#E5E3C9 bold"),
            ("selected", "fg:#94B49F bold"),
            ("text", "fg:#F1E0AC bold"),
        ]
    )

    q1 = "main - Backups Service"
    q2 = "celery - Yay Service"
    q3 = "man - Python Git_automate"
    q4 = "Home_Git"
    q5 = "Flower"
    q6 = "Pip"

    app = questionary.select(
        "What app do you want to use?",
        qmark="[x]",
        pointer="++",
        use_indicator=True,
        style=custom_style_monitor,
        choices=[q1, q2, q3, q4, q5, q6, "Exit"],
    ).ask()

    questions_lst = [q1, q2, q3, q4, q5, q6]
    for i in questions_lst:
        if app == q1:
            path = "/home/mic/python/backups/backups/celery"
            units = ["backups_beat.service", "backups_celery.service"]
        if app == q2:
            path = "/home/mic/python/cli_apps/cli_apps/yay_querying/celery"
            units = ["yay_beat.service", "yay_worker.service"]
        if app == q3:
            path = "/home/mic/python/git_automate/auto/automate"
            units = ["git_worker.service", "git_beat.service"]
        if app == q4:
            path = "none"
            units = ["home_git_updt.service", "home_git_updt.timer"]
        if app == q5:
            path = "none"
            units = ["flower.service"]
        if app == q6:
            path = "none"
            units = ["pypi_updt.service", "pypi_updt.timer"]

    resposta = questionary.checkbox(
        "What do you want to see?",
        qmark="[X]",
        pointer="++",
        style=custom_style_monitor,
        choices=[
            Separator("----- CELERY INFORMATION -----"),
            "See: Active_Nodes",
            "See: Stats",
            "See: Reports",
            "See: Events",
            "See: Clock",
            "See: Scheduled",
            Separator("----- SYSTEMD INFORMATION -----"),
            "See: Timers",
            "See: Active_Services",
            "See: Service_Status",
            "See: Service_Logs",
            Separator("----- SYSTEMD ACTIONS -----"),
            "See: Stop_Service",
            "See: Edit_Service",
            "See: Start_Service",
            "See: Daemon_Reload",
            "See: Reset_Failed",
            "See: Delete_Service",
            "See: Create_Service",
            Separator("----- EXIT -----"),
            "Exit",
        ],
    ).ask()

    print(click.style(f"\n app: {app}\n resposta: {resposta}\n path: {path}\n units: {units}\n", fg="bright_white", bold=True))
    return app, resposta, path, units


if __name__ == "__main__":
    dropdown()
