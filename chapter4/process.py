import subprocess


def run(command):
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    stdout_stream = process.stdout.read()
    stderr_stream = process.stderr.read()
    returncode = process.wait()
    if not isinstance(stdout_stream, str):
        stdout_stream = stdout_stream.decode('utf-8')
    if not isinstance(stderr_stream, str):
        stderr_stream = stderr_stream.decode('utf-8')
    stdout = stdout_stream.splitlines()
    stderr = stderr_stream.splitlines()

    return stdout, stderr, returncode


def is_xfs(device):
    stdout, stderr, code = run(['sudo', 'blkid', device])
    for line in stdout:
        if 'TYPE="xfs"' in line:
            return True
    return False


def stop_container(container):
    stdout, stderr, code = run(['docker', 'stop', container])
    if code != 0:
        raise RuntimeError(f'Unable to stop {container}')


def _lsblk_parser(lines):
    parsed = {}
    for line in lines:
        for item in lines.split('" '):
            key, value = item.split('="')
            parsed[key] = value.strip('"')

    return parsed


def lsblk(device):
    command = [
        'lsblk',
        '-P',   # Produce pairs of key/value
        '-p',   # Return absolute paths
        '-o',   # Define the labels we are interested in
        'NAME,PARTLABEL,TYPE',
        device
    ]

    stdout, stderr, code = run(command)
    return _lsblk_parser(stdout)
