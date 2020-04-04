import json
import re
import urllib.request

from pytube import YouTube


class Helper:
    def __init__(self):
        pass

    def title_to_underscore_title(self, title: str):
        title = re.sub('[\W_]+', "_", title)
        return title.lower()

    def id_from_url(self, url: str):
        return url.rsplit("/", 1)[1]


class IronMan:
    def __init__(self, url: str):
        self.json_url = urllib.request.urlopen(url)
        self.data = json.loads(self.json_url.read())

    def print_data(self):
        print(self.data)

    def get_video_title(self):
        return self.data["items"][0]["snippet"]['title']

    def get_video_description(self):
        return self.data["items"][0]["snippet"]['description']


api_key = "AIzaSyD0hcmDA50YzY038LJ9Q-O_Tkpi4rKuLTI"
# VIDEO ID 從哪看 就是 網址v=的後面
# video_id = "6u8fCbufYUw"
link = "Youtube_links.csv"


with open(link, "r")as f:
    content = f.readlines()
content = list(map(lambda s: s.strip(), content))
content = list(map(lambda s: s.strip(','), content))
# regular expression  url
helper = Helper()

for youtube_url in content:
    video_id = helper.id_from_url(youtube_url)
    # print(video_id)
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
    iron30 = IronMan(url)
    title = iron30.get_video_title()
    title = helper.title_to_underscore_title(title)
    description = iron30.get_video_description()
    iron30.print_data()
    # print(title)
    # print(description)
