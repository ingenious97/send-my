from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
import test_reply

def job_function():
    print("Hello World")

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(test_reply.send_love, 'interval', seconds=10)

sched.start()