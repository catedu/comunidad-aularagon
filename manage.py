#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if os.environ.get("DEBUG") is None or eval(os.environ.get("DEBUG")):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_conf.settings.dev")
    elif not eval(os.environ.get("DEBUG")):
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "project_conf.settings.production"
        )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
