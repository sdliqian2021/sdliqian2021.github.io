# Can We Demonstrate a Process Digital Twin with Public Data?

_Last updated: 2026-07-09 12:40 America/New_York (UTC-04:00)_

**Purpose:** Define a credible public-data demonstration that teaches how a process digital twin works without overstating what an open benchmark can prove.

**Core thesis:** Public data can demonstrate process-state reconstruction, model synchronization, prediction, decision support, and feedback. However, a historical dataset alone is not a complete digital twin. A credible demonstration must add an executable process model or replay environment and organize the system around a concrete decision loop.

---

## Yes—but Not with a Dataset Alone

Public industrial datasets are useful for teaching because they are accessible, reproducible, and free from company confidentiality constraints.

They are also easy to misuse.

A common demonstration looks like this:

```text
download historical data
→ train an anomaly-detection model
→ display predictions in a dashboard
→ call the result a digital twin
```

This is an analytics demonstration, not yet a process digital twin. A twin must connect process state and history to executable predictions, decision rules, and resulting outcomes.

The demonstration therefore needs more than data:

```text
public process data
+ process-state model
+ executable behavioral model
+ operating constraints
+ decision logic
+ event and outcome history
= public reference process-twin demonstrator
```

---

## Recommended Benchmark: The Tennessee Eastman Process

The Tennessee Eastman Process is a widely used industrial process-control benchmark introduced by Downs and Vogel in 1993.

It represents a nonlinear chemical production process containing a reactor, condenser, vapor-liquid separator, compressor, and product stripper connected through recycle streams. The original benchmark includes:

- 41 process measurements;
- 12 manipulated variables;
- interacting process units;
- process disturbances;
- production and control objectives;
- nonlinear and dynamic behavior.

The benchmark is complex enough to demonstrate plant-wide interactions while remaining accessible. Unlike a static classification dataset, its disturbances propagate through time and across process units.

---

## The Decision Loop to Demonstrate

The demonstrator should focus on one clear operational question:

> When process behavior begins to deviate, can the twin identify the current operating state, estimate the likely consequence, and recommend a permitted response before the process violates an operating or quality limit?

The minimum loop would be:

```text
1. Replay process signals as a live stream
2. Reconstruct the current process state
3. Detect a deviation from expected behavior
4. Identify the likely disturbance or affected subsystem
5. Predict short-horizon consequences
6. Evaluate permitted interventions
7. Recommend an action with uncertainty and constraints
8. Apply the action in simulation or replay a recorded response
9. Compare predicted and observed outcomes
10. Store the complete decision history
```

This sequence demonstrates why a process twin is different from a prediction model. Detection is only one step in the loop.

---

## Proposed Demonstrator Architecture

### 1. Process Replay Layer

Historical records are replayed according to their timestamps so that the demonstrator behaves like an operating process.

This layer should handle:

- measurement timing;
- missing or delayed signals;
- unit definitions;
- sensor quality;
- operating modes and intervention events.

### 2. Context and State Layer

The demonstrator maintains explicit process state rather than treating each row as an independent observation.

Example states might include:

```text
startup
normal production
grade or target transition
disturbance developing
constraint approaching
recovery
unstable or shutdown condition
```

It should also maintain the active operating point, control configuration, and recent event history.

### 3. Behavioral Model Layer

The twin needs an executable representation of expected process behavior.

Possible approaches include:

- the original Tennessee Eastman simulator;
- an open-source reimplementation;
- a reduced-order dynamic model;
- a system-identification model;
- a hybrid model combining mass-balance relationships with machine learning.

The model need not reproduce every detail. It must be valid for the selected prediction and intervention comparison.

### 4. Monitoring and Diagnosis Layer

This layer compares measured behavior with expected behavior.

Possible methods include:

- engineering limits and rules;
- residuals between model and measurement;
- principal-component or latent-variable monitoring;
- change-point detection;
- supervised fault classification.

The demonstrator should report uncertainty and alternative explanations rather than presenting every classification as certain.

### 5. Decision Layer

The system evaluates candidate responses against:

- safety and operating constraints;
- actuator limits;
- approved control ranges;
- predicted production impact;
- expected recovery time;
- model validity;
- required human approval.

The initial demonstrator should recommend actions rather than control the process directly.

### 6. Feedback and Audit Layer

Every episode should record:

```text
detected event
→ evidence used
→ model version
→ prediction
→ candidate actions
→ constraints checked
→ recommendation
→ simulated or observed response
→ final outcome
→ prediction error
```

---

## What the Demonstration Can Prove

