# Cyber-Physical Power Grid Simulation

A Python-based simulation of a simplified electrical power grid used to study **cyber-physical failures, load redistribution, and cascading outages**.  

The project models interactions between **power substations and demand regions** to explore how failures or cyber attacks can propagate through critical infrastructure.

---

# Project Overview

Modern power grids are complex cyber-physical systems where failures in one component can propagate through interconnected infrastructure. This simulator models a simplified grid in order to demonstrate:

- substation overload conditions
- load redistribution across infrastructure
- cascading failure scenarios
- the impact of cyber attacks on grid stability

The simulation is intended as a **learning and analysis tool** for understanding resilience challenges in critical infrastructure.

---

# System Architecture

The simulation consists of three core components:

### Substation
Represents a power distribution node with:
- maximum power capacity
- current load
- operational status (online/offline)

Substations detect overload conditions and may shut down to prevent damage.

### Region
Represents a demand source (such as a city or facility).  
Each region distributes its load across connected substations.

### GridController
The central simulation engine that:
- resets loads
- distributes demand across substations
- monitors overload conditions
- handles shutdown events
- displays grid status

---

# Current Features

- Substation modeling (3 substations)
- Region demand modeling (4 regions)
- Load distribution across connected substations
- Substation overload detection and shutdown
- Grid controller simulation logic
- Terminal-based substation load visualization
- Cyber attack scenario simulation (substation shutdown)
- Grid resilience through dynamic load redistribution

---

# Example Simulation Behavior

The simulator demonstrates how failures propagate through interconnected systems.  

Example scenarios include:

- **Demand spikes** causing substation overload
- **Cyber attacks** disabling infrastructure
- **Load redistribution** preventing cascading failures

Detailed walkthroughs of these scenarios can be found in: simulation_analysis.md

This file contains:

- explanations of simulation scenarios
- step-by-step analysis of grid behavior
- terminal output examples
- cybersecurity implications of cascading failures

---

# Project Structure

- `cybergrid.py` – main simulation engine
- `simulation_analysis.md` – explanation of simulation scenarios and results

---

# Future Features

Planned improvements to the simulator include:

- JSON-driven attack scenario framework to model targeted cyber threats (e.g., substation shutdowns, control signal manipulation) with configurable and repeatable simulation inputs  
- Cascading failure detection and propagation logic to model multi-stage outages across interconnected substations  
- Critical infrastructure prioritization (e.g., water treatment plants vs residential regions) with load shedding and resource allocation strategies  
- Event logging system for tracking grid state changes, attack events, and failure timelines for post-simulation analysis  
- Time-stepped simulation engine to model multi-stage grid evolution and dynamic system behavior over successive intervals  
- Resilience analysis metrics to evaluate grid robustness under varying attack conditions and failure scenarios  
- Configurable grid topology via external configuration files (e.g., JSON) to enable flexible modeling of different infrastructure layouts  

---

# Educational Purpose

This project explores how **cybersecurity risks intersect with physical infrastructure systems**.  

Understanding cascading failures and resilience strategies is essential for protecting critical systems such as power grids, water treatment plants, and transportation infrastructure.

---

# Author

Avery Dyer