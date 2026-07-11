# Controlled Systems for industiral AI

_Last updated: 2026-07-09 12:40 America/New_York (UTC-04:00)_

Here we discuss the three steps to build the industrial AI, which must be a controlled AI system. 

## Step 1: Pick one workflow, not “AI transformation”

The better starting point is one specific workflow where AI can create measurable operational value. **it is easy to demostrate the values of digital twin, but not easy to demonstrate the benefits of adding AI, my whole point is without a proper digital twin, there is almost no benefits of introducing AI (industrial AI), to be honest, I am not sure if tire wear performane monitoring is a good choice here, but is something closest to me**

Examples include:

- tire wear performance monitoring
- simulation result comparison


The workflow should have measurable value, such as:

- fewer engineering hours
- faster test-cycle completion
- fewer repeated tests
- better data traceability
- faster report generation
- fewer manual errors
- better use of historical knowledge

A controlled AI system should be judged by workflow improvement, not by how impressive the demo looks.

---

## Step 2: Build the ontology or digital-twin context

The second step is to organize the company’s operational knowledge into a structure the AI system can use.

This is where many companies fail. They have data, but the data is fragmented across reports, spreadsheets, databases, PLM systems, test systems, SharePoint folders, simulation tools, and expert memory.

The AI system needs a domain context layer.

In industrial AI, this layer can be an ontology, a knowledge graph, or a digital twin.

For tire engineering, the ontology may include:

```text
Tire
 ├── size
 ├── construction
 ├── compound
 ├── tread pattern
 ├── stiffness data
 ├── footprint data
 ├── lab abradability
 ├── road-wear result
 ├── vehicle application
 ├── simulation model
 └── validation status

Vehicle
 ├── platform
 ├── axle load
 ├── alignment
 ├── duty cycle
 ├── route
 └── sensor data

Test
 ├── protocol
 ├── date
 ├── location
 ├── engineer
 ├── raw data
 ├── processed data
 ├── quality flag
 └── approved conclusion
```

The LLM should not guess what the company’s data means. It should retrieve information through this structured operational context.

This is also where the company’s competitive advantage begins to appear. The foundation model may be generic, but the ontology is company-specific.

---

## Step 3: Design the controlled execution boundary

This is the core design step.

A controlled AI system must define how work is divided among the LLM, the hardcoded system, the human, and the model infrastructure.

```text

Hardcoded system = rules, permissions, tools, validation, execution, and logging

Human = judgment, accountability, and high-consequence approval

LLM = reasoning, language, synthesis, and interaction

- Model gateway = model selection based on risk, cost, latency, privacy, and data sensitivity

- Permissioned APIs = controlled tool access based on model choice, user role, data sensitivity, and task risk
```

This step includes four related design decisions:

```text
1. Classify the task by risk level.

2. Decide what the LLM, hardcoded system, and human are each allowed to do.

3. Route the task to the right model through a model gateway.

4. Expose tools to the selected model only through permissioned APIs.
```

These should not be treated as separate design problems. They are one system-design problem:

**Who is allowed to do what, using which model, under what conditions, with what evidence, and with what approval?**

The model gateway should come before permissioned APIs because the selected model determines the trust boundary.

An external frontier model should not receive the same tool access as a local or enterprise-controlled model. A public-data model call may only access sanitized information. A local model running inside the company boundary may be allowed to access more sensitive internal data, but still only through controlled APIs.

A useful pattern is:

```text
Task risk level
→ human / system / LLM responsibility boundary
→ model gateway selects the allowed model
→ permissioned APIs expose only the tools and data allowed for that model, user, and task
```

### 3.1 Classify tasks by risk level

The responsibility boundary depends on the consequence level of the task.

```text
Low-risk task:
LLM can summarize, classify, draft, or organize automatically.

Medium-risk task:
LLM can recommend or draft, but human review is required.

High-risk task:
LLM can provide evidence and options, but hardcoded rules and human approval control the final decision.

Safety-critical task:
LLM can support analysis or explanation, but validated deterministic models and human authority control the action.
```

For example:

| Risk level | Example | LLM role | Hardcoded system role | Human role |
|---|---|---|---|---|
| Low | Summarize a public paper | Summarize and organize | Optional source check | Usually not needed |
| Medium | Draft an internal test report | Draft and explain | Check source, format, and data quality | Review before use |
| High | Recommend changing a test plan | Provide evidence and options | Validate inputs, enforce rules, log decision | Approve final action |
| Safety-critical | Control vehicle braking or factory equipment | Explain or support analysis only | Deterministic validated control | Own final authority |

### 3.2 Decouple the LLM, hardcoded system, and human

The LLM should not become the control system.  
The hardcoded software should not try to imitate flexible reasoning.  
The human should not be forced to manually do work that software can reliably automate.

A good controlled AI system assigns each responsibility to the right layer.

The LLM should handle:

- natural-language understanding
- summarization
- comparison
- synthesis
- hypothesis generation
- report drafting
- explanation
- user interaction

The hardcoded system should handle:

- permission checks
- data access
- deterministic calculations
- validated simulation execution
- tool calling
- data-quality rules
- logging
- audit trails
- cost controls
- safety constraints
- approval workflow enforcement

The human should handle:

- judgment
- accountability
- exception handling
- technical approval
- business approval
- safety-sensitive decisions
- final signoff for high-consequence actions

### 3.3 Use a model gateway, not a single hardwired model

The company should not tie every workflow to one model provider.

A model gateway routes tasks based on:

- risk level
- data sensitivity
- cost
- latency
- required reasoning quality
- privacy requirement
- deployment environment
- regulatory or customer constraint

For example:

