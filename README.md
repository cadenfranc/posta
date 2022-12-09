# Social Media Analytics App

This app allows users to analyze their social media data to gain insights about their followers, posts, and engagement. The app also provides the ability to schedule posts for future publishing.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need to have python and pip installed on your system. If you do not have python and pip installed, please follow the instructions [here](https://www.python.org/downloads/) to install them.

#### Instagram Basic Access

In order to authorize your account with the application, please provide a `.json` containing the following information.

```
{
  "account_id": "9085120397183961",
  "client_id": "1230971397019280",
  "client_secret": "38123kjbda91283729173kjad",
  "access_token": "SDbjk1289DJDKB921bjkDDbjk1289DJDKB921bjk"
}
```

If you are unsure of how to obtain these parameters, please follow the guide [here](https://towardsdatascience.com/discover-insights-from-your-instagram-business-account-with-facebook-graph-api-and-python-81d20ee2e751).

### Installing

Once you have python and pip installed, you can install the required packages by running the following command in your terminal:

`pip install -r requirements.txt`

This will install the required packages, including streamlit, plotly, and any other necessary dependencies.

### Running the app

To run the app, simply use the following command in your terminal:

`streamlit run dashboard.py`

This will start the app and open it in your default web browser.

## Using the app

Once the app is running, you can use the `profile.json` file created earlier to authorize your account. The app will then retrieve your data and display various metrics and charts about your followers, posts, and engagement. You can also use the app to schedule posts for future publishing.

## Built With

- [Python](https://www.python.org/)
- [Streamlit](https://www.streamlit.io/) - Web framework and user interface
- [Plotly](https://plotly.com/) - Data visualization
- [APscheduler](https://apscheduler.readthedocs.io/en/stable/) - Manage thread pool for post scheduling

## Author

- [Caden Franc](https://github.com/cadenfranc)
