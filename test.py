from getyoutubeid import get_youtube_id

tests = [
    {'id': '-wtIMTCHWuI', 'url': 'https://www.youtube.com/watch?v=-wtIMTCHWuI'},
    {'id': '-wtIMTCHWuI', 'url': 'http://www.youtube.com/v/-wtIMTCHWuI?version=3&autohide=1'},
    {'id': '-wtIMTCHWuI', 'url': 'http://youtu.be/-wtIMTCHWuI'},
    {'id': 'zc0s358b3Ys', 'url': 'http://www.youtube.com/embed/zc0s358b3Ys'},
    {'id': '-wtIMTCHWuI', 'url': ' http://www.youtube.com/watch?v=-wtIMTCHWuI '},
    {'id': 'zc0s358b3Ys', 'url': 'trytofindhttp://youtu.be/zc0s358b3Ys ME'},
    {'id': 'u8nQa1cJyX8', 'url': 'http://www.youtube.com/watch?v=u8nQa1cJyX8&a=GxdCwVVULXctT2lYDEPllDR0LRTutYfW'},
    {'id': 'u8nQa1cJyX8', 'url': 'http://www.youtube.com/watch?v=u8nQa1cJyX8'},
    {'id': 'zc0s358b3Ys', 'url': 'https://youtu.be/zc0s358b3Ys'},
    {'id': 'zc0s358b3Ys', 'url': 'http://youtu.be/zc0s358b3Ys'},
    {'id': '0zM3nApSvMg', 'url': 'http://www.youtube.com/watch?v=0zM3nApSvMg&feature=feedrec_grec_index'},
    {'id': '0zM3nApSvMg', 'url': 'http://www.youtube.com/v/0zM3nApSvMg?fs=1&amp;hl=en_US&amp;rel=0'},
    {'id': '0zM3nApSvMg', 'url': 'http://www.youtube.com/watch?v=0zM3nApSvMg#t=0m10s'},
    {'id': '0zM3nApSvMg', 'url': 'http://www.youtube.com/embed/0zM3nApSvMg?rel=0'},
    {'id': '0zM3nApSvMg', 'url': 'http://www.youtube.com/watch?v=0zM3nApSvMg'},
    {'id': '0zM3nApSvMg', 'url': 'https://youtu.be/0zM3nApSvMg'},
    {'id': '0zM3nApSvMg', 'url': 'http://www.youtube.com/v/0zM3nApSvMg?fs=1&amp;hl=en_US&amp;rel=0'},
    {'id': '0zM3nApSvMg', 'url': 'http://www.youtube.com/embed/0zM3nApSvMg?rel=0'},
    {'id': '0zM3nApSvMg', 'url': 'http://www.youtube.com/watch?v=0zM3nApSvMg&feature=feedrec_grec_index'},
    {'id': '0zM3nApSvMg', 'url': 'https://www.youtube.com/watch?v=0zM3nApSvMg'},
    {'id': '0zM3nApSvMg', 'url': 'http://youtu.be/0zM3nApSvMg'},
    {'id': '0zM3nApSvMg', 'url': 'http://www.youtube.com/watch?v=0zM3nApSvMg#t=0m10s'},
    {'id': 'QdK8U-VIH_o', 'url': 'http://www.youtube.com/user/IngridMichaelsonVEVO#p/a/u/1/QdK8U-VIH_o'},
    {'id': 'LXilEPmkoQY', 'url': 'https://www.youtube.com/embed/LXilEPmkoQY'},
    {'id': 'LXilEPmkoQY', 'url': 'http://www.youtube.com/v/LXilEPmkoQY'},
    {'id': 'u8nQa1cJyX8', 'url': 'https://www.youtube.com/watch?argv=xyzxyzxyzxy&v=u8nQa1cJyX8'},
    {'id': '0zM3nApSvMg', 'url': 'youtube.com/watch?feature=feedrec_grec_index&v=0zM3nApSvMg '},
    {'id': 'y_Rd2hByRyc', 'url': 'http://www.youtube.com/watch?feature=player_embedded&v=y_Rd2hByRyc'},
    {'id': '0zM3nApSvMg', 'url': 'Check [this](http://youtu.be/0zM3nApSvMg) video!'},
    {'id': 'kKOP79HbtMs', 'url': 'https://www.youtube.com/shared?ci=kKOP79HbtMs'}
]

for i, test in enumerate(tests):
    test_result = get_youtube_id(test['url']) == test['id']

    print('{} test result is\t{}.'.format(i, test_result))
