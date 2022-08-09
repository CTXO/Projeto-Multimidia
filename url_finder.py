import requests
import re
def find_first_video_id(query):
    query_formated = query.replace(' ', '+')
    search_url = f"https://www.youtube.com/results?search_query={query_formated}"
    search_html = requests.get(search_url).text
    re_search = re.search('"/watch\?v=(.+?)"', search_html)
    video_id = re_search.group(1)
    return video_id
