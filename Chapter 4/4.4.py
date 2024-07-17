class EmployeeQueue:
    def __init__(self):
        self.queue = []
        self.departments = {}

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, department, emp_id):
        if department not in self.departments:
            self.queue.append((department, emp_id))
            self.departments[department] = [emp_id]
        else:
            index = next((i for i, (dept, _) in enumerate(self.queue) if dept == department), len(self.queue))
            while index < len(self.queue) and self.queue[index][0] == department:
                index += 1
            self.queue.insert(index, (department, emp_id))
            self.departments[department].append(emp_id)

    def dequeue(self):
        if self.is_empty():
            return "Empty"
        department, emp_id = self.queue.pop(0)
        self.departments[department].remove(emp_id)
        if not self.departments[department]:
            del self.departments[department]
        return emp_id

    def size(self):
        return len(self.queue)

# Input processing
input_str = input("Enter Input : ")
n, a = input_str.split('/')

# Initialize the queue
queue = EmployeeQueue()

# Process commands
for command in a.split(','):
    if command.startswith('D'):
        print(queue.dequeue())
    elif command.startswith('E'):
        _, emp_id = command.split()
        department = None
        for entry in n.split(','):
            dep, id = entry.split()
            if id == emp_id:
                department = dep
                break
        queue.enqueue(department, emp_id)
