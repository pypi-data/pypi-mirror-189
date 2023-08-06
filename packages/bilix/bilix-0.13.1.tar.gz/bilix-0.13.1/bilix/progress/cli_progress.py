import asyncio
from typing import Optional, Any, Set, Union
from rich.progress import Progress, TaskID, TextColumn, BarColumn, DownloadColumn, TransferSpeedColumn, \
    TimeRemainingColumn

from .base_progress import BaseProgress


class CLIProgress(BaseProgress):
    _progress = Progress(
        TextColumn("[progress.description]{task.description}"),
        TextColumn("[progress.percentage]{task.percentage:>4.1f}%"),
        BarColumn(),
        DownloadColumn(),
        TransferSpeedColumn(),
        'ETA',
        TimeRemainingColumn(), transient=True
    )

    def __init__(self, holder=None):
        super().__init__(holder=holder)
        self.own_task_ids: Set[TaskID] = set()
        self._progress.start()  # ensure progress is start

    @classmethod
    def start(cls):
        cls._progress.start()

    @classmethod
    def stop(cls):
        cls._progress.stop()

    @property
    def tasks(self):
        return self._progress.tasks

    async def add_task(
            self,
            description: str,
            start: bool = True,
            total: Optional[float] = 100.0,
            completed: int = 0,
            visible: bool = True,
            **fields: Any,
    ) -> TaskID:
        task_id = self._progress.add_task(description=description, start=start, total=total,
                                          completed=completed, visible=visible, **fields)
        self.own_task_ids.add(task_id)
        return task_id

    @property
    def holder_speed(self):
        if self.holder:
            return sum(self._progress.tasks[task_id].speed for task_id in self.own_task_ids
                       if self._progress.tasks[task_id].speed)
        raise Exception("No holder, No speed")

    async def _check_speed(self, chunk_size):
        if self.holder and self.holder.speed_limit:
            if self.holder_speed > self.holder.speed_limit:
                await asyncio.sleep(self.dynamic_sleep_time(chunk_size))

    async def update(
            self,
            task_id: TaskID,
            *,
            total: Optional[float] = None,
            completed: Optional[float] = None,
            advance: Optional[float] = None,
            description: Optional[str] = None,
            visible: Optional[bool] = None,
            refresh: bool = False,
            **fields: Any,
    ) -> None:
        if advance:
            await self._check_speed(chunk_size=advance)
        self._progress.update(task_id, total=total, completed=completed, advance=advance,
                              description=description, visible=visible, refresh=refresh, **fields)
        if self._progress.tasks[task_id].finished and task_id in self.own_task_ids:
            self.own_task_ids.remove(task_id)
