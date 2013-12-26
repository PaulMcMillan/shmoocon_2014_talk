import sys
import random

from horizon import forms

from looksee.queues import MasscanQueue, MasscanJob

random = random.SystemRandom()


class CreateScan(forms.SelfHandlingForm):
    ports = forms.CharField()
    iprange = forms.CharField(label='IP Scan Range', initial='0.0.0.0/0')
    shards = forms.IntegerField(label='Number of Shards', initial=100)
    proto = forms.ChoiceField(choices=(('tcp', 'tcp'),))
    qoutput = forms.CharField(
        label='Output Queue',
        initial='masscan_results')

    def handle(self, request, data):
        data['seed'] = random.randint(0,sys.maxint)
        job_list = []
        for job_num in range(data['shards']):
            new_job = data.copy()
            new_job['shards'] = '%s/%s' % (job_num + 1, data['shards'])
            job_list.append(MasscanJob(**new_job))
        MasscanQueue().send(*job_list)
        return True
