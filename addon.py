from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://www.whatbitcoindid.com/podcast?format=rss"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://images.squarespace-cdn.com/content/59641a28ff7c5099c12a5eda/1612857082758-RE54NSHW3MSCO3JKF8MH/What+Bitcoin+Did-Podcast-Avatar+2021+%282%29.png"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://images.squarespace-cdn.com/content/59641a28ff7c5099c12a5eda/1612857082758-RE54NSHW3MSCO3JKF8MH/What+Bitcoin+Did-Podcast-Avatar+2021+%282%29.png"},
    ]
    return items
@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items
@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items
if __name__ == '__main__':
    plugin.run()
