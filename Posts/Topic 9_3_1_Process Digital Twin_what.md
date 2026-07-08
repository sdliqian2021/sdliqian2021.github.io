# What Is a Process Digital Twin?

**Purpose:** Establish a precise, practical definition of a process digital twin before discussing its role in Industrial AI.

**Core thesis:** A process digital twin is not a dashboard, a simulation, or a machine-learning model. It is a continuously updated and executable representation of an industrial process that connects process state, history, models, constraints, decisions, and measured outcomes.

---

## Digital Twin Is Becoming Too Broad to Be Useful

The phrase “digital twin” is now applied to many different things:

- a three-dimensional visualization of a factory;
- a dashboard displaying live sensor signals;
- a physics-based simulation;
- a machine-learning model;
- a digital record of an asset;
- a complete virtual representation of a production system.

Each may be useful, but calling all of them digital twins removes the distinctions engineers need when designing real systems.

The first question should therefore not be:

> How do we build a digital twin?

It should be:

> What physical or operational decision must this twin improve?

This question changes the unit of analysis. Instead of attempting to reproduce an entire factory digitally, the organization identifies a bounded process, its important states, and the decisions that determine its outcome.

---

## Product, Asset, and Process Twins Are Different

A **product digital twin** represents the engineering definition and expected behavior of a product. It may include geometry, materials, requirements, simulations, configurations, and validation evidence.

An **asset digital twin** represents a specific physical instance in operation. It may track usage, condition, maintenance history, degradation, and remaining life.

A **process digital twin** represents how work transforms inputs into an outcome.

That process may be physical:

```text
raw material
→ mixing
→ forming
→ curing
→ inspection
→ finished product
```

It may also be an engineering process:

```text
requirements
→ design
→ simulation
→ prototype
→ test
→ validation
→ design update
```

The process twin does not merely describe equipment. It represents the state transitions, dependencies, rules, interventions, and evidence that connect one stage to the next.

---

## A Practical Definition

> A process digital twin is a continuously updated, executable representation of an industrial process that connects its current state, operating history, inputs, models, constraints, decisions, and measured outcomes.

Every part of this definition matters.

### Continuously Updated

The twin must reflect the relevant state of the real process. “Continuous” does not always mean millisecond streaming. A laboratory workflow may update once per test, while a curing process may update many times per second.

The required update rate is determined by the decision latency.

### Executable

The twin must support some form of computation. It should be able to estimate an unmeasured state, evaluate a rule, predict an outcome, compare alternatives, or run a what-if scenario.

A static process map is useful documentation, but it is not yet an operational twin.

### Process Context

A temperature value has little meaning by itself. Its interpretation may depend on:

- the product and revision;
- the material batch;
- the machine and tool;
- the process stage;
- the operating recipe;
- the previous state;
- the sensor location and calibration;
- the environmental condition.

The process twin organizes signals around these relationships.

### Constraints

Industrial decisions operate inside safety limits, equipment capabilities, product specifications, engineering rules, regulatory requirements, and approval authorities.

A prediction without these constraints is not enough for operational use.

### Decisions and Outcomes

The twin must connect information to an action or recommendation and then capture what happened afterward.

Without this final connection, the organization has monitoring—not learning.

---

## The Minimum Process-Twin Architecture

A useful process twin contains at least six layers:

```text
1. Identity and configuration
   What product, batch, machine, model, recipe, and revision are involved?

2. Process state
   What is happening now, and which stage is active?

3. History and lineage
   What happened previously, and how did the current state arise?

4. Behavioral models
   What should happen, what is likely to happen, and with what uncertainty?

5. Rules and decision logic
   What actions are permitted, required, or prohibited?

6. Outcome feedback
   What action was taken, and did it improve the result?
```

The behavioral model may be physics-based, data-driven, rule-based, or hybrid. A digital twin does not require the most sophisticated model available. It requires a model that is valid for the decision being supported.

---

## Example: A Tire-Curing Process Twin

Consider a tire-curing process.

A conventional dashboard may display mold temperature, bladder pressure, cure time, alarms, and press status. This can help an operator see what is happening.

A process digital twin connects those signals to the product and decision context:

```text
material batch
→ green-tire configuration
→ tire specification and revision
→ press and mold identity
→ cure recipe
→ temperature and pressure history
→ estimated cure state
→ process deviation
→ inspection and uniformity results
→ disposition decision
→ feedback to the process model
```

The twin might estimate whether the material reached the required cure state throughout critical regions. It could identify that a temperature deviation matters for one construction but remains inside the validated process window for another. It could recommend inspection, recipe adjustment, or engineering review.

The decision could remain completely human-controlled. The system still qualifies as a process twin if it maintains the state, runs valid models, provides traceable decision support, and learns from the observed outcome.

Autonomy is optional. A closed information-and-learning loop is not.

---

## What a Process Digital Twin Is Not

The following distinctions are important:

```text
Dashboard ≠ process digital twin
Historical database ≠ process digital twin
Simulation model ≠ process digital twin
Machine-learning prediction ≠ process digital twin
3D visualization ≠ process digital twin
```

Each can be a component of the twin.

A dashboard becomes part of a twin when it displays contextualized process state and supports a governed response.

A simulation becomes part of a twin when it is synchronized with the relevant process configuration, updated or calibrated using observations, and used inside a decision loop.

A machine-learning model becomes part of a twin when its inputs, validity domain, uncertainty, recommended response, and outcome are managed as part of the process.

The distinction is architectural, not cosmetic.

---

## Start with the Decision, Not the Factory

Attempting to build a complete factory twin often produces a large integration program with an unclear operational payoff.

A more disciplined starting point is:

```text
Decision:
What recurring decision creates measurable value or risk?

Boundary:
Which process stages influence that decision?

State:
What must be known when the decision is made?

Models:
What calculation or prediction improves the decision?

Constraints:
What rules and validation limits apply?

Feedback:
How will the outcome update future decisions?
```

This approach gives the twin a testable purpose. It also prevents the project from becoming an attempt to collect every available data stream.

---

## A Simple Qualification Test

Before calling a system a process digital twin, ask whether it can answer:

1. What is happening now?
2. How did the process reach this state?
3. What outcome is likely?
4. What intervention is possible?
5. What constraints and validity limits apply?
6. Who is authorized to decide?
7. Did the intervention improve the outcome?

If the system answers only the first question, it is probably a monitoring system.

If it answers the first three, it may be a strong analytical system.

When it connects all seven in a traceable loop, it begins to function as a process digital twin.

---

## Sharp Takeaway

A process digital twin should not be judged by how completely it reproduces a factory on a screen.

It should be judged by whether it creates a valid, traceable, and continuously improving connection between:

```text
process state
→ prediction
→ decision
→ intervention
→ measured outcome
→ updated knowledge
```

> If a proposed digital twin cannot identify the decision it improves and the feedback it captures, is it really a twin—or only another way to visualize industrial data?

---

## Sources and Further Reading

- ISO, [ISO 23247-1:2021 — Digital twin framework for manufacturing](https://www.iso.org/standard/75066.html).
- J. J. Downs and E. F. Vogel, [“A Plant-Wide Industrial Process Control Problem,” *Computers & Chemical Engineering*, 1993](https://doi.org/10.1016/0098-1354(93)80018-I).
- Modelica Association, [Modelica — an open language for modeling complex physical systems](https://modelica.org/).
- Open Source Modelica Consortium, [OpenModelica](https://openmodelica.org/).
