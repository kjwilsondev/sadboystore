# from flask import request
# from flask_restplus import Resource

# from ..util.dto import UserDto
# from ..util.dto import BudgetDto
# from ..service.user_service import save_new_user, get_all_users, get_a_user
# from ..service.budget_service import save_new_budget, get_all_budgets, get_all_user_budgets

# api = BudgetDto.api
# _user = UserDto.user
# _budget = BudgetDto.budget

# @api.route('/<public_id>/')
# @api.param('public_id', 'The User identifier')
# @api.response(404, 'User not found.')
# class Budget(Resource):
#     @api.response(201, 'Budget successfully created.')
#     @api.doc('create a new budget')
#     @api.expect(_budget, validate=True)
#     def post(self, public_id):
#         """Creates a new Budget """
#         data = request.json
#         return save_new_budget(data=data)

# @api.route('/<public_id>/budgets')
# @api.param('public_id', 'The User identifier')
# @api.response(404, 'User not found.')
# class BudgetList(Resource):
#     @api.doc('get a users list of budgets')
#     @api.marshal_list_with(_budget, envelope='data')
#     def get(self, public_id):
#         """get a users budgets given their identifier"""
#         user = get_a_user(public_id)
#         if not user:
#             api.abort(404)
#         else:
#             budgets = get_all_user_budgets(public_id)
#             return budgets