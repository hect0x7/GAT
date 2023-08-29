from jmcomic import *

domain_ls = JmModuleConfig.get_jmcomic_domain_all()
option = JmOption.default()

status_list = {}


def test_domain(domain: str):
    client: JmHtmlClient = option.new_jm_client()
    client.domain_list = [domain]
    msg = 'ok'

    try:
        client.get_album_detail('123456')
    except Exception as e:
        msg = str(e.args)
        pass

    status_list['domain'] = msg


multi_thread_launcher(
    iter_objs=domain_ls,
    apply_each_obj_func=test_domain,
)
