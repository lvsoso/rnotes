import time
import random
import logging
from concurrent import futures
from tqdm import tqdm
from rich.logging import RichHandler

logger = logging.getLogger(__name__.split('.')[0])
handler = RichHandler(rich_tracebacks=True, omit_repeated_times=False, show_path=False)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def download(url):
    total = 1 * 15 * 1024
    downloaded_size = 0
    parallels = 4
    desc_file_name = "test"
    progress = tqdm(
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
        total=total,
        initial=downloaded_size,
        desc=f'Downloading {desc_file_name}',
        ascii='.#',
    )

    def _download_part(tid, start, end):
        try_num = 100000
        count  = 0
        chunk = 10
        while 1 :
            try:
                for i in range(int((end -start + chunk) / chunk)):
                    should_except = random.randint(10, 100)
                    if should_except % 30  == 0 :
                        raise Exception(f"test  {tid} should except: {should_except}")
                    progress.update(chunk)
                break
            except Exception as e:
                logger.error(e.__str__())
            count += 1
            if  count >= try_num:
                raise Exception(f"test  {tid} except: {should_except}")



    executor = futures.ThreadPoolExecutor(max_workers=parallels)
    part_size = 15 * 1024
    tasks = []
    for i in range(int((total + part_size - 1) / part_size)):
        start = i * part_size
        end = start + part_size - 1
        print(start, end)
        tasks.append(executor.submit(_download_part, i, start, end))
    
    done, _ = futures.wait(tasks, return_when=futures.FIRST_EXCEPTION)
    try:
        for task in done:
            task.result()
    except Exception as exc:
        executor.shutdown(wait=False)
        raise exc
    else:
        executor.shutdown(wait=True)

    progress.close()    

if __name__ == '__main__':
    download("abc")