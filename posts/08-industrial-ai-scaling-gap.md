---
layout: default
title: "工业 AI 为什么难以规模化：从概念验证到生产价值"
description: "分析工业 AI 从概念验证走向生产时遇到的数据、信任与系统演变问题，以及“死数据”如何阻碍规模化。"
content_type: essay
display_order: 40
published: 2026-09-21
updated: 2026-10-06
topics:
  - 工业 AI
  - AI 规模化
  - 数据治理
permalink: /posts/08-industrial-ai-scaling-gap.html
nav: essays
page_class: article-page
---

# 工业 AI 为什么难以规模化：从概念验证到生产价值

_最后更新：2026-10-01_

## 写在前面

过去几年我参与或旁观过不少工业 AI 的概念验证（PoC）。它们有一个共同点：演示那天都挺好看。模型准确率过了线，专家点头，PPT 最后一页写着下一步推广到其他产线。然后大半就没有然后了。【待补：自己经历的一个具体 PoC，哪一年、做什么、最后卡在哪一步】

一开始我把这归结为运气，或者某个项目的人没盯住。见得多了才觉得这是结构性的。PoC 里的条件和生产里的条件是两个世界，而我们很少在立项的时候就承认这一点。

这篇笔记想把这件事理清楚。表面上是“规模化鸿沟”，往下挖我看到三样东西：工业数据的底子薄，信任达不到让人敢在运营中用的程度，还有工业系统本身一直在变。再往下挖一层，会碰到一个我觉得比“数据质量差”更要紧的问题，放在后半部分说。文中引的案例都来自公开材料，我自己的判断会单独标出来。

## PoC 过了，生产没过

工业 AI 在有边界的实验里容易证明，在真实运营里难以持续。做 PoC 可以挑数据集、选稳定的运行窗口、请专家坐在旁边、把成功指标定得很窄。生产环境没有这些优待：数据流是杂乱的，设备和材料在换，工作流是工厂的，用户是一线的人，旁边还有风险控制和业务指标盯着。

