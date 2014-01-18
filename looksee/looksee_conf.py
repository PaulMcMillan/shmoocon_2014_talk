import logging
import os
from workers import MasscanWorker, RFBPrintWorker, RFBScreenshotWorker

log = logging.getLogger(__name__)

def run(WorkerClass):
    def wrapped():
        worker = WorkerClass()
        log.info('Started worker:%s:%s', worker.__class__.__name__, os.getpid())
        for job in worker:
            if job:
                log.debug('Completed job: %s', repr(job)[:50])
    return wrapped

# host_regex, func, count
workers = [
    {'host': 's2',
     'func': run(MasscanWorker),
     'count': 1,
     },
    {'host': 's2',
     'func': run(RFBPrintWorker),
     'count': 100,
     },
    ]
