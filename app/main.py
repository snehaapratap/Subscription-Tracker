from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta
import smtplib

app = Flask(__name__)

# In-memory storage for subscriptions
subscriptions = []

@app.route('/')
def index():
    return render_template('index.html', subscriptions=subscriptions)

@app.route('/add', methods=['GET', 'POST'])
def add_subscription():
    if request.method == 'POST':
        name = request.form['name']
        cost = request.form['cost']
        renewal_date = request.form['renewal_date']
        subscriptions.append({
            'name': name,
            'cost': float(cost),
            'renewal_date': datetime.strptime(renewal_date, '%Y-%m-%d'),
        })
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/notify')
def notify():
    # Simulated notification logic
    today = datetime.today()
    for sub in subscriptions:
        if sub['renewal_date'] - today <= timedelta(days=7):
            send_email(sub['name'], sub['renewal_date'])
    return "Notifications sent!"

def send_email(subscription_name, renewal_date):
    # Dummy email function
    sender = "youremail@example.com"
    recipient = "recipient@example.com"
    subject = f"Reminder: {subscription_name} Renewal Due!"
    body = f"Your subscription '{subscription_name}' is due for renewal on {renewal_date.date()}."
    message = f"Subject: {subject}\n\n{body}"
    print(f"Sending email:\n{message}")

if __name__ == '__main__':
    app.run(debug=True)
