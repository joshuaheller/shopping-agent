import os
import sys
from pathlib import Path
import subprocess
import platform

from browser_use.agent.views import ActionResult

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio

from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig, BrowserContextConfig
from browser_use.browser.context import BrowserContext

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Determine Chrome path based on operating system
if platform.system() == 'Darwin':  # macOS
    chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
elif platform.system() == 'Windows':
    chrome_paths = [
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
        os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe')
    ]
    chrome_path = next((path for path in chrome_paths if os.path.exists(path)), None)
    if not chrome_path:
        raise Exception("Chrome not found. Please install Chrome or verify its installation path.")
else:
    raise Exception("Unsupported operating system. This script supports Windows and macOS.")

browser = Browser(
	config=BrowserConfig(
		chrome_instance_path=chrome_path,
		new_context_config=BrowserContextConfig(
			minimum_wait_page_load_time=3,
			maximum_wait_page_load_time=20,
			browser_window_size={
				'width': 1920,
				'height': 2000,
			},
		),
	)
)

# Load task prompt from file
with open('task_prompt.txt', 'r', encoding='utf-8') as f:
    task = f.read()

async def main():
	agent = Agent(
		task=task,
		llm=ChatOpenAI(model='gpt-4o'),
		browser=browser,
	)

	await agent.run()
	await browser.close()

	input('Press Enter to close...')


if __name__ == '__main__':
	asyncio.run(main())
