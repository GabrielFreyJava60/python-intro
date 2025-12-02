# HW 38 Definition

## Integrating the code of calculating expression from HW #36 to the agent

### Updating the agent from CW #38

#### Adding tool for LTR evaluation like ltrEval(expr: string)

#### Adding rule in the system prompt for LTR evaluation tool involvement

#### In the case of applying LTR evaluation only the result of the evaluation should be printed out

## Usage

### Start Phi-3 Agent
```bash
python3 main.py
```

### Example Interactions

**Weather Query:**
```
You: What is the weather in London?
Agent:  Weather in London(United Kingdom): temperature is 10.5°C...
```

**LTR Evaluation:**
```
You: Calculate (3 + 2) * 10
Agent:  50.0
```

```
You: Evaluate 2 ** 3 + 5
Agent:  13.0
```

## Files

- `main.py` - Phi-3 chat agent with tool routing
- `tools.py` - Available tools (getWeather, ltrEval)
- `system_content.py` - System prompt with tool rules
- `thinking_dots.py` - Loading animation
- `ltr_evaluation.py` - LTR expression evaluator from HW#36
- `weather_integration_test.py` - Weather function test

## Requirements

- Ollama with phi3 model running on localhost:11434
- Python 3.10+
- requests library
