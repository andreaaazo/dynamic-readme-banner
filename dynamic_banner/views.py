import requests
import os

from django.shortcuts import render
from django.views.generic import View
from django.utils.safestring import mark_safe

from dynamic_banner_proj.settings import BASE_DIR

from datetime import datetime


# Create your views here.
class TextRenderer(View):
    def get(self, request, *args, **kwargs):
        WAKA_KEY = os.environ.get("WAKATIME_API_KEY")

        # Get data in ISO 8601
        last_commit_day = datetime.fromisoformat(
            str(
                requests.get(
                    f"https://wakatime.com/api/v1/users/current/projects?api_key={WAKA_KEY}"
                ).json()["data"][0]["last_heartbeat_at"]
            ).replace("Z", "+00:00")
        ).strftime("%-d %b")

        # Get all time coding
        all_time_coding = round(
            float(
                requests.get(
                    f"https://wakatime.com/api/v1/users/current/all_time_since_today?api_key={WAKA_KEY}"
                ).json()["data"]["decimal"]
            )
        )

        # Get all fonts in base64
        with open(
            f"{BASE_DIR}/fonts/Sk-Modernist/regular.txt", "r"
        ) as sk_modernist_regular, open(
            f"{BASE_DIR}/fonts/Helvetica Neue/light.txt", "r"
        ) as helvetica_neue_light:
            fonts = {
                "helvetica_neue": {
                    "light": helvetica_neue_light.read(),
                },
                "sk_modernist": {
                    "regular": sk_modernist_regular.read(),
                },
            }
            helvetica_neue_light.close()
            sk_modernist_regular.close()

        # Get all images in base64
        with open(f"{BASE_DIR}/images/background.svg", "r") as background_svg, open(
            f"{BASE_DIR}/images/lettermark.svg", "r"
        ) as lettermark_svg, open(f"{BASE_DIR}/images/logo.svg", "r") as logo_svg:
            images = {
                "background": mark_safe(background_svg.read()),
                "lettermark": mark_safe(lettermark_svg.read()),
                "logo": mark_safe(logo_svg.read()),
            }
            background_svg.close()
            lettermark_svg.close()
            logo_svg.close()

        context = {
            "last_commit_day": last_commit_day,
            "all_time_coding": all_time_coding,
            "images": images,
            "fonts": fonts,
        }

        return render(request, "home.html", context, content_type="image/svg+xml")
