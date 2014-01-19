""" You'd have thought I'd learn not to do this part at the last minute. Nope!
"""
import tasa
import tasa.store
from workers import hmacit
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates/'))
pipe = tasa.store.connection.pipeline()

buckets = ['results_%s' % x for x in range(1, 256)]

BASE_URI = 'http://104dfde118a1f90d0ad2-1b1b9f12b3a6c8f1ea85e43b74e7f99e.r70.cf2.rackcdn.com'

for b in buckets:
    pipe.hlen(b)
bucket_list = zip(buckets, pipe.execute())
template = env.get_template('index.html')
rendered = template.render(bucket_list=bucket_list)
with open('www/index.html', 'w') as f:
    f.write(rendered)

for b in buckets:
    pipe.hgetall(b)

result_list = zip(buckets, pipe.execute())
for bucket, values in result_list:
    parsed_values = [(hmacit(a), b) for a,b in values.items()]
    template = env.get_template('inner_index.html')
    rendered = template.render(values=parsed_values, base_uri=BASE_URI)
    with open('www/%s.html' % bucket, 'w') as f:
        f.write(rendered)
