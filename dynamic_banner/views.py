from django.shortcuts import render
from django.views.generic import View
import requests
import os
from datetime import datetime

# Create your views here.
class TextRenderer(View):
    def get(self, request, *args, **kwargs):
        WAKA_KEY = os.environ.get("WAKATIME_API_KEY")

        wakatime_stats = requests.get(f"https://wakatime.com/api/v1/users/current/projects?api_key={WAKA_KEY}").json() 
        wakatime_all_time_stats = requests.get(f"https://wakatime.com/api/v1/users/current/all_time_since_today?api_key={WAKA_KEY}").json()

        context = {
            "proj_name" : wakatime_stats["data"][0]["name"],
            "last_commit": wakatime_stats["data"][0]["human_readable_last_heartbeat_at"],
            "all_time_coding": wakatime_all_time_stats["data"]["text"]
        }

        return render(request, "home.html", context, content_type="image/svg+xml")
