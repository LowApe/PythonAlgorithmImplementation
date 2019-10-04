# 创建一个列表，其中包含要覆盖的城市
states_needed = set(["mt","wa","or","id","nv","ut","ca","az"]) # 传入一个数组，它被转换为集合，集合重复的只能存在1次

# 广播清单，用散列表表示,键为广播台名称，值为覆盖城市
stations = {}
stations["kone"] = set(["id","nv","ut"])
stations["ktwo"] = set(["wa","id","mt"])
stations["kthree"] = set(["or","nv","ca"])
stations["kfour"] = set(["nv","ut"])
stations["kfive"] = set(["ca","az"])

# 需要一个集合来存储最终选择的广播台
final_stations = set()

while states_needed:
    best_station = None  #覆盖最多广播台
    states_covered = set()  #  覆盖最多的城市，已经覆盖的
    for station,states_for_station in stations.items():  # station 广播台 states_for_station 站台所覆盖的城市
        covered = states_needed & states_for_station  # 将覆盖的从总集合中剔除
        if len(covered) > len(states_covered):  # 检查该广播台覆盖的城市是否比 best_station 多
            best_station = station
            states_covered = covered
        states_needed -= states_covered  # 剔除已经覆盖的城市

    final_stations.add(best_station) # 寻找一轮之后就只有一个最好的覆盖最多的广播台

print(final_stations)