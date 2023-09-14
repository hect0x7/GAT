from common import *


def add_output(k, v):
    os.system(f'echo {k}={v} >> $GITHUB_OUTPUT')


commit_message = sys.argv[1]
print(sys.argv)
p = compile('(.*?): ?(.*)')
match = p.search(commit_message)

if match is None:
    raise NotImplementedError(f'format is wrong: {commit_message}')

ver, msg = match[1], match[2]

add_output('tag', msg)
add_output('body', ver)