```text
Public information task
→ external frontier model

Internal but non-sensitive task
→ enterprise cloud model

Confidential engineering task
→ local open-weight model, private cloud model, or on-prem model

Routine structured task
→ smaller cheaper model

Domain-specific technical task
→ fine-tuned model, adapter-based model, or local domain model

High-risk decision task
→ LLM can assist, but hardcoded validation and human approval are required

Safety-critical task
→ LLM cannot directly act
```

The model gateway makes the model replaceable.

The company should own the architecture, not just subscribe to one model. The LLM is a component inside the system, not the system itself.

#### Where a local open-weight LLM fits

A local open-weight LLM fits inside the model gateway.

It is useful when the task involves:

- confidential engineering data
- internal test results
- proprietary simulation results
- compound or construction information
- customer-sensitive fleet data
- cost-sensitive high-volume tasks
- routine summarization or classification
- domain-specific terminology
- private RAG over internal documents

A local model gives the company stronger control over:

```text
Data boundary
Deployment environment
Logging
Access control
Model version
Fine-tuning / adapters
Cost for repeated tasks
Integration with internal tools
```

But a local model does not automatically make the system controlled.

A weak architecture with a local model is still weak:

```text
Internal data + local chatbot
```

That is not enough.

The local model still needs to operate inside:

```text
Ontology / digital twin context
+ risk classification
+ hardcoded rules
+ permissioned APIs
+ logging
+ human approval
```

The local model protects data better, but the hardcoded boundary remains the real control system.

### 3.4 Expose tools only through permissioned APIs

The LLM becomes useful when it can call tools, but those tools must be controlled by the hardcoded system.

The LLM should not freely access databases, simulations, production systems, or official records. It should call approved APIs.

Examples:

```text
read_test_data(test_id)
compare_model_prediction(tire_id, condition_id)
run_simulation(template_id, parameter_set)
generate_report(section_type, source_ids)
search_prior_validation_cases(tire_size, vehicle_platform)
create_engineering_review_ticket(issue_type, evidence_ids)
```

Each API should include:

- input schema
- permission check
- data-sensitivity rule
- validation logic
- logging
- rollback mechanism if needed
- human approval rule if needed

The API permissions should depend on:

- selected model
- user role
- task risk level
- data sensitivity
- action consequence
- regulatory or customer constraint

For example:

```text
Public information task
→ external frontier model
→ public search / citation APIs only

Internal but non-sensitive task
→ enterprise cloud model
→ restricted internal document APIs

Confidential engineering task
→ local or private model
→ approved test-data and simulation APIs

High-risk engineering task
→ controlled model
→ read-only APIs plus human approval workflow

Safety-critical task
→ LLM cannot directly act
→ deterministic validated system and human authority control the action
```

The key pattern is:

```text
The LLM decides what information or tool may be useful.
The model gateway decides which model is allowed to reason over the task.
The hardcoded system decides whether the tool call is allowed.
The permissioned API performs the actual operation.
The human approves when the risk level requires it.
```

### 3.5 Example in tire engineering

```text
Engineer asks:
“Compare the predicted wear performance of Tire A and Tire B on Model Y.”



Hardcoded system role:
Check permissions, retrieve approved test data, run validated wear algorithms, enforce data-quality rules, calculate error metrics, expose approved tool APIs, route model calls, and log all actions.

LLM role:
Understand the question, retrieve relevant context, summarize differences, identify missing data, and draft the comparison.

- Model gateway:Choose the proper model based on data sensitivity and task risk. Public background information may use an external model. Confidential tire test data may require a local or enterprise-controlled model.

- Permissioned API:
Expose only the approved test-data, simulation, comparison, and reporting tools that are allowed for the selected model, user, and risk level.

Human role:
Review the evidence, judge whether the conclusion is technically sound, and approve the final recommendation.
```

This is the real controlled-AI boundary.
- The hardcoded system owns the control logic.  
- The LLM is placed in the right position: The model gateway controls model exposure; Permissioned APIs control tool access.  
- The human owns final accountability where consequence requires it.

---

## Entrepreneurial opportunity — vertical AI ontology builders

The most attractive entrepreneurial opportunity is not building another generic chatbot. It is building **vertical AI ontology systems** for specific industries.

Many companies already have valuable data, but they do not have a usable operational ontology. Their data is scattered across documents, databases, spreadsheets, engineering tools, test systems, and expert memory.

A startup could help companies convert fragmented domain knowledge into an AI-ready operational structure.

For industrial companies, this means building the layer that connects:

```text
Domain objects
+ historical data
+ engineering rules
+ test results
+ simulation models
+ workflow context
+ human approval logic
```

For tire engineering, a vertical AI ontology could connect:

```text
Tire specifications
+ compound data
+ tread patterns
+ simulation models
+ test protocols
+ vehicle platforms
+ road-wear results
+ fleet duty cycles
+ claims data
+ validation status
+ approved conclusions
```

This ontology becomes the foundation for controlled AI agents.

Instead of asking a generic chatbot:

```text
“Why did this tire wear faster?”
```

The engineer could ask a controlled AI system:

```text
“Compare this tire’s wear result against similar compounds, vehicle platforms, routes, lab abradability, footprint data, and historical validation cases. Show the evidence and identify the most likely contributing factors.”
```

The value is not just the answer. The value is that the answer is grounded in the company’s own structured knowledge, permission rules, tools, and engineering workflow.

This is a strong opportunity because every industrial sector has its own complex domain objects and decision logic.

Examples include:

- tire engineering ontology
- battery testing ontology
- automotive validation ontology
- manufacturing quality ontology
- fleet maintenance ontology
- industrial safety ontology
- lab test management ontology
- supply chain risk ontology

The company that owns the ontology owns the workflow context.  
The company that owns the workflow context controls how AI creates value.  
That is where enterprise AI becomes defensible.
