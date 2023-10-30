import os
import sys
import re


def add_output(k, v):
    if '\n' not in v:
        cmd = f'echo -e "{k}={v}" >> $GITHUB_OUTPUT'
        print(cmd, os.system(cmd))
        return

    for cmd in [
        '''delimiter="$(openssl rand -hex 8)"''',
        '''echo "output-name<<${delimiter}" >> $GITHUB_OUTPUT''',
        f'''echo "{v}" >> $GITHUB_OUTPUT''',
        '''echo "${delimiter}" >> $GITHUB_OUTPUT''',
    ]:
        print(cmd, os.system(cmd))


def parse_body(body):
    if ';' not in body:
        return body

    parts = body.split(";")
    points = []
    for i, e in enumerate(parts):
        e: str = e.strip()
        if e == '':
            continue
        points.append(f'{i}. {e}')

    return r'\n'.join(points)


msg = sys.argv[1]
print(f'msg: {msg}')
p = re.compile('(.*?): ?(.*)')
match = p.search(msg)
assert match is not None, f'commit message format is wrong: {msg}'

tag, body = match[1], match[2]

add_output('tag', tag)
add_output('body', parse_body(body))
