# Twitch Mobile Emulation Test

This project is an automated test created with Selenium in Python, using mobile emulation in Google Chrome to access Twitch, search for a game, and navigate to a streamer's page. The test handles pop-ups and saves a screenshot of the streamer’s page.

## File Structure

- `tests/`: Contains the test script `test_twitch.py`.
- `screenshots/`: Stores screenshots saved during the test run.
- `README.md`: Project documentation.
- `requirements.txt`: List of required libraries.
- `.gitignore`: Specifies files excluded from the repository.

## Prerequisites

1. **Python 3.7+** - Ensure you have Python 3.7 or later installed.
2. **Google Chrome and ChromeDriver** - Download and install the appropriate version of ChromeDriver from [here](https://sites.google.com/chromium.org/driver/).
3. **Selenium and Pytest** - Install the required libraries from `requirements.txt`.

## Setup

1. Clone the repository:
    ```bash
    git clone <repository-URL>
    cd Automation_twitch_test
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # For Mac/Linux
    .venvq\Scripts\activate     # For Windows
    ```

3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

4. Ensure `chromedriver` is in your system PATH. If it’s not, copy the `chromedriver` file to the project directory or add it to your PATH.

## Running the Test

To run the test, use the following command:

```bash
pytest tests/test_twitch.py
