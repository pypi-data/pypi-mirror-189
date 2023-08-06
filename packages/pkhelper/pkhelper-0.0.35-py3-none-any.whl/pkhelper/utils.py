from functools import partial
from asyncio import get_running_loop

async def run_cmds_on_cr(func, *args, **kwargs):
    """
    Execute blocking functions asynchronously
    """
    loop = get_running_loop()
    return await loop.run_in_executor(
        None,
        partial(func, *args, **kwargs)
    )
