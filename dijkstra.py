# 关系图结构
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# 权重
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 父节点
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 处理过的节点
processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)

while node is not None:  # 把所有节点都处理一遍直到最后一个节点
    cost = costs[node]  # 获取从开始到该节点的时间
    neighbors = graph[node]  # 获取该点的邻居
    for n in neighbors.keys():  # 遍历邻居
        new_cost = cost + neighbors[n]  # 从此节点到邻居节点的时间
        if costs[n] > new_cost:  # 如果这个时间小于记录的开销
            costs[n] = new_cost  # 更新开销
            parents[n] = node  # 更新父节点
    processed.append(node)  # 将该节点记录以检查
    node = find_lowest_cost_node(costs)  # 找出下一个未处理的节点

print(costs)
