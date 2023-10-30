from common import *


def parse_body(body):
    if ';' not in body:
        return body

    parts = body.split(";")
    points = []
    for i, e in enumerate(parts):
        e: str = e.strip()
        points.append(f'{i}. {e}')

    return '\\n'.join(points)


def add_output(k, v):
    os.system(f'echo {k}={v} >> $GITHUB_OUTPUT')


commit_message = sys.argv[1]
p = compile('(.*?): ?(.*)')
match = p.search(commit_message)
assert match is not None, f'format is wrong: {commit_message}'

tag, body = match[1], match[2]

add_output('tag', tag)
add_output('body', parse_body(body))
