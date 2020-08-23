import os
import weather_handler
import mail_bot
import time
import utils

# logging configuration

logger = utils.make_console_logger("main")

USER = os.environ.get('BOT_MAIL')
PASS = os.environ.get('BOT_GOOGLE_APP_PASS')
receiver = os.environ.get('MY_MAIL')
city = "Paris, France"
res_file = "data/result.json"
units = "metric"
api_key = os.environ.get('API_WEATHER')
part = "minutely,daily"
look_ahead = 5
total = 1
current_time = 0
run_time = 0


class Weather_Monitor:
    def __init__(self, weather):
        self.weather = utils.open_json_file(res_file)
        logger.info("Initialisation succeeded")

    @staticmethod
    def weather_is_changing(current, hour):
        if current != hour:
            state = f"Weather is changing to {hour}"
            logger.info(f"Weather change: {hour}")
            return state
        else:
            return None

    @staticmethod
    def temperature_is_changing(current, hour):
        current = int(current)
        hour = int(hour)
        if current > hour:
            state = f"Temperature is dropping to from {current} to {hour}."
            logger.info("Temp dropping")
            return state
        elif hour > current:
            state = f"Temperature is rising from {current} to {hour}"
            logger.info("Temp rising")
            return state
        else:
            return None

    def main(self):
        """     message = ""
        if weather_is_changing(current_weather, next_weather):
            message += weather_is_changing + "\n"

        if temp_is_changing:
            message += temp_is_changing + "\n"

        if len(message) != 0:
            message += "I'm a bot :)"

            mb = mail_bot.Mail_Bot(USER, PASS)
            mb.send_mail(receiver, message) """


if __name__ == "__main__":
    while current_time < total:
        current_time += 1
        weather = utils.get_weather(city, part, units, api_key, res_file)
        m = Weather_Monitor(weather)
        h = weather_handler.Weather_Handler(weather, look_ahead)

        current_weather = h.get_state(h.current)

        logger.info(f"Process ran {current_time} time(s)")
        time.sleep(run_time)
"""
        wm.weather_is_changing(current_weather, next_weather)

        current_temp = handler.get_temperature(full_weather)
        next_temp = handler.get_temperature(next_full_weather)
        wm.temperature_is_changing(current_temp, next_temp) """
