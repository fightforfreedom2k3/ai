import heapq

def dijkstra(graph, start, end):
    distances = {}
    previous_nodes = {}
    priority_queue = []

    # Khởi tạo các giá trị ban đầu
    for node in graph['nodes']:
        node_name = node['node']
        distances[node_name] = float('inf')
        previous_nodes[node_name] = None
        heapq.heappush(priority_queue, node_name)

    distances[start] = 0

    while priority_queue:
        # Lấy node có khoảng cách ngắn nhất từ đỉnh đầu tiên trong hàng đợi ưu tiên
        current = heapq.heappop(priority_queue)

        # Duyệt qua các node kề của node hiện tại
        for edge in [edge for edge in graph['edges'] if edge['node1'] == current]:
            neighbor = edge['node2']
            total_distance = distances[current] + edge['weight']

            # Nếu khoảng cách tính được ngắn hơn khoảng cách hiện tại
            if total_distance < distances[neighbor]:
                distances[neighbor] = total_distance
                previous_nodes[neighbor] = current

                # Cập nhật độ ưu tiên trong hàng đợi ưu tiên
                heapq.heappush(priority_queue, neighbor)

    # Xây dựng đường đi từ endNode đến startNode
    path = [end]
    current = end
    while current != start:
        current = previous_nodes[current]
        path.insert(0, current)

    return path