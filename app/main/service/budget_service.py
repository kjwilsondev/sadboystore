import uuid
import datetime

from app.main import db
from app.main.model.budget import Budget

def save_new_budget(data):
    new_budget = Budget(
        set_on = datetime.datetime.utcnow(),
        length = data['length'],
        amount = float(data['amount']),
        success= data['success'] == "True",
        public_id= data['public_id']
    )
    save_changes(new_budget)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return response_object, 201

# TODO:
# Get budgets by day
# Get budgets by time length
# Get budgets by amount of money
# Get budgets by success

def get_all_budgets():
    return Budget.query.all()


def get_all_user_budgets(public_id):
    return Budget.query.filter_by(public_id=public_id).all()


def save_changes(data):
    db.session.add(data)
    db.session.commit()