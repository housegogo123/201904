import requests
import pandas as pd
def get_info(language):
    url = 'https://api.github.com/search/repositories?q=language:%s&sort=stars'%(language)
    r = requests.get(url)
    if r.status_code == 200:
        print ('success')
        return r.json()
response_python = get_info('python')
def ret_dr(response_dict):
    df = pd.DataFram(columns = ['created_at', 'updated_at', 'name', 'forks', 'stars', 'size'])
    for resp_dict in response_dict['items']:
        df = df.append({
                'created_at': resp_dict['created_at'],
                'updaed_at': resp_dict['updated_at'],
                'name': resp_dict['name'],
                'forks': resp_dict['forks'],
                'stars': resp_dict['starsgazers_count'],
                'size': resp_dict['size']}, ignore_index = True)
    c = df.json()
    return c


