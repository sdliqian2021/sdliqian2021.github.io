---
layout: default
title: "工业 AI 为什么难以规模化：从概念验证到生产价值"
description: "分析工业 AI 从概念验证走向生产时遇到的数据、信任与系统演变问题，以及“死数据”如何阻碍规模化。"
content_type: essay
display_order: 40
published: 2026-09-21
updated: 2026-09-21
topics:
  - 工业 AI
  - AI 规模化
  - 数据治理
permalink: /posts/08-industrial-ai-scaling-gap.html
nav: essays
page_class: article-page
---

# 工业 AI 为什么难以规模化：从概念验证到生产价值

_最后更新：2026-09-21_

**目的：** 本文梳理当前工业人工智能的核心问题及其背后的主要原因。

**核心论点：** 工业人工智能可以在受控的概念验证（PoC）中表现良好，却常常无法规模化进入生产环境并带来可重复的投资回报（ROI）。规模化鸿沟是表面可见的问题。更深层的原因在于薄弱的工业数据基础、不足以支撑运营使用的信任，以及工业系统本身会随时间演变这一事实。

---

## 主要问题：概念验证没有转化为生产价值

工业人工智能往往在有边界的实验中容易证明，却难以在真实运营中持续。概念验证可以使用精选的数据集、稳定的运行窗口、专家的支持和狭窄的成功指标。而生产环境要求人工智能系统在杂乱的数据流、不断变化的设备与材料、工厂工作流、一线用户、风险控制和业务指标之间都能正常工作。

