# Why Industrial AI Struggles to Scale

_Last updated: 2026-07-09 12:40 America/New_York (UTC-04:00)_

**Purpose:** This note frames the central problem of current Industrial AI and the main reasons behind it.

**Core thesis:** Industrial AI can perform well in a controlled proof of concept, but it often fails to scale into production and deliver repeatable ROI. The scaling gap is the visible problem. The deeper reasons are weak industrial data foundations, insufficient trust for operational use, and the fact that industrial systems evolve over time.

---

## Main Problem: Proof of Concept Does Not Become Production Value

Industrial AI is often easier to prove in a bounded experiment than to sustain in real operations. A proof of concept can use a selected dataset, a stable operating window, expert support, and a narrow success metric. Production requires the AI system to work across messy data flows, changing equipment and materials, plant workflows, frontline users, risk controls, and business metrics.

McKinsey's 2025 AI survey reports broad AI adoption but says only about one-third of respondents report scaling AI programs across their organizations.[1] In manufacturing, this matters because an AI model has value only when it changes real decisions and produces measurable results such as lower downtime, lower scrap, better yield, safer maintenance, or better cost performance.

**Concrete example.** Novelis already had predictive-analytics use cases, but Deloitte reports that it lacked a strategy to scale them across manufacturing facilities before creating a Plant of the Future roadmap.[8]

**Analysis.** The example shows the difference between having industrial AI use cases and having an industrial AI capability. Scaling requires more than model success: it requires repeatable deployment, workflow ownership, data access, governance, and a value case that survives outside the pilot environment.

---

## Three Root Reasons

## 1. Weak Industrial Data and System Foundations

Industrial AI depends on data that are reliable, contextualized, and connected to the physical process. In practice, industrial data may be missing, noisy, poorly labeled, trapped in legacy systems, or detached from the asset, batch, material, operating condition, or maintenance event that gives the data meaning.

The Manufacturing Leadership Council reports that 65% of manufacturers lack the right data for AI applications and 62% cite unstructured or poorly formatted data.[2] PwC reports that poor data quality has affected value from digital initiatives for many operations leaders.[3] MIT Sloan similarly argues that industrial AI needs the right data at the right time, not simply more data.[4]

**Concrete example 1.** McKinsey describes an iron ore company building an optimizer for a palletization process that discovered a critical project sensor had been broken for six months before the work started.[9]

**Analysis.** This is a basic data-readiness failure. The optimizer may be mathematically strong, but it cannot learn from a critical signal that was never measured correctly.

**Concrete example 2.** Belden describes its Richmond factory as a brownfield environment with machines and devices of different vintages and makes; its predictive-maintenance work first had to connect equipment and capture contextualized OT data without replacing all legacy equipment.[10]

**Analysis.** Industrial AI cannot scale when every asset and plant requires a new data rescue project. Fragmented IT/OT systems turn deployment effort into integration effort.

**Concrete example 3.** At the same Belden plant, a predictive-maintenance pilot collected about 300 GB of data from 150 sensors and used those data to identify at-risk components such as abnormal vibration linked to belt-alignment issues.[10]

**Analysis.** Data volume becomes useful only when it is converted into decision-relevant information. The value was not collecting sensor streams; it was producing a maintenance finding someone could act on.

---

## 2. Insufficient Trust for Operational Use

Industrial AI must be trusted before it can influence production, maintenance, quality, safety, or engineering decisions. Trust is broader than model accuracy. It includes validation, explainability, reliability, cybersecurity, intellectual-property protection, human acceptance, and clear authority boundaries between AI recommendations and human decisions.

NIST's AI Risk Management Framework treats trustworthiness as a lifecycle requirement for AI systems.[5] NIST's industrial AI evaluation work also asks whether AI tools reduce manufacturing risk and create system-level value, not only whether the model looks accurate in isolation.[11]

**Concrete example 1.** Siemens reports that false calls from automated optical inspection in PCB manufacturing can accumulate into alarm fatigue for human inspectors and increase inspection mistakes.[13]

**Analysis.** Trust can fail at the human-machine interface. If AI or automation repeatedly burdens users with false alarms, operators learn to discount it even when a real issue appears.

**Concrete example 2.** Siemens positions its Industrial Copilot for tasks such as maintenance configuration and remediation, while Reuters reports that manufacturers have expressed concern about response accuracy and hallucinations in generative AI rollouts.[6][12]

**Analysis.** In industrial work, a fluent answer is not enough. If generated guidance can affect troubleshooting or maintenance, users need approved knowledge sources, evidence, review rules, and escalation when uncertainty is high.

**Concrete example 3.** In 2023, Samsung semiconductor staff reportedly entered sensitive source code and in-development semiconductor information into ChatGPT while seeking work help.[14]

**Analysis.** Trust also includes governance. Industrial AI cannot scale responsibly if using it exposes proprietary code, process knowledge, yield evidence, or operational data outside approved controls.

**Concrete example 4.** NIST's industrial AI work explicitly includes human-agent communication and human-in-the-loop learning, and its AI-enhanced manufacturing monitoring work emphasizes operator interactivity and input in intelligent automation.[17][18]

**Analysis.** Production use requires authority boundaries. A plant must define when AI may observe, recommend, schedule, change parameters, stop a process, or require human approval.

---

## 3. Industrial Systems Evolve

