import functools
from typing import Callable, List
from concurrent.futures import ThreadPoolExecutor, wait


class Func(object):
    sub_tasks: list
    workers: ThreadPoolExecutor

    def __init__(self, fn, *, concurrent: int = 1):
        self.f: Callable = fn
        self.thrds = concurrent

    def __len__(self):
        return len(self.sub_tasks)

    def __iter__(self):
        if hasattr(self, 'sub_tasks'):
            yield from self.sub_tasks
        else:
            raise Exception('func not start')

    def __enter__(self):
        return self

    def __exit__(self, *args):
        ...

    def __del__(self):
        self.cancel(shutdown=True)

    def __call__(self, *args, block=False, **kwargs):
        thrds = min(self.thrds, 5)
        if thrds > 0:
            self.workers = ThreadPoolExecutor(thrds)
            self.sub_tasks = [self.workers.submit(self.f, *args, **kwargs)
                              for _ in range(self.thrds)]
            return block and self.result() or self
        raise Exception('concurrent: 0')

    def wait(self, timeout=None):
        wait(self.sub_tasks, timeout=timeout)

    def result(self):
        res = [t.result() for t in self.sub_tasks]
        ret = res[0] if len(res) == 1 else res
        return {self.f.__name__.upper(): ret}

    def cancel(self, shutdown=False):
        if hasattr(self, 'sub_tasks'):
            [t.cancel() for t in self if not (
                    t.running() or t.done() or t.exception()
            )]
        if hasattr(self, 'workers') and shutdown:
            self.workers.shutdown(wait=False)


def concurrent_wraps(fn=None, *, concurrent=1, **default_args):
    def wrap(f):
        @functools.wraps(f)
        def inner(*args, **kwargs):
            params = {**default_args, **kwargs}
            return Func(f, concurrent=concurrent)(*args, **params)

        return inner

    return fn and wrap(fn) or wrap


class Group(object):
    sub_tasks: list
    workers: ThreadPoolExecutor

    def __init__(self, fns: List = None, *, concurrency=1):
        self.concurrency = concurrency
        self.group = [self.add(f) for f in fns or []]

    def __enter__(self):
        return self

    def __exit__(self, *args):
        ...

    def __len__(self):
        return len(self.sub_tasks)

    def __del__(self):
        self.cancel(shutdown=True)

    def __iter__(self):
        if hasattr(self, 'sub_tasks'):
            while self.sub_tasks:
                yield self.sub_tasks.pop(0)
        else:
            raise Exception('group not start')

    def __call__(self, block=False):
        concurrency = min(self.concurrency, len(self.group), 5)
        if concurrency > 0:
            self.workers = ThreadPoolExecutor(concurrency)
            self.sub_tasks = [self.workers.submit(f) for f in self.group]
            return block and [t.result() for t in self.sub_tasks] or self
        raise Exception('concurrency: 0')

    @staticmethod
    def _f_wrap(f):
        @functools.wraps(f)
        def inner(*args, **kwargs):
            return {f.__name__.upper(): f(*args, **kwargs)}

        return inner

    def add(self, fn=None, **default_kwargs):
        def pack(f):
            f = self._f_wrap(f)

            @functools.wraps(f)
            def inner(*args, **kwargs):
                params = {**default_kwargs, **kwargs}
                self.group.append(functools.partial(f, *args, **params))

            return inner

        return fn and pack(fn) or pack

    def cancel(self, shutdown=False):
        if hasattr(self, 'sub_tasks'):
            [t.cancel() for t in self.sub_tasks if not (
                    t.running() or t.done() or t.exception()
            )]
        if hasattr(self, 'workers') and shutdown:
            self.workers.shutdown(wait=False)


__all__ = ('Func', 'concurrent_wraps', 'Group')
