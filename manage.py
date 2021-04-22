#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    environment = (
        "dev" if os.environ.get("SETTINGS_SELECTION") in ["dev", None] else "production"
    )

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", f"project_conf.settings.{environment}"
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
