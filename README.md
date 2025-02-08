<h1 align="center">Enable AI to do your groceries 🤖</h1>

[![LinkedIn Follow](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/joshua-heller-1b5326140/)
[![Twitter Follow](https://img.shields.io/twitter/follow/thishellerguy?style=social)](https://x.com/thishellerguy)



This project is a shopping agent that automates interactions with online shopping platforms.

## Demo

[Original prompt (German)](task_prompt.txt): Einkaufen bei dm.

[English prompt](task_prompt_en.txt): Buy groceries from dm.

![Buying orange juice from dm](https://github.com/joshuaheller/shopping-agent/blob/main/agent_demo.gif?raw=true)


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
python shopping_agent.py
```

Adjust the prompt:
- Just edit the prompt in the `task_prompt.txt` file.

## Security notice
- The agent should always use a new Chrome profile to avoid any user data from being used.

- Always monitor the agent's behavior and stop it if it does not work as expected.

- API usage can incur high costs. Always monitor the API usage and stop the agent if the cost is too high.

### Liability disclaimer

The author does not guarantee the accuracy and reliability of the software. The author does not accept any liability for damages that may result from using the software.

## Roadmap

- [ ] be able to use other LLMs (especially cheaper ones)
- [ ] Add more shops to the shopping agent (Rewe, Edeka, Amazon, Alibaba, ...)
- [ ] Multi-step shopping tasks (e.g. look for recipe for a meal and then buy the respective ingredients)


## Contributing

I love contributions! Feel free to open issues for bugs or feature requests.

## Acknowledgements
Thanks to [Browser-use](https://github.com/browser-use/browser-use) for the browser agent framework.

## License

This project is licensed under the terms included in the LICENSE file (WTFPL).

## Contact

For questions or feedback, please contact me at joshua@theaisoftwarecompany.com

*Me with my first order from the AI agent:*

![Me with my first order from the AI agent](https://github.com/joshuaheller/shopping-agent/blob/ded938a33243ed6c89e861a95a07a7f002fc0952/me.jpg?raw=true)

**Or on LinkedIn:** [Joshua Heller](https://www.linkedin.com/in/joshua-heller-1b5326140/)

**Or on X:** [@thishellerguy](https://x.com/thishellerguy)
