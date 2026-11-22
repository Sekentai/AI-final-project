# ParkPilot — Final Presentation (7 Slides)

**AI Fundamentals · 2026–2027 · Serikzhan Beisembek (Серикжан Бейсембек)**

[▶ Watch the 2-minute 30-second video demo](https://app.heygen.com/videos/parkpilot-ai-2-min-30-sec-demo-serikzhan-beisembek-624248bcc9d73cab7e912a1a5440023a)

> This is the **GitHub-readable version** of the 7-slide PowerPoint. The original `Presentation.pptx` is inside the [downloadable project ZIP](../ParkPilot_Verified_v5_1%20(1).zip), under `Mini_Smart_Parking_Guide/docs/`. The 7-slide deck explains the same three algorithms and maps. The current video link is also clickable in the updated PowerPoint distributed in the ChatGPT conversation.

---

## Slide 1 of 7 — ParkPilot: Smart Parking Guide

**An explainable AI parking assistant**

- **BFS** — find the shortest road
- **Bayesian inference** — estimate whether a parking spot is occupied
- **MDP** — choose whether to DRIVE or RECHECK

**Three parking maps · Three independent Python algorithms · Interactive demo**

**Say:** “Our project is ParkPilot. It shows how three different AI techniques solve one parking problem. The maps and sensors are simulated for education.”

---

## Slide 2 of 7 — Problem, Goal, and AI Pipeline

### The problem
A parking space may look free, but sensors can give incorrect signals. The best spot also needs to be reachable by a road.

### The goal
Help a simulated driver **find a reachable space and make an informed choice**.

| Step | Input | Output |
| --- | --- | --- |
| 1. BFS | Start point, obstacles, selected bay | Shortest route |
| 2. Bayes | Prior occupancy, sensor signal | Updated occupancy probability |
| 3. MDP | Occupancy belief, rewards, transitions | DRIVE or RECHECK |

**Say:** “Route planning, uncertainty and decision-making are different problems. Our application gives each one a separate algorithm.”

---

## Slide 3 of 7 — Algorithm 1: Breadth-First Search (BFS)

**Question:** What is the shortest route to a selected parking space?

- **Input:** a 5×5 grid, car entry, target, and blocked cells.
- **Process:** a first-in-first-out queue explores neighboring cells in layers.
- **Output:** a shortest path with total steps and expanded cells.
- **Example:** Mall entrance → Space A = **4 steps**.
- **Why BFS:** moves have equal cost, so BFS gives a shortest path.

**Say:** “Click BFS. The blue route shows the answer. Then click Play car movement to follow the route while avoiding obstacles.”

---

## Slide 4 of 7 — Algorithm 2: Bayesian Inference

**Question:** What is the probability that this space is occupied, given a noisy sensor?

\[
P(O\mid S) = \frac{P(S\mid O)P(O)}{P(S\mid O)P(O)+P(S\mid F)P(F)}
\]

- Prior occupancy at Mall Space A: **25.0%**
- Assumed sensor sensitivity: **85%**
- Assumed specificity: **90%**
- Sensor **CLEAR** → posterior occupancy ≈ **5.3%**
- Sensor **ALERT** → posterior occupancy ≈ **73.9%**

**Say:** “The sensor is not perfectly reliable. Bayes updates our estimate when evidence changes. Click ‘Looks taken’ to see the probability increase.”

---

## Slide 5 of 7 — Algorithm 3: Markov Decision Process (MDP)

**Question:** Should the driver go to the selected space or check it again?

- Two states: **FREE** and **OCCUPIED**.
- Two actions: **DRIVE** and **RECHECK**.
- Uses a one-step Bellman update with **γ = 0.60**.
- Formula: `Q(s,a) = R(s,a) + γ × Σ P(s'|s,a)V(s')`.
- The occupancy belief weights both state-specific action values.
- Select the action with the **higher expected score**.

**Say:** “MDP does not simply choose the nearest spot. It compares the consequences of driving now and checking again. The rewards and transitions are teaching assumptions.”

---

## Slide 6 of 7 — Maps, Live Demo & Testing

| Map | Entrance | Unique feature |
| --- | --- | --- |
| **Mall** | (4,0) | Simple access with planted islands |
| **Campus** | (4,4) | New entry and closed central walkways |
| **Stadium** | (4,2) | Event-day obstacles near the centre |

**What to show live:**
1. Select Mall, Space A → click **BFS** and play the car.
2. Click **Bayes**, switch CLEAR → ALERT.
3. Click **MDP** and show the recommended action.
4. Switch to Campus or Stadium to show a different map.

**Verification:** **25/25 Python unit tests passed** in the project environment; all nine map/space combinations have reachable paths.

**Say:** “All three buttons call separate Python endpoints, and the results change across scenarios.”

---

## Slide 7 of 7 — Results, Limitations & Video

### What works
- Correct shortest-path search on each map
- Bayes updates probabilities from noisy simulated sensors
- MDP compares two actions using a one-step expected reward
- A clear, interactive application for demonstrating AI concepts

### Limitations
- Small 5×5 maps; simulated sensors, probabilities, rewards
- Not a live parking service; no trained model or real-world accuracy claims
- Future work: real sensor data, larger maps, longer-horizon planning

**▶ [Watch the 2:30 ParkPilot Demo (HeyGen)](https://app.heygen.com/videos/parkpilot-ai-2-min-30-sec-demo-serikzhan-beisembek-624248bcc9d73cab7e912a1a5440023a)**

**Project and source:** https://github.com/Sekentai/AI-final-project

**THANK YOU — Questions?**

---

*Created with substantial AI assistance, as disclosed in the project's AI-use declaration. The videos and web interface illustrate a small teaching simulation rather than production parking predictions.*
