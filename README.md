# ParkPilot v5 — Three Parking Maps, Three Independent AI Algorithms

**AI Fundamentals Final Project | Interactive browser application | Python 3.9+**

**Project author:** Serikzhan Beisembek (Серикжан Бейсембек)  
**GitHub:** [Sekentai](https://github.com/Sekentai)  
**Version:** 5.1 — three parking maps, independently verified algorithms

ParkPilot is a **teaching simulation**, not a service with live parking availability. It shows three genuine algorithms from different AI Fundamentals topics. **Each Run button calls a different Python endpoint**, so the methods can be demonstrated individually.

## Final submission: presentation and video

- **[Final presentation — 7 slides (read directly on GitHub)](docs/Presentation.md)**
- **[ParkPilot demo video — 2 minutes 30 seconds on HeyGen](https://app.heygen.com/videos/parkpilot-ai-2-min-30-sec-demo-serikzhan-beisembek-624248bcc9d73cab7e912a1a5440023a)**
- **[Video details and viewing instructions](docs/VIDEO_DEMO.md)**
- **[Full project ZIP with the PowerPoint, code, tests and documents](ParkPilot_Verified_v5_1%20(1).zip)**

*Video is hosted by HeyGen, so its viewing permissions are managed there. The PowerPoint file is included inside the ZIP at `Mini_Smart_Parking_Guide/docs/Presentation.pptx`. The GitHub-friendly 7-slide text presentation is linked above.*

## How to open the website

**Windows:** Extract the ZIP. Open `Mini_Smart_Parking_Guide`, then double-click **`run_windows.bat`**. Keep the command-prompt window open. A browser should open automatically; otherwise use **http://127.0.0.1:8765/**. If you see `ERR_CONNECTION_REFUSED`, the Python server is not running.

**Mac / Linux:** open a terminal in this folder and run `python3 app.py`, then open http://127.0.0.1:8765/.

Python 3.9+ is required. **No packages, internet connection, real sensors, trained model, or database are needed to run the website.**

## Demo: three maps, three independent AI modes

1. Click **1 Mall**, **2 Campus** or **3 Stadium** above the parking image. Each has its own vehicle entrance, obstacles, bay positions and sensor assumptions. Switching maps resets the selected space to A and clears old results.
2. Click **Space A** on the active parking map (selected by default).
3. Click **BFS**. A blue route appears, showing **4 road steps**. Click **Play car movement** to animate the car along the shortest route. This runs Python's `bfs()` via `/api/bfs`.
4. Click **Bayes**. With Space A's initial **CLEAR** reading and 25% prior, the estimated occupancy is **5.3%**. Click **Looks taken** to make it **73.9%**. This runs `bayesian_occupancy()` via `/api/bayes`.
5. Click **MDP**. The system compares expected values for **DRIVE** and **RECHECK** and now recommends **RECHECK**. It uses the latest Bayes result (73.9%). This runs `one_step_mdp()` via `/api/mdp`.
6. Click **Space C**, then **Bayes**, then **MDP**. Space C's default CLEAR reading gives 20.0% estimated occupancy and DRIVE is chosen under the hypothetical rewards. Click **Restart demo** to reset everything.

You can click **BFS, Bayes, or MDP in any order**; they run separately. If you run MDP before Bayes for a space, it uses that space's initial prior and says so in the panel. For each algorithm, click **Show the actual calculations** to display the input, intermediate steps, and output. Selecting a different parking space reruns whichever algorithm is currently selected.

### What you see on screen

| Button | Question | Visual output | Python function |
|---|---|---|---|
| **BFS** | Which road is shortest? | Blue route, step count, visited nodes, smooth car animation | `bfs()` |
| **Bayes** | How likely is this bay occupied? | Two sensor options, adjustable prior, updated probability and formula | `bayesian_occupancy()` |
| **MDP** | Should I drive or check again? | Two expected utility scores and a clear recommendation | `one_step_mdp()` |

Each map is a simplified **5×5 unweighted graph**. Mall uses planted islands, Campus uses closed pedestrian lanes, Stadium uses event-day traffic barriers. The simulated roads, sensors and rewards differ by map. The visuals show painted parking spaces and a car. The animation smooths the geometry of the logical BFS route; it is *not* a physics-based simulation.

## Source code

- `parking_ai.py`: tested BFS, Bayesian inference, and one-step MDP, plus an integrated `analyze()` pipeline.
- `app.py`: standard-library local HTTP server. Independent map-specific `POST /api/bfs`, `POST /api/bayes`, `POST /api/mdp`, integrated `POST /api/analyze` endpoints, and `GET /api/maps` for map layouts.
- `web/index.html`, `web/styles.css`, `web/ui.js`: minimal interactive English-language user interface and animated map.
- `tests/test_algorithms.py` and `tests/test_maps.py`: **25** algorithm, integration, and map-specific unit tests.
- `tests/browser_smoke.py`: optional Playwright browser workflow and actual HTTP checks for all three endpoints (requires Playwright + Chromium **only for the test**, not to run the app).
- `examples/`: reference integration results and test logs.
- `assets/`: screenshots of BFS, Bayes, MDP and mobile interface.
- `docs/`: technical report, seven-slide PowerPoint, AI-use declaration, contribution statement, script and submission checklist.

## Tests

Run the original unit tests:

```bash
python -m unittest discover -s tests -v
```

**25/25 passed** in the packaging environment.

Optional UI/API test on a machine with Playwright and Chromium:

```bash
python tests/browser_smoke.py
```

This test performs real HTTP calls to the **three individual Python API endpoints**. Because Chromium cannot open local network ports in some isolated environments, its UI exercise uses a direct bridge to the same Python algorithm functions. It verifies real UI interactions and JavaScript errors, but it is **not claimed to be an end-to-end browser/server network test**.

## Three map scenarios

| Map | Entrance | Obstacles | Available choices |
|---|---|---|---|
| **1 Mall** | (4,0) | (1,1), (2,1), (3,3) | A (0,0), B (0,4), C (3,4) |
| **2 Campus** | (4,4) | (1,2), (2,2), (3,1) | A (0,4), B (0,0), C (3,0) |
| **3 Stadium** | (4,2) | (1,2), (2,2), (3,3), (2,0) | A (0,1), B (0,4), C (3,0) |

All **nine spot routes are reachable** and all three Python algorithms can be run separately for any of the nine combinations. Each map has its own initial priors and simulated sensor signals. The frontend receives authoritative layout definitions from `GET /api/maps` so displayed positions match Python BFS.

## Math assumptions (all invented for this educational simulation)

- Default Mall layout: start `(4,0)`; walls `(1,1)`, `(2,1)`, `(3,3)`; A `(0,0)`, B `(0,4)`, C `(3,4)`; see the three-map table above.
- Mall prior P(occupied): A `0.25`, B `0.45`, C `0.60`. Initial reports: A CLEAR, B ALERT, C CLEAR. Campus and Stadium have map-specific priors.
- Sensor sensitivity `P(ALERT|OCCUPIED) = 0.85`; specificity `P(CLEAR|FREE) = 0.90`.
- Bayes formula: `P(O|signal) = P(signal|O) × P(O) / [P(signal|O)×P(O) + P(signal|F)×P(F)]`.
- MDP has two states (FREE, OCCUPIED) and actions (DRIVE, RECHECK), defined transitions and rewards, a one-step Bellman update and discount `γ = 0.6`. All utilities are sample model values, **not real prices or predicted losses**.
- The integrated `analyze()` endpoint runs all three per bay, then compares reachable DRIVE candidates using `expected DRIVE utility − 0.70 × BFS route length`.

## GitHub and submission

This project is published in the public repository `Sekentai/AI-final-project`. A GitHub repository does not host this Python-backed website by itself; run the local server as described above. Repository URL: https://github.com/Sekentai/AI-final-project. The updated report and seven-slide presentation are in `docs/` and cover all three maps.

**Responsible AI-use disclosure:** ChatGPT was substantially used to develop this prototype, tests, UI and materials. The file `docs/AI_Use_Declaration.docx` accurately discloses assistance. The author name is pre-filled where known. Add the actual class group, student number (if required), and document only genuine human or team contributions. Before submission, independently understand the algorithms and run the demonstration yourself.

## Math verification note (v5.1)

All three maps were independently cross-checked against Dijkstra's algorithm (shortest paths), direct Bayes formulas and manually recomputed Bellman expected values. All nine map/space combinations matched the backend results. An additional 1,000 randomized Bayes/MDP cases matched independent formulas. The expanded MDP display now retains ten decimal places for the input probabilities, so rounding does not make the displayed arithmetic appear inconsistent; scores remain rounded to two decimal places. All input probabilities, transition tables, rewards and route penalties are teaching assumptions, not measurements. The per-space MDP compares DRIVE against RECHECK before any route-length penalty; route cost is used later by the integrated recommender to rank DRIVE options.