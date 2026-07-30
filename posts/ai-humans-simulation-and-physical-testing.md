---
layout: default
title: "From the long tail problem to the relations of AI and Humans"
description: "A technical note on how AI and human judgment can complement one another rather than compete for the same role."
content_type: essay
published: 2026-07-08
updated: 2026-07-29
topics:
  - Industrial AI
  - Human judgment
permalink: /posts/ai-humans-simulation-and-physical-testing.html
nav: essays
page_class: article-page
---

# From the long tail problem to the relations of AI and Humans

_Last updated: 2026-07-09 12:40 America/New_York (UTC-04:00)_

## part 1
A few days ago a colleage ask me an question, he said, Qian, from my last 25 years experience in various companies: big or small, I found often in those big companies, they like to hire the best talents, but keep them working on the 螺丝钉一样的流水线工作，而不能发挥他们的潜力；还有一种情况就是，在很多流程上总是会有很多资历很深的工程师在做一些看是很枯燥繁琐而且没有什么技术含量的活，其实这些活完全可以找一些technican或者刚入职的年轻人去做就可以了， 为什么不去让这些资深的工程师去做一些难度很高的研发工作呢。

这是一个很有意思的话题，为什么大公司需要把有能力和有经验的人放在枯燥无聊的成熟的流程上？这可能有很多种原因，有的人会说这是因为大公司有钱养的起有能力和有经验的人去做这些没技术含量的工作，有的人会说大公司注重流程成熟，任何人在上面都是在跟流程，跟你有多少经验和能力没关系。我想或许这里有还有一个原因就是所谓的long tail problem，这个名词是我偶尔在看一些智能驾驶的文章时发现的，里面说无人智能驾驶从十年前就在一般的驾驶环境中表现已经很惊艳了，也就是可以涵盖了驾驶中99%的场景问题，但是呢，就是是哪1%的场景始终无法完全保证，所以呢迟迟不能完全商业化和规模化，以至于现在waymo和tesla 的robotaxi还是在慢慢的一边测试一边使用中，而然还是总是时不时看到这个那个robotaxi造成不便的消息。这让我联想到大公司的流程问题，大公司流程成熟，最注重就是这个流程一直跑的通而不出任何故障，一旦出了问题，这个时候需要尽可能迅速的解决，把downtime减到最低值，在平日里跑流程的时候其实可能不需要这些有经验和有解决问题能力的员工，但在这种极端情况发生的时候必须要有这样的人才在这里，他们的价值不能体现在日常，往往体现在流程出现问题的时候，也就是所谓的long tail问题出现的时候。类似的教训也多次出现在我在工业界工作的经验里，有的时候一个流程出了问题，最好能够找到这个流程的developer，有的时候往往是那个平日里都不怎么接触的，快要退休了的人，不然要是自己去修改或者debugging这个流程的话，往往不如自己推倒了重新建一个新的来的快和有效果。

现实是退休的总归要退休，年轻人接收这套流程后，要么有能力自己推倒了重建，要么就是等着这个流程不知道哪一天忽然宕机。这让我想到了现在的AI。

首先她就像一个年轻的新人，现在无法胜任关键的long tail 问题，尤其在众多的legacy 流程面前，她完全无法独当一面，所以我不认为短期内像anthoropi 或者open Ai的boss 在那里宣传的那样会在几年内替代人类，当然这里还有trust和责任归属的原因，不单单是这个long tail；另外，她又极其的有能力，有可能帮助一些有能力的工程是推倒现有的流程去进行重建。虽然有这个可能性， 但对于一些大公司来说，这条路往往走不通，尤其是在花了大笔投资在生成机器之后又花了大量的实践和物力建立很成熟流程的那些公司，很难劝说他们去重建，虽然他们更情愿拿着AI到处修修补补。倒是一些小公司，或者那些刚买了新机器还没有建立成熟的属于自己的生产流程的小公司倒是更有可能做到AI native。但是无论如何，只是从技术角度去讲的话，有没有AI，那种long tail 问题我认为永远会需要熟悉整个流程的人。


## part 2
Over the weekends I saw several ariticles discussing the topics of whether AI is replacing the human labors. And suddenly realize some analogies to the discussions we have had regarding the relations between simulations and physical testings in the industry. 

Over the years we have been developing higher and higher fidliety simulations, with faster and faster speed, and making it more and more user friendly. And people says one day the simulations will replace not all, but the marjority of the testing, so there would be less and less testing engineers or technicans needed. However, this is paritally true that simulations in deed becomes more powerful, it enables the engineer explore much larger design space in the early design phase, which can not be done through the tradiational testing ways. However, no matter how advanced the simulation models are, we still rely on the testing as the criterion to judge the design. Simulations have been best used for ranking the order, pointing the directions, rather than giving the absolute predictions. There are rare cases we purely rely on the simulations but not testing to make the critical decisions. 

In addition, due to the increased needs of running simulations for exploring more design space, we had to increase the testing capacities to satisfy the needs; and since the simulations needs to be run on computeres, we had to increase the investment in the computing infrastructure to meet the needs. Furthermore, to be able to develop higher fidelity models, we had to invest in better and smarter testing machines that can provide better data for us to close the gaps between simualtiosn and physical testings. Those all have somehow contribute to creating more jobs in the area of hardware. 

So if we consider AI as the modeling and simulations of human intelligence, the anology here is straight forward. AI can generate answers and automate tasks, but people are still needed to define the problem, judge the output, understand context, and most imortantly take responsibility for the final decisions. The producities go up 10X, then it will need more people to do the final check; the needs on the computing hardware will definitly create more jobs in that areas; In addition, not mentioning there are more and more AI researcher and engineers keep working on developing better models.  

So like we always say simulation and testing are friends, rather than the enermy, they compliment each other for a much more productive industry process. Similarly in the  case of AI, the better model is not replacement. It should be a feedback loop. 

Simulation improves through physical testing, and physical testing becomes smarter through simulation. AI can improve human productivity, while human judgment keeps AI useful, valid, and safe.


- **another interesting angle** is this: in the big companies, there has been many matured process, it is so matured that there is almost no one is not replaceable, but why the big companies are still try to hire the best talents and engineers or scitists to do such repetive and tedious jobs but they just follow the process. if they are so repetives, repeatable, why do not the company hire just technicans to just follow the process. My understanding is that the long tail problem. 99% of time you do not need an engineer to debug the process, but the company could not afford the 1% of the process is down, which might cause signficant loss.

more thinking about the relations between physical and digital 

- when I talk about the modeling and simulations here, I am just refer to a physical object, it can be a process 

- there is better hardware, there will be more data collected, and there will be better and smarted algorithms can be built, just like the tire wear algorithms

- the world I envisoned is everthing have their own digtial twin model or you called AI model, that can be plugged into the basic knowledge model anytime. those AI model are trained by the invidual,
