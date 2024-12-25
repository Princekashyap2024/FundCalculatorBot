
# FundCalculatorBot  

FundCalculatorBot is a Telegram bot that helps users calculate investment funds and the total money required based on their inputs. Users can provide initial investment, number of levels, and multiplier to get a detailed breakdown of the fund calculation.  

## Features  
- Dynamic fund calculation based on user input.  
- Inline buttons for multiplier selection.  
- Saves user data for later analysis.  
- Simple and intuitive commands for ease of use.  

## Commands  
### `/start`  
Displays a welcome message and explains the bot's functionality.  

### `/help`  
Provides detailed instructions on how to use the bot.  

### `/multiplier`  
Allows users to choose a multiplier using inline buttons.  

### Dynamic Input  
Users can send input in the following format:  
```
<starting_amount> <levels> <multiplier>  
```
For example:  
```
10 5 3  
```

## Setup Instructions  

### Prerequisites  
- Python 3.12+  
- `python-telegram-bot` library  

### Installation  
1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/FundCalculatorBot.git  
   cd FundCalculatorBot  
   ```  

2. Create a virtual environment:  
   ```bash
   python3 -m venv myenv  
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate  
   ```  

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt  
   ```  

4. Add your Telegram bot token in the code:  
   Replace the `TOKEN` variable in `fund_calculator_bot.py` with your bot's token.  

### Running the Bot  
```bash
python fund_calculator_bot.py  
```  

## Example Usage  
1. Start the bot: `/start`  
2. Get help: `/help`  
3. Choose a multiplier: `/multiplier`  
4. Provide input: `10 5 3`  

## File Structure  
- `fund_calculator_bot.py`: Main bot code.  
- `user_data.txt`: Stores user data for reference.  
- `requirements.txt`: Contains project dependencies.  

## Contributing  
Contributions are welcome! Feel free to fork this repository and submit a pull request.  

## License  
This project is licensed under the MIT License.  

## Author  
Created by [Amit Kumar Raikwar](https://github.com/princekashyap2024).  
