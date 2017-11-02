from django.contrib.admin import SimpleListFilter

class SchoolFilter(SimpleListFilter):
    title = 'country' # or use _('country') for translated title
    parameter_name = 'country'

    def lookups(self, request, model_admin):
        print model_admin.model.objects.all()
        # countries = set([c.school for c in model_admin.model.objects.all()])
        return [('AFRICA', 'AFRICA - ALL')]