A public reference demonstrator can show:

- why time-series data needs process context;
- how a twin maintains state across time;
- how physics, rules, and machine learning can work together;
- how model validity and uncertainty affect recommendations;
- how what-if calculation differs from anomaly detection;
- how decisions and outcomes become traceable.

The same pattern can later be mapped to tire manufacturing:

```text
Tennessee Eastman disturbance
→ tire-process deviation

chemical operating point
→ product, material, machine, and recipe configuration

process-quality prediction
→ uniformity, dimensional, cure, or inspection outcome

manipulated variable
→ permitted process adjustment

simulated recovery
→ validated what-if process response
```

---

## What the Demonstration Cannot Prove

Public benchmark data cannot establish that the architecture is production-ready for a real factory.

It usually does not capture the full difficulty of:

- undocumented process changes;
- inconsistent asset identifiers;
- calibration drift and failed sensors;
- maintenance, material genealogy, and product revisions;
- cybersecurity and access control;
- integration with historians, MES, PLM, LIMS, and quality systems;
- organizational ownership and regulatory validation;
- long-term model monitoring and financial return.

The correct claim is therefore:

> The demonstrator proves the architecture and explains the decision loop. It does not prove plant deployment, model transferability, or business value.

---

## Advantages of Using Public Data

### Reproducibility

Readers can inspect the data, run the code, challenge assumptions, and compare alternative models.

### No Confidentiality Barrier

The complete workflow can be published without exposing product designs, process windows, production rates, or internal quality information.

### Known Disturbances

Benchmarks often include labeled conditions that make diagnosis and evaluation easier to explain.

### Educational Clarity

The architecture can be taught without first solving enterprise data-access problems.

### Reusable Test Environment

New monitoring methods, agents, rules, and interfaces can be tested against the same reference process.

---

## Disadvantages and Risks

### False Realism

A polished user interface can make a limited benchmark appear more industrially complete than it is.

### Benchmark Overfitting

A model may perform well because the faults, operating conditions, and data-generation assumptions are already known.

### Missing Human Workflow

Public datasets rarely include why an operator acted, what alternatives were rejected, or how an engineering approval was reached.

### Weak Domain Transfer

Success on a chemical benchmark does not prove success for mixing, extrusion, tire building, curing, inspection, or vehicle testing.

### Digital-Twin Label Inflation

If the project stops at streaming data and displaying a prediction, it reinforces confusion rather than teaching the concept.

---

## A Practical Build Sequence

The demonstrator should be developed in five increments:

```text
Version 1: Replay and contextualize the process data
Version 2: Reconstruct state and detect deviations
Version 3: Predict short-horizon process outcomes
Version 4: Compare constrained interventions
Version 5: Record decisions, outcomes, and model error
```

Only after Version 5 should an AI agent be added.

The agent could then answer questions such as:

- What changed?
- Which evidence supports the diagnosis?
- Is the current condition inside the model’s validated range?
- What actions are permitted?
- What does the simulator predict for each action?
- Which prior events are similar?
- What happened after the previous recommendation?

This keeps the language model in an appropriate role: interacting with the twin rather than pretending to be the twin.

---

## Sharp Takeaway

Public data is sufficient to demonstrate the logic of a process digital twin, but not if the project is only a model and dashboard.

The demonstration must make the complete chain visible:

```text
data
→ context
→ process state
→ prediction
→ constrained decision
→ intervention
→ outcome
→ updated knowledge
```

> The goal is not to claim that an open benchmark is a factory. The goal is to make the architecture of industrial learning concrete, inspectable, and reproducible.

---

## Sources and Public Resources

- J. J. Downs and E. F. Vogel, [“A Plant-Wide Industrial Process Control Problem,” *Computers & Chemical Engineering*, 1993](https://doi.org/10.1016/0098-1354(93)80018-I).
- Harvard Dataverse, [Additional Tennessee Eastman Process Simulation Data](https://doi.org/10.7910/DVN/6C3JR1).
- ISO, [ISO 23247-1:2021 — Digital twin framework for manufacturing](https://www.iso.org/standard/75066.html).
- NASA Prognostics Center of Excellence, [C-MAPSS Jet Engine Simulated Data](https://data.nasa.gov/dataset/cmapss-jet-engine-simulated-data).
- Singapore University of Technology and Design iTrust, [SWaT and Other Public Cyber-Physical-System Datasets](https://www.sutd.edu.sg/itrust/itrust-labs/datasets/).
- Open Source Modelica Consortium, [OpenModelica](https://openmodelica.org/).
