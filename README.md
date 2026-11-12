# 심준범 202630114
## 11월 12일 11주차

📚 자료구조 학습 정리: 원형 큐(Circular Queue) & 트리(Tree)Python을 활용한 선형 자료구조(원형 큐)와 비선형 자료구조(이진 트리, 이진 탐색 트리)의 핵심 개념 및 구현 정리입니다.   
📑 목차
원형 큐 (Circular Queue)
트리의 개념과 이진 트리 (Binary Tree)
이진 트리 순회 (Tree Traversal)
이진 탐색 트리 (Binary Search Tree, BST)
Python 실습 코드: 이진 트리 구현
1. 원형 큐 (Circular Queue)
💡 등장 배경: 순차 큐의 한계일반 순차 큐에서는 앞쪽 공간이 비어 있더라도 rear가 배열의 마지막 인덱스에 도달하면 새로운 데이터를 바로 삽입할 수 없습니다.
데이터를 삽입하려면 기존 원소들을 모두 왼쪽으로 한 칸씩 이동시킨 뒤 front와 rear 값을 1씩 감소시켜야 하므로, 데이터 크기가 클수록 심각한 오버헤드(Overhead)가 발생합니다.   
🔄 원형 큐의 구조와 원리개념: 순차 큐의 처음과 끝을 논리적으로 연결하여, 데이터 이동 없이 빈 공간을 재활용하는 구조입니다.   
초기화: 순차 큐는 front = rear = -1로 초기화하지만, 원형 큐는 인덱스 회전 계산을 위해 front = rear = 0으로 초기화합니다.   
공백과 포화 상태 구분: 배열의 모든 칸을 채우면 front == rear가 되어 빈 상태와 구분할 수 없게 되므로, 항상 한 칸을 비워둔 상태를 포화 상태로 정의합니다.   
상태 및 연산핵심 조건식 및 동작 로직비고공백 상태 (Empty)front == rear   
초기 상태 및 모든 데이터 추출 후 상태   포화 상태 (Full)(rear + 1) % SIZE == front   메모리 한 칸을 비워두어 공백 상태와 구분   
데이터 삽입 (enQueue)rear = (rear + 1) % SIZEqueue[rear] = data   
포화 상태 여부를 먼저 검사 후 실행   
데이터 추출 (deQueue)front = (front + 1) % SIZEdata = queue[front]queue[front] = None   
공백 상태 여부를 먼저 검사 후 실행   
2. 트리의 개념과 이진 트리 (Binary Tree)🌳 트리(Tree) 기본 용어회사 조직도나 컴퓨터의 디렉터리(폴더) 구조처럼 상하 계층 관계를 표현하기 위해 나무를 거꾸로 뒤집어 놓은 형태의 비선형 자료구조입니다.   
루트 노드 (Root): 트리의 최상단(레벨 0)에 위치한 시작 노드   
에지 (Edge): 노드와 노드를 연결하는 간선   
부모-자식 노드: 에지로 직접 연결된 상하 관계의 노드   
차수 (Degree): 특정 노드가 가지고 있는 자식 노드의 개수   리프 노드 (Leaf Node): 자식 노드가 없는 최하단 단말노드   
높이 (Height): 루트 노드(레벨 0)부터 가장 깊은 리프 노드까지의 레벨 수   
🔀 이진 트리 (Binary Tree)의 종류모든 노드의 자식 노드가 최대 2개(왼쪽·오른쪽 서브 트리) 이하로 구성된 트리입니다.   
종류구조적 특징포화 이진 트리 (Full Binary Tree)
모든 레벨이 노드로 꽉 차 있는 트리 (높이가 $h$일 때 총 노드 수 = $2^{h+1} - 1$)   
완전 이진 트리 (Complete Binary Tree)마지막 레벨을 제외한 모든 레벨이 꽉 차 있으며, 마지막 레벨은 왼쪽부터 순서대로 채워진 트리   
일반 이진 트리
중간 레벨에 빈자리가 있거나 규칙 없이 자식이 2개 이하로 연결된 트리   
편향 이진 트리 (Skewed Binary Tree)
모든 노드가 왼쪽 또는 오른쪽 한 방향으로만 일렬로 연결된 트리   
🧩 이진 트리 노드 구조하나의 노드는 [왼쪽 링크 | 데이터 | 오른쪽 링크]로 구성된 이중 연결 리스트 형태로 구현합니다.   Pythonclass TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None
3. 이진 트리 순회 (Tree Traversal)트리의 모든 노드를 중복 없이 한 번씩 방문하는 과정을 순회(Traversal)라고 하며, 현재 노드의 데이터를 처리하는 시점에 따라 3가지로 나뉩니다.   
순회 방식
방문 순서
탐색 핵심
전위 순회 (Preorder)
현재 노드  왼쪽 서브 트리  오른쪽 서브 트리   
루트 노드를 가장 먼저 처리   
중위 순회 (Inorder)
왼쪽 서브 트리  현재 노드 오른쪽 서브 트리   
왼쪽 끝 노드부터 순서대로 처리   
후위 순회 (Postorder)
왼쪽 서브 트리  오른쪽 서브 트리  현재 노드   
하위 서브 트리를 모두 처리한 뒤 루트 처리   
간편 판별 팁: 루트 노드의 왼쪽에서 출발해 트리 외곽선을 따라 한 붓 그리기로 돌 때, 각 노드의 왼쪽을 지나면 전위 순회, 아래쪽을 지나면 중위 순회, 오른쪽을 지나면 후위 순회 순서가 됩니다.   
4. 이진 탐색 트리 (Binary Search Tree, BST)
📌 이진 탐색 트리의 4가지 규칙데이터의 크기를 기준으로 정렬된 형태를 유지하여 빠른 검색을 지원하는 이진 트리입니다.   
1.왼쪽 서브 트리는 루트 노드보다 모두 작은 값을 가집니다.   
2.오른쪽 서브 트리는 루트 노드보다 모두 큰 값을 가집니다.   
3.모든 서브 트리 역시 위 1, 2번 규칙을 재귀적으로 만족합니다.   
4.모든 노드 값은 고유하며, 중복된 값은 저장할 수 없습니다.   
⚙️ 주요 동작 원리 및 응용데이터 삽입 (Insert): 루트 노드부터 크기 비교를 시작하여 삽입할 값이 현재 노드보다 작으면 왼쪽, 크면 오른쪽으로 이동하며 빈 링크(None)를 만날 때 새 노드를 연결합니다.   
데이터 검색 (Search): 루트 노드부터 값을 비교해 일치하면 탐색을 종료하고, 찾으려는 값이 작으면 왼쪽 서브 트리로, 크면 오른쪽 서브 트리로 이동하며 탐색합니다.  
활용 사례: 도서관 도서 관리 프로그램처럼 도서 목록(bookAry)을 책 이름 기준 BST와 작가 이름 기준 BST로 각각 구축하면 대규모 데이터에서도 원하는 정보를 빠르게 조회할 수 있습니다.   
5. Python 실습 코드: 이진 트리 구현강의 내용을 바탕으로 음료수 데이터를 활용해 높이가 2이고 노드가 6개인 완전 이진 트리를 직접 구현한 코드입니다.   
📐구현된 트리 구조Plaintext        
        [커피]
       /      \
   [우유]    [주스]
   /    \      /
 [물] [콜라] [사이다]
💻 소스 코드 (binary_tree.py)
Pythonclass tree_node:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


# 루트 노드 생성 (Level 0)
node1 = tree_node()
node1.data = "커피"

# Level 1 노드 생성 및 연결
node2 = tree_node()
node2.data = "우유"
node1.left = node2

node3 = tree_node()
node3.data = "주스"
node1.right = node3

# Level 2 노드 생성 및 연결
node4 = tree_node()
node4.data = "물"
node2.left = node4

node5 = tree_node()
node5.data = "콜라"
node2.right = node5

node6 = tree_node()
node6.data = "사이다"
node3.left = node6

# 트리 구조 출력
print("=== 이진 트리 구조 ===")
print(node1.data, end=" ")
print()
print(node1.left.data, node1.right.data, end=" ")
print()
print(node1.left.left.data, node1.left.right.data, node1.right.left.data)
🖥️ 실행 결과Plaintext=== 이진 트리 구조 ===
커피 
우유 주스 
물 콜라 사이다
