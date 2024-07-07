from collections.abc import Callable
import os
from pathlib import Path
from typing import Any, List
import pickle

from ilock import ILock


class EarlyBirdLocker:
    """
    A lock provider that either:
    - runs your function if you are the "early bird"
    - if you are not the early bird, waits until the early bird has finished,
      then returns the result of the function from the early bird

    The lock that manages who is and isn't the early bird:
    - is identified by the `tmp_dir` and `lock_keys_base` given to the
      constructor, and the `lock_keys` given to the acquire function
    - is created if it doesn't exist
    - is saved as a file in the tmp_dir path
    """

    def __init__(self, *lock_keys_base: List[str], tmp_dir: Path, worker_id="worker"):
        self.lock_keys_base = lock_keys_base
        self.tmp_dir = tmp_dir
        self.worker_id = worker_id

    def acquire(self, *lock_keys: List[str], do_work: Callable[[], Any]) -> Any:
        """Acquires the lock and yields the result of the given function. For
        subsequent workers, this function will yield the result of the given
        function from the first worker to acquire.

        Args:
            lock_keys (List[str]): The keys to use to identify the lock.
            do_work (Callable[[], Any]): The function to call if the lock is acquired.

        Returns:
            Any: The result of the given function.
        """
        lock_id = "once-per-" + "--".join([*self.lock_keys_base, *lock_keys])

        result_file = self.tmp_dir / f"{lock_id}.pickle"

        is_early_bird = None

        def save_result(result):
            with result_file.open("wb") as f:
                pickle.dump(result, f)
                os.fsync(f.fileno())

        def load_result():
            return pickle.loads(result_file.read_bytes())

        with ILock(lock_id):
            # if the result_fils doesn't exist, that means the caller is the early bird
            if is_early_bird := not result_file.is_file():
                # run do_work *inside* the lock so that other workers have to
                # wait until the early bird is finished
                try:
                    result = ("success", do_work())
                    save_result(result)
                    return result
                except Exception as e:  # pylint: disable=broad-except
                    save_result(("early-bird-failed", type(e).__name__, str(e), e.args))
                    return ("exception", e)

        if not is_early_bird:
            # load results outside the lock so that other worker's aren't
            # serialized by waiting for non-early bird workers to finish within
            # the lock
            return load_result()
