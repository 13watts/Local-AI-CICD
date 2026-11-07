import platform
import sys

import django
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "project": "Local AI CI/CD",
        "python_version": platform.python_version(),
        "django_version": django.get_version(),
        "platform": platform.system(),
        "components": [
            ("Django Web Server", "Online"),
            ("SQLite Database", "Configured"),
            ("AI Inference Engine", "Pending"),
            ("Code Analysis Engine", "Pending"),
            ("Automated Repair Engine", "Pending"),
            ("CI/CD Test Runner", "Pending"),
        ],
    }

    return render(
        request,
        "dashboard/index.html",
        context,
    )