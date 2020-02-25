from force_field import Sim

data = [] # 2-dimensional plane of data projection from globe

sim = Sim(len(data), 'cylindrical') # size of vector and type of map projection
sim.add_vector([1, [0., 0.]])
sim.build(-1)

print(a.get_nns_by_item(0, 100))
print(a.get_nns_by_vector([1.0, 0.5, 0.5], 100))