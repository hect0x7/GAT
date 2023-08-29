from jmcomic import *

option = JmOption.default()
option.client.domain = ['18comic.vip']

def get_domain_ls():
    template = 'https://jmcmomic.github.io/go/{}.html'
    url_ls = [
        template.format(i)
        for i in range(300, 309)
    ]
    domain_set: Set[str] = set()

    def fetch_domain(url):
        postman = JmModuleConfig.new_postman()
        text = postman.get(url, allow_redirects=False).text
        for domain in JmcomicText.analyse_jm_pub_html(text):
            domain_set.add(domain)

    multi_thread_launcher(
        iter_objs=url_ls,
        apply_each_obj_func=fetch_domain,
    )
    return domain_set


domain_set = get_domain_ls()
status_dict = {}


def test_domain(domain: str):
    client: JmHtmlClient = option.new_jm_client()
    client.domain_list = [domain]
    msg = 'ok'

    try:
        client.get_album_detail('123456')
    except Exception as e:
        msg = str(e.args)
        pass

    status_dict[domain] = msg


multi_thread_launcher(
    iter_objs=domain_set,
    apply_each_obj_func=test_domain,
)

for domain, status in status_dict.items():
    print(f'{domain}: {status}')
