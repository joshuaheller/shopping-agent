# Shopping Agent

This project implements a shopping agent that automates interactions with online shopping platforms.

## Demo

[Original prompt (German)](task_prompt.txt): Einkaufen bei dm.

[English prompt](task_prompt_en.txt): Buy groceries from dm.

![Groceries from dm](agent_demo.gif)


## Prerequisites

- Python 3.11 or higher
- Playwright browser automation
- OpenAI API key (for AI capabilities)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/shopping-agent.git
cd shopping-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install Playwright browsers:
```bash
playwright install
```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Fill in your API keys and preferences in `.env`

5. Install Chrome from Website: https://www.google.com/chrome/ (if not already installed)

6. Create a new Chrome profile (to make sure no user data is available to the agent. This is optional, but recommended for security reasons)

## Configuration

The following environment variables can be configured in your `.env` file:
- `OPENAI_API_KEY`: Your OpenAI API key

## Usage
Make sure Chrome is closed before running the script.

Run the shopping agent:

```bash
python rewe_shopping.py
```

Adjust the prompt:
- Just edit the prompt in the `task_prompt.txt` file.

## Roadmap

- [ ] Improve memory management

## Contributing

I love contributions! Feel free to open issues for bugs or feature requests.


## License

This project is licensed under the terms included in the LICENSE file (WTFPL).

## Contact

For questions or feedback, please contact me at joshua@theaisoftwarecompany.com

Or on LinkedIn: [Joshua Heller](https://www.linkedin.com/in/joshua-heller-1b5326140/)

Or on X: [@thishellerguy](https://x.com/thishellerguy)
