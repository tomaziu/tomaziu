"""Generate the light and dark SVGs used by the profile README."""

import html
import json
import os
import urllib.request
from datetime import datetime, timezone

USER = "tomaziu"
JOINED_YEAR = 2024
W = 60

ART = r"""
       :  ..     ..-.-..:--::-::- .
      :   -:     .-:-:..-::-..-:   :
     :   .--.    .--:..-.:.-...:    :
    .    :--:    .:...:::..-...      :
    :   -::--.   .: ....: :.:..      .
   :   :--:--:    : .=:: -*=          :
   :  .----:--:   :  *+.:#+%.         .
  .    ----::--     .-:.%#=*=          :
  :    .----::     :*:%%%%*%%+         :
  .   ..-----: .   :%-%%%%%*%+         .
  .  .=:.:::-..-   :%:+%%%%+%=          .
 .  :--- :-:: --   .#*=%%%#%%:          .
 .  --:::.--..--.  -%%*+%%#+#           .
 . .-::::.:- :--:  -%#%=%%%%+           .
 .  ::--::...----  =%##.:#=:   ..       .
 .  ------. :--..+#=#%:     *% #% =*    .
 .  ------::-:.=%%%*--      %%:+#:%%+   .
 .. ----::---.*#*+*##=+    :*+.:=-%%-   .
  . ---::::--.++#%%%%%*#  *%+ **=++= . .
  : :-::--::-::%+%%%%%#=+%%%+:##****-%+.
  . :------:--.#%+%%%%%=%%%%+-#####*+%*.
   ::---------.=%#+%%#+-%%%%*:*#####+%=
   ::---------::%%#++*%=*%%%*:+**###:=:
    ::-:-------.*%%%%%%--%%%*.+*+=**
    -:-:---::--::**##%%  %%%+.+##*+: :
    :-.::-::----.     .  --  =-=**-.:
    .=-::::-----                   :
      --:------:                  ..
"""

TOKEN = os.environ.get("GITHUB_TOKEN", "")


def github(url, payload=None):
    headers = {"Accept": "application/vnd.github+json"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode() if payload else None,
        headers=headers,
    )
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read() or "{}")


def graphql(query, variables=None):
    response = github(
        "https://api.github.com/graphql",
        {"query": query, "variables": variables or {}},
    )
    if response.get("errors"):
        raise RuntimeError(response["errors"])
    return response["data"]


def fetch_stats():
    current_year = datetime.now(timezone.utc).year
    yearly_contributions = "\n".join(
        f'y{year}: contributionsCollection(from: "{year}-01-01T00:00:00Z", '
        f'to: "{year + 1}-01-01T00:00:00Z") '
        "{ totalCommitContributions restrictedContributionsCount }"
        for year in range(JOINED_YEAR, current_year + 1)
    )
    user = graphql(
        f"""
        query {{
          user(login: "{USER}") {{
            followers {{ totalCount }}
            repositories(first: 100, ownerAffiliations: OWNER) {{
              totalCount
              nodes {{ stargazerCount }}
            }}
            repositoriesContributedTo(
              first: 1,
              contributionTypes: [COMMIT, PULL_REQUEST, REPOSITORY]
            ) {{ totalCount }}
            {yearly_contributions}
          }}
        }}
        """
    )["user"]

    contributions = [user[f"y{year}"] for year in range(JOINED_YEAR, current_year + 1)]
    return {
        "repos": user["repositories"]["totalCount"],
        "contributed": user["repositoriesContributedTo"]["totalCount"],
        "stars": sum(repo["stargazerCount"] for repo in user["repositories"]["nodes"]),
        "commits": sum(
            item["totalCommitContributions"] + item["restrictedContributionsCount"]
            for item in contributions
        ),
        "followers": user["followers"]["totalCount"],
    }


PALETTES = {
    "dark": {
        "bg": "#0d1117",
        "border": "#30363d",
        "art": "#8b949e",
        "heading": "#58a6ff",
        "key": "#ffa657",
        "value": "#c9d1d9",
        "dim": "#484f58",
    },
    "light": {
        "bg": "#ffffff",
        "border": "#d0d7de",
        "art": "#57606a",
        "heading": "#0969da",
        "key": "#953800",
        "value": "#24292f",
        "dim": "#afb8c1",
    },
}


def key_value(key, value, width=W):
    dots = "." * max(width - len(key) - len(str(value)) - 3, 1)
    return [(f"{key}: ", "key"), (dots + " ", "dim"), (str(value), "value")]


def two_values(first_key, first_value, second_key, second_value):
    return (
        key_value(first_key, first_value, 33)
        + [(" | ", "dim")]
        + key_value(second_key, second_value, 24)
    )


def rule(title):
    label = f"- {title} "
    return [(label, "heading"), ("-" * (W - len(label)), "dim")]


def info_lines(stats):
    number = lambda value: f"{value:,}"
    return [
        [(f"{USER}@github ", "heading"), ("-" * (W - len(USER) - 8), "dim")],
        [],
        key_value("OS", "Windows"),
        key_value("Status", "Information Systems Student"),
        key_value("School", "UNIGRANDE"),
        key_value("Focus", "APIs, automation and web"),
        key_value("Tools", "Git, GitHub, VS Code, Render"),
        [],
        key_value("Languages.Programming", "Python, JavaScript, HTML, CSS"),
        key_value("Frameworks", "FastAPI, Node.js"),
        key_value("Current.project", "Reecorta AI"),
        [],
        rule("Contact"),
        key_value("GitHub", "github.com/tomaziu"),
        key_value("Email", "tomaziu@gmail.com"),
        [],
        rule("GitHub Stats"),
        two_values(
            "Repos",
            f"{stats['repos']} {{Contributed: {stats['contributed']}}}",
            "Stars",
            number(stats["stars"]),
        ),
        two_values("Commits", number(stats["commits"]), "Followers", number(stats["followers"])),
    ]


def render(mode, stats):
    palette = PALETTES[mode]
    output = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="900" height="500" '
        'viewBox="0 0 900 500" font-family="Consolas, Menlo, monospace" font-size="13px">',
        f'<rect x="0.5" y="0.5" width="899" height="499" rx="10" '
        f'fill="{palette["bg"]}" stroke="{palette["border"]}"/>',
    ]
    for index, line in enumerate(ART.strip("\n").split("\n")):
        output.append(
            f'<text x="20" y="{40 + index * 15}" fill="{palette["art"]}" '
            f'xml:space="preserve">{html.escape(line)}</text>'
        )
    for index, segments in enumerate(info_lines(stats)):
        if not segments:
            continue
        spans = "".join(
            f'<tspan fill="{palette[color]}">{html.escape(text)}</tspan>'
            for text, color in segments
        )
        output.append(
            f'<text x="370" y="{45 + index * 23}" xml:space="preserve">{spans}</text>'
        )
    output.append("</svg>")
    return "\n".join(output)


def write_profiles(stats):
    for mode in PALETTES:
        with open(f"{mode}_mode.svg", "w", encoding="utf-8") as profile:
            profile.write(render(mode, stats))


if __name__ == "__main__":
    if not TOKEN:
        raise RuntimeError("GITHUB_TOKEN is required to refresh profile statistics")
    profile_stats = fetch_stats()
    print("stats:", profile_stats)
    write_profiles(profile_stats)
    print("wrote dark_mode.svg and light_mode.svg")
