from .queues import MasscanQueue

class MasscanWorker(BaseWorker):
    qinput = MasscanQueue()
    qoutput = None  # set by each job as it is handled

    output_chunk_size=1000

    def handle(self, job):
        self.qoutput = ScanResultQueue(job.qoutput)
        return super(MasscanWorker, self).handle(job)

    def run(self, job):
        command = ['masscan',
                   '--range', job.range,
                   '--ports', job.ports,
                   '--shards', job.shards,
                   '--seed', job.seed,
                   ]
        proc = subprocess.Popen(command,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        for line in proc.stdout:
            match = re.match(
                'Discovered open port (\d+)/%s on (\d+\.\d+\.\d+\.\d+)' % (
                    jobs.proto),
                line.strip())
            if match:
                yield match.groups()
        proc.wait()