麦肯锡 2025 年的人工智能调查显示，人工智能已经被广泛采用，但只有约三分之一的受访者说已经在整个组织内规模化推广了人工智能项目。[【1】](#ref-1) 在制造业这个数字格外刺眼，因为一个模型只有改变了真实决策，并且带来可衡量的结果，比如停机更少、废品更少、良率更高、维护更安全、成本更好，才算有价值。模型放在那里不算。

Novelis 的例子很典型。据德勤的报告，这家公司早就有预测分析类的用例，但在制定“未来工厂”（Plant of the Future）路线图之前，缺少把这些用例推广到各个制造基地的策略。[【8】](#ref-8) 我读到这里的感受是，有用例和有能力是两回事。规模化要的是可重复的部署、工作流有人认领、数据拿得到、有治理，还要有一个在试点环境之外依然站得住的价值论证。模型成功只是其中一项。

## 底子薄：数据和系统

工业 AI 靠的是可靠、带上下文、和物理过程连着的数据。实际拿到手的数据经常缺失、有噪声、标注很差、困在遗留系统里，或者和能解释它的资产、批次、材料、运行工况、维护事件脱了钩。

数字不好看。制造业领导力委员会（Manufacturing Leadership Council）报告说，65% 的制造商缺少适用于人工智能应用的合适数据，62% 提到数据是非结构化的或格式不佳。[【2】](#ref-2) 普华永道的报告说数据质量差已经拖累了很多运营负责人从数字化举措里拿到价值。[【3】](#ref-3) 麻省理工斯隆管理学院的说法我比较认同：工业 AI 要的是在正确的时间拿到正确的数据，光是更多的数据不够。[【4】](#ref-4)

麦肯锡讲过一家铁矿石公司的事。他们为球团工艺建优化器，项目开始之后才发现一个关键的传感器已经坏了六个月。[【9】](#ref-9) 这是最基本的数据就绪度没过关。优化器在数学上可以很强，但一个从来没被正确测量过的关键信号，它学不到任何东西。

Belden 的里士满工厂是另一种情形。他们自己把它描述为一个既有（棕地）工厂，机器和设备的年代、品牌各不相同，预测性维护工作第一步得先把设备连起来，在不更换全部遗留设备的前提下采集带上下文的 OT 数据。[【10】](#ref-10) 如果每一项资产、每一座工厂都要先做一个数据抢救项目，工业 AI 就没法规模化。部署变成了集成，IT 和 OT 的碎片化在这里直接变成工期。

同一座工厂后面的结果也值得看。一个预测性维护试点从 150 个传感器采了约 300 GB 的数据，用这些数据识别出了有风险的部件，比如和皮带对中问题相关的异常振动。[【10】](#ref-10) 我想强调的是，300 GB 本身没有价值，价值在最后产出了一个有人可以据此去拧螺丝的维护发现。数据量只在被转化成和决策相关的信息时才算数。

## 信任没到能用的程度

工业 AI 要影响生产、维护、质量、安全或工程决策，得先有人信它。这里的信任比模型准确率宽得多：验证、可解释性、可靠性、网络安全、知识产权保护、人的接受度，还有 AI 建议和人的决策之间清楚的权限边界，都在里面。

美国国家标准与技术研究院（NIST）的人工智能风险管理框架把可信性当作贯穿 AI 系统全生命周期的要求。[【5】](#ref-5) NIST 做工业 AI 评估时问的也是这一类问题：这个工具有没有降低制造风险，有没有创造系统层面的价值。模型孤立地看准不准，在那套评估里排不到前面。[【11】](#ref-11)

信任最常在人机界面那里断掉。西门子报告过 PCB 制造里的一个现象：自动光学检测的误报会一点点累积成人工检验员的告警疲劳，检验错误反而增加。[【13】](#ref-13) 人被误报烦够了就会学着忽视它，真问题来的时候也一样忽视。

生成式 AI 把这个问题又放大了一层。西门子把它的 Industrial Copilot 定位在维护配置和故障修复这类任务上，路透社则报道制造商对生成式 AI 推广中的回答准确性和幻觉问题表示担忧。[【6】](#ref-6)[【12】](#ref-12) 在工业工作里，一个流畅的回答什么都证明不了。生成的指导如果会影响故障排查或维护，用户就需要知道它引用了哪些经过批准的知识来源，有什么证据，谁审过，不确定性高的时候往哪里上报。

治理也是信任的一部分。2023 年有报道说三星半导体的员工在找工作帮助时，把敏感源代码和在研半导体的信息输进了 ChatGPT。[【14】](#ref-14) 如果用工业 AI 会把专有代码、工艺知识、良率证据或运营数据暴露在经批准的控制之外，它就不可能负责任地规模化，再准也不行。

最后是权限。NIST 的工业 AI 工作明确把人和代理之间的沟通、人在回路的学习纳入其中，它的 AI 增强型制造监控工作也强调智能自动化里操作员的交互和输入。[【17】](#ref-17)[【18】](#ref-18) 落到工厂里就是一张要事先写清楚的表：AI 什么时候只能看，什么时候可以建议，什么时候可以排程、改参数、停工艺，什么时候必须有人批。

## 系统自己会变

工业 AI 部署到的是一个不断变化的物理系统。机器磨损，传感器漂移，供应商和材料换了，方法修订了，产品演进了，操作员插手了，运行工况变了。一个在受控 PoC 里表现很好的模型，进了生产就可能变得不准，物理上站不住，甚至不安全。

NIST 指出，工业 AI 的数据必须覆盖真实的运行场景和物理认知，光有方便取得的历史样本不够。[【7】](#ref-7) 这件事部署之后只会更糟，因为被建模的那个系统不会停在那里等你。

欧姆龙（Omron）描述过一个制造缺陷预测的用例：4M（人、机、料、法）的变化会诱发概念漂移，而这种漂移必须和缺陷征兆分开检测。[【15】](#ref-15) 这就是为什么不能默认生产环境的行为和试点数据集一致。人、设备、材料、方法中任何一项变了，工艺就可能偏移，模型的假设悄悄失效，没有人会收到通知。

另一个方向是让模型本身带着物理。在刀具磨损和剩余使用寿命预测上，近期融入物理规律的研究明确地对磨损动力学和可解释的物理特性建模，没有只靠对历史数据做黑箱拟合。[【16】](#ref-16) 系统在变，但它变的方式仍然服从工程约束。能规模化的模型，是那种在磨损、载荷变化、新的运行区间以及超出 PoC 数据范围的外推情形下还保持物理意义的模型。

## “数据才是问题”，这话对但不够

圈子里常听到一句话：模型不是主要问题，数据才是问题。方向上我同意，但停在这里就太浅了。

现代机器早就在产大量的传感器读数、告警、生产记录、质量结果、维护历史、图像、工程文件、仿真输出和操作员观察。成熟的组织也花了很多年把这些东西收进历史数据库、制造系统、实验室数据库、工程资料库、云平台和数据湖。数据是有的。可其中大部分除了喂仪表盘、做回顾性报告、撑一次精心准备的 PoC 演示之外，几乎没产生过什么价值。

我的解释是：这些数据是死的。

死数据不等于错数据或没用的数据。它指的是那些被存下来了，却和赋予它运营意义的上下文、关系、工作流和决策脱了节的数据。

```text
采集到的数据未必是连接起来的数据。
连接起来的数据未必是具备上下文的数据。
具备上下文的数据未必是活数据。
活数据未必是可行动的数据。
```

这条链要全部接上，工业 AI 才产生价值。

## 数据是怎么死的

第一种死法是被组织边界切开。设计、仿真、测试、制造、质量、维护、供应链、现场服务各用各的系统，每个职能手里都有有用的数据，但这些系统互相不知道对方的存在。一条试验结果可能没有关联到确切的设计版本；一次制造偏差可能没有和材料批次、机器状态、工艺设定、下游性能连起来；现场失效回不到它之前的仿真假设和设计决策。组织有数据，却没有一份关于产品或流程怎么演变过来的连贯记忆。

第二种是没有共享的身份标识和上下文。工业记录难以连接，常常是因为各家用了不同的资产与产品标识符、命名规范、时间戳与采样率、单位与坐标系、版本与配置定义、质量规则、工艺边界、模型版本。AI 模型没法从彼此脱节的表格里可靠地推断这些关系。在高级推理成为可能之前，组织得先有一种受治理的办法回答几个很基本的问题：

```text
这条记录描述的是哪个物理对象或流程？
它代表的是哪个版本、哪种状态、哪种运行工况？
在它之前和之后发生了什么？
哪些其他记录、模型和决策与它相关？
```

答不上来这些，数据越多，模糊越多。

第三种，数据是被动的。很多工业数据平台的初衷就是存储、可视化和检索。它们告诉你发生了什么，却没有嵌进决定“接下来该发生什么”的工作流里。一个仪表盘也许能看出趋势异常，但它不知道谁负责响应，适用哪条工程规则，信号是否有效，该跑哪个模型，允许采取什么行动，需要什么审批，行动之后结果有没有改善。数据不参与决策和反馈，就一直停在观察层，进不了运营层。

第四种最隐蔽：数据不知道自己的关系。工业性能是由关系创造的。

```text
材料 + 设计 + 工艺 + 机器 + 环境 + 使用 = 结果
```

传统数据库可能把每一项都存了，却丢掉了把它们连起来的因果结构和时间结构。工程领域尤其吃这个亏，因为价值很少藏在某一个变量里，要看配置、条件、干预和结果之间怎么相互作用。缺的那一层是关于系统及其关系的运营模型，再建一个数据库补不上。

## PoC 为什么看着比生产系统好

现在可以回答开头那个问题了。一个小型工业 AI PoC 能成功，是因为有一支专职团队手工重建了缺失的上下文。他们挑干净的数据集，对齐时间戳，解决标识符问题，排除无效运行工况，访谈领域专家，再把目标定得很窄。模型看着成功了，因为人力投入暂时让死数据活了过来。

这部分看不见的集成工作很少变成组织的永久基础设施。公司想把这个用例推到另一台机器、另一款产品、另一个基地、另一条工作流时，同样的重建工作得再做一遍。

这就是为什么很多工业 AI 试点展示了模型能力，却没有形成可复用的组织能力。试点回答的问题是：模型能不能从这份准备好的数据集里得出有用的结果。规模化要回答的问题完全是另一个：组织能不能持续地组装有效的上下文、跑对的模型、支撑一个受治理的决策、从结果里学习，然后把这套能力在别处再用一次。这首先是架构和工作流的问题，模型选哪个排在后面。

## 该把什么当作进展的单位

我的建议是，别再把孤立的 PoC 当作工业 AI 进展的主要单位。一次成功的演示是证据，不是转型。

战略单位应该是端到端的价值流和它的决策闭环。对一个物理产品来说，这条流从需求开始，经过设计、仿真、测试、制造、质量、现场性能，最后反馈到下一代设计。把每一个字节都集中到一个庞大系统里，这不是目标。目标是让相关的数据、模型、状态、关系和决策在这条流上能互操作。

转型有两条路。

第一条是把工作流重新设计成 AI 原生的。AI 原生的工作流从一开始就按这样的要求设计：工作产出机器可读，状态显式，模型和工具可以被程序化调用，验证内建，反馈自动捕获。做到了会是什么样？设计意图是结构化的，没有埋在文档里；仿真和分析可复现；数据血缘保留；审批和约束可执行；AI 代理通过受治理的工具运行；结果自动更新组织记忆。这是最干净的架构，连通性从一开始就在里面，用不着事后补。可是把成熟的工业运营推倒重来既贵又伤筋动骨。现有设备、软件、法规要求、供应商接口，还有几十年的工作习惯，很多是说换也换不掉的。

第二条是围绕现有工作流建流程数字孪生。对成熟的组织，务实的做法往往是先建流程数字孪生把现有系统连起来，不急着替换每一个工具和工作流。这个孪生不该又是一块可视化仪表盘。它要表示流程的当前状态，在流程中流转的实体，数据、模型、设备、人员和决策之间的关系，变更和干预的历史，规则、约束和有效性边界，预期结果和观测结果，以及学习所需的反馈。然后围绕关键价值流建一个联邦式的流程孪生网络：设计孪生、仿真孪生、测试孪生、制造孪生、产品或资产孪生、现场性能孪生，彼此连着。这个网络就是工业 AI 的运营上下文层，模型和代理在上面推理，孪生负责维护受治理的状态、关系、可追溯性和反馈闭环。

这个雄心最终也许能覆盖整个企业，但动手要从控制着最重要决策的流程和接口开始。给每一项活动都建一个互不连通的“数字孪生”，只是用新名字把同样的碎片化再复制一遍。

## 拿轮胎开发比一下

一家轮胎公司手里很可能早就有胶料数据、有限元仿真结果、转鼓和整车试验结果、制造参数、均匀性测量、检测图像、质保记录和车队数据。把这些全倒进一个数据湖，机会不会自动冒出来。

机会出现在组织能把这条链追下来的时候：从设计意图，到材料与几何版本，到仿真假设与预测，到制造配置，到工艺偏差，到试验条件与实测性能，到现场运行工况，到磨损、耐久或失效结果，再到更新后的模型和下一个设计决策。【待补：一次因为试验结果没关联到正确设计版本而走弯路的具体经历，或者一个追下来了的正面例子】

追得下来，数据就从一堆历史遗物变成一个活的工程系统。AI 能做的也就不止于预测一个孤立的目标：它可以找出仿真和试验之间对不上的地方，把制造变异和产品性能关联起来，推荐下一次实验，把不确定性摆出来，还能在产品世代之间把学到的东西留住。

## 自测一下在哪一级

```text
Level 0：数据被产生但未被系统性地保留
Level 1：数据被采集到本地系统中
Level 2：数据可在组织范围内访问
Level 3：数据具备身份标识、时间、配置和数据血缘等上下文
Level 4：数据跨流程与生命周期边界连接起来
Level 5：数据活在受治理的决策与反馈闭环之中
Level 6：AI 代理在流程数字孪生网络上运行
```

大多数组织会高估自己。最常见的错位是把 Level 1 或 Level 2 的数据基础设施当成了 Level 5 的运营智能。

## 写在后面

写完回头看，我对三个根本原因的信心不太一样。数据底子薄和系统会变，证据够多，我没什么怀疑。信任这一条我拿不准的是它的权重：它是真正的瓶颈，还是数据问题解决之后自然会缓解的次生问题？文中引的几个案例都能支持前一种说法，但也都可以解释成数据和治理没做好。

另一个拿不准的是两条路的选择。我倾向第二条，先建流程数字孪生，可这个倾向有一部分来自我所在的行业本身就是成熟的、满是遗留系统的。一家新建的工厂也许该直接走第一条。

真正让我动笔的，是一个老问题的新版本。如果一个组织已经坐在多年的工业数据上，却仍然没法规模化 AI，它该再投一个模型，还是重新设计那个让数据活起来的连通决策系统？我的答案显然是后者，但我也知道，前者在预算会上好过得多。

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
