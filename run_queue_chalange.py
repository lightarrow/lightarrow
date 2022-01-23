from queue_challenge import Job, PrintQueue, Printer
my_queue = PrintQueue()
my_job = Job()
my_printer = Printer()
my_queue.enqueue('apple')
my_job.print_page()
