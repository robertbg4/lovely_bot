import os
import glob
import getpass

from crontab import CronTab


with open("sender.py"):
    pass
cron = CronTab(user=getpass.getuser())
cron.remove_all()
home_dir = os.path.dirname(os.path.abspath(__file__))
python_path = os.path.join(os.environ['PATH'].split(':')[0], 'python')
job = cron.new(command= f'{python_path} sender.py >> cron.log 2>&1')
job.hour.on(4)
job.env['HOME'] = home_dir

cron.write()
