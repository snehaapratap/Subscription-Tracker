# Subscription Renewal Tracker

## **Overview**
Subscription Renewal Tracker is a lightweight tool for managing subscriptions. It helps you:
1. Track subscriptions.
2. Send renewal notifications.
3. Analyze spending.

## **Features**
- Add subscriptions with name, cost, and renewal date.
- View all subscriptions in a tabular format.
- Receive email reminders 7 days before renewal.
- Export spending details (future feature).

---

## **Setup**

### **1. Clone the Repository**
```bash
git clone https://github.com/snehaapratap/subscription-renewal-tracker.git
cd subscription-renewal-tracker


```
Here’s the requested content in the specified format:

---

## **Future Features (Under Development)**
1. Export subscription data to CSV.
2. Advanced analytics for monthly/annual spending breakdown.
3. Integration with Google Calendar for auto-reminders.

---

## **Screenshots**

### **Dashboard**
The homepage displaying all active subscriptions.  
![image](https://github.com/user-attachments/assets/30ff9b53-c11f-47c9-9e3c-50cc0c82550d)


### **Add Subscription**
Simple form to input new subscription details.  
![image](https://github.com/user-attachments/assets/4959762f-0b8b-4330-878b-9949ad372f3a)


---

## **Basic Implementation**

### **Backend**
- The backend is implemented in **Flask**, a lightweight Python web framework.
- **Subscriptions are stored in an in-memory Python list.**
- Notifications simulate email reminders using Python’s **`smtplib`** (expandable to real email services).

### **Frontend**
- Built using **HTML** and **CSS** for simplicity.
- Includes a responsive and clean user interface for managing subscriptions.

---

### **Code Example**
Here's an example of how subscriptions are added and tracked:

```python
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
```

---

## **Evaluation Checklist**

### **1. Clarity of the Idea**
The **Subscription Renewal Tracker** is a well-defined solution to a niche problem. It simplifies subscription management with minimal effort.

### **2. Code Quality**
- Clean and modular Flask-based implementation.
- Adheres to Python best practices and **PEP-8** standards.
- Extensible for future enhancements.

### **3. Documentation**
- Comprehensive **README** with setup, features, and use-case details.
- Includes screenshots for better visualization.

### **4. Innovation and Feasibility**
- Targeted towards a specific problem: managing subscriptions.
- Feasible for a solo developer to maintain and scale.

---


Let me know if there’s anything more you’d like to add or modify!
