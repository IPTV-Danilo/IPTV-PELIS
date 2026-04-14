def add_item(f, title, url, logo, group, desc):
    f.write(f'#EXTINF:-1 group-title="{group}" tvg-logo="{logo}",{title}\n')
    f.write(url + "\n")


def create_m3u(items, output="output/playlist.m3u"):
    with open(output, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n\n")

        for i in items:
            add_item(
                f,
                i["title"],
                i["url"],
                i["logo"],
                i["group"],
                i.get("desc", "")
            )
