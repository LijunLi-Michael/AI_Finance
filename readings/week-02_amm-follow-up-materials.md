# AMM Follow-up Materials & Next Class Lab

**MB/CSE 599 — AI Finance**

In our Sep 12 class, we covered the math behind Automated Market Makers. This week, we'll approach it from the other direction: first the story, then hands-on practice. Please go through the materials below before next class.

### **📚 Readings & Videos**

**1. A Short History of Uniswap — by Hayden Adams himself**  
 [https://blog.uniswap.org/uniswap-history](https://blog.uniswap.org/uniswap-history)  
 Before we go deeper into AMM math, meet the person who built it. Hayden was laid off from his engineering job at Siemens in 2017, had never written a smart contract, and taught himself Solidity — this is his own account, starting with the actual text messages he sent his friend that day. A 10-minute read.

**2. How To Use Uniswap — Step-by-Step Guide**  
 [https://beincrypto.com/learn/how-to-use-uniswap/](https://beincrypto.com/learn/how-to-use-uniswap/)  
 A written walkthrough of swapping and providing liquidity. Pay attention to the short section on x·y=k — this is the same formula from last week's lecture, now attached to the buttons you'll actually click.

**3. Uniswap Tutorial for Beginners [How To Swap & Provide Liquidity]**  
 [https://www.youtube.com/watch?v=GYHLBD9I_Ts](https://www.youtube.com/watch?v=GYHLBD9I_Ts)  
 Video walkthrough covering swaps, cross-chain swaps, and providing liquidity on Ethereum, Base, and Arbitrum — the same networks we use in this course.

**4. How to Trade on Uniswap (2025)**  
 [https://www.youtube.com/watch?v=sf9ewic8mNY](https://www.youtube.com/watch?v=sf9ewic8mNY)  
 A shorter chaptered tutorial: connecting a wallet, choosing tokens, setting slippage, confirming a trade. When you watch the "price impact" number change with trade size — that IS x·y=k in action. We'll do this live in class next week.

### **🔧 Next Class: Hands-on Lab**

We're flipping the order this time — you'll touch the AMM before we revisit the math.

**Part 1 — Trade on a live AMM**  
 I'll deploy an AMM contract live at the start of class, and everyone will swap against the same pool. Watch what happens to the price as more of you trade in the same direction — that's the x·y=k curve moving in real time, and we'll read the numbers off the screen together.

**Part 2 — Deploy your own AMM**  
 Then you'll each deploy your own AMM. The contract code is already written and will be provided — your job is to deploy it, seed the pool with initial liquidity, and make the first swap against your own market. By the end of class, you'll have created the same kind of market Hayden Adams built in 2018 — which is why the reading above starts with his story.

**⚠️ Before class:** Make sure your wallet is set up and funded with testnet tokens. If you had trouble with wallet setup, come 10 minutes early.