麦肯锡 2025 年的人工智能调查报告显示，人工智能已被广泛采用，但只有约三分之一的受访者表示已在整个组织内规模化推广人工智能项目。[【1】](#ref-1) 在制造业，这一点尤为重要，因为一个人工智能模型只有在改变了真实决策、并产生诸如更少停机时间、更少废品、更高良率、更安全的维护或更好的成本表现等可衡量结果时，才算有价值。

**具体案例。** Novelis 早已拥有预测分析类的用例，但据德勤报告，在制定“未来工厂”（Plant of the Future）路线图之前，该公司缺乏把这些用例推广到各制造基地的策略。[【8】](#ref-8)

**分析。** 这个例子说明了“拥有工业人工智能用例”与“拥有工业人工智能能力”之间的差别。规模化需要的不只是模型成功：它需要可重复的部署、工作流的归属、数据访问、治理，以及一个在试点环境之外依然成立的价值论证。

---

## 三个根本原因

### 1. 薄弱的工业数据与系统基础

工业人工智能依赖于可靠、具备上下文、并与物理过程相连接的数据。实际中，工业数据可能缺失、有噪声、标注不良、被困在遗留系统里，或者与赋予数据意义的资产、批次、材料、运行工况或维护事件相脱节。

制造业领导力委员会（Manufacturing Leadership Council）报告称，65% 的制造商缺乏适用于人工智能应用的合适数据，62% 提到数据是非结构化的或格式不佳。[【2】](#ref-2) 普华永道报告称，数据质量差已影响了许多运营负责人从数字化举措中获取价值。[【3】](#ref-3) 麻省理工斯隆管理学院同样指出，工业人工智能需要的是在正确的时间获得正确的数据，而不仅仅是更多的数据。[【4】](#ref-4)

**具体案例 1。** 麦肯锡描述了一家铁矿石公司为球团工艺构建优化器的经历：在工作启动之前，一个关键的项目传感器已经损坏了六个月，直到项目开始才被发现。[【9】](#ref-9)

**分析。** 这是一个基本的数据就绪度失败。优化器在数学上可能很强，但它无法从一个从未被正确测量的关键信号中学习。

**具体案例 2。** Belden 将其里士满工厂描述为一个既有（棕地）工厂环境，机器和设备的年代与品牌各不相同；其预测性维护工作首先必须把设备连接起来，并在不更换全部遗留设备的前提下采集具备上下文的 OT 数据。[【10】](#ref-10)

**分析。** 如果每一项资产、每一座工厂都需要一个新的数据抢救项目，工业人工智能就无法规模化。碎片化的 IT／OT 系统会把部署工作变成集成工作。

**具体案例 3。** 在同一座 Belden 工厂，一个预测性维护试点从 150 个传感器采集了约 300 GB 的数据，并利用这些数据识别出了存在风险的部件，例如与皮带对中问题相关的异常振动。[【10】](#ref-10)

**分析。** 数据量只有在被转化为与决策相关的信息时才有用。价值不在于采集传感器数据流，而在于产出一个有人可以据此行动的维护发现。

---

### 2. 不足以支撑运营使用的信任

工业人工智能必须先获得信任，才能影响生产、维护、质量、安全或工程决策。信任的范围比模型准确率更广。它包括验证、可解释性、可靠性、网络安全、知识产权保护、人的接受度，以及人工智能建议与人类决策之间清晰的权限边界。

美国国家标准与技术研究院（NIST）的人工智能风险管理框架将可信性视为人工智能系统全生命周期的要求。[【5】](#ref-5) NIST 的工业人工智能评估工作也会追问：人工智能工具是否降低了制造风险、是否创造了系统层面的价值，而不只是模型孤立地看起来是否准确。[【11】](#ref-11)

**具体案例 1。** 西门子报告称，在 PCB 制造中，自动光学检测的误报会逐渐累积成人工检验员的告警疲劳，并增加检验错误。[【13】](#ref-13)

**分析。** 信任可能在人机界面处失效。如果人工智能或自动化反复用误报给用户增加负担，操作员就会学会忽视它，即便真正的问题出现时也是如此。

**具体案例 2。** 西门子将其 Industrial Copilot 定位于维护配置和故障修复等任务，而路透社报道称，制造商对生成式人工智能推广中的回答准确性和幻觉问题表达了担忧。[【6】](#ref-6)[【12】](#ref-12)

**分析。** 在工业工作中，一个流畅的回答是不够的。如果生成的指导可能影响故障排查或维护，用户就需要经过批准的知识来源、证据、审核规则，以及在不确定性较高时的上报机制。

**具体案例 3。** 2023 年，据报道三星半导体的员工在寻求工作帮助时，将敏感源代码和在研半导体信息输入了 ChatGPT。[【14】](#ref-14)

**分析。** 信任也包括治理。如果使用工业人工智能会把专有代码、工艺知识、良率证据或运营数据暴露在经批准的控制之外，它就无法负责任地规模化。

**具体案例 4。** NIST 的工业人工智能工作明确包含人与代理之间的沟通以及人在回路的学习，其 AI 增强型制造监控工作也强调智能自动化中操作员的交互性与输入。[【17】](#ref-17)[【18】](#ref-18)

**分析。** 生产使用需要权限边界。工厂必须定义人工智能在何时可以观察、建议、排程、更改参数、停止工艺，或者必须获得人工批准。

---

### 3. 工业系统会演变

工业人工智能被部署到不断变化的物理系统中。机器会磨损，传感器会漂移，供应商和材料会更换，方法会修订，产品会演进，操作员会干预，运行工况会变化。因此，一个在受控概念验证中表现良好的模型，在生产环境中可能变得不准确、物理上站不住脚，甚至不安全。

NIST 指出，工业人工智能的数据必须覆盖真实运行场景和物理认知，而不只是方便取得的历史样本。[【7】](#ref-7) 这个问题在部署之后会进一步加剧，因为被建模的系统不会保持不变。

**具体案例 1。** 欧姆龙（Omron）描述了制造缺陷预测的用例，其中 4M（人、机、料、法）的变化可能诱发概念漂移，而这种漂移必须与缺陷征兆分开检测。[【15】](#ref-15)

**分析。** 这就是为什么不能假定生产环境中的行为与试点数据集一致。人员、设备、材料或方法的变化都可能使工艺发生偏移，并悄无声息地使模型假设失效。

**具体案例 2。** 在刀具磨损和剩余使用寿命预测中，近期融入物理规律的研究明确地对磨损动力学和可解释的物理特性进行建模，而不是仅依赖对历史数据的黑箱拟合。[【16】](#ref-16)

**分析。** 演变中的系统依然遵守工程约束。规模化需要的模型，是在磨损、载荷变化、新的运行区间以及超出概念验证数据范围的外推情形下，仍然保持物理意义的模型。

---

---

## 问题已经超越了数据采集本身

工业人工智能领域有一句常见的说法：

> 人工智能模型不是主要问题。数据才是问题。

方向上这是对的，但已经不够深入。

现代机器早已产生大量的传感器读数、告警、生产记录、质量结果、维护历史、图像、工程文件、仿真输出和操作员观察。成熟的组织已经花了多年时间，把这些信息收集在历史数据库、制造系统、实验室数据库、工程资料库、云平台和数据湖中。

数据是存在的。然而其中的大部分，除了仪表盘、回顾性报告和精心准备的概念验证演示之外，几乎没有产生什么价值。

为什么？

因为这些数据是**死**的。

“死数据”并不是指错误或无用的数据。它指的是那些虽然被存储下来，却与赋予其运营意义的上下文、关系、工作流和决策相脱节的数据。

```text
采集到的数据未必是连接起来的数据。
连接起来的数据未必是具备上下文的数据。
具备上下文的数据未必是活数据。
活数据未必是可行动的数据。
```

只有当这条链完整闭合时，工业人工智能才能创造价值。

---

## 是什么让工业数据变成死数据？

### 1. 数据被组织边界分隔

设计、仿真、测试、制造、质量、维护、供应链和现场服务往往使用不同的系统。每个职能都可能拥有有用的数据，但这些系统并不理解彼此之间的关系。

一条试验结果可能没有关联到确切的设计版本。一次制造偏差可能没有与材料批次、机器状态、工艺设定和下游性能连接起来。现场失效可能无法回流到先于它们的仿真假设或设计决策。

组织拥有数据，却没有一份关于产品或流程如何演变的连贯记忆。

### 2. 数据没有共享的身份标识或上下文

工业记录之所以经常难以连接，是因为它们使用了不同的：

- 资产与产品标识符；
- 命名规范；
- 时间戳与采样率；
- 单位与坐标系；
- 版本与配置定义；
- 质量规则；
- 工艺边界；
- 模型版本。

人工智能模型无法从彼此脱节的表格中可靠地推断这些关系。在高级推理成为可能之前，组织需要一种受治理的方式来回答一些基本问题：

```text
这条记录描述的是哪个物理对象或流程？
它代表的是哪个版本、哪种状态、哪种运行工况？
在它之前和之后发生了什么？
哪些其他记录、模型和决策与它相关？
```

缺少这些上下文，更多的数据带来的可能是更多的模糊，而不是更多的智能。

### 3. 数据是被动的

许多工业数据平台的设计初衷主要是存储、可视化和检索信息。它们展示发生了什么，却没有嵌入到决定“接下来应该发生什么”的工作流中。

一个仪表盘也许能识别出异常趋势。但它未必能确定：

- 谁负责响应；
- 适用哪条工程规则；
- 信号是否有效；
- 应该运行哪个模型；
- 允许采取什么行动；
- 需要什么审批；
- 行动是否改善了结果。

如果数据不参与决策与反馈闭环，它就始终停留在观察层面，而非运营层面。

### 4. 数据不知道自己的关系

工业性能是由关系创造的：

```text
材料 + 设计 + 工艺 + 机器 + 环境 + 使用 = 结果
```

传统数据库可能存储了每一个要素，却丢失了把它们连接起来的因果结构和时间结构。这在工程领域尤为有害，因为价值往往不在于某一个变量，而在于理解配置、条件、干预和结果之间如何相互作用。

缺失的那一层并不只是又一个数据库。它是关于系统及其关系的运营模型。

---

## 为什么概念验证往往看起来比生产系统更好

一个小型的工业人工智能概念验证之所以能够成功，是因为有一支专职团队手工重建了缺失的上下文。团队挑选干净的数据集、对齐时间戳、解决标识符问题、排除无效运行工况、访谈领域专家，并定义一个狭窄的目标。

模型看起来成功了，是因为人力投入暂时让死数据活了起来。

但这种看不见的集成工作很少被转化为组织的永久性基础设施。当公司试图把这个用例推广到另一台机器、另一款产品、另一个基地或另一条工作流时，同样的重建工作必须再做一遍。

这解释了一个重要的现象：

> 许多工业人工智能试点展示了模型能力，却未能形成可复用的组织能力。

试点回答的是：“人工智能模型能否从这份准备好的数据集中得出有用的结果？”

而规模化的问题则不同：

> “组织能否持续地组装有效的上下文、运行正确的模型、支撑一个受治理的决策、从结果中学习，并在其他地方复用这一能力？”

这首先是一个架构与工作流的问题，而不是一个模型选择的问题。

---

## 战略应对：端到端构建连通的数据流

组织应当不再把孤立的概念验证当作工业人工智能进展的主要单位。一次成功的演示是证据，而不是转型。

战略单位应该是**端到端价值流及其决策闭环**。

对于一个物理产品而言，这条流可能包括：

```text
需求
→ 设计
→ 仿真
→ 测试
→ 制造
→ 质量
→ 现场性能
→ 反馈到下一代设计
```

目标不是把每一个字节的数据都集中到一个庞大的系统里。目标是让相关的数据、模型、状态、关系和决策在这条流中实现互操作。

有两条主要的转型路径。

---

## 路径一：把工作流重新设计为 AI 原生

AI 原生的工作流从一开始就被设计成：工作产出是机器可读的，状态是显式的，模型与工具可以被程序化调用，验证是内建的，反馈是自动捕获的。

在这种方式下：

- 设计意图是结构化的，而不是埋在文档里；
- 仿真与分析是可复现的；
- 数据血缘得以保留；
- 审批和约束是可执行的；
- AI 代理通过受治理的工具运行；
- 结果自动更新组织记忆。

这是最干净的架构，因为连通性是设计进工作流的，而不是事后添加的。

然而，从零开始重新设计成熟的工业运营既昂贵又具破坏性。现有设备、软件、法规要求、供应商接口以及数十年的工作实践并不总是可以被替换。

---

## 路径二：围绕现有工作流构建流程数字孪生

对于成熟的组织，务实的路径往往是创建流程数字孪生，把现有系统连接起来，而无需立刻替换每一个工具和工作流。

流程数字孪生不应是又一个可视化仪表盘。它应当表示：

- 流程的当前状态；
- 在流程中流转的实体；
- 数据、模型、设备、人员与决策之间的关系；
- 变更与干预的历史；
- 规则、约束与有效性边界；
- 预期结果与观测结果；
- 学习所需的反馈。

然后，组织可以围绕关键价值流构建一个联邦式的流程孪生网络：

```text
设计孪生
↔ 仿真孪生
↔ 测试孪生
↔ 制造孪生
↔ 产品或资产孪生
↔ 现场性能孪生
```

这个连通的孪生网络成为工业人工智能的运营上下文层。人工智能模型和代理可以在其上进行推理，而孪生则维护受治理的状态、关系、可追溯性和反馈闭环。

这一雄心最终或许可以覆盖整个企业，但实施应当从控制着最重要决策的流程和接口开始。为每一项活动都建一个互不连通的“数字孪生”，只会以新的名字复制同样的碎片化。

---

## 案例：轮胎产品开发

一家轮胎公司可能早已拥有胶料数据、有限元仿真结果、转鼓与整车试验结果、制造参数、均匀性测量、检测图像、质保记录和车队数据。

技术上的机会并不仅仅来自把这些记录全部放进一个数据湖。

机会出现在组织能够追溯以下链条之时：

```text
设计意图
→ 材料与几何版本
→ 仿真假设与预测
→ 制造配置
→ 工艺偏差
→ 试验条件与实测性能
→ 现场运行工况
→ 磨损、耐久或失效结果
→ 更新后的模型与下一个设计决策
```

到那时，数据不再是一堆历史遗物的集合。它变成了一个活的工程系统。

人工智能能做的也就不止于预测一个孤立的目标。它可以帮助识别仿真与试验之间的不匹配，把制造变异与产品性能关联起来，推荐下一次实验，揭示不确定性，并在产品世代之间保留学习成果。

---

## 拟议的成熟度模型

```text
Level 0：数据被产生但未被系统性地保留
Level 1：数据被采集到本地系统中
Level 2：数据可在组织范围内访问
Level 3：数据具备身份标识、时间、配置和数据血缘等上下文
Level 4：数据跨流程与生命周期边界连接起来
Level 5：数据活在受治理的决策与反馈闭环之中
Level 6：AI 代理在流程数字孪生网络上运行
```

大多数组织会高估自己的成熟度，因为它们把 Level 1 或 Level 2 的数据基础设施误认为 Level 5 的运营智能。

---

## 一句话结论

真正的工业人工智能分水岭，不会出现在拥有更好基础模型的公司与拥有更差基础模型的公司之间。可比的模型人人都能获得。

分水岭将出现在：

- 数据依然存放在互不连通的系统中的组织；以及
- 把数据转化为活的、具备上下文的、端到端运营流的组织。

前者会继续产出令人印象深刻的试点。后者则会建立一个持续复利的工业智能系统。

> 如果一个组织已经拥有多年的工业数据，却仍然无法规模化人工智能，它应该再投资一个模型，还是重新设计那个让数据活起来的连通决策系统？

## 参考文献

<a id="ref-1"></a>【1】 McKinsey & Company. (2025). *The State of AI: Global Survey 2025.* https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai

<a id="ref-2"></a>【2】 Manufacturing Leadership Council / National Association of Manufacturers. (2025). *Shaping the AI-Powered Factory of the Future.* https://manufacturingleadershipcouncil.com/wp-content/uploads/2025/05/Shaping-the-AI-Powered-Factory-of-the-Future-Report.pdf

<a id="ref-3"></a>【3】 PwC. (2026). *PwC's 2026 Digital Trends in Operations Survey.* https://www.pwc.com/us/en/services/consulting/business-transformation/digital-supply-chain-survey.html

<a id="ref-4"></a>【4】 MIT Sloan School of Management. (2025). *6 Steps to Succeeding with Industrial AI.* https://mitsloan.mit.edu/ideas-made-to-matter/6-steps-to-succeeding-industrial-ai

<a id="ref-5"></a>【5】 National Institute of Standards and Technology. (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0).* https://www.nist.gov/itl/ai-risk-management-framework

<a id="ref-6"></a>【6】 Reuters. (2024). *Manufacturers slow Gen AI rollout on rising accuracy concerns, says study.* https://www.reuters.com/technology/artificial-intelligence/manufacturers-slow-gen-ai-rollout-rising-accuracy-concerns-says-study-2024-07-10/

<a id="ref-7"></a>【7】 National Institute of Standards and Technology. (2025). *How to Find the Right Balance of Data for Your Industrial AI System.* https://www.nist.gov/blogs/manufacturing-innovation-blog/how-find-right-balance-data-your-industrial-ai-system

<a id="ref-8"></a>【8】 Deloitte. *Novelis: Predictive Analytics in Manufacturing.* https://www.deloitte.com/us/en/services/consulting/case-studies/predictive-analytics-in-manufacturing.html

<a id="ref-9"></a>【9】 McKinsey & Company. (2023). *Clearing Data Quality Roadblocks: Unlocking AI in Manufacturing.* https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/clearing-data-quality-roadblocks-unlocking-ai-in-manufacturing

<a id="ref-10"></a>【10】 Belden. (2023). *Laying the Foundation for Predictive Maintenance in Manufacturing.* https://www.belden.com/knowledge-hub/resources/case-studies/laying-the-foundation-for-predictive-maintenance-in-manufacturing

<a id="ref-11"></a>【11】 National Institute of Standards and Technology. (2022). *Are Industrial AI Tools Worth It? NIST Researchers Offer an Evaluation Procedure.* https://www.nist.gov/news-events/news/2022/02/are-industrial-ai-tools-worth-it-nist-researchers-offer-evaluation

<a id="ref-12"></a>【12】 Siemens. *Siemens Industrial Copilot.* https://www.siemens.com/global/en/products/automation/topic-areas/industrial-ai/industrial-copilot.html

<a id="ref-13"></a>【13】 Siemens. (2023). *When Automated Processes Actually Slow Down Production.* https://blogs.sw.siemens.com/opcenter/when-automated-processes-actually-slow-down-production/

<a id="ref-14"></a>【14】 The Register. (2023). *Samsung Reportedly Leaked Its Own Secrets Through ChatGPT.* https://www.theregister.com/2023/04/06/samsung_reportedly_leaked_its_own/

<a id="ref-15"></a>【15】 OMRON. (2025). *Proposal of Concept Drift Detection in Factory Automation Domain.* https://www.omron.com/global/en/technology/omrontechnics/vol57/003.html

<a id="ref-16"></a>【16】 Blume, S., et al. (2025). *Physics-informed symbolic regression for tool wear and remaining useful life predictions in manufacturing.* Journal of Manufacturing Systems. https://doi.org/10.1016/j.jmsy.2025.03.023

<a id="ref-17"></a>【17】 National Institute of Standards and Technology. *Industrial Artificial Intelligence Management and Metrology (IAIMM).* https://www.nist.gov/programs-projects/industrial-artificial-intelligence-management-and-metrology-iaimm

<a id="ref-18"></a>【18】 National Institute of Standards and Technology. (2024). *NIST Explores AI-Enhanced Monitoring in Manufacturing Processes.* https://www.nist.gov/blogs/manufacturing-innovation-blog/nist-explores-ai-enhanced-monitoring-manufacturing-processes

---

**系列导航：** [上一篇：什么是工业 AI](/posts/industrial-ai-and-digital-twins.html) · [下一篇：流程数字孪生](/posts/09-process-digital-twin-for-industrial-ai.html)
