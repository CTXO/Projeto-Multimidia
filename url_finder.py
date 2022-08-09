import requests
def find_first_result(query):
    query_formated = query.replace(' ', '+')
    search_url = f"https://www.youtube.com/results?search_query={query_formated}"
    search_html = requests.get(search_url).text
    start_of_string = '"/watch?v='
    initial_index_of_first_video = search_html.index(start_of_string)
    final_index_of_first_video = search_html.index('"', initial_index_of_first_video + len(start_of_string))
    video_url = search_html[initial_index_of_first_video + 1:final_index_of_first_video]
    return video_url[1:]