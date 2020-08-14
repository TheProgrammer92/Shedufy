"""Django's command-line utility for administrative tasks."""
import os
import sys
from asgiref.sync import async_to_sync


@async_to_sync
async def sync_function():
    print("bonjour ma func")


sync = async_to_sync(sync_function)


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ict_resources_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
