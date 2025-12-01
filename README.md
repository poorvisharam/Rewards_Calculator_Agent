# Rewards_Calculator_Agent

# Table of Contents

- [Pitch](#pitch)
- [Architecture](#architecture)
- [Code](#code)
    - [Project Structure](#project-structure)
    - [Design](#design)
- [How to run](#how-to-run)
- [Concepts applied from google kaggle 5 day workshop](#concepts-applied-from-google-kaggle-5-day-workshop)
- [Supporting screenshots](#supporting-screenshots)

# Pitch

Most people use multiple credit cards, each offering different reward rates for various purchases. Remembering these reward structures and calculating which card gives the highest points at the moment of purchase is difficult. Using the wrong card can result in earning fewer points and losing potential savings.

For example, for a $100 grocery purchase:

Robinhood card: 3X → 300 points
Chase Freedom: 1.5X → 150 points

Choosing the right card makes a significant difference.

This agent helps users to determine which of their credit card will maximize their rewards for about-to-do purchase. By analyzing reward structures and bonus categories, the agent recommends the optimal card ensuring users makes good use of rewards for each card.

# Architecture

![[Architecture]](./architecture.png)

# Code

## Project structure

```
agent-dir
 |
 |- agents/ ( sub agents )
 |- models/ ( pydantic models )
 |- tools/ ( custom function tools )
 agent.py ( root agent or runner initialization )
```

## Design

### Populate users and benefits
For the scope of this project, instead of considering full fledged open api that gives user card mapping and card benefit mappings from a database. We are populating few dummy data intially when program starts up.

### Authentication and Authorization
Agent will respond with what user ID needed, since auth components are not implemented for this version.

### Marketplace agent
Based on purchase sentence from user message, the agent will search the internet to find what that marketplace generally sells and then based on product user trying to buy, it will pick a reward category.

### Google search
Tool useful for marketplace agent (gemini LLM) to find what is typically sold in Trader Joes vs Best buy etc.

### Rewards agent
Gets user's cards with given user ID
Gets user's card's benefits
Keeps a note on the category output from marketplace agent
Picks the reward percentage for each card
Calculate the rewards for each user's cards based rewards percentage and category
Picks the top credit card for this purchase

### Output schema
The rewards agent will also give standard format output in json format which can be used in downstream services easily.

This also has pydantic model so validations are done seamlessly.

### Root agent
Connects all sub agents and exposes to adk service

### Sequential agent
We used sequential flow because we needed reward category for the purchase always before calculating the rewards.


# How to run

```
cd <parent folder to where this agent is placed>
adk web .
open http://localhost:8000 in new tab or browser
select Rewards_Calculator_Agent in agent pick drop down

User massage: 
    User ID: user1
    Purchasing: iphone
    Marketplace: Best Buy
    Amount: $1000

```

# Concepts applied from google kaggle 5 day workshop

### Multi agent
* agent powered by LLM
* sequential agents

### Tools
* custom tools
* built in tools
* gemini use for summarizing internet search into single reward category

### Observability
* events from adk
* trace from adk

### Others
* eval from adk

# Supporting screenshots

## Sample run
![[Sample Run]](./sample-run.png)

## Observability
### Trace
![[Trace]](./trace.png)
### Events
![[Events]](./events.png)

## Agent evaluation
![[Eval]](./eval.png)
