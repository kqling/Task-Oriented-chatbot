任务型聊天机器人
[运行test.py进行测试]


  
NLU（自然语言理解）：
  
   把来自用户的句子映射到机器可读的语义结构，包含实体（entity）抽取，意图（intent）识别，话题（domain）识别等。
  
DST(对话状态跟踪)：  
   
   在NLU的基础上，状态跟踪需要把多轮对话历史进行总结，理解上下文中的含义。这个模块对于跟踪用户需求有着至关重要的作用，因为很多时候需要通过综合考
   虑用户多轮输入才能真正理解他们的需求。
    
DP(对话策略)：
  
   在有了对话状态后，对话策略需要决定下一步应该做什么行动（action）。行动包括查询数据库，或者产生下面要说的一句话。相当于对话系统的高层决策者。
    
NLG(自然语言生成)：
  
   负责把对话策略的行动装换成自然语言
    
  
  
  
  
  
