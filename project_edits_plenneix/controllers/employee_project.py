from odoo import http
from odoo.http import request, Response
import json


class EmployeeProjectController(http.Controller):

    @http.route('/api/employees_projects', type='http', auth='basic', methods=['GET'])
    def get_employees_with_projects(self, **kwargs):
        # Authenticate user
        if not request.httprequest.authorization:
            return Response('Unauthorized', status=401)

        username = request.httprequest.authorization.username
        password = request.httprequest.authorization.password
        employees = request.env['project.project'].search([])
        data = []
        for employee in employees:
            active_projects = employee.project_ids.filtered(lambda p: p.active)
            project_data = [{'name': project.name, 'description': project.description} for project in active_projects]
            data.append({
                'employee_name': employee.name,
                'employee_id': employee.id,
                'active_projects': project_data
            })

        # Return JSON response
        return Response(json.dumps(data), content_type='application/json')