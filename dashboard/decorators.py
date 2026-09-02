from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test


def agent_required(view_func):
    return user_passes_test(
        lambda u: u.is_authenticated and (
            u.is_superuser or u.groups.filter(name="Agent").exists()
        ),
        login_url="/"
    )(view_func)