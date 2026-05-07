# Practical Training Repository

This repository contains the reconstructed code and outcome screenshots for all assignments and experiments from the practical training (day01 to day22 and comprehensive projects).

## Structure
The structure follows the requirement:
- `practical-training/`
  - `dayXX/` (e.g., day01a, day01b)
    - `code/`: Contains the executable code or HTML/CSS/JS files for the task.
    - `pictures/`: Contains the captured screenshots of the execution results or web page rendering.
  - `projectX/` (Comprehensive projects)
    - `code/`: Project code (e.g., Streamlit apps, data generation scripts).
    - `pictures/`: Screenshots of the running application or terminal outputs.

## Setup and Requirements
The codebase uses Python 3.11+. The required dependencies are listed in `requirements.txt`.
You can install them via:
```bash
pip install -r requirements.txt
```

Note: Several tasks from Day 12 to 22 involve OpenAI API and Ali Qwen Models, which require setting the `DASHSCOPE_API_KEY`. Streamlit apps can be run locally using `streamlit run <script_path.py>`.
