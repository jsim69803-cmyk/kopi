# queue 초기화 함수
def init_queue(size):
    global print_q, front, rear
    print_q = [None] * size
    front = -1
    rear = -1
    return print("큐 초기화 완료! 큐 크기: " + str(size))

def enqueue(data):
    global rear
    if is_queue_full():
        return print("큐가 꽉 찼습니다.")
    else:
        rear += 1
        print_q[rear] = data
        return print("현재 rear:" + str(rear))

def dequeue():
    global front
    if is_queue_empty():
        return print("큐가 비어 있습니다! 삭제할 데이터가 없습니다.")
    front += 1
    temp = print_q[front]
    print_q[front] = None
    return temp

def peek():
    global front
    if is_queue_empty():
        return print("큐가 비어 있습니다! Peek 불가.")
    else:
        temp = print_q[front + 1]
        return temp

def is_queue_empty():
    global front, rear
    if front == rear:
        return True
    else:
        return False

def is_queue_full():
    global rear
    if rear == len(print_q) - 1:
        return True
    else:
        return False

def print_queue():
    print("=== 큐 상태 ===")
    print("큐 크기: " + str(len(print_q)))
    for i in range(len(print_q)):
        print(print_q[i])
    print("현재 front:" + str(front))
    print("현재 rear:" + str(rear))
    print("===============")

init_queue(5)
enqueue("커피")
enqueue("우유")
enqueue("주스")
enqueue("물")
enqueue("콜라")
print("================ peek() 함수 호출 전 ================")
print(peek())
print("================ peek() 함수 호출 후 ================")
print(peek())
print_queue()
