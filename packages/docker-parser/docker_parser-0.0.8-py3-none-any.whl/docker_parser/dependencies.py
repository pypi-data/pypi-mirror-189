import sys, os
import bashlex
from .bashlex_utils import bashlex_commands

def multisplit(lvar, *tokens):
    result = []
    if len(tokens) == 0:
        return result
    token, *tokens = tokens
    for item in lvar:
        result.extend(item.split(token))
    if len(tokens) == 0:
        return result
    return multisplit(result, *tokens) 


class Dependency:
    def __init__(self, value, package = None, vendor = None, version = None) -> None:
        self.value = value
        self.vendor = vendor
        self.package = package
        self.version = version
        if not self.package:
            self.package = self.value
    def __repr__(self) -> str:
        return f'{type(self).__name__}({self.package}, {self.version})'
    @classmethod
    def parse(cls, _):
        raise Exception('Not Implemented!')


class GIT(Dependency):
    def __init__(self, url, destination=None, branch=None) -> None:
        super().__init__(
             os.path.basename(url).replace('.git', ''),
             vendor = os.path.basename(os.path.dirname(url)),
             version = branch
        )
        self.url = url
        self.destination = destination
        self.branch = branch

    @classmethod
    def parse(cls, asn):
        branch = None
        url = None
        target = None
        if asn.parts[1].word != 'clone':
            return []
        i = 2
        while i < len(asn.parts):
            if asn.parts[i].word in ('-b', '--branch'):
                branch = asn.parts[i + 1].word
                i += 1
            elif not asn.parts[i].word.startswith('-'):
                if url:
                    target = asn.parts[i].word
                else:
                    url = asn.parts[i].word
            i += 1
        return [cls(url, target, branch)]


class APT(Dependency):
    def __init__(self, package) -> None:
        super().__init__(package)
        if '=' in self.package:
            self.package, self.version = self.package.split('=')
    
    @classmethod
    def parse(cls, asn):
        process = list(map(lambda x: x.word, asn.parts[1:]))
        process.reverse()
        action = None
        while len(process) > 0:
            sub = process.pop()
            if not sub.startswith('-'):
                action = sub
                break
        if action != 'install':
            return []
        while len(process) > 0:
            sub = process.pop()
            if not sub.startswith('-'):
                yield cls(sub)


class WGET(Dependency):
    __IGNORE = ('bin', '.tar.gz', '.gz', '.zip', '.tar')
    def __init__(self, url) -> None:
        super().__init__(
            self._sanitize_filename(os.path.basename(url)),
        )
        self.url = url
        self.file = os.path.basename(url)

        if '-' in self.package:
            self.package, self.version = self.package.rsplit('-', 1)
    @classmethod
    def _sanitize_filename(cls, fn):
        for ignore in cls.__IGNORE:
            fn = fn.replace(ignore, '')
        return fn.rstrip('.-_')
    @classmethod
    def parse(cls, asn):
        return [cls(asn.parts[-1].word)]


class GenericPackageInstaller(Dependency):
    def __init__(self, value, package=None, vendor=None, version=None) -> None:
        super().__init__(value, package, vendor, version)
    @classmethod
    def try_parse(cls, svar):
        package = svar
        vendor = None
        version = None
        if '?' in package:
            package = package.split('?')[0]
        if '=' in package:
            package, *_, version = package.split('=')
        if '/' in package:
            *_, vendor, package = package.split('/')
        if not package:
            return None
        return cls(svar, package, vendor, version)
    @classmethod
    def parse(cls, asn):
        for pasn, cmd in bashlex_commands(asn):
            action = 'install'
            if action not in cmd:
                action = 'require'
                if action not in cmd:
                    continue
            i = cmd.index(action)
            while i + 1 < len(cmd):
                i += 1
                if cmd[i].startswith('-'):
                    continue
                result = cls.try_parse(cmd[i])
                if result:
                    yield result


class Base(Dependency):
    def __init__(self, image) -> None:
        super().__init__(image.id, image.name, version=image.tag)


def process_run(parts):
    processor = {
        'wget': WGET,
        'apt': APT,
        'apt-get': APT,
        'git': GIT
    }
    result = []
    for part in parts:
        for pasn, cmd in bashlex_commands(part):
            parser = processor.get(cmd[0].lower(), GenericPackageInstaller)
            for dep in parser.parse(pasn):
                result.append(dep)
        
    return result


def process_copy(copy):
    for source in copy.sources:
        if source.startswith('https://'):\
            yield WGET(source)
        if source.endswith('.git'):
            yield GIT(source, copy.destination)


def get_dependencies(docker):
    for command in docker.run():
        try:
            processed = bashlex.parse(command.arg)
        except Exception:
            continue
        yield from process_run(processed)
    for copy in docker.copy():
        yield from process_copy(copy)
    yield Base(docker.stages[-1].image)
