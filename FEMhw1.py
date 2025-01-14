from femedu.domain import *
from femedu.elements.linear import *
from femedu.materials import ElasticSection

# create a system interface
model = System()

# The model object will hold all
# information forming your finite element model,
# as well as provide the interface for analysis control, plotting, and data gathering.

# Next, we are creating nodes as Node objects.
nd0 = Node( 0.0, 0.0)
nd1 = Node( 8.0, 6.0)
nd2 = Node(16.0, 0.0)

# add nodes to the model
model.addNode(nd0, nd1, nd2)

# define material parameters
params = dict(
    E = 1000.,   # Young's modulus
    A = 1.0,     # cross section area
)

# define an element and add to the model
elem0 = Truss(nd0, nd1, ElasticSection(params))
model.addElement(elem0)

# enforce Boundary Conditions
nd0.fixDOF(['ux','uy'])   # pin
nd2.fixDOF(['uy'])        # horizontal roller

# apply loads
nd1.addLoad([-1.0],['uy'])

# generate report
model.report()

