from queue_challenge import Job, PrintQueue, Printer
my_queue = PrintQueue()
my_job = Job()
my_printer = Printer()
my_queue.enqueue(my_job)
my_printer.print_job(my_queue)
