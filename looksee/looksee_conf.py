""" This was originally intended to house per-worker config. It has
grown and should be refactored.
"""

import logging
import os
import socket
import workers

from setproctitle import setproctitle

from tasa.store import connection

log = logging.getLogger(__name__)

def run(WorkerClass):
    def wrapped():
        worker = WorkerClass()
        worker_identifier = '%s:%s:%s' % (
            socket.gethostname(), worker.__class__.__name__, os.getpid())
        setproctitle(worker_identifier)
        connection.client_setname(worker_identifier)
        log.info('Started worker: %s' % worker_identifier)
        for job in worker:
            if job:
                log.debug('Completed job: %s', repr(job)[:50])
    return wrapped

# host_regex, func, count
workers = [
    {'host': r's\d+',
     'func': run(workers.MasscanWorker),
     'count': 1,
     },
    {'host': r'cloud-worker',
     'func': run(workers.RFBScreenshotWorker),
     'count': 50,
     },
    {'host': r'cloud-worker',
     'func': run(workers.RFBPrintWorker),
     'count': 50,
     },
    ]