Industrial AI is deployed into physical systems that change. Machines wear, sensors drift, suppliers and materials change, methods are revised, products evolve, operators intervene, and operating conditions shift. A model that performed well in a controlled proof of concept may therefore become inaccurate, physically weak, or unsafe in production.

NIST notes that industrial AI data have to cover real operating scenarios and physical understanding, not only convenient historical samples.[7] This problem grows after deployment because the system being modeled does not stay fixed.

**Concrete example 1.** Omron describes manufacturing defect-prediction use cases where 4M changes - man, machine, material, and method - can induce concept drift that must be detected separately from defect signs.[15]

**Analysis.** This is why production behavior cannot be assumed to match the pilot dataset. A change in people, equipment, material, or method can shift the process and quietly invalidate model assumptions.

**Concrete example 2.** In tool-wear and remaining-useful-life prediction, recent physics-informed work explicitly models wear dynamics and interpretable physical aspects instead of relying only on a black-box fit to historical data.[16]

**Analysis.** Evolving systems still obey engineering constraints. Scaling needs models that remain physically meaningful under wear, changing loads, new operating regimes, and extrapolation beyond the proof-of-concept data.

---

## Short Synthesis

The main problem of current Industrial AI is the gap between **proof-of-concept performance** and **production-scale ROI**.

That gap is driven by three root problems:

1. **Data:** industrial data are often unreliable, fragmented, and insufficiently contextualized.
2. **Trust:** AI outputs must be valid, secure, understandable, governable, and usable by people in real workflows.
3. **Evolving systems:** physical assets, materials, processes, and operating conditions change, so model validity cannot be assumed to persist.

This framing keeps scaling as the central concern while explaining why scaling fails. An Industrial AI system does not scale just because its algorithm works in a controlled environment; it scales when data, trust, and engineering validity survive production reality.

---

## References

[1] McKinsey & Company. (2025). *The State of AI: Global Survey 2025.* https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai

[2] Manufacturing Leadership Council / National Association of Manufacturers. (2025). *Shaping the AI-Powered Factory of the Future.* https://manufacturingleadershipcouncil.com/wp-content/uploads/2025/05/Shaping-the-AI-Powered-Factory-of-the-Future-Report.pdf

[3] PwC. (2026). *PwC's 2026 Digital Trends in Operations Survey.* https://www.pwc.com/us/en/services/consulting/business-transformation/digital-supply-chain-survey.html

[4] MIT Sloan School of Management. (2025). *6 Steps to Succeeding with Industrial AI.* https://mitsloan.mit.edu/ideas-made-to-matter/6-steps-to-succeeding-industrial-ai

[5] National Institute of Standards and Technology. (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0).* https://www.nist.gov/itl/ai-risk-management-framework

[6] Reuters. (2024). *Manufacturers slow Gen AI rollout on rising accuracy concerns, says study.* https://www.reuters.com/technology/artificial-intelligence/manufacturers-slow-gen-ai-rollout-rising-accuracy-concerns-says-study-2024-07-10/

[7] National Institute of Standards and Technology. (2025). *How to Find the Right Balance of Data for Your Industrial AI System.* https://www.nist.gov/blogs/manufacturing-innovation-blog/how-find-right-balance-data-your-industrial-ai-system

[8] Deloitte. *Novelis: Predictive Analytics in Manufacturing.* https://www.deloitte.com/us/en/services/consulting/case-studies/predictive-analytics-in-manufacturing.html

[9] McKinsey & Company. (2023). *Clearing Data Quality Roadblocks: Unlocking AI in Manufacturing.* https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/clearing-data-quality-roadblocks-unlocking-ai-in-manufacturing

[10] Belden. (2023). *Laying the Foundation for Predictive Maintenance in Manufacturing.* https://www.belden.com/knowledge-hub/resources/case-studies/laying-the-foundation-for-predictive-maintenance-in-manufacturing

[11] National Institute of Standards and Technology. (2022). *Are Industrial AI Tools Worth It? NIST Researchers Offer an Evaluation Procedure.* https://www.nist.gov/news-events/news/2022/02/are-industrial-ai-tools-worth-it-nist-researchers-offer-evaluation

[12] Siemens. *Siemens Industrial Copilot.* https://www.siemens.com/global/en/products/automation/topic-areas/industrial-ai/industrial-copilot.html

[13] Siemens. (2023). *When Automated Processes Actually Slow Down Production.* https://blogs.sw.siemens.com/opcenter/when-automated-processes-actually-slow-down-production/

[14] The Register. (2023). *Samsung Reportedly Leaked Its Own Secrets Through ChatGPT.* https://www.theregister.com/2023/04/06/samsung_reportedly_leaked_its_own/

[15] OMRON. (2025). *Proposal of Concept Drift Detection in Factory Automation Domain.* https://www.omron.com/global/en/technology/omrontechnics/vol57/003.html

[16] Blume, S., et al. (2025). *Physics-informed symbolic regression for tool wear and remaining useful life predictions in manufacturing.* Journal of Manufacturing Systems. https://doi.org/10.1016/j.jmsy.2025.03.023

[17] National Institute of Standards and Technology. *Industrial Artificial Intelligence Management and Metrology (IAIMM).* https://www.nist.gov/programs-projects/industrial-artificial-intelligence-management-and-metrology-iaimm

[18] National Institute of Standards and Technology. (2024). *NIST Explores AI-Enhanced Monitoring in Manufacturing Processes.* https://www.nist.gov/blogs/manufacturing-innovation-blog/nist-explores-ai-enhanced-monitoring-manufacturing-processes
