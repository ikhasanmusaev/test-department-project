from django.views.generic import TemplateView, ListView

from .models import Department, Employee


class TreeView(TemplateView):
    template_name = 'department/tree.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        departments = Department.objects.filter(parent=None)

        context['departments'] = self.build_tree(departments)
        return context

    def build_tree(self, departments):
        tree = []
        for department in departments:
            node = {
                'id': department.id,
                'text': department.name,
                'children': self.build_tree(department.children.all()),
                'a_attr': {'href': f'department/{department.id}/'}
            }
            tree.append(node)
        return tree


class DepartmentDetailView(ListView):
    model = Department
    template_name = 'department/detail.html'
    context_object_name = 'employees'
    paginate_by = 50

    def get_queryset(self):
        self.department = Department.objects.get(pk=self.kwargs['pk'])
        return Employee.objects.filter(department=self.department)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = self.department
        return context
