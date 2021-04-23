# coding: utf-8
import webbrowser
import funcs
def browser():
    sites = {"https://vk.com": ["vk"], 'https://www.youtube.com/': ['youtube'], 'https://ru.wikipedia.org': ["wiki"], 'https://ru.aliexpress.com': ['aliexpress'], 'http://google.com': ['google'], 'https: // www.amazon.com': ['амазон', 'amazon'], 'https: // www.apple.com / ru': ['apple']}
    site = funcs.voice.split()[-1]
    for k, v in sites.items():
        for i in v:
            if i not in site.lower():
                open_tab = None
            else:
                open_tab = webbrowser.open_new_tab(k)
                break

        if open_tab is not None:
            break

        if open_tab is not None:
            break