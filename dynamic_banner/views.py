from django.shortcuts import render
from django.views.generic import View
import requests
import os
from datetime import datetime

# Create your views here.
class TextRenderer(View):
    def get(self, request, *args, **kwargs):
        WAKA_KEY = os.environ.get("WAKATIME_API_KEY")

        wakatime_stats = requests.get(
            f"https://wakatime.com/api/v1/users/current/projects?api_key={WAKA_KEY}"
        ).json()
        wakatime_all_time_stats = requests.get(
            f"https://wakatime.com/api/v1/users/current/all_time_since_today?api_key={WAKA_KEY}"
        ).json()

        base64Icon1 = "data:image/jpeg;base64,PHN2ZyB3aWR0aD0iMTUiIGhlaWdodD0iMTMiIHZpZXdCb3g9IjAgMCAxNSAxMyIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTAgMFY0LjYxNTM4SDMuMjUwODNMNS4xOTIzMSA4LjAyMzk2VjEyLjExNTRIOS44MDc2OVY3LjVINi4yMjEwOEw0LjU3OTMzIDQuNjE1MzhINC42MTUzOFYyLjg4NDYxSDEwLjM4NDZWNC42MTUzOEgxNVYwSDEwLjM4NDZWMS43MzA3N0g0LjYxNTM4VjBIMFpNMS4xNTM4NSAxLjE1Mzg1SDMuNDYxNTRWMy40NjE1NEgxLjE1Mzg1VjEuMTUzODVaTTExLjUzODUgMS4xNTM4NUgxMy44NDYyVjMuNDYxNTRIMTEuNTM4NVYxLjE1Mzg1Wk02LjU4NzI5IDguNjUzODRIOC42NTM4NVYxMC45NjE1SDYuMzQ2MTVWOC43OTEzMkw2LjU4NzI5IDguNjUzODRaIiBmaWxsPSJ1cmwoI3BhaW50MF9saW5lYXJfMV81OCkiLz4KPGRlZnM+CjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQwX2xpbmVhcl8xXzU4IiB4MT0iNy41IiB5MT0iMC4xNjExMzUiIHgyPSI3LjUiIHkyPSIxMi4wOTIyIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+CjxzdG9wIHN0b3AtY29sb3I9IiNFQjU5NUIiLz4KPHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjRTQxQjM5Ii8+CjwvbGluZWFyR3JhZGllbnQ+CjwvZGVmcz4KPC9zdmc+Cg=="

        context = {
            "proj_name": wakatime_stats["data"][0]["name"],
            "last_commit": wakatime_stats["data"][0][
                "human_readable_last_heartbeat_at"
            ],
            "all_time_coding": wakatime_all_time_stats["data"]["text"],
            "icon_1": base64Icon1,
        }

        return render(request, "home.html", context, content_type="image/svg+xml")
