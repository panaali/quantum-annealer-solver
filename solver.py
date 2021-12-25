import networkx as nx
s5 = nx.star_graph(4)
from dimod.reference.samplers import ExactSolver
sampler = ExactSolver()
import dwave_networkx as dnx
print(dnx.min_vertex_cover(s5, sampler))
from dwave.system import DWaveSampler, EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler())
print(dnx.min_vertex_cover(s5, sampler))
w5 = nx.wheel_graph(5)
print(dnx.min_vertex_cover(w5, sampler))   
print(dnx.min_vertex_cover(w5, sampler))     
c5 = nx.circular_ladder_graph(5)
print(dnx.min_vertex_cover(c5, sampler))   
print(dnx.min_vertex_cover(c5, sampler))   
