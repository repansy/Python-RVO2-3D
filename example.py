#!/usr/bin/env python

import rvo2_3d

sim = rvo2_3d.PyRVOSimulator(1/60., 1.5, 5, 1.5, 0.4, 2)

# Pass either just the position (the other parameters then use
# the default values passed to the PyRVOSimulator constructor),
# or pass all available parameters.
a0 = sim.addAgent((0, 0, 0))
a1 = sim.addAgent((1, 0, 0))
a2 = sim.addAgent((1, 1, 0))
a3 = sim.addAgent((0, 1, 0), 1.5, 5, 1.5, 0.4, 2, (0, 0, 0))

sim.setAgentPrefVelocity(a0, (1, 1, 0))
sim.setAgentPrefVelocity(a1, (-1, 1, 0))
sim.setAgentPrefVelocity(a2, (-1, -1, 0))
sim.setAgentPrefVelocity(a3, (1, -1, 0))

print('Simulation has %i agents in it.' %
      (sim.getNumAgents()))

print('Running simulation')

for step in range(20):
    sim.doStep()

    positions = ['(%5.3f, %5.3f, %5.3f)' % sim.getAgentPosition(agent_no)
                 for agent_no in (a0, a1, a2, a3)]
    print('step=%2i  t=%.3f  %s' % (step, sim.getGlobalTime(), '  '.join(positions)))