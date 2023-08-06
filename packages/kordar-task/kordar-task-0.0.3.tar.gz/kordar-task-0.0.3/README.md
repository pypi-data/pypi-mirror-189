# 多进程任务
> 计算密集型应用

```python
# 实例化多进程任务句柄
import time
from kordar_task import task, processmgr

# work_size=工作进程（请设置小于cpu数据）
# queue_buff_len=投递任务最大数量，send队列满则阻塞
handler = processmgr.ProcessTaskHandler(work_size=5, queue_buff_len=20)
# 添加任务逻辑
handler.add_task(task.DefaultTask())
# 启动任务处理器
handler.start_work_pool()

# 发送任务数据到进程队列
handler.send(task.DefaultBody())
handler.send(task.DefaultBody())

time.sleep(10)
```

# 基于异步IO的任务
> IO密集型应用

```python
# 实例化异步处理对象
import time
from kordar_task import task, asyncmgr

# work_size=工作池数量，根据实际情况设置，越大并发越高
# queue_buff_len=投递任务最大数量，send队列满则异常
h = asyncmgr.AsyncTaskHandler(work_size=5, queue_buff_len=20)
# 添加异步任务
# TODO 注意：设置task为异步处理函数
h.add_task(task.DefaultAsyncTask())

# 运行异步任务
h.start_work_pool()

# 向异步队列发送数据
h.send(task.DefaultAsyncBody(1))
h.send(task.DefaultAsyncBody(2))

time.sleep(10)
```

# 自定义任务
```python
from kordar_task.task import ibody, itask
from kordar_task import write_logger
import asyncio

## 同步任务
class DefaultBody(ibody):
    def task_id(self):
        return "default-kordar_task"


class DefaultTask(itask):
    def id(self):
        return "default-kordar_task"

    def execute(self, body):
        write_logger("defaultTask, name = %s" % body.task_id())

# 异步任务
class DefaultAsyncBody(ibody):
    def __init__(self, tid):
        self.id = tid

    def task_id(self):
        return "default-kordar_async_task"


class DefaultAsyncTask(itask):
    def id(self):
        return "default-kordar_async_task"

    async def execute(self, body):
        i = 0
        while i < 5:
            write_logger("DefaultAsyncTask, id = %s" % body.id)
            i = i + 1
            await asyncio.sleep(1)

```
